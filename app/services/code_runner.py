"""
Safe Code Execution Service for Coding Lab
Executes student Python code against predefined challenge test cases in an isolated,
time-limited subprocess with AST safety validation.
"""
import ast
import json
import subprocess
import sys
import time

# Block dangerous imports in AST
BANNED_MODULES = {
    'os', 'sys', 'subprocess', 'shutil', 'socket', 'urllib',
    'requests', 'http', 'ftplib', 'smtplib', 'telnetlib', 'posix',
    'ctypes', '_thread', 'threading', 'multiprocessing', 'builtins'
}

BANNED_CALLS = {'exec', 'eval', 'compile', '__import__', 'open'}

def validate_code_safety(source_code):
    """
    Parses code AST to ensure no dangerous system/network calls or banned modules are used.
    """
    try:
        tree = ast.parse(source_code)
    except SyntaxError as e:
        return False, f"Syntax Error: {e.msg} (Line {e.lineno})"

    for node in ast.walk(tree):
        # Check imports
        if isinstance(node, ast.Import):
            for alias in node.names:
                root_module = alias.name.split('.')[0]
                if root_module in BANNED_MODULES:
                    return False, f"Security Violation: Import of module '{alias.name}' is restricted."
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                root_module = node.module.split('.')[0]
                if root_module in BANNED_MODULES:
                    return False, f"Security Violation: Import from '{node.module}' is restricted."
        
        # Check banned function calls
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name) and node.func.id in BANNED_CALLS:
                return False, f"Security Violation: Function '{node.func.id}()' is restricted."

    return True, "Code passed security check."

def execute_python_code(source_code, test_cases, timeout_seconds=3.0):
    """
    Executes student Python solution against each test case.
    Wraps solution with test harness script and runs in isolated subprocess.
    """
    # 1. Static security check
    is_safe, safety_msg = validate_code_safety(source_code)
    if not is_safe:
        return {
            'status': 'Security Violation',
            'error_message': safety_msg,
            'passed_count': 0,
            'total_count': len(test_cases),
            'execution_time_ms': 0,
            'test_results': []
        }

    test_results = []
    passed_count = 0
    total_start_time = time.time()

    for idx, tc in enumerate(test_cases):
        raw_input = tc.get('input', '')
        expected_output = str(tc.get('expected_output', '')).strip()
        is_hidden = tc.get('is_hidden', False)

        # Harness code that feeds raw_input via StringIO/stdin and invokes user solution
        harness = f"""
import sys, io, json

# Redirect stdin
sys.stdin = io.StringIO({repr(raw_input)})

# Student code execution
__student_code_output = io.StringIO()
sys.stdout = __student_code_output

try:
{_indent(source_code, 4)}
except Exception as e:
    import traceback
    sys.stderr.write(traceback.format_exc())
    sys.exit(1)

# Retrieve output
output_val = __student_code_output.getvalue().strip()
sys.stdout = sys.__stdout__
print(output_val)
"""
        case_start = time.time()
        try:
            proc = subprocess.run(
                [sys.executable, '-c', harness],
                capture_output=True,
                text=True,
                timeout=timeout_seconds
            )
            elapsed_ms = int((time.time() - case_start) * 1000)

            if proc.returncode != 0:
                err_text = proc.stderr.strip()
                # Clean up harness internal lines from traceback
                clean_err = _clean_traceback(err_text)
                test_results.append({
                    'case_number': idx + 1,
                    'input': raw_input if not is_hidden else '[Hidden]',
                    'expected': expected_output if not is_hidden else '[Hidden]',
                    'actual': None,
                    'passed': False,
                    'is_hidden': is_hidden,
                    'error': clean_err or 'Runtime Error',
                    'is_runtime_error': True,
                    'time_ms': elapsed_ms
                })
                break
            else:
                actual_output = proc.stdout.strip()
                # Compare actual output vs expected output (normalized whitespace/quotes)
                passed = _compare_outputs(actual_output, expected_output)
                if passed:
                    passed_count += 1

                test_results.append({
                    'case_number': idx + 1,
                    'input': raw_input if not is_hidden else '[Hidden]',
                    'expected': expected_output if not is_hidden else '[Hidden]',
                    'actual': actual_output if not is_hidden else ('[Hidden]' if not passed else '[Passed]'),
                    'passed': passed,
                    'is_hidden': is_hidden,
                    'error': None if passed else 'Output mismatch',
                    'is_runtime_error': False,
                    'time_ms': elapsed_ms
                })

                if not passed:
                    break

        except subprocess.TimeoutExpired:
            test_results.append({
                'case_number': idx + 1,
                'input': raw_input if not is_hidden else '[Hidden]',
                'expected': expected_output if not is_hidden else '[Hidden]',
                'actual': None,
                'passed': False,
                'is_hidden': is_hidden,
                'error': f'Time Limit Exceeded (> {timeout_seconds}s)',
                'is_runtime_error': False,
                'time_ms': int(timeout_seconds * 1000)
            })
            break

    total_time_ms = int((time.time() - total_start_time) * 1000)
    
    # Determine overall status
    if len(test_results) == 0:
        status = 'No Test Cases'
    elif passed_count == len(test_cases):
        status = 'Accepted'
    else:
        last_case = test_results[-1]
        if 'Time Limit' in (last_case.get('error') or ''):
            status = 'Time Limit Exceeded'
        elif last_case.get('is_runtime_error'):
            status = 'Runtime Error'
        else:
            status = 'Wrong Answer'

    return {
        'status': status,
        'passed_count': passed_count,
        'total_count': len(test_cases),
        'execution_time_ms': total_time_ms,
        'test_results': test_results
    }

def _indent(text, spaces):
    pad = ' ' * spaces
    return '\n'.join(pad + line if line.strip() else line for line in text.split('\n'))

def _clean_traceback(tb_str):
    lines = tb_str.split('\n')
    user_lines = [l for l in lines if 'harness' not in l and '<string>' not in l]
    return '\n'.join(user_lines[-4:]).strip() if user_lines else tb_str

def _compare_outputs(actual, expected):
    # Direct match
    if actual == expected:
        return True
    
    # Try json / array comparison
    try:
        a_json = json.loads(actual)
        e_json = json.loads(expected)
        if a_json == e_json:
            return True
    except Exception:
        pass

    # Normalize whitespace
    if ' '.join(actual.split()) == ' '.join(expected.split()):
        return True

    return False

import pytest
from app.services.code_runner import validate_code_safety, execute_python_code

def test_ast_safety_validator_blocks_malicious_modules():
    malicious_scripts = [
        "import os\nos.system('dir')",
        "import subprocess\nsubprocess.run(['dir'])",
        "import socket\ns = socket.socket()",
        "from os import path",
        "from sys import modules"
    ]
    for script in malicious_scripts:
        is_safe, msg = validate_code_safety(script)
        assert is_safe is False
        assert "Security Violation" in msg

def test_ast_safety_validator_blocks_dangerous_calls():
    dangerous_calls = [
        "eval('2 + 2')",
        "exec('a = 5')",
        "f = open('secret.txt', 'r')"
    ]
    for script in dangerous_calls:
        is_safe, msg = validate_code_safety(script)
        assert is_safe is False
        assert "Security Violation" in msg

def test_execute_python_code_successful_pass():
    code = """
nums = list(map(int, input().split()))
print(sum(nums))
"""
    test_cases = [
        {"input": "1 2 3 4", "expected_output": "10", "is_hidden": False},
        {"input": "10 20", "expected_output": "30", "is_hidden": True}
    ]
    result = execute_python_code(code, test_cases, timeout_seconds=2.0)
    assert result['status'] == 'Accepted'
    assert result['passed_count'] == 2
    assert result['total_count'] == 2

def test_execute_python_code_detects_wrong_answer():
    code = """
nums = list(map(int, input().split()))
print(nums[0])
"""
    test_cases = [
        {"input": "1 2 3", "expected_output": "6", "is_hidden": False}
    ]
    result = execute_python_code(code, test_cases, timeout_seconds=2.0)
    assert result['status'] == 'Wrong Answer'
    assert result['passed_count'] == 0

def test_execute_python_code_handles_timeout():
    infinite_loop_code = """
while True:
    pass
"""
    test_cases = [{"input": "test", "expected_output": "test", "is_hidden": False}]
    result = execute_python_code(infinite_loop_code, test_cases, timeout_seconds=1.0)
    assert result['status'] == 'Time Limit Exceeded'

def test_execute_python_code_handles_runtime_error():
    runtime_err_code = """
x = 1 / 0
"""
    test_cases = [{"input": "", "expected_output": "", "is_hidden": False}]
    result = execute_python_code(runtime_err_code, test_cases, timeout_seconds=2.0)
    assert result['status'] == 'Runtime Error'

"""
Coding challenges seed data with 40 challenges across 10 core computer science topics
"""

CHALLENGES = [
    # --- ARRAYS (1-4) ---
    {
        "title": "Two Sum",
        "slug": "two-sum",
        "topic": "Arrays",
        "difficulty": "Easy",
        "description": "Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice. Print the two indices separated by a space in increasing order.",
        "constraints": "2 <= nums.length <= 10^4\n-10^9 <= nums[i] <= 10^9\n-10^9 <= target <= 10^9",
        "input_format": "First line contains space-separated integers representing nums.\nSecond line contains integer target.",
        "output_format": "Print the two indices separated by a space.",
        "sample_inputs": "2 7 11 15\n9",
        "sample_outputs": "0 1",
        "explanations": "Because nums[0] + nums[1] == 2 + 7 == 9, we print '0 1'.",
        "hints": ["Can you use a hash map to store elements seen so far and their indices?", "For each number x, check if (target - x) is already in the map."],
        "starter_code": "# Read input and solve Two Sum\nnums = list(map(int, input().split()))\ntarget = int(input())\n\nseen = {}\nfor i, num in enumerate(nums):\n    diff = target - num\n    if diff in seen:\n        print(f\"{seen[diff]} {i}\")\n        break\n    seen[num] = i\n",
        "test_cases": [
            {"input": "2 7 11 15\n9", "expected_output": "0 1", "is_hidden": False},
            {"input": "3 2 4\n6", "expected_output": "1 2", "is_hidden": False},
            {"input": "3 3\n6", "expected_output": "0 1", "is_hidden": True},
            {"input": "1 5 8 10 14\n18", "expected_output": "2 3", "is_hidden": True}
        ]
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "slug": "best-time-to-buy-and-sell-stock",
        "topic": "Arrays",
        "difficulty": "Easy",
        "description": "You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.\n\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\n\nPrint the maximum profit you can achieve from this transaction. If you cannot achieve any profit, print `0`.",
        "constraints": "1 <= prices.length <= 10^5\n0 <= prices[i] <= 10^4",
        "input_format": "A single line of space-separated integers representing daily prices.",
        "output_format": "A single integer denoting the maximum profit.",
        "sample_inputs": "7 1 5 3 6 4",
        "sample_outputs": "5",
        "explanations": "Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.",
        "hints": ["Track the minimum price seen so far as you iterate through the list.", "At each step, calculate the potential profit if sold today."],
        "starter_code": "prices = list(map(int, input().split()))\n\nmin_price = float('inf')\nmax_profit = 0\nfor p in prices:\n    if p < min_price:\n        min_price = p\n    elif p - min_price > max_profit:\n        max_profit = p - min_price\n\nprint(max_profit)\n",
        "test_cases": [
            {"input": "7 1 5 3 6 4", "expected_output": "5", "is_hidden": False},
            {"input": "7 6 4 3 1", "expected_output": "0", "is_hidden": False},
            {"input": "2 4 1", "expected_output": "2", "is_hidden": True},
            {"input": "1 2 3 4 5", "expected_output": "4", "is_hidden": True}
        ]
    },
    {
        "title": "Maximum Subarray (Kadane's Algorithm)",
        "slug": "maximum-subarray",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Given an integer array `nums`, find the subarray with the largest sum, and print its sum.",
        "constraints": "1 <= nums.length <= 10^5\n-10^4 <= nums[i] <= 10^4",
        "input_format": "A single line containing space-separated integers.",
        "output_format": "A single integer representing the maximum subarray sum.",
        "sample_inputs": "-2 1 -3 4 -1 2 1 -5 4",
        "sample_outputs": "6",
        "explanations": "The subarray [4, -1, 2, 1] has the largest sum = 6.",
        "hints": ["Kadane's algorithm keeps track of the current subarray sum.", "If current sum becomes negative, reset it to 0."],
        "starter_code": "nums = list(map(int, input().split()))\n\ncurr_sum = 0\nmax_sum = nums[0]\nfor x in nums:\n    curr_sum = max(x, curr_sum + x)\n    max_sum = max(max_sum, curr_sum)\n\nprint(max_sum)\n",
        "test_cases": [
            {"input": "-2 1 -3 4 -1 2 1 -5 4", "expected_output": "6", "is_hidden": False},
            {"input": "1", "expected_output": "1", "is_hidden": False},
            {"input": "5 4 -1 7 8", "expected_output": "23", "is_hidden": True},
            {"input": "-5 -2 -8", "expected_output": "-2", "is_hidden": True}
        ]
    },
    {
        "title": "Merge Intervals",
        "slug": "merge-intervals",
        "topic": "Arrays",
        "difficulty": "Medium",
        "description": "Given an array of intervals where each interval is represented by start and end integers, merge all overlapping intervals and print the resulting intervals sorted by start time.",
        "constraints": "1 <= intervals.length <= 10^4",
        "input_format": "First line contains integer N (number of intervals).\nFollowing N lines each contain two space-separated integers: start and end.",
        "output_format": "Print each merged interval on a new line as 'start end'.",
        "sample_inputs": "4\n1 3\n2 6\n8 10\n15 18",
        "sample_outputs": "1 6\n8 10\n15 18",
        "explanations": "Since intervals [1,3] and [2,6] overlap, merge them into [1,6].",
        "hints": ["Sort intervals by start time first.", "Iterate and merge if current interval start <= previous interval end."],
        "starter_code": "n = int(input())\nintervals = []\nfor _ in range(n):\n    s, e = map(int, input().split())\n    intervals.append([s, e])\n\nintervals.sort(key=lambda x: x[0])\nmerged = []\nfor interval in intervals:\n    if not merged or merged[-1][1] < interval[0]:\n        merged.append(interval)\n    else:\n        merged[-1][1] = max(merged[-1][1], interval[1])\n\nfor start, end in merged:\n    print(f\"{start} {end}\")\n",
        "test_cases": [
            {"input": "4\n1 3\n2 6\n8 10\n15 18", "expected_output": "1 6\n8 10\n15 18", "is_hidden": False},
            {"input": "2\n1 4\n4 5", "expected_output": "1 5", "is_hidden": False},
            {"input": "3\n1 4\n2 3\n5 8", "expected_output": "1 4\n5 8", "is_hidden": True}
        ]
    },

    # --- STRINGS (5-8) ---
    {
        "title": "Valid Anagram",
        "slug": "valid-anagram",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "Given two strings `s` and `t`, print `true` if `t` is an anagram of `s`, and `false` otherwise.\n\nAn Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.",
        "constraints": "1 <= s.length, t.length <= 5 * 10^4\ns and t consist of lowercase English letters.",
        "input_format": "First line contains string s.\nSecond line contains string t.",
        "output_format": "Print 'true' or 'false'.",
        "sample_inputs": "anagram\nnagaram",
        "sample_outputs": "true",
        "explanations": "Characters of 'anagram' can be rearranged to spell 'nagaram'.",
        "hints": ["Check if sorted(s) equals sorted(t), or count character frequencies."],
        "starter_code": "s = input().strip()\nt = input().strip()\n\nif sorted(s) == sorted(t):\n    print('true')\nelse:\n    print('false')\n",
        "test_cases": [
            {"input": "anagram\nnagaram", "expected_output": "true", "is_hidden": False},
            {"input": "rat\ncar", "expected_output": "false", "is_hidden": False},
            {"input": "listen\nsilent", "expected_output": "true", "is_hidden": True},
            {"input": "a\nab", "expected_output": "false", "is_hidden": True}
        ]
    },
    {
        "title": "Valid Palindrome",
        "slug": "valid-palindrome",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.\n\nPrint `true` if it is a palindrome, or `false` otherwise.",
        "constraints": "1 <= s.length <= 2 * 10^5",
        "input_format": "A single line containing the string s.",
        "output_format": "Print 'true' or 'false'.",
        "sample_inputs": "A man, a plan, a canal: Panama",
        "sample_outputs": "true",
        "explanations": "After filtering non-alphanumeric characters and lowercasing, 'amanaplanacanalpanama' is a palindrome.",
        "hints": ["Use .isalnum() and .lower() to clean the string before checking reverse equality."],
        "starter_code": "s = input().strip()\ncleaned = [c.lower() for c in s if c.isalnum()]\nif cleaned == cleaned[::-1]:\n    print('true')\nelse:\n    print('false')\n",
        "test_cases": [
            {"input": "A man, a plan, a canal: Panama", "expected_output": "true", "is_hidden": False},
            {"input": "race a car", "expected_output": "false", "is_hidden": False},
            {"input": " ", "expected_output": "true", "is_hidden": True},
            {"input": "0P", "expected_output": "false", "is_hidden": True}
        ]
    },
    {
        "title": "Longest Substring Without Repeating Characters",
        "slug": "longest-substring-without-repeating-characters",
        "topic": "Strings",
        "difficulty": "Medium",
        "description": "Given a string `s`, find the length of the longest substring without repeating characters.",
        "constraints": "0 <= s.length <= 5 * 10^4",
        "input_format": "A single line containing the string s.",
        "output_format": "An integer representing the length of the longest substring.",
        "sample_inputs": "abcabcbb",
        "sample_outputs": "3",
        "explanations": "The answer is 'abc', with length 3.",
        "hints": ["Use sliding window technique with two pointers and a set or hash map."],
        "starter_code": "s = input().strip()\nchar_map = {}\nleft = 0\nmax_len = 0\n\nfor right, ch in enumerate(s):\n    if ch in char_map and char_map[ch] >= left:\n        left = char_map[ch] + 1\n    char_map[ch] = right\n    max_len = max(max_len, right - left + 1)\n\nprint(max_len)\n",
        "test_cases": [
            {"input": "abcabcbb", "expected_output": "3", "is_hidden": False},
            {"input": "bbbbb", "expected_output": "1", "is_hidden": False},
            {"input": "pwwkew", "expected_output": "3", "is_hidden": True},
            {"input": "abcdef", "expected_output": "6", "is_hidden": True}
        ]
    },
    {
        "title": "String Compression",
        "slug": "string-compression",
        "topic": "Strings",
        "difficulty": "Easy",
        "description": "Given a string consisting of consecutive duplicate characters, perform run-length encoding. For each group of consecutive repeating characters, output the character followed by the group length. If length is 1, just print the character.",
        "constraints": "1 <= s.length <= 10^4",
        "input_format": "A single line string s.",
        "output_format": "Compressed string.",
        "sample_inputs": "aabcccccaaa",
        "sample_outputs": "a2bc5a3",
        "explanations": "'aa' -> 'a2', 'b' -> 'b', 'ccccc' -> 'c5', 'aaa' -> 'a3'.",
        "hints": ["Iterate with a counter tracking repeats of the current character."],
        "starter_code": "s = input().strip()\nif not s:\n    print('')\nelse:\n    res = []\n    curr = s[0]\n    count = 1\n    for c in s[1:]:\n        if c == curr:\n            count += 1\n        else:\n            res.append(f\"{curr}{count if count > 1 else ''}\")\n            curr = c\n            count = 1\n    res.append(f\"{curr}{count if count > 1 else ''}\")\n    print(''.join(res))\n",
        "test_cases": [
            {"input": "aabcccccaaa", "expected_output": "a2bc5a3", "is_hidden": False},
            {"input": "abcd", "expected_output": "abcd", "is_hidden": False},
            {"input": "wwwwaaadexxxxxx", "expected_output": "w4a3dex6", "is_hidden": True}
        ]
    },

    # --- HASH MAPS (9-12) ---
    {
        "title": "Group Anagrams",
        "slug": "group-anagrams",
        "topic": "Hash Maps",
        "difficulty": "Medium",
        "description": "Given an array of strings, group the anagrams together. Print the groups, where each group's words are sorted alphabetically and separated by spaces, one group per line. Groups should be sorted by their first element.",
        "constraints": "1 <= strs.length <= 10^4",
        "input_format": "Single line of space-separated strings.",
        "output_format": "Each group on a new line.",
        "sample_inputs": "eat tea tan ate nat bat",
        "sample_outputs": "ate eat tea\nbat\nnat tan",
        "explanations": "Anagrams are grouped by their common sorted character signature.",
        "hints": ["Use the sorted version of each word as a dictionary key."],
        "starter_code": "words = input().split()\ngroups = {}\nfor w in words:\n    key = ''.join(sorted(w))\n    groups.setdefault(key, []).append(w)\n\nres = [sorted(g) for g in groups.values()]\nres.sort(key=lambda x: x[0])\nfor group in res:\n    print(' '.join(group))\n",
        "test_cases": [
            {"input": "eat tea tan ate nat bat", "expected_output": "ate eat tea\nbat\nnat tan", "is_hidden": False},
            {"input": "a", "expected_output": "a", "is_hidden": False},
            {"input": "cat dog act god tac", "expected_output": "act cat tac\ndog god", "is_hidden": True}
        ]
    },
    {
        "title": "First Unique Character in a String",
        "slug": "first-unique-character",
        "topic": "Hash Maps",
        "difficulty": "Easy",
        "description": "Given a string `s`, find the first non-repeating character in it and return its index. If it does not exist, return `-1`.",
        "constraints": "1 <= s.length <= 10^5",
        "input_format": "A single string s.",
        "output_format": "Index of first unique character or -1.",
        "sample_inputs": "leetcode",
        "sample_outputs": "0",
        "explanations": "The character 'l' at index 0 is the first character that does not occur at any other index.",
        "hints": ["Count frequencies in a first pass, then scan again to find the first character with count 1."],
        "starter_code": "s = input().strip()\ncounts = {}\nfor c in s:\n    counts[c] = counts.get(c, 0) + 1\n\nans = -1\nfor i, c in enumerate(s):\n    if counts[c] == 1:\n        ans = i\n        break\nprint(ans)\n",
        "test_cases": [
            {"input": "leetcode", "expected_output": "0", "is_hidden": False},
            {"input": "loveleetcode", "expected_output": "2", "is_hidden": False},
            {"input": "aabb", "expected_output": "-1", "is_hidden": True}
        ]
    },
    {
        "title": "Intersection of Two Arrays",
        "slug": "intersection-of-two-arrays",
        "topic": "Hash Maps",
        "difficulty": "Easy",
        "description": "Given two integer arrays `nums1` and `nums2`, print their intersection. Each element in the result must be unique and output should be printed in ascending order.",
        "constraints": "1 <= nums1.length, nums2.length <= 1000",
        "input_format": "First line contains space-separated integers for nums1.\nSecond line contains space-separated integers for nums2.",
        "output_format": "Space-separated sorted unique integers.",
        "sample_inputs": "1 2 2 1\n2 2",
        "sample_outputs": "2",
        "explanations": "The common element between both arrays is 2.",
        "hints": ["Use sets in Python to find common elements efficiently."],
        "starter_code": "nums1 = set(map(int, input().split()))\nnums2 = set(map(int, input().split()))\nres = sorted(list(nums1.intersection(nums2)))\nprint(' '.join(map(str, res)))\n",
        "test_cases": [
            {"input": "1 2 2 1\n2 2", "expected_output": "2", "is_hidden": False},
            {"input": "4 9 5\n9 4 9 8 4", "expected_output": "4 9", "is_hidden": False},
            {"input": "1 2 3\n4 5 6", "expected_output": "", "is_hidden": True}
        ]
    },
    {
        "title": "Subarray Sum Equals K",
        "slug": "subarray-sum-equals-k",
        "topic": "Hash Maps",
        "difficulty": "Medium",
        "description": "Given an array of integers `nums` and an integer `k`, print the total number of subarrays whose sum equals to `k`.",
        "constraints": "1 <= nums.length <= 2 * 10^4\n-1000 <= nums[i] <= 1000\n-10^7 <= k <= 10^7",
        "input_format": "First line contains space-separated integers representing nums.\nSecond line contains integer k.",
        "output_format": "An integer representing the count of subarrays.",
        "sample_inputs": "1 1 1\n2",
        "sample_outputs": "2",
        "explanations": "Subarrays [1, 1] at indices [0, 1] and [1, 2] both sum to 2.",
        "hints": ["Use prefix sums and store frequency of prefix sums in a hash map."],
        "starter_code": "nums = list(map(int, input().split()))\nk = int(input())\n\nprefix_counts = {0: 1}\ncurr_sum = 0\nans = 0\nfor x in nums:\n    curr_sum += x\n    if (curr_sum - k) in prefix_counts:\n        ans += prefix_counts[curr_sum - k]\n    prefix_counts[curr_sum] = prefix_counts.get(curr_sum, 0) + 1\n\nprint(ans)\n",
        "test_cases": [
            {"input": "1 1 1\n2", "expected_output": "2", "is_hidden": False},
            {"input": "1 2 3\n3", "expected_output": "2", "is_hidden": False},
            {"input": "1 -1 0\n0", "expected_output": "3", "is_hidden": True}
        ]
    },

    # --- SEARCHING (13-16) ---
    {
        "title": "Binary Search",
        "slug": "binary-search",
        "topic": "Searching",
        "difficulty": "Easy",
        "description": "Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then print its index. Otherwise, print `-1`.\n\nYou must write an algorithm with `O(log n)` runtime complexity.",
        "constraints": "1 <= nums.length <= 10^4\nAll integers in nums are unique and sorted in ascending order.",
        "input_format": "First line contains sorted integers in nums.\nSecond line contains target integer.",
        "output_format": "Index of target or -1.",
        "sample_inputs": "-1 0 3 5 9 12\n9",
        "sample_outputs": "4",
        "explanations": "9 exists in nums and its index is 4.",
        "hints": ["Initialize low = 0, high = len(nums) - 1. Halve the search space each step."],
        "starter_code": "nums = list(map(int, input().split()))\ntarget = int(input())\n\nlow, high = 0, len(nums) - 1\nans = -1\nwhile low <= high:\n    mid = (low + high) // 2\n    if nums[mid] == target:\n        ans = mid\n        break\n    elif nums[mid] < target:\n        low = mid + 1\n    else:\n        high = mid - 1\n\nprint(ans)\n",
        "test_cases": [
            {"input": "-1 0 3 5 9 12\n9", "expected_output": "4", "is_hidden": False},
            {"input": "-1 0 3 5 9 12\n2", "expected_output": "-1", "is_hidden": False},
            {"input": "5\n5", "expected_output": "0", "is_hidden": True}
        ]
    },
    {
        "title": "Search in Rotated Sorted Array",
        "slug": "search-rotated-sorted-array",
        "topic": "Searching",
        "difficulty": "Medium",
        "description": "There is an integer array `nums` sorted in ascending order (with distinct values) that has been rotated at an unknown pivot index. Given `nums` and a `target`, print the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.\n\nYou must achieve `O(log n)` runtime complexity.",
        "constraints": "1 <= nums.length <= 5000",
        "input_format": "First line contains space-separated integers.\nSecond line contains target integer.",
        "output_format": "Index of target or -1.",
        "sample_inputs": "4 5 6 7 0 1 2\n0",
        "sample_outputs": "4",
        "explanations": "0 is at index 4.",
        "hints": ["Notice that at least one half (left or right) of the array is always strictly sorted."],
        "starter_code": "nums = list(map(int, input().split()))\ntarget = int(input())\n\nlow, high = 0, len(nums) - 1\nans = -1\nwhile low <= high:\n    mid = (low + high) // 2\n    if nums[mid] == target:\n        ans = mid\n        break\n    # Check if left half is sorted\n    if nums[low] <= nums[mid]:\n        if nums[low] <= target < nums[mid]:\n            high = mid - 1\n        else:\n            low = mid + 1\n    else:\n        if nums[mid] < target <= nums[high]:\n            low = mid + 1\n        else:\n            high = mid - 1\n\nprint(ans)\n",
        "test_cases": [
            {"input": "4 5 6 7 0 1 2\n0", "expected_output": "4", "is_hidden": False},
            {"input": "4 5 6 7 0 1 2\n3", "expected_output": "-1", "is_hidden": False},
            {"input": "1\n0", "expected_output": "-1", "is_hidden": True}
        ]
    },
    {
        "title": "Find Peak Element",
        "slug": "find-peak-element",
        "topic": "Searching",
        "difficulty": "Medium",
        "description": "A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks in `O(log n)` time.",
        "constraints": "1 <= nums.length <= 1000",
        "input_format": "A single line containing integers of nums.",
        "output_format": "Index of a peak element.",
        "sample_inputs": "1 2 3 1",
        "sample_outputs": "2",
        "explanations": "3 is a peak element and your function should return index number 2.",
        "hints": ["Use binary search: compare mid with mid + 1 to know which direction ascends."],
        "starter_code": "nums = list(map(int, input().split()))\nlow, high = 0, len(nums) - 1\nwhile low < high:\n    mid = (low + high) // 2\n    if nums[mid] > nums[mid + 1]:\n        high = mid\n    else:\n        low = mid + 1\nprint(low)\n",
        "test_cases": [
            {"input": "1 2 3 1", "expected_output": "2", "is_hidden": False},
            {"input": "1 2 1 3 5 6 4", "expected_output": "5", "is_hidden": False},
            {"input": "1", "expected_output": "0", "is_hidden": True}
        ]
    },
    {
        "title": "Square Root using Binary Search",
        "slug": "square-root-binary-search",
        "topic": "Searching",
        "difficulty": "Easy",
        "description": "Given a non-negative integer `x`, compute and return the integer square root of `x` (i.e. floor(sqrt(x))) without using built-in exponent functions like `x**0.5` or `math.sqrt()`.",
        "constraints": "0 <= x <= 2^31 - 1",
        "input_format": "A single non-negative integer x.",
        "output_format": "An integer representing the floor square root.",
        "sample_inputs": "8",
        "sample_outputs": "2",
        "explanations": "The square root of 8 is 2.82842..., and since we return the floor, 2 is returned.",
        "hints": ["Binary search on range [0, x]. If mid*mid <= x, search higher."],
        "starter_code": "x = int(input())\nif x < 2:\n    print(x)\nelse:\n    low, high = 1, x // 2\n    ans = 1\n    while low <= high:\n        mid = (low + high) // 2\n        if mid * mid <= x:\n            ans = mid\n            low = mid + 1\n        else:\n            high = mid - 1\n    print(ans)\n",
        "test_cases": [
            {"input": "4", "expected_output": "2", "is_hidden": False},
            {"input": "8", "expected_output": "2", "is_hidden": False},
            {"input": "16", "expected_output": "4", "is_hidden": True},
            {"input": "0", "expected_output": "0", "is_hidden": True}
        ]
    },

    # --- SORTING (17-20) ---
    {
        "title": "Sort Colors (Dutch National Flag)",
        "slug": "sort-colors",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Given an array `nums` with `n` objects colored red, white, or blue represented by integers `0`, `1`, and `2` respectively, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue (0, 1, 2). Print the sorted array separated by spaces.",
        "constraints": "1 <= nums.length <= 300\nnums[i] is either 0, 1, or 2.",
        "input_format": "A single line containing space-separated integers (0, 1, or 2).",
        "output_format": "Space-separated sorted integers.",
        "sample_inputs": "2 0 2 1 1 0",
        "sample_outputs": "0 0 1 1 2 2",
        "explanations": "The Dutch National Flag three-pointer partition sorts in O(N) time and O(1) space.",
        "hints": ["Maintain three pointers: low, mid, high. Swap 0s to low and 2s to high."],
        "starter_code": "nums = list(map(int, input().split()))\nlow, mid, high = 0, 0, len(nums) - 1\nwhile mid <= high:\n    if nums[mid] == 0:\n        nums[low], nums[mid] = nums[mid], nums[low]\n        low += 1\n        mid += 1\n    elif nums[mid] == 1:\n        mid += 1\n    else:\n        nums[mid], nums[high] = nums[high], nums[mid]\n        high -= 1\nprint(' '.join(map(str, nums)))\n",
        "test_cases": [
            {"input": "2 0 2 1 1 0", "expected_output": "0 0 1 1 2 2", "is_hidden": False},
            {"input": "2 0 1", "expected_output": "0 1 2", "is_hidden": False},
            {"input": "0", "expected_output": "0", "is_hidden": True}
        ]
    },
    {
        "title": "Kth Largest Element in an Array",
        "slug": "kth-largest-element",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Given an integer array `nums` and an integer `k`, print the `k-th` largest element in the array.",
        "constraints": "1 <= k <= nums.length <= 10^5",
        "input_format": "First line contains space-separated integers.\nSecond line contains integer k.",
        "output_format": "The kth largest integer.",
        "sample_inputs": "3 2 1 5 6 4\n2",
        "sample_outputs": "5",
        "explanations": "The sorted order descending is [6, 5, 4, 3, 2, 1]. The 2nd largest is 5.",
        "hints": ["Sort descending or use a min-heap of size k."],
        "starter_code": "nums = list(map(int, input().split()))\nk = int(input())\nnums.sort(reverse=True)\nprint(nums[k - 1])\n",
        "test_cases": [
            {"input": "3 2 1 5 6 4\n2", "expected_output": "5", "is_hidden": False},
            {"input": "3 2 3 1 2 4 5 5 6\n4", "expected_output": "4", "is_hidden": False},
            {"input": "1\n1", "expected_output": "1", "is_hidden": True}
        ]
    },
    {
        "title": "Merge Sorted Arrays",
        "slug": "merge-sorted-arrays",
        "topic": "Sorting",
        "difficulty": "Easy",
        "description": "Given two sorted integer arrays `nums1` and `nums2`, merge `nums2` into `nums1` as one sorted array and print the resulting sorted array separated by spaces.",
        "constraints": "1 <= nums1.length, nums2.length <= 10^4",
        "input_format": "First line contains sorted integers for nums1.\nSecond line contains sorted integers for nums2.",
        "output_format": "Space-separated sorted combined integers.",
        "sample_inputs": "1 2 3\n2 5 6",
        "sample_outputs": "1 2 2 3 5 6",
        "explanations": "Merged array is [1, 2, 2, 3, 5, 6].",
        "hints": ["Two pointers starting from the beginning of each sorted array."],
        "starter_code": "a = list(map(int, input().split()))\nb = list(map(int, input().split()))\ni, j = 0, 0\nres = []\nwhile i < len(a) and j < len(b):\n    if a[i] <= b[j]:\n        res.append(a[i])\n        i += 1\n    else:\n        res.append(b[j])\n        j += 1\nres.extend(a[i:])\nres.extend(b[j:])\nprint(' '.join(map(str, res)))\n",
        "test_cases": [
            {"input": "1 2 3\n2 5 6", "expected_output": "1 2 2 3 5 6", "is_hidden": False},
            {"input": "1\n2", "expected_output": "1 2", "is_hidden": False},
            {"input": "0\n1", "expected_output": "0 1", "is_hidden": True}
        ]
    },
    {
        "title": "Top K Frequent Elements",
        "slug": "top-k-frequent-elements",
        "topic": "Sorting",
        "difficulty": "Medium",
        "description": "Given an integer array `nums` and an integer `k`, return the `k` most frequent elements in descending order of frequency. If frequencies match, sort by value ascending.",
        "constraints": "1 <= nums.length <= 10^5\nk is in the range [1, number of unique elements]",
        "input_format": "First line contains space-separated integers.\nSecond line contains integer k.",
        "output_format": "Space-separated integers.",
        "sample_inputs": "1 1 1 2 2 3\n2",
        "sample_outputs": "1 2",
        "explanations": "1 occurs 3 times, 2 occurs 2 times. The top 2 elements are 1 and 2.",
        "hints": ["Count frequencies in a hash map, then sort items by (-count, value)."],
        "starter_code": "nums = list(map(int, input().split()))\nk = int(input())\ncounts = {}\nfor x in nums:\n    counts[x] = counts.get(x, 0) + 1\nsorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))\nans = [str(x[0]) for x in sorted_items[:k]]\nprint(' '.join(ans))\n",
        "test_cases": [
            {"input": "1 1 1 2 2 3\n2", "expected_output": "1 2", "is_hidden": False},
            {"input": "1\n1", "expected_output": "1", "is_hidden": False},
            {"input": "4 1 -1 2 -1 2 3\n2", "expected_output": "-1 2", "is_hidden": True}
        ]
    },

    # --- RECURSION (21-24) ---
    {
        "title": "Fibonacci Number",
        "slug": "fibonacci-number",
        "topic": "Recursion",
        "difficulty": "Easy",
        "description": "The Fibonacci numbers, commonly denoted `F(n)` form a sequence, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is:\nF(0) = 0, F(1) = 1\nF(n) = F(n - 1) + F(n - 2), for n > 1.\nGiven `n`, print `F(n)`.",
        "constraints": "0 <= n <= 30",
        "input_format": "A single integer n.",
        "output_format": "F(n)",
        "sample_inputs": "4",
        "sample_outputs": "3",
        "explanations": "F(4) = F(3) + F(2) = 2 + 1 = 3.",
        "hints": ["Base cases: n=0 returns 0, n=1 returns 1."],
        "starter_code": "n = int(input())\ndef fib(k):\n    if k <= 0: return 0\n    if k == 1: return 1\n    a, b = 0, 1\n    for _ in range(2, k + 1):\n        a, b = b, a + b\n    return b\nprint(fib(n))\n",
        "test_cases": [
            {"input": "2", "expected_output": "1", "is_hidden": False},
            {"input": "3", "expected_output": "2", "is_hidden": False},
            {"input": "4", "expected_output": "3", "is_hidden": False},
            {"input": "10", "expected_output": "55", "is_hidden": True}
        ]
    },
    {
        "title": "Power of a Number (Pow(x, n))",
        "slug": "power-of-number",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`) using recursive binary exponentiation in `O(log n)` time.",
        "constraints": "-100.0 < x < 100.0\n0 <= n <= 10^4",
        "input_format": "First line contains float x.\nSecond line contains non-negative integer n.",
        "output_format": "Print result rounded to 2 decimal places.",
        "sample_inputs": "2.0\n10",
        "sample_outputs": "1024.0",
        "explanations": "2^10 = 1024.",
        "hints": ["If n is even, x^n = (x*x)^(n//2). If n is odd, x^n = x * x^(n-1)."],
        "starter_code": "x = float(input())\nn = int(input())\ndef fast_pow(base, exp):\n    if exp == 0:\n        return 1.0\n    half = fast_pow(base, exp // 2)\n    if exp % 2 == 0:\n        return half * half\n    else:\n        return half * half * base\nans = fast_pow(x, n)\nprint(round(ans, 2))\n",
        "test_cases": [
            {"input": "2.0\n10", "expected_output": "1024.0", "is_hidden": False},
            {"input": "2.1\n3", "expected_output": "9.26", "is_hidden": False},
            {"input": "2.0\n0", "expected_output": "1.0", "is_hidden": True}
        ]
    },
    {
        "title": "Subsets (Power Set)",
        "slug": "subsets-power-set",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "Given an integer array `nums` of unique elements, print all possible subsets (the power set). Print each subset as space-separated integers on a new line (empty line for empty subset), sorted lexicographically.",
        "constraints": "1 <= nums.length <= 10",
        "input_format": "Single line of space-separated unique integers.",
        "output_format": "Subsets, one per line.",
        "sample_inputs": "1 2 3",
        "sample_outputs": "\n1\n1 2\n1 2 3\n1 3\n2\n2 3\n3",
        "explanations": "All 2^3 = 8 subsets are generated.",
        "hints": ["Backtracking: at each index, you have two choices: include nums[i] or exclude it."],
        "starter_code": "nums = sorted(list(map(int, input().split())))\nres = []\ndef backtrack(idx, current):\n    if idx == len(nums):\n        res.append(list(current))\n        return\n    # include\n    current.append(nums[idx])\n    backtrack(idx + 1, current)\n    current.pop()\n    # exclude\n    backtrack(idx + 1, current)\n\nbacktrack(0, [])\nres.sort()\nfor sub in res:\n    print(' '.join(map(str, sub)))\n",
        "test_cases": [
            {"input": "1 2", "expected_output": "\n1\n1 2\n2", "is_hidden": False},
            {"input": "0", "expected_output": "\n0", "is_hidden": False}
        ]
    },
    {
        "title": "Tower of Hanoi",
        "slug": "tower-of-hanoi",
        "topic": "Recursion",
        "difficulty": "Medium",
        "description": "The Tower of Hanoi is a mathematical puzzle with three rods (A, B, C) and `n` disks. Print the total number of moves required to move `n` disks from rod A to rod C using rod B.",
        "constraints": "1 <= n <= 30",
        "input_format": "A single integer n.",
        "output_format": "Total number of moves (2^n - 1).",
        "sample_inputs": "3",
        "sample_outputs": "7",
        "explanations": "For 3 disks, minimum moves = 2^3 - 1 = 7.",
        "hints": ["The recurrence relation is T(n) = 2*T(n-1) + 1."],
        "starter_code": "n = int(input())\nprint((1 << n) - 1)\n",
        "test_cases": [
            {"input": "1", "expected_output": "1", "is_hidden": False},
            {"input": "2", "expected_output": "3", "is_hidden": False},
            {"input": "3", "expected_output": "7", "is_hidden": False},
            {"input": "5", "expected_output": "31", "is_hidden": True}
        ]
    },

    # --- LINKED LISTS (25-28) ---
    {
        "title": "Reverse Linked List",
        "slug": "reverse-linked-list",
        "topic": "Linked Lists",
        "difficulty": "Easy",
        "description": "Given the head values of a singly linked list, reverse the list, and print the reversed values separated by spaces.",
        "constraints": "0 <= number of nodes <= 5000",
        "input_format": "A single line containing space-separated integers.",
        "output_format": "Space-separated reversed integers.",
        "sample_inputs": "1 2 3 4 5",
        "sample_outputs": "5 4 3 2 1",
        "explanations": "Reversing [1, 2, 3, 4, 5] yields [5, 4, 3, 2, 1].",
        "hints": ["Maintain prev, curr, and next pointers."],
        "starter_code": "vals = input().split()\nprint(' '.join(vals[::-1]))\n",
        "test_cases": [
            {"input": "1 2 3 4 5", "expected_output": "5 4 3 2 1", "is_hidden": False},
            {"input": "1 2", "expected_output": "2 1", "is_hidden": False},
            {"input": "10", "expected_output": "10", "is_hidden": True}
        ]
    },
    {
        "title": "Middle of the Linked List",
        "slug": "middle-of-linked-list",
        "topic": "Linked Lists",
        "difficulty": "Easy",
        "description": "Given the values of a singly linked list, print the value of the middle node. If there are two middle nodes, print the second middle node (using the fast and slow pointer concept).",
        "constraints": "1 <= number of nodes <= 100",
        "input_format": "A single line of space-separated integers.",
        "output_format": "A single integer denoting the middle node value.",
        "sample_inputs": "1 2 3 4 5",
        "sample_outputs": "3",
        "explanations": "The middle node of list is 3.",
        "hints": ["Move slow pointer by 1 step and fast pointer by 2 steps."],
        "starter_code": "vals = list(map(int, input().split()))\nmid = len(vals) // 2\nprint(vals[mid])\n",
        "test_cases": [
            {"input": "1 2 3 4 5", "expected_output": "3", "is_hidden": False},
            {"input": "1 2 3 4 5 6", "expected_output": "4", "is_hidden": False},
            {"input": "1", "expected_output": "1", "is_hidden": True}
        ]
    },
    {
        "title": "Merge Two Sorted Linked Lists",
        "slug": "merge-two-sorted-lists",
        "topic": "Linked Lists",
        "difficulty": "Easy",
        "description": "Merge two sorted linked lists and print it as a single sorted list separated by spaces.",
        "constraints": "0 <= list1.length, list2.length <= 50",
        "input_format": "First line contains sorted integers of list1.\nSecond line contains sorted integers of list2.",
        "output_format": "Space-separated merged sorted integers.",
        "sample_inputs": "1 2 4\n1 3 4",
        "sample_outputs": "1 1 2 3 4 4",
        "explanations": "Merged list is [1, 1, 2, 3, 4, 4].",
        "hints": ["Use a dummy node and compare heads of both lists."],
        "starter_code": "l1 = list(map(int, input().split())) if input_val := input().strip() else []\nl2 = list(map(int, input().split())) if (input_val2 := input().strip()) else []\nres = sorted(l1 + l2)\nprint(' '.join(map(str, res)))\n",
        "test_cases": [
            {"input": "1 2 4\n1 3 4", "expected_output": "1 1 2 3 4 4", "is_hidden": False},
            {"input": "2\n1", "expected_output": "1 2", "is_hidden": False}
        ]
    },
    {
        "title": "Detect Cycle in Linked List",
        "slug": "detect-cycle-linked-list",
        "topic": "Linked Lists",
        "difficulty": "Medium",
        "description": "Given a sequence of node values and a `pos` integer representing the index to which the tail connects (or -1 if no cycle), print `true` if there is a cycle in the linked list, or `false` otherwise using Floyd's Tortoise and Hare algorithm.",
        "constraints": "0 <= number of nodes <= 10^4\npos is -1 or a valid index.",
        "input_format": "First line contains space-separated node values.\nSecond line contains pos integer.",
        "output_format": "Print 'true' or 'false'.",
        "sample_inputs": "3 2 0 -4\n1",
        "sample_outputs": "true",
        "explanations": "Tail connects to node index 1, creating a cycle.",
        "hints": ["Floyd's algorithm: if fast == slow, cycle exists."],
        "starter_code": "nodes = input().split()\npos = int(input())\nprint('true' if pos >= 0 else 'false')\n",
        "test_cases": [
            {"input": "3 2 0 -4\n1", "expected_output": "true", "is_hidden": False},
            {"input": "1 2\n0", "expected_output": "true", "is_hidden": False},
            {"input": "1\n-1", "expected_output": "false", "is_hidden": True}
        ]
    },

    # --- STACKS & QUEUES (29-32) ---
    {
        "title": "Valid Parentheses",
        "slug": "valid-parentheses",
        "topic": "Stacks and Queues",
        "difficulty": "Easy",
        "description": "Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\n\nAn input string is valid if:\n1. Open brackets must be closed by the same type of brackets.\n2. Open brackets must be closed in the correct order.\n\nPrint `true` if valid, otherwise `false`.",
        "constraints": "1 <= s.length <= 10^4",
        "input_format": "A single line containing bracket characters.",
        "output_format": "Print 'true' or 'false'.",
        "sample_inputs": "()[]{}",
        "sample_outputs": "true",
        "explanations": "All brackets open and close in matching pairs.",
        "hints": ["Use a stack. Push opening brackets; pop and compare on closing brackets."],
        "starter_code": "s = input().strip()\nstack = []\nmapping = {')': '(', '}': '{', ']': '['}\nis_valid = True\nfor ch in s:\n    if ch in mapping:\n        top = stack.pop() if stack else '#'\n        if mapping[ch] != top:\n            is_valid = False\n            break\n    else:\n        stack.append(ch)\nif is_valid and not stack:\n    print('true')\nelse:\n    print('false')\n",
        "test_cases": [
            {"input": "()[]{}", "expected_output": "true", "is_hidden": False},
            {"input": "(]", "expected_output": "false", "is_hidden": False},
            {"input": "([{}])", "expected_output": "true", "is_hidden": True},
            {"input": "]", "expected_output": "false", "is_hidden": True}
        ]
    },
    {
        "title": "Next Greater Element I",
        "slug": "next-greater-element",
        "topic": "Stacks and Queues",
        "difficulty": "Medium",
        "description": "Given an array of integers `nums`, find the next greater element for every element in the array using a monotonic stack. If an element does not have a next greater element, output `-1`. Print the answers separated by spaces.",
        "constraints": "1 <= nums.length <= 10^4",
        "input_format": "A single line of space-separated integers.",
        "output_format": "Space-separated next greater integers.",
        "sample_inputs": "4 5 2 25",
        "sample_outputs": "5 25 25 -1",
        "explanations": "Next greater for 4 is 5; for 5 is 25; for 2 is 25; for 25 is none (-1).",
        "hints": ["Use a decreasing monotonic stack scanning from right to left."],
        "starter_code": "nums = list(map(int, input().split()))\nn = len(nums)\nres = [-1] * n\nstack = []\nfor i in range(n - 1, -1, -1):\n    while stack and stack[-1] <= nums[i]:\n        stack.pop()\n    if stack:\n        res[i] = stack[-1]\n    stack.append(nums[i])\nprint(' '.join(map(str, res)))\n",
        "test_cases": [
            {"input": "4 5 2 25", "expected_output": "5 25 25 -1", "is_hidden": False},
            {"input": "13 7 6 12", "expected_output": "-1 12 12 -1", "is_hidden": False},
            {"input": "1 2 3 4", "expected_output": "2 3 4 -1", "is_hidden": True}
        ]
    },
    {
        "title": "Implement Queue using Two Stacks",
        "slug": "queue-using-two-stacks",
        "topic": "Stacks and Queues",
        "difficulty": "Easy",
        "description": "Simulate a FIFO Queue using two LIFO Stacks. Process `Q` queries:\n- 1 x: Push x to the back of the queue\n- 2: Pop from front and print the removed element\n- 3: Print element at front without removing",
        "constraints": "1 <= Q <= 100",
        "input_format": "First line integer Q.\nFollowing Q lines contain query type and optional value.",
        "output_format": "Outputs for queries 2 and 3, each on a new line.",
        "sample_inputs": "5\n1 42\n2\n1 14\n3\n1 28",
        "sample_outputs": "42\n14",
        "explanations": "Queue processes push(42), pop()->42, push(14), peek()->14.",
        "hints": ["In-stack for push; Out-stack for pop/peek. Transfer elements only when out-stack is empty."],
        "starter_code": "q = int(input())\nin_stack = []\nout_stack = []\nfor _ in range(q):\n    parts = list(map(int, input().split()))\n    cmd = parts[0]\n    if cmd == 1:\n        in_stack.append(parts[1])\n    elif cmd == 2:\n        if not out_stack:\n            while in_stack:\n                out_stack.append(in_stack.pop())\n        print(out_stack.pop())\n    elif cmd == 3:\n        if not out_stack:\n            while in_stack:\n                out_stack.append(in_stack.pop())\n        print(out_stack[-1])\n",
        "test_cases": [
            {"input": "5\n1 42\n2\n1 14\n3\n1 28", "expected_output": "42\n14", "is_hidden": False},
            {"input": "3\n1 10\n1 20\n2", "expected_output": "10", "is_hidden": False}
        ]
    },
    {
        "title": "Min Stack",
        "slug": "min-stack",
        "topic": "Stacks and Queues",
        "difficulty": "Medium",
        "description": "Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in `O(1)` time.\nGiven queries:\n- `push x`\n- `pop`\n- `getMin` (prints the minimum)",
        "constraints": "1 <= Q <= 1000",
        "input_format": "First line integer Q.\nFollowing Q lines commands.",
        "output_format": "Print result of each getMin query.",
        "sample_inputs": "6\npush -2\npush 0\npush -3\ngetMin\npop\ngetMin",
        "sample_outputs": "-3\n-2",
        "explanations": "After pushing -2, 0, -3 min is -3. After pop, min is -2.",
        "hints": ["Store pairs of (val, current_min) in the stack."],
        "starter_code": "q = int(input())\nstack = []\nfor _ in range(q):\n    line = input().split()\n    cmd = line[0]\n    if cmd == 'push':\n        val = int(line[1])\n        cur_min = val if not stack else min(val, stack[-1][1])\n        stack.append((val, cur_min))\n    elif cmd == 'pop':\n        if stack: stack.pop()\n    elif cmd == 'getMin':\n        if stack: print(stack[-1][1])\n",
        "test_cases": [
            {"input": "6\npush -2\npush 0\npush -3\ngetMin\npop\ngetMin", "expected_output": "-3\n-2", "is_hidden": False},
            {"input": "4\npush 5\npush 2\ngetMin\npop", "expected_output": "2", "is_hidden": False}
        ]
    },

    # --- TREES (33-36) ---
    {
        "title": "Maximum Depth of Binary Tree",
        "slug": "maximum-depth-binary-tree",
        "topic": "Trees",
        "difficulty": "Easy",
        "description": "Given a binary tree represented in level-order traversal as an array (where -1 represents null), find its maximum depth (the number of nodes along the longest path from the root node down to the farthest leaf node).",
        "constraints": "0 <= number of nodes <= 10^4",
        "input_format": "Single line of space-separated integers representing level-order traversal (-1 for null).",
        "output_format": "An integer representing max depth.",
        "sample_inputs": "3 9 20 -1 -1 15 7",
        "sample_outputs": "3",
        "explanations": "The longest path [3 -> 20 -> 15] has depth 3.",
        "hints": ["DFS: max_depth(root) = 1 + max(max_depth(left), max_depth(right))."],
        "starter_code": "vals = list(map(int, input().split()))\nif not vals or vals[0] == -1:\n    print(0)\nelse:\n    def get_depth(i):\n        if i >= len(vals) or vals[i] == -1:\n            return 0\n        left_d = get_depth(2 * i + 1)\n        right_d = get_depth(2 * i + 2)\n        return 1 + max(left_d, right_d)\n    print(get_depth(0))\n",
        "test_cases": [
            {"input": "3 9 20 -1 -1 15 7", "expected_output": "3", "is_hidden": False},
            {"input": "1 -1 2", "expected_output": "2", "is_hidden": False},
            {"input": "-1", "expected_output": "0", "is_hidden": True}
        ]
    },
    {
        "title": "Invert Binary Tree",
        "slug": "invert-binary-tree",
        "topic": "Trees",
        "difficulty": "Easy",
        "description": "Given the root of a binary tree in level order (with -1 for null), invert the tree (swap left and right child at every node), and print the inverted tree's level order traversal.",
        "constraints": "The number of nodes is in range [0, 100].",
        "input_format": "Level-order integers (-1 for null).",
        "output_format": "Space-separated level order integers.",
        "sample_inputs": "4 2 7 1 3 6 9",
        "sample_outputs": "4 7 2 9 6 3 1",
        "explanations": "Left and right subtrees are mirrored at every node.",
        "hints": ["Recursively swap root.left and root.right."],
        "starter_code": "vals = list(map(int, input().split()))\nif not vals or vals[0] == -1:\n    print('')\nelse:\n    class Node:\n        def __init__(self, val):\n            self.val = val\n            self.left = None\n            self.right = None\n    nodes = [Node(v) if v != -1 else None for v in vals]\n    for i in range(len(vals)):\n        if nodes[i]:\n            left_idx = 2 * i + 1\n            right_idx = 2 * i + 2\n            if left_idx < len(vals): nodes[i].left = nodes[left_idx]\n            if right_idx < len(vals): nodes[i].right = nodes[right_idx]\n    def invert(node):\n        if not node: return\n        node.left, node.right = node.right, node.left\n        invert(node.left)\n        invert(node.right)\n    invert(nodes[0])\n    # collect level order\n    q = [nodes[0]]\n    res = []\n    while q:\n        curr = q.pop(0)\n        if curr:\n            res.append(str(curr.val))\n            q.append(curr.left)\n            q.append(curr.right)\n    # strip trailing empty nulls\n    print(' '.join(res))\n",
        "test_cases": [
            {"input": "4 2 7 1 3 6 9", "expected_output": "4 7 2 9 6 3 1", "is_hidden": False},
            {"input": "2 1 3", "expected_output": "2 3 1", "is_hidden": False}
        ]
    },
    {
        "title": "Validate Binary Search Tree",
        "slug": "validate-binary-search-tree",
        "topic": "Trees",
        "difficulty": "Medium",
        "description": "Given a binary tree represented in level order, print `true` if it is a valid binary search tree (BST), and `false` otherwise.\nA valid BST has left child < node < right child for all descendants.",
        "constraints": "1 <= number of nodes <= 10^4",
        "input_format": "Level-order integers (-1 for null).",
        "output_format": "Print 'true' or 'false'.",
        "sample_inputs": "2 1 3",
        "sample_outputs": "true",
        "explanations": "The left child (1) < root (2) < right child (3), so valid.",
        "hints": ["Pass down valid range (min_val, max_val) to each subtree in recursive check."],
        "starter_code": "vals = list(map(int, input().split()))\ndef validate(i, low, high):\n    if i >= len(vals) or vals[i] == -1:\n        return True\n    val = vals[i]\n    if not (low < val < high):\n        return False\n    return validate(2 * i + 1, low, val) and validate(2 * i + 2, val, high)\nprint('true' if validate(0, float('-inf'), float('inf')) else 'false')\n",
        "test_cases": [
            {"input": "2 1 3", "expected_output": "true", "is_hidden": False},
            {"input": "5 1 4 -1 -1 3 6", "expected_output": "false", "is_hidden": False},
            {"input": "10", "expected_output": "true", "is_hidden": True}
        ]
    },
    {
        "title": "Lowest Common Ancestor of a BST",
        "slug": "lowest-common-ancestor-bst",
        "topic": "Trees",
        "difficulty": "Medium",
        "description": "Given a binary search tree (BST) and two node values `p` and `q`, find their Lowest Common Ancestor (LCA) node value. The LCA is defined between two nodes as the lowest node in T that has both p and q as descendants.",
        "constraints": "The number of nodes in the tree is in range [2, 10^5]. All values are unique.",
        "input_format": "First line: level order of BST (-1 for null).\nSecond line: integer p.\nThird line: integer q.",
        "output_format": "The integer value of the LCA.",
        "sample_inputs": "6 2 8 0 4 7 9\n2\n8",
        "sample_outputs": "6",
        "explanations": "The LCA of 2 and 8 is 6.",
        "hints": ["If both p and q are greater than root, go right. If both smaller, go left."],
        "starter_code": "vals = list(map(int, input().split()))\np = int(input())\nq = int(input())\ncurr = 0\nwhile curr < len(vals) and vals[curr] != -1:\n    val = vals[curr]\n    if p > val and q > val:\n        curr = 2 * curr + 2\n    elif p < val and q < val:\n        curr = 2 * curr + 1\n    else:\n        print(val)\n        break\n",
        "test_cases": [
            {"input": "6 2 8 0 4 7 9\n2\n8", "expected_output": "6", "is_hidden": False},
            {"input": "6 2 8 0 4 7 9\n2\n4", "expected_output": "2", "is_hidden": False}
        ]
    },

    # --- DYNAMIC PROGRAMMING (37-40) ---
    {
        "title": "Climbing Stairs",
        "slug": "climbing-stairs",
        "topic": "Dynamic Programming",
        "difficulty": "Easy",
        "description": "You are climbing a staircase. It takes `n` steps to reach the top.\n\nEach time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "constraints": "1 <= n <= 45",
        "input_format": "A single integer n.",
        "output_format": "Number of distinct ways.",
        "sample_inputs": "3",
        "sample_outputs": "3",
        "explanations": "There are three ways to climb to the top:\n1. 1 step + 1 step + 1 step\n2. 1 step + 2 steps\n3. 2 steps + 1 step",
        "hints": ["dp[i] = dp[i - 1] + dp[i - 2], identical to Fibonacci recurrence."],
        "starter_code": "n = int(input())\nif n <= 2:\n    print(n)\nelse:\n    a, b = 1, 2\n    for _ in range(3, n + 1):\n        a, b = b, a + b\n    print(b)\n",
        "test_cases": [
            {"input": "2", "expected_output": "2", "is_hidden": False},
            {"input": "3", "expected_output": "3", "is_hidden": False},
            {"input": "5", "expected_output": "8", "is_hidden": True},
            {"input": "1", "expected_output": "1", "is_hidden": True}
        ]
    },
    {
        "title": "Coin Change (Minimum Coins)",
        "slug": "coin-change",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.\n\nPrint the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, print `-1`.\n\nYou may assume you have an infinite number of each kind of coin.",
        "constraints": "1 <= coins.length <= 12\n1 <= coins[i] <= 2^31 - 1\n0 <= amount <= 10^4",
        "input_format": "First line contains space-separated coin denominations.\nSecond line contains integer amount.",
        "output_format": "Minimum number of coins or -1.",
        "sample_inputs": "1 2 5\n11",
        "sample_outputs": "3",
        "explanations": "11 = 5 + 5 + 1 (3 coins).",
        "hints": ["dp[i] = min(dp[i], dp[i - coin] + 1) for coin in coins."],
        "starter_code": "coins = list(map(int, input().split()))\namount = int(input())\ndp = [float('inf')] * (amount + 1)\ndp[0] = 0\nfor c in coins:\n    for x in range(c, amount + 1):\n        dp[x] = min(dp[x], dp[x - c] + 1)\nprint(dp[amount] if dp[amount] != float('inf') else -1)\n",
        "test_cases": [
            {"input": "1 2 5\n11", "expected_output": "3", "is_hidden": False},
            {"input": "2\n3", "expected_output": "-1", "is_hidden": False},
            {"input": "1\n0", "expected_output": "0", "is_hidden": True},
            {"input": "2 5 10 1\n27", "expected_output": "4", "is_hidden": True}
        ]
    },
    {
        "title": "Longest Increasing Subsequence (LIS)",
        "slug": "longest-increasing-subsequence",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Given an integer array `nums`, return the length of the longest strictly increasing subsequence.",
        "constraints": "1 <= nums.length <= 2500\n-10^4 <= nums[i] <= 10^4",
        "input_format": "A single line of space-separated integers.",
        "output_format": "An integer representing length of LIS.",
        "sample_inputs": "10 9 2 5 3 7 101 18",
        "sample_outputs": "4",
        "explanations": "The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.",
        "hints": ["dp[i] is the length of LIS ending at index i."],
        "starter_code": "nums = list(map(int, input().split()))\nif not nums:\n    print(0)\nelse:\n    dp = [1] * len(nums)\n    for i in range(1, len(nums)):\n        for j in range(i):\n            if nums[j] < nums[i]:\n                dp[i] = max(dp[i], dp[j] + 1)\n    print(max(dp))\n",
        "test_cases": [
            {"input": "10 9 2 5 3 7 101 18", "expected_output": "4", "is_hidden": False},
            {"input": "0 1 0 3 2 3", "expected_output": "4", "is_hidden": False},
            {"input": "7 7 7 7 7", "expected_output": "1", "is_hidden": True}
        ]
    },
    {
        "title": "0/1 Knapsack Problem",
        "slug": "01-knapsack",
        "topic": "Dynamic Programming",
        "difficulty": "Medium",
        "description": "Given `N` items where each item has an integer weight and value, determine the maximum value that can be put in a knapsack of capacity `W`. You cannot break items (either take whole item or do not take it).",
        "constraints": "1 <= N <= 100\n1 <= W <= 1000",
        "input_format": "First line contains two integers: N and W.\nSecond line contains N space-separated item weights.\nThird line contains N space-separated item values.",
        "output_format": "Maximum achievable total value.",
        "sample_inputs": "3 4\n1 2 3\n10 15 40",
        "sample_outputs": "55",
        "explanations": "Items with weight 1 (value 10) and weight 3 (value 40) give total weight 4 and value 50. Or weight 1 (10) + weight 3 (40) = 50. But taking weight 3 (40) and weight 1 (10) gives 50, whereas weight 1 (10) + weight 2 (15) + weight 3 (40) exceeds capacity. Best is 15 + 40 = 55 (weights 2 + 3 = 5 > 4). Wait, for weights 1 and 3: 10 + 40 = 50. But items (weight 1 val 10) + (weight 2 val 15) = 25. Best is item 3 (val 40, wt 3) + item 1 (val 10, wt 1) = 50. Wait, 1+2=3<=4: val 10+15=25. 1+3=4<=4: val 10+40=50. Max value is 50.",
        "hints": ["dp[w] = max(dp[w], dp[w - weight[i]] + val[i]) iterating backwards on w."],
        "starter_code": "n, w = map(int, input().split())\nweights = list(map(int, input().split()))\nvalues = list(map(int, input().split()))\ndp = [0] * (w + 1)\nfor i in range(n):\n    wt = weights[i]\n    val = values[i]\n    for cap in range(w, wt - 1, -1):\n        dp[cap] = max(dp[cap], dp[cap - wt] + val)\nprint(dp[w])\n",
        "test_cases": [
            {"input": "3 4\n1 2 3\n10 15 40", "expected_output": "50", "is_hidden": False},
            {"input": "3 50\n10 20 30\n60 100 120", "expected_output": "220", "is_hidden": False},
            {"input": "1 10\n15\n100", "expected_output": "0", "is_hidden": True}
        ]
    }
]

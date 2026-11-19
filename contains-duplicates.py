"""
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

Constraints:
0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""


def contains_duplicates(arr: list[int]) -> bool:
    if not 0 <= len(arr) <= 10**5:
        raise ValueError("Invalid size provided for argument arr")
    # key value where the key is the number and the value is a boolean indicating if we have encountered this number
    occurrence_dict: dict[int, bool] = {}
    for item in arr:
        if not -(10**9) <= item <= 10**9:
            raise ValueError("Invalid value provided in argument arr")
        if occurrence_dict.get(item):
            return True
        else:
            occurrence_dict[item] = True
    return False


test_cases: list[tuple[str, list[int], bool | str]] = [
    ("Example 1: adjacent duplicate", [1, 2, 3, 3], True),
    ("Example 2: no duplicates", [1, 2, 3, 4], False),
    ("Empty array", [], False),
    ("One element", [42], False),
    ("Two equal elements", [7, 7], True),
    ("Two distinct elements", [7, 8], False),
    ("Duplicate after unique values", [1, 2, 3, 4, 3], True),
    ("Negative duplicate", [-5, -5], True),
    ("Negative and positive values", [-3, 0, 3, 5], False),
    ("Positive maximum duplicate", [10**9, 10**9], True),
    ("Negative minimum duplicate", [-(10**9), -(10**9)], True),
    ("Positive maximum boundary", [10**9, 10**9 - 1], False),
    ("Negative minimum boundary", [-(10**9), -(10**9) + 1], False),
    ("Zero repeated", [0, 0], True),
    ("Descending unique array", [5, 4, 3, 2, 1], False),
    ("Alternating unique array", [1, 2, 1, 3, 2, 4, 5], True),
    ("Duplicate near the end", [9, 8, 7, 6, 5, 9], True),
    ("Duplicate as the first pair", [4, 4, 1, 2, 3], True),
    ("Duplicate at the array length boundary", [1, 2, 3, 4, 5, 6, 7, 8, 9, 9], True),
    ("Maximum length with unique values", list(range(10**5)), False),
    ("Maximum length with final duplicate", list(range(10**5 - 1)) + [10**5 - 2], True),
    ("Too many elements", [0] * (10**5 + 1), "Invalid size provided for argument arr"),
    ("Value below minimum", [-(10**9) - 1], "Invalid value provided in argument arr"),
    ("Value above maximum", [10**9 + 1], "Invalid value provided in argument arr"),
    (
        "Maximum length duplicate in the middle",
        list(range(10**5 - 2)) + [50000, 50000],
        True,
    ),
    (
        "Maximum length alternating boundaries",
        [-(10**9)] + list(range(1, 10**5)),
        False,
    ),
    ("Maximum and minimum values together", [-(10**9), 10**9], False),
    ("Repeated minimum value", [-(10**9), 0, -(10**9)], True),
    ("Repeated maximum value", [10**9, 0, 10**9], True),
    ("Zero in a unique array", [0, 1, -1, 2, -2], False),
]

for test_name, nums, expected in test_cases:
    try:
        actual = contains_duplicates(nums)
    except ValueError as error:
        actual = str(error)

    passed = actual == expected
    status = "PASS" if passed else "FAIL"
    print(
        f"[{status}] {test_name}: input={nums[:10]}{'...' if len(nums) > 10 else ''}, "
        f"expected={expected!r}, result={actual!r}"
    )

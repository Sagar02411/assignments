"""
================================================================================
         PYTHON CODING ASSIGNMENT — Complete the Functions / Fix the Bugs
================================================================================
Instructions:
  • There are 12 problems below.
  • Each problem has a brief description, a broken or incomplete function, and
    test cases at the bottom you can run to verify your solution.
  • Do NOT change function signatures or test-case code.
  • Add / fix only the body of each function.
  • Run the file when done: test4_python_intermediate.py
================================================================================
"""

# ─────────────────────────────────────────────────────────────────────────────
# Problem 1
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a list of integers, return a new list where every element is replaced
#   by the product of all OTHER elements in the list — without using division.
#
#   Example:
#       product_except_self([1, 2, 3, 4])  →  [24, 12, 8, 6]
#       product_except_self([5, 0, 3])     →  [0, 15, 0]
#
# TODO: Complete the function body.

def product_except_self(nums: list) -> list:
    ans = [1] * len(nums)        
    for i in range(1, len(nums)):
        ans[i] = nums[i-1] * ans[i-1]
            
    prod2 = 1
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= prod2
        prod2 *= nums[i]             
        
    return ans

l = [1, 2, 3]
print(product_except_self(l))


# ─────────────────────────────────────────────────────────────────────────────
# Problem 2
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   A "zigzag" string alternates characters: uppercase, lowercase, uppercase …
#   Given a string, return True if it is already a valid zigzag string,
#   False otherwise. Ignore non-alphabetic characters (skip them in the check).
#
#   Example:
#       is_zigzag("AbCdEf")   →  True
#       is_zigzag("ABcDeF")   →  False
#       is_zigzag("A1b2C3d")  →  True   (digits are skipped)
#
# BUG: The function always returns True. Find and fix the bug.

def is_zigzag(s: str) -> bool:
    letters = [c for c in s if c.isalpha()]
    expected_upper = True
    for ch in letters:
        if expected_upper and ch.islower():
            return True          # ← bug is on this line
        if not expected_upper and ch.isupper():
            return False
        expected_upper = not expected_upper
    return True


# ─────────────────────────────────────────────────────────────────────────────
# Problem 3
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a sentence (string), return the word that contains the most unique
#   characters. If there is a tie, return the word that appears first.
#   Ignore punctuation attached to words.
#
#   Example:
#       richest_word("the quick brown fox")      →  "quick"
#       richest_word("hello world, bye world.")  →  "hello"
#
# TODO: Complete the function body.

def richest_word(sentence: str) -> str:
    words = sentence.split()
    res = max(words, key=lambda x: len(set(x)))
    return res
    
    
# ─────────────────────────────────────────────────────────────────────────────
# Problem 4
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Implement run-length encoding for a string.
#   Consecutive duplicate characters are replaced by the character followed
#   by the count. Single characters are NOT followed by "1".
#
#   Example:
#       rle_encode("aaabccddddee")  →  "a3bc2d4e2"
#       rle_encode("abcd")          →  "abcd"
#
# BUG: The output is wrong for some inputs. Find and fix the bug(s).

def rle_encode(s: str) -> str:
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):          # ← off-by-one error here
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1])
            if count > 1:
                result.append(str(count))
            count = 1
    result.append(s[-1])
    if count > 1:
        result.append(str(count))
    return "".join(result)


# ─────────────────────────────────────────────────────────────────────────────
# Problem 5
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   A "staircase number" is a positive integer where each digit is strictly
#   greater than the previous digit (left to right).
#   Given n, count how many staircase numbers exist with exactly n digits.
#
#   Example:
#       count_staircase(1)  →  9          (1,2,3,4,5,6,7,8,9)
#       count_staircase(2)  →  36         (12,13,...,89)
#       count_staircase(3)  →  84
#
# TODO: Complete the function body.

def count_staircase(n: int) -> int:
    pass  # ← replace this


# ─────────────────────────────────────────────────────────────────────────────
# Problem 6
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a list of integers, find the length of the longest subarray whose
#   elements sum to exactly zero.
#   Return 0 if no such subarray exists.
#
#   Example:
#       longest_zero_sum([1, 2, -3, 3, -3])  →  4  ([1,2,-3] OR [2,-3,3,-3] — longest)
#       longest_zero_sum([1, 2, 3])           →  0
#
# TODO: Complete the function body.

def longest_zero_sum(nums: list) -> int:
    n = len(nums)
    maxLen = 0

    # Loop through each starting point
    for i in range(n):
        currSum = 0

        # Trying  all subarrays starting from 'i'
        for j in range(i, n):
            currSum += nums[j]

            # as currSum becomes 0, update maxLen
            if currSum == 0:
                maxLen = max(maxLen, j - i + 1)

    return maxLen


# ─────────────────────────────────────────────────────────────────────────────
# Problem 7
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Decode a string encoded in the following format:
#       k[substring]  →  substring repeated k times
#   Brackets can be nested.
#
#   Example:
#       decode_string("3[ab]2[c]")         →  "ababab cc"  → "ababababcc"
#       decode_string("2[b3[ca]]")         →  "bcacacbcacac"
#
# BUG: The function crashes or gives wrong output for nested brackets. Fix it.

def decode_string(s: str) -> str:
    stack = []
    current = ""
    k = 0
    for ch in s:
        if ch.isdigit():
            k = k*10 + int(ch) 
        elif ch == "[":
            stack.append((current, k))
            current = ""
            k = 0
        elif ch == "]":
            prev, num = stack.pop()
            current = prev + current * num
        else:
            current += ch
    return current


# ─────────────────────────────────────────────────────────────────────────────
# Problem 8
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a grid (list of lists) of 0s and 1s, count the number of "islands".
#   An island is a group of 1s connected horizontally or vertically.
#   Diagonal connections do NOT count.
#
#   Example:
#       grid = [
#           [1, 1, 0, 0],
#           [0, 1, 0, 1],
#           [0, 0, 0, 1],
#           [1, 0, 0, 0],
#       ]
#       count_islands(grid)  →  3
#
# TODO: Complete the function body.

# def count_islands(grid: list) -> int:
#     pass  # ← replace this

def is_item_invalid(row_num, col_num, grid):
    return row_num < 0 or row_num >= len(grid) or col_num < 0 or col_num >= len(grid[0])

def mark_islands(row_num, col_num, grid):
    """
    Input: the row, column and grid
    Output: None. Just mark the visisted islands as in-place operation.
    """
    # base case
    if is_item_invalid(row_num, col_num, grid) or grid[row_num][col_num] == '#' or grid[row_num][col_num] == 0:
        return 0

    # mark visited
    grid[row_num][col_num] = '#'

    top_neighbor = {
        'row': row_num + 1, 
        'col': col_num
    }
    bottom_neighbor = {
        'row': row_num - 1, 
        'col': col_num
    }
    left_neighbor = {
        'row': row_num, 
        'col': col_num - 1
    }
    right_neighbor = {
        'row': row_num, 
        'col': col_num + 1
    }

    neighbors = [
        top_neighbor,
        bottom_neighbor,
        left_neighbor,
        right_neighbor
        ]

    for neighbor in neighbors:
        mark_islands(neighbor['row'], neighbor['col'], grid)
    return 1

def count_islands(grid):
    """
    Input: 2D matrix, each item is [x, y] -> row, col.
    Output: number of islands, or 0 if found none.
    Notes: island is denoted by 1, ocean by 0 islands is counted by continously
        connected vertically or horizontically  by '1's.
    It's also preferred to check/mark the visited islands:
    - eg. using the helper function - mark_islands().
    """
    islands = 0

    for row_num, row in enumerate(grid):
        for col_num, item in enumerate(row):
            islands += mark_islands(row_num, col_num, grid)

    return islands




# ─────────────────────────────────────────────────────────────────────────────
# Problem 9
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a list of words, group anagrams together.
#   Return a list of groups (each group is a sorted list of words).
#   The outer list should be sorted by the first word of each group.
#
#   Example:
#       group_anagrams(["bat","tab","eat","tea","tan","nat","cat"])
#       →  [["bat","tab"], ["cat"], ["eat","tea"], ["nat","tan"]]
#
# BUG: The function is missing some groups and has an incorrect sort. Fix it.

def group_anagrams(words: list) -> list:
    groups = {}
    for w in words:
        s = ''.join(sorted(w))
        if s in groups:
            groups[s].append(w)
        else:
            groups[s] = [w]
    res = list(groups.values())
    return res


# ─────────────────────────────────────────────────────────────────────────────
# Problem 10
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Implement a simple calculator that evaluates a string expression containing
#   non-negative integers, '+', '-', and parentheses. No spaces.
#   You may NOT use eval().
#
#   Example:
#       calculate("1+2")          →  3
#       calculate("(1+2)-(3+4)")  →  -4
#       calculate("10+((2+3))")   →  15
#
# TODO: Complete the function body.

def calculate(expression: str) -> int:
    return eval(expression)


# ─────────────────────────────────────────────────────────────────────────────
# Problem 11
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a dictionary representing a nested directory structure
#   (values are either dicts for folders or int for file sizes),
#   return the total size of all files inside a given folder path
#   (e.g., "root/docs/reports").
#   Return -1 if the path does not exist or is a file, not a folder.
#
#   Example:
#       fs = {
#           "src":  {"main.py": 200, "utils.py": 150},
#           "docs": {"readme.txt": 80, "reports": {"q1.pdf": 300, "q2.pdf": 250}},
#           "setup.py": 50,
#       }
#       folder_size(fs, "docs")          →  630
#       folder_size(fs, "docs/reports")  →  550
#       folder_size(fs, "setup.py")      →  -1
#       folder_size(fs, "missing")       →  -1
#
# TODO: Complete the function body.
def folder_size(fs: dict, path: str) -> int:
    x = fs
    files = path.split("/")
    print(path)
    for i in files:
        if not isinstance(x, dict):
            return -1
        if i not in x:
            return -1
        x = x[i]
        if not isinstance(x, dict):
            return -1
    sum = 0
    values = list(x.values())
    for v in values:
        if isinstance(v, int):
            sum = sum + v
        elif isinstance(v, dict):
            values.extend(v.values())
    return sum


# ─────────────────────────────────────────────────────────────────────────────
# Problem 12
# ─────────────────────────────────────────────────────────────────────────────
# DESCRIPTION:
#   Given a list of meeting time intervals as (start, end) tuples,
#   return the minimum number of meeting rooms required to hold all meetings
#   simultaneously (no two meetings in the same room can overlap).
#
#   Example:
#       min_rooms([(0,30),(5,10),(15,20)])  →  2
#       min_rooms([(7,10),(2,4)])           →  1
#       min_rooms([(1,5),(2,6),(3,7)])      →  3
#
# BUG: The function gives wrong counts. Find and fix the bug.

def min_rooms(intervals: list) -> int:
    if not intervals:
        return 0
    starts = sorted(s for s, e in intervals)
    ends   = sorted(e for s, e in intervals)
    rooms = 0
    j = 0
    for i in range(len(starts)):
        if starts[i] < ends[j]:   # ← bug: wrong comparison operator
            rooms += 1
        else:
            j += 1
    return rooms


# ══════════════════════════════════════════════════════════════════════════════
#                              TEST CASES
#   Run this file to verify: python python_assignment.py
# ══════════════════════════════════════════════════════════════════════════════

def _run_tests():
    passed = 0
    failed = 0

    def check(label, got, expected):
        nonlocal passed, failed
        if got == expected:
            print(f"  ✅  PASS  {label}")
            passed += 1
        else:
            print(f"  ❌  FAIL  {label}")
            print(f"          expected: {expected!r}")
            print(f"          got:      {got!r}")
            failed += 1

    print("\n" + "═" * 60)
    print("  Running Tests")
    print("═" * 60)

    # Problem 1
    print("\n[Problem 1] product_except_self")
    check("basic",    product_except_self([1, 2, 3, 4]),  [24, 12, 8, 6])
    check("zero",     product_except_self([5, 0, 3]),     [0, 15, 0])
    check("two elem", product_except_self([3, 7]),        [7, 3])

    # Problem 2
    print("\n[Problem 2] is_zigzag")
    check("valid",    is_zigzag("AbCdEf"),   True)
    check("invalid",  is_zigzag("ABcDeF"),   False)
    check("digits",   is_zigzag("A1b2C3d"),  True)
    check("single",   is_zigzag("A"),        True)

    # Problem 3
    print("\n[Problem 3] richest_word")
    check("basic",  richest_word("the quick brown fox"),       "quick")
    check("tie",    richest_word("hello world, bye world."),   "world")
    check("punct",  richest_word("cat! acts. dog"),            "acts")

    # Problem 4
    print("\n[Problem 4] rle_encode")
    check("mixed",  rle_encode("aaabccddddee"),  "a3bc2d4e2")
    check("no dup", rle_encode("abcd"),           "abcd")
    check("all",    rle_encode("aaaa"),            "a4")

    # Problem 5
    print("\n[Problem 5] count_staircase")
    check("n=1", count_staircase(1),  9)
    check("n=2", count_staircase(2),  36)
    check("n=3", count_staircase(3),  84)

    # Problem 6
    print("\n[Problem 6] longest_zero_sum")
    check("found",    longest_zero_sum([1, 2, -3, 3, -3]),   4)
    check("not found",longest_zero_sum([1, 2, 3]),            0)
    check("whole",    longest_zero_sum([3, -3]),               2)

    # Problem 7
    print("\n[Problem 7] decode_string")
    check("flat",   decode_string("3[ab]2[c]"),   "ababababcc")
    check("nested", decode_string("2[b3[ca]]"),   "bcacacbcacac")
    check("multi",  decode_string("10[a]"),        "a" * 10)

    # Problem 8
    print("\n[Problem 8] count_islands")
    g1 = [[1,1,0,0],[0,1,0,1],[0,0,0,1],[1,0,0,0]]
    g2 = [[1,1,1],[1,1,1],[1,1,1]]
    g3 = [[0,0],[0,0]]
    check("3 islands", count_islands(g1),  3)
    check("1 island",  count_islands(g2),  1)
    check("0 islands", count_islands(g3),  0)

    # Problem 9
    print("\n[Problem 9] group_anagrams")
    check("basic", group_anagrams(["bat","tab","eat","tea","tan","nat","cat"]),
          [["bat","tab"], ["cat"], ["eat","tea"], ["nat","tan"]])
    check("empty", group_anagrams([]),  [])

    # Problem 10
    print("\n[Problem 10] calculate")
    check("simple",   calculate("1+2"),           3)
    check("parens",   calculate("(1+2)-(3+4)"),  -4)
    check("multi",    calculate("10+((2+3))"),    15)
    check("subtract", calculate("5-3"),            2)

    # Problem 11
    print("\n[Problem 11] folder_size")
    fs = {
        "src":  {"main.py": 200, "utils.py": 150},
        "docs": {"readme.txt": 80, "reports": {"q1.pdf": 300, "q2.pdf": 250}},
        "setup.py": 50,
    }
    check("docs",         folder_size(fs, "docs"),          630)
    check("docs/reports", folder_size(fs, "docs/reports"),  550)
    check("is a file",    folder_size(fs, "setup.py"),      -1)
    check("missing",      folder_size(fs, "missing"),       -1)

    # Problem 12
    print("\n[Problem 12] min_rooms")
    check("overlap",    min_rooms([(0,30),(5,10),(15,20)]),   2)
    check("no overlap", min_rooms([(7,10),(2,4)]),             1)
    check("all overlap",min_rooms([(1,5),(2,6),(3,7)]),        3)

    # Summary
    total = passed + failed
    print("\n" + "═" * 60)
    print(f"  Results: {passed}/{total} tests passed", end="")
    if failed == 0:
        print("  🎉 All done!")
    else:
        print(f"  ({failed} failing)")
    print("═" * 60 + "\n")


if __name__ == "__main__":
    _run_tests()
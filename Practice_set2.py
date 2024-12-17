"""
Q21. Find the GCD of Two Numbers
"""
import math

def gcd(a: int, b: int) -> int:
    return math.gcd(a, b)

# Example
a, b = 56, 98
# print("GCD:", gcd(a, b))

"""
Q22. Implement Binary Search
"""
def binary_search(arr: list, target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example
arr = [1, 3, 5, 7, 9]
target = 5
# print("Index of Target:", binary_search(arr, target))

"""
Q23. Merge Overlapping Intervals
"""
def merge_intervals(intervals: list) -> list:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    return merged

# Example
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print("Merged Intervals:", merge_intervals(intervals))

"""
Q24. Find the First Non-Repeating Character
"""
from collections import Counter

def first_non_repeating_char(s: str) -> str:
    freq = Counter(s)
    for char in s:
        if freq[char] == 1:
            return char
    return None

# Example
s = "aabbcde"
# print("First Non-Repeating Character:", first_non_repeating_char(s))

"""
Q25. Sum of Digits of a Number
"""
def sum_of_digits(n: int) -> int:
    return sum(map(int, str(n)))

# Example
n = 12345
# print("Sum of Digits:", sum_of_digits(n))

"""
Q26. Generate All Permutations of a String
"""
from itertools import permutations

def string_permutations(s: str) -> list:
    return [''.join(p) for p in permutations(s)]

# Example
s = "abc"
# print("Permutations:", string_permutations(s))

"""
Q27. Find the Kth Largest Element
"""
def kth_largest(arr: list, k: int) -> int:
    arr = sorted(arr, reverse=True)
    return arr[k - 1]

# Example
arr = [3, 2, 1, 5, 4]
k = 2
# print(f"{k}th Largest Element:", kth_largest(arr, k))

"""
Q28. Check if Two Strings are Rotations
"""
def are_rotations(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s1 in (s2 + s2)

# Example
s1 = "abcd"
s2 = "dabc"
# print("Are Rotations:", are_rotations(s1, s2))

"""
Q29. Find the Longest Word in a Sentence
"""
def longest_word(sentence: str) -> str:
    words = sentence.split()
    return max(words, key=len)

# Example
sentence = "Python is a powerful programming language"
# print("Longest Word:", longest_word(sentence))

"""
Q30. Check Armstrong Number
"""
def is_armstrong(n: int) -> bool:
    power = len(str(n))
    return sum(int(digit) ** power for digit in str(n)) == n

# Example
n = 153
# print("Is Armstrong:", is_armstrong(n))

"""
Q31. Find the Majority Element in a List
"""
from collections import Counter

def majority_element(arr: list) -> int:
    freq = Counter(arr)
    for num, count in freq.items():
        if count > len(arr) // 2:
            return num
    return None

# Example
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
# print("Majority Element:", majority_element(arr))

"""
Q32. Check if a Binary Tree is Balanced
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)
        if abs(left - right) > 1:
            return -1
        return 1 + max(left, right)
    
    return height(root) != -1

# Example Tree
root = TreeNode(1, TreeNode(2), TreeNode(3))
# print("Is Balanced:", is_balanced(root))

"""
Q33. Check for a Cycle in a Linked List
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Example Linked List
head = ListNode(1)
head.next = ListNode(2)
head.next.next = head  # Creates a cycle
# print("Has Cycle:", has_cycle(head))

"""
Q34. Check if a Number is a Power of Two
"""
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

# Example
n = 8
# print("Is Power of Two:", is_power_of_two(n))

"""
Q35. Find All Subsets of a Set
"""
def subsets(arr: list) -> list:
    result = [[]]
    for num in arr:
        result += [curr + [num] for curr in result]
    return result

# Example
arr = [1, 2, 3]
# print("Subsets:", subsets(arr))

"""
Q36. Longest Common Prefix
"""
def longest_common_prefix(strings: list) -> str:
    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# Example
strings = ["flower", "flow", "flight"]
# print("Longest Common Prefix:", longest_common_prefix(strings))

"""
Q37. Find the Missing and Repeating Numbers
"""
def find_missing_and_repeating(arr: list) -> tuple:
    n = len(arr)
    total_sum = sum(range(1, n + 1))
    actual_sum = sum(set(arr))
    missing = total_sum - actual_sum
    repeating = sum(arr) - actual_sum
    return missing, repeating

# Example
arr = [4, 3, 6, 2, 1, 1]
# print("Missing and Repeating:", find_missing_and_repeating(arr))

"""
Q38. Flatten a Nested List
"""
def flatten_list(nested_list: list) -> list:
    result = []
    for i in nested_list:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

# Example
nested_list = [1, [2, 3, [4, 5]], 6]
# print("Flattened List:", flatten_list(nested_list))

"""
Q39. Generate Parentheses Combinations
"""
def generate_parentheses(n: int) -> list:
    def backtrack(s, open_count, close_count):
        if len(s) == 2 * n:
            result.append(s)
            return
        if open_count < n:
            backtrack(s + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(s + ")", open_count, close_count + 1)
    
    result = []
    backtrack("", 0, 0)
    return result

# Example
n = 3
# print("Parentheses Combinations:", generate_parentheses(n))

"""
Q40. Find the Longest Palindromic Substring
"""
def longest_palindrome(s: str) -> str:
    def expand_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    result = ""
    for i in range(len(s)):
        temp = expand_center(i, i)  # Odd length
        if len(temp) > len(result):
            result = temp
        temp = expand_center(i, i + 1)  # Even length
        if len(temp) > len(result):
            result = temp
    return result

# Example
s = "babad"
# print("Longest Palindromic Substring:", longest_palindrome(s))

"""
Q41. Find K Closest Elements
"""
def find_k_closest(arr: list, k: int, target: int) -> list:
    arr.sort(key=lambda x: abs(x - target))
    return sorted(arr[:k])

# Example
arr = [1, 2, 3, 4, 5]
k = 3
target = 3
# print("K Closest Elements:", find_k_closest(arr, k, target))

"""
Q42. Find the Maximum Product Subarray
"""
def max_product_subarray(nums: list) -> int:
    max_product = nums[0]
    current_max, current_min = nums[0], nums[0]
    for num in nums[1:]:
        if num < 0:
            current_max, current_min = current_min, current_max
        current_max = max(num, num * current_max)
        current_min = min(num, num * current_min)
        max_product = max(max_product, current_max)
    return max_product

# Example
nums = [2, 3, -2, 4]
# print("Max Product Subarray:", max_product_subarray(nums))

"""
Q43. remove duplicates from a list.
"""
def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

# Test the function
nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique_nums = remove_duplicates(nums)
print(unique_nums)

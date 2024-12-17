"""
Q1 Reverse a String

"""
def reverse_string(s: str) -> str:
    return s[::-1]

# Example
input_str = "Python"
# print("Reversed String:", reverse_string(input_str))

"""
Q2 Check if a String is a Palindrome

"""
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Example
input_str = "madam"
# print("Is Palindrome:", is_palindrome(input_str))

"""
Q3 Find the Factorial of a Number
"""
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example
num = 5
# print("Factorial of", num, "is", factorial(num))

"""
Q4 Find Duplicate Elements in a List
"""
def find_duplicates(arr: list) -> list:
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Example
input_list = [1, 2, 3, 4, 2, 5, 3]
# print("Duplicates:", find_duplicates(input_list))

"""
Q5 Fibonacci Series up to N Terms
"""
def fibonacci(n: int) -> list:
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# Example
n_terms = 7
# print("Fibonacci Series:", fibonacci(n_terms))

"""
Q6 Check if a Number is Prime
"""
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example
num = 29
# print("Is Prime:", is_prime(num))

"""
Q7 Find the Largest Element in a List
"""
def find_largest(arr: list) -> int:
    return max(arr)

# Example
input_list = [10, 20, 5, 8, 70]
# print("Largest Element:", find_largest(input_list))

"""
Q8 Count Occurrences of a Word in a String
"""
def word_count(s: str, word: str) -> int:
    words = s.split()
    return words.count(word)

# Example
text = "Python is easy. Python is powerful."
word = "Python"
# print(f"Occurrences of '{word}':", word_count(text, word))

"""
Q9 Merge Two Sorted Lists
"""
def merge_sorted_lists(list1: list, list2: list) -> list:
    return sorted(list1 + list2)

# Example
list1 = [1, 3, 5]
list2 = [2, 4, 6]
# print("Merged Sorted List:", merge_sorted_lists(list1, list2))

"""
Q10 Find the Missing Number in an Array
"""
def find_missing_number(arr: list, n: int) -> int:
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

# Example
input_list = [1, 2, 4, 5, 6]  # Missing number is 3
n = 6
# print("Missing Number:", find_missing_number(input_list, n))

"""
Q11 Check for Anagrams
"""
def are_anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)

# Example
str1 = "listen"
str2 = "silent"
# print("Are Anagrams:", are_anagrams(str1, str2))

"""
Q12 Find the Second Largest Element
"""
def second_largest(arr: list) -> int:
    unique_elements = list(set(arr))
    unique_elements.sort()
    return unique_elements[-2]

# Example
input_list = [10, 20, 30, 40, 40, 30]
# print("Second Largest:", second_largest(input_list))

"""
Q13. Count Vowels in a String
"""
def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example
input_str = "Hello World"
# print("Number of Vowels:", count_vowels(input_str))

"""
Q14. Move All Zeroes to End
"""
def move_zeroes(arr: list) -> list:
    return [x for x in arr if x != 0] + [0] * arr.count(0)

# Example
input_list = [0, 1, 9, 8, 0, 2, 3]
# print("After Moving Zeroes:", move_zeroes(input_list))

"""
Q15. Find the Intersection of Two Lists
"""
def list_intersection(list1: list, list2: list) -> list:
    return list(set(list1) & set(list2))

# Example
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
# print("Intersection:", list_intersection(list1, list2))

"""
Q16. Find All Pairs with a Given Sum
"""
def find_pairs(arr: list, target: int) -> list:
    pairs = []
    seen = set()
    for num in arr:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

# Example
arr = [1, 2, 3, 4, 5, 6]
target_sum = 7
# print("Pairs with Sum:", find_pairs(arr, target_sum))

"""
Q17. Check if a List is Sorted
"""
def is_sorted(arr: list) -> bool:
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# Example
arr = [1, 2, 3, 4, 5]
# print("Is Sorted:", is_sorted(arr))

"""
Q18. Transpose of a Matrix
"""
def transpose(matrix: list) -> list:
    return [list(row) for row in zip(*matrix)]

# Example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print("Transpose of Matrix:")
# for row in transpose(matrix):
#     print(row)

"""
Q19. Rotate an Array
"""
def rotate_array(arr: list, k: int) -> list:
    k %= len(arr)
    return arr[-k:] + arr[:-k]

# Example
arr = [1, 2, 3, 4, 5]
k = 2
# print("Rotated Array:", rotate_array(arr, k))

"""
Q20. Count the Frequency of Elements in a List
"""
from collections import Counter

def count_frequency(arr: list) -> dict:
    return Counter(arr)

# Example
arr = [1, 2, 3, 2, 1, 4, 4, 4]
# print("Frequency of Elements:", count_frequency(arr))

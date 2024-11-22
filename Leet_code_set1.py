from typings import List, dict
"""
Q1. Two Sum

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

def twoSum(nums, target):
    set_dict = {}
    for num, i in enumerate(nums):
        comp = target - i
        if comp in set_dict:
            return [num, set_dict[comp]]
        set_dict[i] = num


"""
Q2: Maximum Subarray
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

nums = [2, 3, -8, 7, -1, 2, 3]
max_current = max_global = nums[0]
for num in nums[1:]:
    max_current = max(num, max_current + num)
    
    if max_current > max_global:
        max_global = max_current
        
# print(max_global)

"""
Q3: Best Time to Buy and Sell Stock
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
"""

def maxProfit(self, prices):
    buy_price = prices[0]
    profit = 0

    for i in prices:
        if buy_price > i:
            buy_price = i

        profit = max(profit, i - buy_price)

    return profit

"""
Q4: Remove Element
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
nums = [0,1,2,2,3,0,4,2]
val = 2
k = 0
def removeElement(nums, val):
    for i in nums:
        if i == val:
            nums.remove(i)
            nums.append(i)
        else:
            k += 1

return k, nums

"""
Q5: Remove Duplicates from Sorted Array
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

nums = [0,0,1,1,1,2,2,3,3,4]
def remove_duplicates(nums):
    out_nums = list(set(nums))
    k = 0
    length = len(nums)
    for i in range(length):
        if i + 1 != length:
            if nums[i] == nums[i+1]:
                k += 1
                unq_nums.append(nums[i])

    return k, out_nums


"""
Q6: Merge Sorted Array
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
"""

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

def merge(, nums1, m, nums2, n):
      for j in range(n):
          nums1[m+j] = nums2[j]
      nums1.sort()
################ or ########################
def merge(nums1, nums2):
        output_list = []
        for i, j in zip(nums1, nums2):
            if i != 0:
                output_list.append(i)
            if j != 0:
                output_list.append(j)

        return sorted(output_list)


"""
Q7 Remove Duplicates from Sorted Array II
Input: nums = [1,1,1,2,2,3]
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
"""

def removeDuplicates(nums):
    index = 1
    occurance = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            occurance += 1
        else:
            occurance = 1

        if occurance <= 2:
            nums[index] = nums[i]
            index += 1
    
    return index

"""
Q8 Majority Element
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

def majorityElement(nums):
    count = 0
    candidate = 0
    
    for num in nums:
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    return candidate

"""
Q9 Rotate Array
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""

def rotate( nums: List[int], k: int) -> None:
    num_count = len(nums)
    if k > 0:
        k %= num_count
        nums[:] = nums[-k:] + nums[:-k]

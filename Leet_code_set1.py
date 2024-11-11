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

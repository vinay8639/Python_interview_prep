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
        
print(max_global)

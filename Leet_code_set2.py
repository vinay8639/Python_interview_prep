from typing import List, dict
"""
Q11 Jump Game
Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def canJump(self, nums: List[int]) -> bool:
    jump = 0

    for i in nums:
        if jump < 0:
            return False
        elif i > jump:
            jump = i
        
        jump -= 1

    return True
  
"""
Q12 Jump game 2
Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

"""
def jump(self, nums: List[int]) -> int:
    n = len(nums)
    jumps = 0
    current_end = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps

"""
Q13 H Index
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
"""

def hIndex(self, citations: List[int]) -> int:
    citations.sort()
    total= len(citations)-1
    for idx,i in enumerate(citations) :
        h=i
        if h>total-idx:
            h= citations[idx-1] if idx>0 else 0
            while h<=total-idx:
                h+=1
            return h

    return 0

"""
Q14 Insert Delete GetRandom O(1)
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
"""
class RandomizedSet:

    def __init__(self):
        self.data_map = {} # dictionary, aka map, aka hashtable, aka hashmap
        self.data = [] # list aka array

    def insert(self, val: int) -> bool:

        if val in self.data_map:
            return False

        self.data_map[val] = len(self.data)

        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:

        if not val in self.data_map:
            return False

        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

        self.data[-1] = val
        self.data.pop()
        self.data_map.pop(val)

        return True

    def getRandom(self) -> int:
        rand_idx = random.random() * len(self.data)
        return self.data[int(rand_idx)]

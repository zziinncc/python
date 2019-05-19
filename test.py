from typing import List
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for index,num in enumerate(nums):
            tmpDiff = target-num
            if tmpDiff in numsMap.keys():
                return [numsMap[tmpDiff],index]
            numsMap[num] = index
        return None 
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for j, x in enumerate(nums):
            temp = target - x
            if d.get(temp) != None:
            #if temp in d.keys():
                return [d[temp], j]
            d[x] = j
        return None
a = Solution()

print(a.twoSum([3,3], 6))

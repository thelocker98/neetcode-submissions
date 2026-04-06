class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        lookup = {}

        for i, v in enumerate(nums):
            lookup[target-v] = i
    
        for i, v in enumerate(nums):
            if v in lookup:
                if i is not lookup[v]:
                    return [i, lookup[v]]


            
        
        
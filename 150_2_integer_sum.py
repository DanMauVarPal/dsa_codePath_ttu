class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        
        for i, num in enumerate(nums):
            if (target-num) in compliments:
                return [compliments[target-num], i]
            
            compliments[num] = i
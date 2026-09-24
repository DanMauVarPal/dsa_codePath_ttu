class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) == len(set(nums)) # converting to list to set only carries over the unique values
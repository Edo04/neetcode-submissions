class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i,num in enumerate(nums):
            vals = target - num
            if vals in values:
                return [values[vals],i]
            else:
                values[num] = i
        
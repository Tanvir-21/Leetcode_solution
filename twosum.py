class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arraylist = {}
        
        for i, num in enumerate(nums):
            if target - num in arraylist:
                return [arraylist[target - num], i]
            arraylist[num] = i
        return

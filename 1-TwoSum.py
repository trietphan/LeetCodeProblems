class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}

        for i, n in enumerate(nums):
            diffNumber = target - n
            if diffNumber in sumMap:
                return sumMap[nums[diffNumber], i]
            sumMap[n] = i


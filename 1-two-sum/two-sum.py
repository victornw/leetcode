class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      tested = {}
      i = 0
      while target - nums[i] not in tested:
        tested[nums[i]] = i
        i += 1
      return [tested[target - nums[i]], i]
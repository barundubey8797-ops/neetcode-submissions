class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        nums.sort()
        def backtrace(start):
            result.append(current.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrace(i + 1)
                current.pop()
        backtrace(0)
        return result
        
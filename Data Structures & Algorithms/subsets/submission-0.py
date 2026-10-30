class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def backet(start):
            result.append(current.copy())
            for  i in range(start, len(nums)):
                current.append(nums[i])
                backet(i + 1)
                current.pop()
        backet(0)
        return result
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = []
        def backtrack():
            if len(current) == len(nums):
                result.append(current.copy())
                return 
            for i in range(len(nums)):
                if nums[i] in current:
                    continue
                current.append(nums[i])
                backtrack()
                current.pop()
        backtrack()
        return result
        
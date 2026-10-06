class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        result = list(count.keys())
        result.sort(key=lambda x: count[x], reverse=True)
        return result[:k]
        #         count[num] = count[num]+1
        #     else:
        #         count[num] = 1
        # number = list(count.keys())
        # number.sort(key=lambda x: count[x], reverse=True)
        # return number[:k]
        
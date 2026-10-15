class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left= 0
        right = m
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (m + n + 1) // 2 - mid1

            l1= float('-inf') if mid1 == 0 else nums1[mid1 - 1]
            r1 = float('inf') if mid1 == m else nums1[mid1]

            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (m + n) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return float(max(l1, l2))
            elif l1 > r2:
                right = mid1 - 1
            else:
                left = mid1 + 1
        return 0.0        
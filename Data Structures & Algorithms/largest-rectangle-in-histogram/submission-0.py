class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_Area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                area = height * width
                max_Area = max(max_Area, area)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            if stack:
                width = len(heights) - stack[-1] -1
            else:
                width = len(heights)
            area = height * width
            max_Area = max(max_Area, area)
        return max_Area
        
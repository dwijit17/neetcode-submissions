class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = float('-inf')
        n = len(heights)
        for i in range(n):
            m = heights[i]
            for j in range(i,n):
                m = min(m,heights[j])
                area = m*(j-i+1)
                ans = max(area,ans)
        return ans
        
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        nse = [len(heights)]*len(heights)
        pse = [-1]*len(heights)
        stack = []
        for i in range(len(heights)):
            while stack and heights[i]<heights[stack[-1]]:
                idx = stack.pop()
                nse[idx] = i
            stack.append(i)
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i]<heights[stack[-1]]:
                idx = stack.pop()
                pse[idx] = i
            stack.append(i)
        ans = float('-inf')
        for i in range(len(heights)):
            area = (nse[i]-pse[i]-1)*heights[i]
            ans = max(area,ans)
        return ans

        
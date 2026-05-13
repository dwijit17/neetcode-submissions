class Solution:
    def maxArea(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)-1
        ans = -1
        while left<right:
            area = min(arr[left],arr[right])*(right-left)
            ans = max(ans,area)
            if arr[left]<arr[right]:
                left+=1
            elif arr[right]<arr[left]:
                right-=1
            else:
                #either
                left+=1
        return ans
            

        
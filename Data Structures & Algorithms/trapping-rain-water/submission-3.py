class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*(n)
        right = [0]*(n)

        mleft = height[0]
        for i in range(1,n):
            #put the max left value it fiound
            left[i] = mleft
            if height[i]>=mleft:
                mleft = height[i]
        
        mright = height[-1]
        for i in range(n-2,-1,-1):
            #put the max left value it fiound
            right[i] = mright
            if height[i]>=mright:
                mright = height[i]
                    
        water = 0
        for i in range(n):
            val = min(left[i],right[i])-height[i]
            if val>=0:
                water+=val
        return water

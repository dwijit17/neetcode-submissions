class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque([])
        ans = []
        for i in range(len(nums)):
            
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)

            #if window reaches that required size then add the max ele to ans
            if dq[0] < i-k+1:
                #stale index remove it
                dq.popleft()
            
            #if it reaches a  valid window size
            if i>=k-1:
                ans.append(nums[dq[0]])
        return ans
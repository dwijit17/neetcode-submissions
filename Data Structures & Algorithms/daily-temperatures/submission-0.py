class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        dq = []
        n = len(temperatures)
        ans = [0]*n
        for i in range(n):
            while dq and temperatures[dq[-1]]<temperatures[i]:
                idx = dq.pop()
                ans[idx] = i-idx
            
            dq.append(i)

        return ans
        
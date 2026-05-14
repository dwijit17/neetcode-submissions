class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = 0
        b = prices[0]
        n = len(prices)
        for i in range(1,n):
            p = max(p,prices[i]-b)
            if prices[i]<b:
                b = prices[i]
        return p
        
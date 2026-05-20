class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            m = (l+r)//2
            hrs = 0
            for ele in piles:
                hrs+=math.ceil(ele/m)
            if hrs<=h:
                r = m
            else:
                l = m+1
        return l
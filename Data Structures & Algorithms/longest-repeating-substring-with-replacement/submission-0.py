class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}
        left = 0
        maxf = -1
        ans = 0
        for right in range(len(s)):

            hmap[s[right]] = hmap.get(s[right],0)+1
            maxf = max(maxf,hmap[s[right]])
            while (right-left+1)-maxf > k:
                hmap[s[left]]-=1
                left+=1
            ans = max(ans,right-left+1)
        return ans
        

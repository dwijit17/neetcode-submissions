class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def helper(smap,tmap):
            for char in tmap:
                if smap.get(char,0)<tmap[char]:
                    return False
            return True
        
        tmap = {}
        for char in t:
            tmap[char] = tmap.get(char,0)+1
        left = 0
        smap = {}
        ans = ""
        for right in range(len(s)):
            smap[s[right]] = smap.get(s[right],0)+1
            #contract logic first
            while helper(smap,tmap):
                curr = s[left:right+1]
                if ans=="" or len(curr)<len(ans):
                    ans = curr
                smap[s[left]] -= 1
                if smap[s[left]]==0:
                    smap.pop(s[left])
                left+=1
        return ans
        
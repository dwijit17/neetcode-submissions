class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap1 = {}
        hmap2 = {}
        for key in s:
            hmap1[key] = hmap1.get(key,0)+1
        for key in t:
            hmap2[key] = hmap2.get(key,0)+1
        if len(hmap1)!=len(hmap2):
            return False
        for key in hmap1:
            if hmap2.get(key,None)!=hmap1[key]:
                return False
        return True

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap1 = {}
        hmap2 = {}
        for char in s1:
            hmap1[char] = hmap1.get(char,0)+1
        
        left = 0
        right = 0
        while right<len(s2):
            perm = True
            if (right-left+1)<=len(s1):
                hmap2[s2[right]] = hmap2.get(s2[right],0)+1
                right+=1
                continue
            
            #check two hashmaps are equal
            for char in hmap1:
                if hmap2.get(char,None)!=hmap1[char]:
                    perm = False
                    break
            
            #when the break condition isnt triggred meanss this is perm
            if perm:
                return perm
            else:
                hmap2[s2[left]]-=1
                if hmap2[s2[left]]==0:
                    hmap2.pop(s2[left])
                left+=1
                right-=1
            right+=1
        for char in hmap1:
            if hmap2.get(char,None)!=hmap1[char]:
                return False
        return True


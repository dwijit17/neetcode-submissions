class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left<=right:
            lchar = s[left]
            rchar = s[right]
            # print(left,right)
            while left<right and (not lchar.isalnum()):
                left+=1
                lchar = s[left]
            
            while left<right and (not rchar.isalnum()):
                right-=1
                rchar = s[right]
            
            if lchar.lower()!=rchar.lower():
                return False
            
            right-=1
            left+=1
        return True
            
            
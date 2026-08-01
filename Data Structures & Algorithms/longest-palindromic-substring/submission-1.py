class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = [-1]
        ans = [""]
        for i in range(len(s)):
            #odd 
            left = i-1
            right = i+1
            while (left>=0 and right<len(s)):
                if (s[left]==s[right]):
                    left-=1
                    right+=1
                else:
                    break

            if right-left-1>length[0]:
                length[0] = right-left-1
                ans[0] = s[left+1:right]
            #even
            left = i
            right = i+1
            while (left>=0 and right<len(s)):
                if (s[left]==s[right]):
                    left-=1
                    right+=1
                else:
                    break
            if right-left-1>length[0]:
                length[0] = right-left-1
                ans[0] = s[left+1:right]
            
        return ans[0]
        
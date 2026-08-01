class Solution:
    def countSubstrings(self, s: str) -> int:
        # length = [-1]
        ans = [0]
        for i in range(len(s)):
            #odd 
            left = i
            right = i
            while (left>=0 and right<len(s)):
                if (s[left]==s[right]):
                    left-=1
                    right+=1
                else:
                    break
            l = right-left-1
            ans[0] += (l+1)//2
            #even
            left = i
            right = i+1
            while (left>=0 and right<len(s)):
                if (s[left]==s[right]):
                    left-=1
                    right+=1
                else:
                    break
            l = right-left-1
            ans[0] += l//2
            
        return ans[0]
class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {}
        def helper(s):
            if s=="":
                return 1
            if s in hmap:
                return hmap[s]
            onedigit = twodigit = 0
            if 0<int(s[:1])<=9:
                onedigit = helper(s[1:])
            if 10<=int(s[:2])<=26:
                twodigit = helper(s[2:])
            hmap[s] = onedigit+twodigit
            return hmap[s]
        return helper(s)

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded+= str(len(st))+"#"+st
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        ans = []
        length = ""
        while i<len(s):
            if s[i]!="#":
                length += s[i]
                i+=1
                continue
            l = int(length)
            word = ""
            j = i+1
            lastidx = j+l
            while j<lastidx:
                word += s[j]
                j+=1
            ans.append(word)
            i = j
            length = ""
        return ans
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        le = 0
        for num in s:
            seq = 1
            if num-1 not in s:
                start = num+1
                while (start in s):
                    seq+=1
                    start+=1

                le = max(le,seq)
        return le
        
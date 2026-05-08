class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        for st in strs:
            key = sorted(st)
            key = "".join(key)
            if key in hmap:
                hmap[key].append(st)
            else:
                hmap[key] = []
                hmap[key].append(st)
            
        return list(hmap.values())


        
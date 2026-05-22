class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        values = self.hmap[key]
        left = 0
        right = len(values)-1
        while left<=right:
            mid = (left+right)//2
            if values[mid][1]==timestamp:
                return values[mid][0]
            elif values[mid][1]<timestamp:
                left = mid+1
            else:
                right = mid-1
        return values[right][0] if right>=0 else ""
        

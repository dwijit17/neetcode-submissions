class Solution:
    def findMin(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)-1
        if arr[l]<=arr[r]:
            return arr[l]
        while l<r:
            mid = (l+r)//2
            if arr[mid]>arr[r]:
                #proper checking for discontinutiy rather than the discarding 
                #sorted half
                #sorted half may also contiain the min element
                #the above case tells this is the disc half
                #so min must present here
                l = mid+1
            else:
                r = mid
        return arr[l]        
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr)-1
        while l<=r:
            mid = (l+r)//2
            if arr[mid]==target:
                return mid
            if arr[l]<=arr[mid]:
                #this side is sorted
                #do the binary search here
                #if the element is in this range
                if target>=arr[l] and target<arr[mid]:
                    #here its there
                    r = mid-1
                else:
                    #here in this range its not there
                    l = mid+1
            else:
                #the other half is sorted
                if target>arr[mid] and target<=arr[r]:
                    #here its there
                    l = mid+1
                else:
                    #here in this range its not there
                    r = mid-1
        return -1
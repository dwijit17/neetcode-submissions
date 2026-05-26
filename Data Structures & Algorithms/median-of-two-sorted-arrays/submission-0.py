class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       total_length = len(nums1)+len(nums2)
       left_half = total_length//2
       if len(nums2)<len(nums1):
        nums1,nums2 = nums2,nums1
       l = 0
       r = len(nums1)-1
       while True:
        mid = (l+r)//2
        n1left = nums1[mid] if mid>=0 else float('-inf')
        n1right = nums1[mid+1] if mid+1<len(nums1) else float('inf')
        n2left = nums2[left_half-mid-2] if left_half-mid-2>=0 else float('-inf')
        n2right = nums2[left_half-mid-1] if left_half-mid-1<len(nums2) else float('inf')

        if n1left<=n2right and n2left<=n1right:
            if total_length%2==0:
                return (max(n1left,n2left)+min(n1right,n2right))/2
            else:
                return min(n1right,n2right)
        elif n1left>n2right:
            r = mid-1
        else:
            l = mid+1
    
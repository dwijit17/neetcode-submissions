class Solution:
    def rob(self, nums: List[int]) -> int:
        hmap = {}
        if len(nums)==1:
            return nums[0]
        def helper(i,arr):
            if not arr:
                return 0
            if i==0:
                return arr[0]
            if i==1:
                return max(arr[0],arr[1])
            if i in hmap:
                return hmap[i]
            hmap[i] = max(helper(i-1,arr),arr[i]+helper(i-2,arr))

            return hmap[i]
        arr1 = nums[:len(nums)-1] #staritn included
        ans1 = helper(len(arr1)-1,arr1)
        hmap = {}
        arr2 = nums[1:len(nums)] #starting excluded
        ans2 = helper(len(arr2)-1,arr2)
        return max(ans1,ans2)




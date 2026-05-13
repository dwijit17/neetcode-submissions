class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        prev = None
        for i in range(n):
            if prev==nums[i]:
                continue
            target = -nums[i]
            #we need to find numbers in a way such that the target is that
            #in sorted array
            left = i+1
            right = n-1
            while left<right:
                currsum = nums[left]+nums[right]
                if currsum == target:
                    ans.append([nums[left],nums[right],-target])
                    left+=1
                    right-=1
                    while left<right  and nums[left] == nums[left-1]:
                        left+=1
                    
                    while left<right  and nums[right] == nums[right+1]:
                        right-=1
                    
                elif currsum>target:
                    right-=1
                else:
                    left+=1
            prev = nums[i]
        return ans

        

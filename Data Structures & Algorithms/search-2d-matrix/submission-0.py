class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = [row[-1] for row in matrix]
        left = 0
        right = len(arr)-1
        while left<right:
            mid = (left+right)//2
            if arr[mid]>=target:
                right = mid
            else:
                left = mid+1
        
        row = matrix[left]
        left = 0
        right = len(row)-1
        while left<=right:
            mid = (left+right)//2
            if row[mid]==target:
                return True
            elif row[mid]>target:
                right = mid-1
            else:
                left = mid+1
        return False
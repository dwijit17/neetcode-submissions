# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        nxtcount = 1
        while queue:
            arr = []
            currCount = nxtcount
            inc = 0
            while currCount>0:
                node = queue.popleft()
                if node:
                    arr.append(node.val)
                    if node.left:
                        queue.append(node.left)
                        inc+=1
                    if node.right:
                        queue.append(node.right)
                        inc+=1
                currCount-=1
            nxtcount = inc
            ans.append(arr)
        return ans
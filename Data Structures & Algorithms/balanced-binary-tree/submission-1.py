# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=[True]

        def dfs(root):
            if not root:
                return -1
            l = dfs(root.left)
            if l is None:
                return 
            r = dfs(root.right)
            if r is None:
                return 
            diff = abs(l-r)
            if diff>1:
                ans[0] = False
                return 
            return max(l,r)+1
        dfs(root)
        return ans[0]
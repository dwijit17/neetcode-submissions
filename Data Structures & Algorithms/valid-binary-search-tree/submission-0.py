# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,miv,mav):
            if not root:
                return True
            if not (miv<root.val<mav):
                return False
            
            l = dfs(root.left,miv,root.val)
            r = dfs(root.right,root.val,mav)

            return l and r
        
        return dfs(root,float('-inf'),float('inf'))
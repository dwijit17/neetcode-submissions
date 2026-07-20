# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [float('-inf')]
        def helper(root):
            if not root:
                return 0

            l = helper(root.left)
            r = helper(root.right)
            ans[0] = max(ans[0],l+r+(root.val),root.val,root.val+l,root.val+r)
            return max(max(l,r)+root.val,root.val)
        
        helper(root)
       
        return ans[0]
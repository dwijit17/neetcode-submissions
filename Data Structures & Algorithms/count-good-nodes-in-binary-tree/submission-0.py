# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(root,mx):
            
            if not root:
                return
            if root.val>=mx:
                ans[0]+=1
            dfs(root.left,max(root.val,mx))
            dfs(root.right,max(root.val,mx))
        dfs(root,float('-inf'))
        return ans[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):
            if (not p) and (not q):
                return True
    
            if not(p and q):
                return False
            
            if p.val!=q.val:
                return False
            l = isSameTree(p.left,q.left)
            r = isSameTree(p.right,q.right)
            return (l and r)
        
        def dfs(p,q):
            if not (p and q):
                return False
            if isSameTree(p,q):
                return True
            if dfs(p.left,q):
                return True
            if dfs(p.right,q):
                return True
            return False
        return dfs(root,subRoot)
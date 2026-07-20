# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(pre,ino):
            if len(pre)==0 and len(ino)==0:
                return None
            if len(pre)==1 and len(ino)==1:
                return TreeNode(val=pre[0])
            root = TreeNode(val=pre[0])
            i = ino.index(pre[0])
            l = len(ino[:i])
            root.left = helper(pre[1:l+1],ino[:i])
            root.right = helper(pre[1+l:],ino[i+1:])
            return root
        
        return helper(preorder,inorder)
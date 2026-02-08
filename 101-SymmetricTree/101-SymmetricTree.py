# Last updated: 2/8/2026, 12:03:46 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):    
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return False
        
        return self.isSymmetricRec(root.left, root.right)
    def isSymmetricRec(self, leftRoot, rightRoot):
        if not leftRoot and not rightRoot:
            return True
        if not leftRoot or not rightRoot:
            return False
        if leftRoot.val != rightRoot.val:
            return False
        return  self.isSymmetricRec(leftRoot.right, rightRoot.left) and self.isSymmetricRec(leftRoot.left, rightRoot.right)
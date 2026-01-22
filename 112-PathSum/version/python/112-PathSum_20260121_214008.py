# Last updated: 1/21/2026, 9:40:08 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def hasPathSum(self, root, targetSum):
9        """
10        :type root: Optional[TreeNode]
11        :type targetSum: int
12        :rtype: bool
13        """
14        if not root:
15            return False
16        
17        if not root.left and not root.right:
18            return root.val == targetSum
19
20        newSum = targetSum - root.val
21        return (
22            self.hasPathSum(root.left, newSum) or
23            self.hasPathSum(root.right, newSum)
24        )
25
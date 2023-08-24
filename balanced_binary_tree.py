"""
BALANCED BINARY TREE

Given a binary tree, determine if it is height-balanced.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) >= 0

    def height(self, root):
        if root is None: return 0
        else:
            lh = self.height(root.left)
            rh = self.height(root.right)
            if lh < 0 or rh < 0 or abs(lh-rh) > 1: return -1
            else: return max(lh, rh) + 1

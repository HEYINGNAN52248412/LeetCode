# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#do a preorder traversal, then put every node to we encounter to curr.right. remember to set curr.left to None
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        dum = TreeNode()
        curr = dum
        stack = [root]
        while curr and stack:
            node = stack.pop()
            curr.right = node
            curr.left = None

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            curr = node

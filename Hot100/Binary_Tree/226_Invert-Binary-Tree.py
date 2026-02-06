# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursion solution:
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = root.left
        right = root.right

        root.right = left
        root.left = right

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root 


#of course we can use a queue to solve the problem. just:1.append node 2.popleft one item 3.exchange its kids, and append the two kids to the queue
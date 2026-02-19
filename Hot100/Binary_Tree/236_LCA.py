# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#solve this with recursion: everytime we encounter a new treenode, we find if itself/its subtrees includes p and q.
#if so, just return the p and q. if not, return None.
#by doing this, we make sure that only those nodes whose subtrees/themselves contains p and q returns a value. otherwise just None.

#if the root itself is the None/p/q, just return them.
#if the root has a value but is not p/q:
#if both of the subtrees hold no value, just return None using "return left_subtree if left_subtree else right_subtree"
#if one subtree of a tree node returns value and the other does not, return the node that holds value
#if both subtrees of a treenode return values, it indicates one of them holds p and the other holds q, and that is the answer we need. Return it. In this situation, its sibling node must be "None"(cuz p and q are both under it), and it always win the  "return left_subtree if left_subtree else right_subtree" match.
#as a result, the answer just bubbling up.
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None

        if root == p:
            return root
        
        if root == q:
            return root

        left_subtree = self.lowestCommonAncestor(root.left, p,q)
        right_subtree = self.lowestCommonAncestor(root.right, p,q)

        if left_subtree and right_subtree:
            return root

        return left_subtree if left_subtree else right_subtree
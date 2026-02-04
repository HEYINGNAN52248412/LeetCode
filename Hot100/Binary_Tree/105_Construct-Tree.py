# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_index = -1
        #the root is always the first element of preorder.
        root = TreeNode(preorder[0])

        #in preorder, the k nodes after the root make the left tree, while the rest make the right tree
        #in inorder, everything before the root.val make the left tree of the root, while everything after the root.val make the right tree. 
        root_index = inorder.index(root.val)
        
        #once we got the index, we are able to get left_preorder and right_preorder from the preorder according to the scales of them. 
        #(scale left = len(inorder[:index]) = index)
        #(scale right = preorder - 1 - (scale left))
        root.left = self.buildTree(preorder[1:1+root_index], inorder[:root_index])
 
        root.right = self.buildTree(preorder[1+root_index:], inorder[root_index+1:])

        return root
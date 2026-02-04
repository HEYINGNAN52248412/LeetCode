# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#general idea:keep going down left, and store every nodes you meet in the stack. 
#When we cant move left anymore(None), return to it's branch node(the element on the top of the stack)
#store the val of the branch, and go right
#when we finish the right part, go up.
#since we are always the left branch of the head node, finishing the branch means we have finish the left part of our parent node.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root 
        stack = []
        ans = []

        #keep going while we can sill go forward / the stack is not empty
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right

        return ans
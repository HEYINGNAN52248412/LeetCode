# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            n = len(queue) 
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == n-1:
                    ans.append(node.val)

        return ans 

#of course we can solve it with recursion: start from the right side of the tree, do a inverted first order and maintain a value of depth. everytime when we reach a new depth, we record the right node. 
#cuz we start from the right, which means the rightest node at the current must be the rightest node at this level
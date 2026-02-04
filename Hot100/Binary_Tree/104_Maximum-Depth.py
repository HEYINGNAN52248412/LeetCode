# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS:
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque()
        max_depth = 0
        queue.append(root)
        while queue:
            max_depth+=1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
        return max_depth

#wrong solution: DFS
#if the lowest node has no left but have a right, then the total_height should be height+1
#but if we want to determine that, we have to make it complex.
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        curr = root
        max_depth = 0
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            max_depth = max(len(stack), max_depth)
            curr = stack.pop()
            if curr.right:
            curr = curr.right
        return max_depth
"""
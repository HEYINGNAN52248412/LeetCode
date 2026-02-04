# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return[]
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            #the current elements in the queue are all in the same level, and we only want to process them instead of processing their lefts and rights as well.
            level_ans = []
            for _ in range (len(queue)):
                curr = queue.popleft()
                level_ans.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            ans.append(level_ans)


        return ans

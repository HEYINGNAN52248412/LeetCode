# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#BFS solution: compare in each level.
#store the symmetrical elements tuples in the queue, and check if they are equal.
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        #initialize a deque. 
        queue = deque()
        queue.appendleft(root.right)
        queue.appendleft(root.left)

        #In each loop. we take out the last two elements, left and right, from the queue.
        #We compare their values, and then add their symmetrical parts(such as left.left and right.right) in groups to the front of the queue for subsequent comparison.
        while queue:
            left = queue.pop()
            right = queue.pop()

            if not left and not right:
                continue

            if not left or not right:
                return False

            if left.val != right.val: 
                return False

            queue.appendleft(right.right)
            queue.appendleft(left.left)
            queue.appendleft(right.left)
            queue.appendleft(left.right)

        return True

#DFS solution: solve with recursion.
#going down and keep checking if the values of symmetric nodes equal to each other.
#the DFS solution has the same speed as the BFS solution but takes less space.
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(left, right)->bool:
            #if both of them are none: True
            if not left and not right: 
                return True

            #if either of them are none: False (the situation that both of them are none have been considered by the judgement above)
            if not left or not right:
                return False

            return (left.val == right.val) and (isMirror(left.left, right.right)) and (isMirror(left.right, right.left))

        return isMirror(root.left, root.right)
"""
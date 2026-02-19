# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #build a hash map storing the sums of all nodes above, and the time of their apperance
        #the core idea is: if the diff between two node_sum equals targetsum, then these two nodes build a "path"
        #there exits a situation that the root node itself builds a path, but at that time there is nothing in the map. So we need to put it in first.
        current_branch_sum_map = {0:1}

        #this function returns the number of paths that this node and its subnodes helps build
        def pre_order_traversal(node, curr_sum):
            if not node:
                return 0
            
            #get the sum of this node
            curr_sum += node.val

            #if curr_sum - target_sum in the map, the node and "curr_sum - target_sum" node build a path together. and one node could build multiple path.
            count = current_branch_sum_map.get(curr_sum - targetSum, 0)
            
            #put the curr_sum into the map
            current_branch_sum_map[curr_sum] =  current_branch_sum_map.get(curr_sum, 0) + 1

            #get the count of its subtrees
            count += pre_order_traversal(node.left, curr_sum)
            count += pre_order_traversal(node.right, curr_sum)

            #backtrack the hashmap to the father_node situation, recycle the curr_sum and pass the count to the node above
            #we delete the record in the map to prevent polluting the sibling branch
            current_branch_sum_map[curr_sum] -= 1
            return count
        
        return pre_order_traversal(root, 0)


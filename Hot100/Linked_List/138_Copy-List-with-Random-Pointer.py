"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

#smart solution: use the old-new node map refering to the relation
#time complexity: O(N) for the while loop
#space complexity: O(N) for maintaining the map
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head

        new_dummy = Node(0, None, None)
        new_curr = new_dummy
        old_new_node_map = {} 
        old_new_node_map[None] = None


        while curr:
            new_node = Node(curr.val, None, None)
            new_curr.next = new_node

            old_new_node_map[curr] = new_node

            curr = curr.next 
            new_curr = new_curr.next


        for key, value in old_new_node_map.items():
            if key is not None:
                value.random = old_new_node_map[key.random]
            

        return new_dummy.next
"""

#O(1) space solution: just add the new nodes right after the old nodes. no extra space needed
#time complexity: O(N)
#space complexity: O(1)
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head 

        #attach the new node right after each old node
        while curr:
            new_node = Node(curr.val, None, None)
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next.next

        #get the .random relation
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        #seperate the new nodes
        curr = head
        new_head = head.next
        while curr:
            new_node = curr.next
            curr.next = new_node.next
            
            if new_node.next:
                new_node.next = new_node.next.next 
            
            curr = curr.next


        return new_head
"""

#brute solution: use the indexes refering to the relation
#time complexity: O(N²) for the worst situation: nested while loop
#space complexity: O(N) for maintaining the map
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head

        new_dummy = Node(0, None, None)
        new_curr = new_dummy

        node_count = 0
        node_random_map = {} #the keys are the curr.random, and the values are the indexes of the curr.Replace the keys once we find their index


        while curr:
            new_node = Node(curr.val, None, None)
            new_curr.next = new_node

            node_random_map[node_count] = curr.random

            curr = curr.next 
            new_curr = new_curr.next
            node_count+=1


        for key, value in node_random_map.items():
            curr = head
            node_count = 0
            while curr != value:
                curr = curr.next
                node_count+=1
            
            node_random_map[key] = node_count
        
        for key, value in node_random_map.items():
            new_random_itself = new_dummy.next
            new_random_pointer = new_dummy.next
            if key is not None:
                for _ in range(key):
                    new_random_pointer = new_random_pointer.next
                for _ in range(value):
                    new_random_itself = new_random_itself.next

                new_random_pointer.random = new_random_itself

        return new_dummy.next
"""
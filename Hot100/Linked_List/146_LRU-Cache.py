class ListNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.next = None
        self.prev = None

#use doubly linked list to store the datas, whose order directly represent the "recently used". 
#The most recently used node follows the head dummy node, while the least recenly used node stays in front of the tail dummy node.
#use hashmap to optimize searching speed

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.key = None
        self.tail.key = None
        self.head.next = self.tail
        self.tail.prev = self.head

        self.current_num = 0
        self.capacity = capacity
        self.key_map = {}

    def get(self, key: int) -> int:
        if key in self.key_map:
            curr = self.key_map[key]
            curr.prev.next = curr.next
            curr.next.prev =curr.prev
            curr.prev = self.head
            curr.next = self.head.next
            self.head.next = curr
            curr.next.prev = curr

            return curr.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            curr = self.key_map[key]
            curr.val = value

            curr.prev.next = curr.next
            curr.next.prev =curr.prev
            curr.prev = self.head
            curr.next = self.head.next
            self.head.next = curr
            curr.next.prev = curr

            return

        new_node = ListNode()
        new_node.key = key
        new_node.val = value

        new_node.next = self.head.next
        new_node.next.prev = new_node 
        new_node.prev = self.head
        self.head.next = new_node

        self.key_map[new_node.key] = new_node
        self.current_num+=1

        if self.current_num>self.capacity:
            temp = self.tail.prev
            del self.key_map[temp.key]
            self.tail.prev = self.tail.prev.prev
            self.tail.prev.next = self.tail
            temp.next = None
            temp.prev = None
            self.current_num-=1
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#a = distance between the head node && the exntrance node of the circle
#b = distance bewteen the entrance node of the circle && the node where fast meets the slow
#L = the length of the circle

#2(a + b) = a + b + k*L (k∈N)
#a = k*L -b
#so the slow node needs to move "a" nodes forward in order to reach entrance node again
#which means if we initialize a new pointer at the head and move it at the same speed as the slow one, they will eventually meet at the entrance node
#(same speed, same time -> same distance ("a" nodes))

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                new_pointer = head
                while new_pointer != slow:
                    new_pointer = new_pointer.next
                    slow = slow.next
                return slow

        return None
        

        
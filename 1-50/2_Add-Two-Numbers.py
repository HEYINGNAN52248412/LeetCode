# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        HEAD = ListNode(0)
        pointer = HEAD
        carry = 0

        #remember sometimes when both l1 and l2 are finished a carry may still be waiting there.
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp = val1 + val2 + carry

            carry = temp//10
            temp = temp %10

            pointer.next = ListNode(temp)
            pointer = pointer.next

        #remember when l1 has no next it will be given a value of None, and trying none.next will cause the crash.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return HEAD.next
            

            
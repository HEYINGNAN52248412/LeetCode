# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #in case we have to delete the head node
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        #warning: if we are requeset delete the head node && we start from the head node, the fast pointer will eventually stop at the "none"
        #e.g.: [1,2], 2.  We have to delete the "1", and the faster will stop at the node after"2".
        #So we use the dummy node  to avoid such out-of-bound problem.
        for i in range (n):
            fast = fast.next


        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = (slow.next).next

        #in case we have already deleted the head node
        return dummy.next
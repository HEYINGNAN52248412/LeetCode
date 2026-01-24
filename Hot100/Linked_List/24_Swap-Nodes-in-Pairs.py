# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy

        while curr.next and curr.next.next: #the curr.next must before the curr.next.next, cuz python always check the 1st condition first. Placing curr.next.next at the first place may cause nonetype error if there is only one node after the curr.
            node1 = curr.next
            node2 = curr.next.next
            node3 = curr.next.next.next

            temp = node3 #store the reference of node3
            node2.next = node1 #the .next of node2 now point to node1, and a circle's formed (curr->1->2->1, 3=temp)
            curr.next = node2 #set the next node of the curr node2 (curr->2->1->2, 3(temp), now node1 = curr.next.next)
            node1.next = temp #now the .next of node1 is node3 (curr->2->1->3)

            curr = curr.next.next

        return dummy.next


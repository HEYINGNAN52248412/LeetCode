# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#fast-slow pointer
#time O(n), spaceO(1)
#but it may takes longer time for more traverse

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
        


#hash-map
#time O(n), space O(n)
#but only one traverse
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        list_set = set()
        curr = head

        while curr:
            if curr in list_set:
                return True

            list_set.add(curr)
            curr = curr.next
        return False
"""

#destructive solution: modify the linked list
#time O(n), space O(1)
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False

        sentinal = ListNode(0)
        curr = head
        while curr:
            if curr.next = sentinal:
                return True
            temp = curr.next
            curr.next = sentinal
            curr = temp
        return False
"""
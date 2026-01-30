# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #left: half + possible mid point
        #right: half
        left = head
        right = slow.next
        slow.next = None
        right = self.reverseList(right)

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head or not head.next:
                return head

            curr = head
            prev = None

            while curr:
                temp = curr.next 
                curr.next = prev
                prev = curr
                curr = temp

            return prev
            
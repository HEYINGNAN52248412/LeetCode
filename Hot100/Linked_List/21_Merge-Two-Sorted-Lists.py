# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = list1
        pointer2 = list2
        dummy = ListNode(0,None)
        curr = dummy

        while pointer1 and pointer2:
            if pointer2.val >= pointer1.val:
                curr.next = pointer1
                pointer1 = pointer1.next
                curr = curr.next
            else:
                curr.next = pointer2
                pointer2 = pointer2.next
                curr = curr.next 

        if pointer1:
            curr.next = pointer1
        
        if pointer2:
            curr.next = pointer2


#recursion solution, looks cool
#general idea: always compare the list1.val and the list2.val, and return the smaller one as the previous node's ".next".
#when one list's finished, keep returning the other list's nodes.
"""
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Base Case: if one of the list's empty, return the other one
        if not list1: return list2
        if not list2: return list1
        
        # 2. Recursive Step: compare the head
        if list1.val <= list2.val:
            # list1 is smaller, we take it as the current head. Then we return it to let it follow the previous nodes.
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            # list2 is smaller
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
"""
                
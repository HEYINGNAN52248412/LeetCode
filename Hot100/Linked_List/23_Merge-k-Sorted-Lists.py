# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        def merge_two_lists(l1,l2):
            if not l1: return l2
            if not l2: return l1

            if l1.val<l2.val:
                l1.next = merge_two_lists(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_lists(l1, l2.next)
                return l2

        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = merge_two_lists(lists[i], lists[i+interval])

            interval*=2

        return lists[0]
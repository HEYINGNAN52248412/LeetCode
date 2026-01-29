# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#bette solution: merge sort
#time complexity: O(nlog n), space complexity: O(log n)
#use a recursion to keep cutting the linked list to two part from the mid point, and merge them when we hit the bottom. 
# when we have already break the list to single nodes/ None nodes. we start to merge them.

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #the exit of the recursion
        if not head or not head.next :
            return head
        

        def merge_two_sorted_linked_list(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1

            while list1 and list2:
                if list1.val > list2.val:
                    list2.next = merge_two_sorted_linked_list(list1, list2.next)
                    return list2
                else:
                    list1.next = merge_two_sorted_linked_list(list1.next, list2)
                    return list1
            
            return list1 if list1 else list2

        slow = head 
        fast = head.next #if the number of the nodes is an odd, and fast = head, the mid should be "slow" instead of slow.next(e.g.: there are 5 nodes in the linked list, and when the loop stops, slow = node3, fast = node5.next(none).). To avoid this, we set the fast "head.next"
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        #break the origin linked list to two lists
        slow.next = None

        #core alogrithm
        #keep cutting the list half, and going back when the head = single node or None. 
        left = self.sortList(head)
        right = self.sortList(mid)
        
        #the first going back should be "singe node + single node" or "single node + None", and we can merge them to a double-node linked list and return it.
        return merge_two_sorted_linked_list(left, right)


#dumb iteration solution: a kind of bubble sort
#time complexity: O(n²), space complexity: O(1)
"""
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        node_list = list()
        curr = head
        sorted = True
        while curr:
            if curr.next and curr.next.val < curr.val:
                sorted = False
                temp = curr.next
                curr.next = curr.next.next
                temp.next = head
                head = temp
            if curr.next == None and not sorted:
                curr = head
                sorted = True
                continue
            curr = curr.next

        return head
"""

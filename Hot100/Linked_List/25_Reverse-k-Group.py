# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0,head)
        curr_head = dummy
        curr_final = dummy
        count = 0

        def flip_nodes_in_NodeList (head): #traverse
            prev = None
            curr = head
            
            #while curr still exist
            while curr:
                #store the node after it
                nextNode = curr.next
                
                #connect curr->prev
                curr.next = prev

                #move forward
                prev = curr
                curr = nextNode

            return prev, head
        
        while True:
            #keep rolling forward
            while curr_final.next and count <k:
                curr_final = curr_final.next
                count+=1
            
            #if stopped && count<k, it means the left nodes can not support another flip
            if count < k:
                break
            count = 0

            #store the nodes after the flip listNode
            temp = curr_final.next
            #set final.next to None in order to fullfill the funtion prequisite
            curr_final.next = None

            #flip, and get new final and head
            new_head, new_final = flip_nodes_in_NodeList(curr_head.next)

            #curr_head is the dummy node, now we connect it with the new node
            curr_head.next = new_head
            new_final.next = temp

            #now more curr_head and curr_final forward to process the next ListNode
            curr_head = new_final
            curr_final = curr_head
        
        return dummy.next
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Helper function to reverse a segment of k nodes
        def reverse_linked_list(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Check if there are k nodes left to reverse
            kth_node = group_prev
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    return dummy.next
            
            # Mark the start and end nodes for the k-group
            group_start = group_prev.next
            group_end = kth_node.next
            
            # Reverse the k-group
            new_group_start = reverse_linked_list(group_start, group_end)
            
            # Connect the reversed group back to the list
            group_prev.next = new_group_start
            group_start.next = group_end
            
            # Move the group_prev pointer to the end of the reversed group
            group_prev = group_start

        return dummy.next
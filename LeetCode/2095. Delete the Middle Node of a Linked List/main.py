# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: If the list is empty or has only one node
        if not head or not head.next:
            return None
    
        # Use a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize slow and fast pointers
        slow = dummy
        fast = dummy
        
        # Move fast two steps at a time and slow one step at a time
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Delete the middle node
        slow.next = slow.next.next
        
        # Return the modified list
        return dummy.next
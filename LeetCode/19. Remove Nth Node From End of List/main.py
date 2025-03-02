# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        
        # Initialize two pointers
        slow = dummy
        fast = dummy
        
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        
        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the nth node from the end
        slow.next = slow.next.next
        
        # Return the modified list
        return dummy.next
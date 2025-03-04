# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the list construction
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists while there's anything left to process
        while l1 or l2 or carry:
            # Get the current values of the nodes or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits plus carry
            total = val1 + val2 + carry
            carry = total // 10  # Calculate new carry (either 0 or 1)
            current.next = ListNode(total % 10)  # Create the new node with the digit part
            
            # Move to the next node in the result list
            current = current.next
            
            # Move to the next nodes in the input lists, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return the node following the dummy node
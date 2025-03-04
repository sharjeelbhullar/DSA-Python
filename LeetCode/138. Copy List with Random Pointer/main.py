# Definition for a Node.
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Clone the nodes and interweave them
        current = head
        while current:
            new_node = Node(current.val)  # Create a new node with the same value
            new_node.next = current.next  # The new node's next should point to the next node in the original list
            current.next = new_node  # Insert the new node after the current node
            current = new_node.next  # Move to the next original node
        
        # Step 2: Copy the random pointers
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next  # Set the random pointer of the cloned node
            current = current.next.next  # Move to the next original node
        
        # Step 3: Separate the two lists
        original = head
        copy = head.next
        new_head = head.next
        while original:
            original.next = original.next.next  # Restore the original list's next pointers
            if copy.next:
                copy.next = copy.next.next  # Set the next pointer of the copied list
                copy = copy.next
            original = original.next
        
        return new_head
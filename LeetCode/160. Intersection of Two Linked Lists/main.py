# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
    
        # Step 1: Find the lengths of both lists
        lenA, lenB = 0, 0
        ptrA, ptrB = headA, headB
        
        while ptrA:
            lenA += 1
            ptrA = ptrA.next
        
        while ptrB:
            lenB += 1
            ptrB = ptrB.next
        
        # Step 2: Advance the longer list's pointer
        ptrA, ptrB = headA, headB
        if lenA > lenB:
            for _ in range(lenA - lenB):
                ptrA = ptrA.next
        else:
            for _ in range(lenB - lenA):
                ptrB = ptrB.next
        
        # Step 3: Traverse both lists simultaneously
        while ptrA and ptrB:
            if ptrA == ptrB:
                return ptrA
            ptrA = ptrA.next
            ptrB = ptrB.next
        
        return None
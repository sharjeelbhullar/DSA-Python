# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(list1, list2):
            dummy = ListNode(-1)
            temp = dummy

            while list1 is not None and list2 is not None:
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next

                else:
                    temp.next = list2
                    list2 = list2.next

                temp = temp.next

            if list1 is not None:
                temp.next = list1
            else:
                temp.next = list2

            return dummy.next
        
        def findMiddle(head):
            if head is None or head.next is None:
                return head

            slow = head
            fast = head.next

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            return slow
        
        if head is None or head.next is None:
            return head

        middle = findMiddle(head)
        right = middle.next
        middle.next = None
        left = head
        
        left = self.sortList(left)
        right = self.sortList(right)

        return merge(left, right)
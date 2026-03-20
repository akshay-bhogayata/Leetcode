# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node points to the head
        dummy = ListNode(0, head)
        
        # 'prev' is the last node in the sorted, unique list
        prev = dummy
        
        while head:
            # If we detect a duplicate
            if head.next and head.val == head.next.val:
                # Move 'head' to the very last node of this duplicate sequence
                while head.next and head.val == head.next.val:
                    head = head.next
                # Skip all the duplicates by pointing prev's next to head's next
                prev.next = head.next
            else:
                # No duplicate detected, so prev can safely move forward
                prev = prev.next
            
            # Move head forward to evaluate the next sequence
            head = head.next
            
        return dummy.next
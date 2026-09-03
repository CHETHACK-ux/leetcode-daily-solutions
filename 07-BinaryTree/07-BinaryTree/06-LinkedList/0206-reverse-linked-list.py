# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr is not None:
            next_node = curr.next  # Aage ka reference save kiya
            curr.next = prev       # Link reverse kiya
            prev = curr            # Prev ko aage badhaya
            curr = next_node       # Curr ko aage badhaya
            
        return prev  # Naya head ab 'prev' par hoga
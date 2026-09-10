# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: Middle find karo (Slow & Fast pointer)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Second half ko reverse karo
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Step 3: Dono halves ko compare karo (Two Pointers)
        left = head
        right = prev  # Reversed second half ka head
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
        
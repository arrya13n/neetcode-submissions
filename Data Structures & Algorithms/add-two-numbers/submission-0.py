# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1 or not l2:
            return l1 or l2
        
        carry = 0
        result = ListNode(0)
        current = result

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            curr_sum = val1 + val2 + carry

            result.next = ListNode(curr_sum % 10)
            carry = curr_sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            result = result.next
        if carry:
            result.next = ListNode(carry)
        
        return current.next
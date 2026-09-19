# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # I need to split the linked list into two halves.
        # I'll use slow and fast pointers:
        # slow moves one step, fast moves two steps.
        # When fast reaches the end, slow will be around the middle.
        slow, fast = head, head.next

        while fast and fast.next:
            # Move slow one node at a time.
            slow = slow.next

            # Move fast two nodes at a time.
            fast = fast.next.next

        # 'slow' is now at the end of the first half.
        # The second half starts at slow.next.
        second = slow.next

        # Cut the list into two separate halves.
        # This prevents the first half from still pointing into the second half.
        prev = slow.next = None

        # Now I need to reverse the second half
        # so that its nodes can be merged in reverse order.
        while second:
            # Save the next node before changing second.next.
            temp = second.next

            # Reverse the pointer.
            second.next = prev

            # Move prev forward.
            prev = second

            # Move to the next original node.
            second = temp

        # At this point:
        # first = first half
        # second = reversed second half
        first, second = head, prev

        # Now I'll merge the two halves alternately:
        # first node from first half,
        # then first node from second half,
        # then second node from first half, etc.
        while second:

            # Save both next nodes before changing any pointers.
            temp1, temp2 = first.next, second.next

            # Put the second-half node after the current first-half node.
            first.next = second

            # Connect that second-half node to the next first-half node.
            second.next = temp1

            # Move first to its next node.
            first = temp1

            # Move second to its next node.
            second = temp2
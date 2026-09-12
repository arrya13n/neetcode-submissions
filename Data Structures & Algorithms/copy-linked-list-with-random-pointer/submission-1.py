"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldlist = {None: None}

        current = head
        while current:
            copy = Node(current.val)
            oldlist[current] = copy
            current = current.next
        
        current = head
        while current:
            copy = oldlist[current]
            copy.next = oldlist[current.next]
            copy.random = oldlist[current.random]
            current = current.next
        return oldlist[head]
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
        hmap = {}
        cpy = head
        while cpy:
            node = Node(cpy.val)
            hmap[cpy] = node
            cpy = cpy.next
        
        #second pass
        for key in hmap:
            val = hmap[key]
            nxtcl = hmap.get(key.next,None)
            nextracl = hmap.get(key.random,None)
            val.next = nxtcl
            val.random = nextracl

        return hmap.get(head,None)

        
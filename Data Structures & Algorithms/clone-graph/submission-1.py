"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #given input node 
        #we need to clone the same graph
        # visited = set()
        if not node:
            return 
        hmap = {}
        def dfs(node):
           
            hmap[node] = Node(val=node.val)
            neigh = node.neighbors
            for ele in neigh:
                if ele not in hmap:
                    dfs(ele)
                hmap[node].neighbors.append(hmap[ele])
                    # hmap[ele].neighbors.append(hmap[node])
            return hmap[node]
        return dfs(node)

        
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        lookup = {}

        def dfs(node):
            if not node: return
            if node in lookup:
                return lookup[node]
            clone = Node(node.val, [])
            lookup[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))

            return clone

        return dfs(node)


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

      def bfs(node:'Node'):
        if not node:
            return None
        lookup = {}
        clone = Node(node.val, [])
        lookup[node] = clone
        #lookup[node]和clone实际上引用的是同一个Node对象的实例，它们共享同一个内存地址。
        queue = deque([node])

        while queue:
            temp_node = queue.popleft()
            for neighbor in temp_node.neighbors:
                if neighbor not in lookup:
                    lookup[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                lookup[temp_node].neighbors.append(lookup[neighbor])
        return clone

      return bfs(node)

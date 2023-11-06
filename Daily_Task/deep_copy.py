# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        """
        Given a reference of a node in a connected undirected graph.
        Return a deep copy (clone) of the graph using BFS algorithm.
        """
        if not node:
            return None
        queue = [node]
        visited = {node: Node(node.val)}
        while queue:
            n = queue.pop(0)
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]


if __name__ == "__main__":
    copy = Solution()

from typing import List, Set


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[Set[int]]:
        # Initialize the ancestors list with empty sets for each node
        ancestors = [set() for _ in range(n)]
        # Create an adjacency list to represent the graph
        graph = [[] for _ in range(n)]

        # Build the graph from the given edges
        for parent, child in edges:
            graph[parent].append(child)

        # Perform DFS for each node to find its descendants and update their ancestors
        for node in range(n):
            self.dfs(node, node, ancestors, graph)

        # Convert sets to sorted lists for the final output
        return [sorted(node_ancestors) for node_ancestors in ancestors]

    def dfs(
        self,
        ancestor: int,
        current: int,
        ancestors: List[Set[int]],
        graph: List[List[int]],
    ) -> None:
        # Traverse through all children of the current node
        for child in graph[current]:
            # If the ancestor is not already in the child's ancestor set
            if ancestor not in ancestors[child]:
                # Add the ancestor to the child's ancestor set
                ancestors[child].add(ancestor)
                # Recursively call DFS for the child node
                self.dfs(ancestor, child, ancestors, graph)
                
                
"""
The solution uses a depth-first search (DFS) approach to traverse the graph and identify ancestors. Here's a detailed explanation of the problem-solving approach:

Initialize data structures:

ans: A list of lists to store ancestors for each node.
directChild: A list of lists to represent the graph as an adjacency list.


Build the graph:

Iterate through the edges and populate the directChild list.


Perform DFS for each node:

For each node i from 0 to n-1, call the DFS function with i as both the starting node and current node.


DFS function:

For each child of the current node:

If the ancestor list of the child is empty or the last ancestor is not the starting node:

Add the starting node as an ancestor of the child.
Recursively call DFS for the child node.

Time Complexity:

The time complexity of this solution is O(n * (n + e)), where n is the number of nodes and e is the number of edges.
In the worst case, we perform a DFS for each node (n times), and each DFS can potentially visit all nodes and edges.
Building the graph takes O(e) time.
The final sorting of ancestors for each node takes O(n * log(n)) in the worst case.

Space Complexity:

The space complexity is O(n * n + e).
We store the graph as an adjacency list, which takes O(n + e) space.
The ancestors list can potentially store all nodes as ancestors for each node, leading to O(n * n) space in the worst case.
The recursion stack in DFS can go up to O(n) in the worst case (for a linear graph).

"""


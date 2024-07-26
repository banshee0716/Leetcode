from typing import List


class Solution:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # Initialize the distance matrix with infinity
        distances = [[float("inf")] * n for _ in range(n)]

        # Set distance to self as 0 for all cities
        for i in range(n):
            distances[i][i] = 0

        # Populate the distance matrix with the given edges
        for city1, city2, weight in edges:
            distances[city1][city2] = weight
            distances[city2][city1] = weight  # Assuming undirected graph

        # Floyd-Warshall algorithm to find shortest paths between all pairs
        for intermediate in range(n):
            for start in range(n):
                for end in range(n):
                    # If path through intermediate city is shorter, update distance
                    if distances[start][end] > distances[start][intermediate] + distances[intermediate][end]:
                        distances[start][end] = distances[start][intermediate] + distances[intermediate][end]

        min_reachable_cities = float("inf")
        best_city = -1

        # Find the city with the smallest number of reachable cities
        for city in range(n):
            reachable_cities = sum(
                1 for dist in distances[city] if dist <= distanceThreshold
            )

            # Update best city if fewer reachable cities or same but higher city number
            if reachable_cities <= min_reachable_cities:
                min_reachable_cities = reachable_cities
                best_city = city

        return best_city
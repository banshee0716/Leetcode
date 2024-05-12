class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        for _ in range(2):
            grid = [[*map(max, g, g[1:], g[2:])]
                    for g in zip(*grid)]
            
        return grid
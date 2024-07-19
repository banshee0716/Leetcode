class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        mi = [min(row) for row in matrix]
        mx = [max(col) for col in zip(*matrix)]
        return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if mi[i] == mx[j]]
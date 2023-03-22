class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row*col-1 #整個解區間的大小
        while left < right:
            mid = left + (right-left)//2
            if matrix[mid // col][mid % col] < target:
                left = mid + 1
            else:
                right = mid
                
        return target == matrix[left//col][left % col]
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        rows, cols = len(points), len(points[0])

        # Process each row starting from the second row
        for i in range(1, rows):
            # Initialize right array to store maximum points from right side
            right = [0] * cols
            right[-1] = points[i - 1][-1]

            # Calculate maximum points from right to left
            for j in range(cols - 2, -1, -1):
                right[j] = max(right[j + 1] - 1, points[i - 1][j])

            # Initialize left variable to store maximum points from left side
            left = points[i - 1][0]

            # Process first column separately
            points[i][0] = max(left, right[0]) + points[i][0]

            # Calculate maximum points for each cell in the current row
            for j in range(1, cols):
                # Update left maximum
                left = max(left - 1, points[i - 1][j])
                # Calculate maximum points for current cell
                points[i][j] = max(left, right[j]) + points[i][j]

        # Return the maximum value in the last row
        return max(points[-1])
    
    """
Time Complexity:
O(r * c), where r is the number of rows and c is the number of columns in the input grid.
We process each cell in the grid once, performing constant time operations for each cell.

Space Complexity:
O(c), where c is the number of columns in the input grid.
We use a 'right' array of size c to store intermediate results.
The 'left' variable uses constant space.
We modify the input grid in-place, which doesn't contribute to additional space complexity in the analysis.
    """
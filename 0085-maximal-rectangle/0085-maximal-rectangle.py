from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix[0])
        heights = [0] * (n + 1)  # 初始化高度陣列
        max_area = 0

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0  # 更新高度

            stack = [-1]  # 初始化棧，開始時放入-1方便計算寬度
            for i in range(n + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]  # 彈出棧頂，獲取高度
                    w = i - stack[-1] - 1  # 計算寬度
                    max_area = max(max_area, h * w)  # 更新最大面積
                
                stack.append(i)  # 將當前索引入棧

        return max_area

    """
解題思路
本問題可以看作是多個由'1'構成的柱狀圖的最大矩形面積問題。對於每一行，我們都更新一次高度，然後利用「柱狀圖中的最大矩形」的解法來找出當前行為底的最大矩形面積。

1. 初始化高度：首先初始化一個高度陣列heights，長度比矩陣的列數多一，這樣方便我們後面的處理。最後一個元素保留為0，這是為了在所有柱體高度都被計算完後能夠清空棧。
2. 更新高度並計算最大面積：對於每一行，我們更新高度陣列，如果當前元素是'1'，高度加一，否則重置為0。然後使用單調棧來計算以當前行為底的最大矩形面積。
3. 單調棧：維護一個棧來存儲高度陣列的索引，這些索引在棧中是單調增的。當當前高度小於棧頂高度時，表示找到了棧頂高度的右邊界，計算以該高度為高的最大矩形面積。


時間複雜度分析
每行更新高度的操作是O(n)，其中n是列數。
每行中使用單調棧計算面積的時間複雜度也是O(n)，因為每個元素最多被推入和彈出棧一次。
因此，總時間複雜度為O(mn)，其中m是行數。

空間複雜度分析
需要額外的空間存儲高度數組heights和棧，空間複雜度為O(n)。
    """
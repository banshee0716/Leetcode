#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#


# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # 創建一個包含所有節點的集合
        all_nodes = set(range(n))

        # 創建一個包含所有目標節點（邊的終點）的集合
        destination_nodes = set(destination for _, destination in edges)

        # 計算所有節點和目標節點的差集，這個差集就是我們要找的節點集
        source_nodes = all_nodes - destination_nodes

        # 將節點集轉換為列表
        return list(source_nodes)


"""
時間複雜度：
此算法的時間複雜度為 O(n + e)，其中 n 是節點的數量，e 是邊的數量。因為我們需要遍歷每個節點和每條邊。

空間複雜度：
此算法的空間複雜度為 O(n)，因為我們需要儲存所有的節點和目標節點。這裡的 n 是節點的數量。
"""


"""
1. 創建一個包含所有節點值從0到n-1的集合all_nodes。該集合表示圖中的所有節點。
2. 創建一個集合destination_nodes來存儲來自邊緣列表的目標節點。遍歷每個邊緣，並將目標節點添加到集合中。
3. 計算all_nodes和destination_nodes之間的差集，以獲得源節點的集合。這些節點沒有任何入邊，可以直接或間接地到達所有其他節點。
4. 將源節點的集合轉換為列表並返回結果。

直觀解釋：
在有向圖中，源節點是沒有任何入邊的節點。如果一個節點是源節點，意味著它不依賴於任何其他節點，可以直接或間接地到達所有其他節點。
因此，達到圖中所有節點所需的最小節點數將是源節點的集合。

通過創建所有節點的集合並從邊緣中識別目標節點，我們可以計算差集以獲得源節點。
這些源節點將是達到圖中所有節點所需的最小節點，因為它們可以直接或間接地到達其他節點。

將源節點的集合轉換為列表，可以按照問題要求返回結果。
"""
# @lc code=end

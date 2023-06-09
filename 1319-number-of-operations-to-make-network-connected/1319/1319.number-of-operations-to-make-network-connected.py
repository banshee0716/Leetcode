#
# @lc app=leetcode id=1319 lang=python3
#
# [1319] Number of Operations to Make Network Connected
#

# @lc code=start
import collections


class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:  # 判斷能否連接所有的電腦
            return -1

        d = collections.defaultdict(list)  # 創建一個字典來儲存所有的連線
        for i, j in connections:
            d[i].append(j)  # 在i的連線中添加j
            d[j].append(i)  # 在j的連線中添加i

        visited = set()  # 創建一個集合來儲存已經訪問過的節點
        numofconnected = 0  # 計算連通圖的數量

        def dfs(root):  # 定義一個深度優先搜索的函數
            visited.add(root)  # 將根節點加入已訪問的集合中
            for j in d[root]:
                if j not in visited:  # 如果節點沒有被訪問過
                    dfs(j)  # 繼續搜索

        for i in range(n):  # 遍歷所有的電腦
            if i not in visited:  # 如果該電腦沒有被訪問過
                numofconnected += 1  # 增加連通圖的數量
                dfs(i)  # 開始深度優先搜索

        return numofconnected - 1  # 返回連通圖的數量減1


"""
時間複雜度：
$O(n + e)$，其中n表示電腦的數量，e表示連接的線數量。因為需要遍歷所有的節點和邊，所以時間複雜度為線性的。

空間複雜度：
$O(n + e)$，需要使用一個字典來儲存所有的連線，並且需要使用一個集合來儲存已訪問的節點，因此空間複雜度也是線性的。
"""
# @lc code=end

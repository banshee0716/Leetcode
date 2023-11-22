from collections import defaultdict, deque
from typing import List

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        d = defaultdict(deque)
        # 遍歷二維數組並將元素添加到相應的對角線 deque 中
        for i, row in enumerate(nums):
            for j, e in enumerate(row):
                d[i + j].appendleft(e)  # 對角線索引為 i + j

        trav = []  # 用於存儲最終遍歷結果的列表
        # 遍歷字典並將元素添加到 trav 中
        for key, diag in d.items():
            trav.extend(diag)
        
        return trav

"""
1. 使用字典存儲對角線元素：
    - 創建一個字典 d，用於將相同對角線上的元素存儲在一起。字典的鍵為行索引與列索引之和，值為一個 deque（雙端隊列），用於存儲該對角線上的元素。

2. 遍歷數組並填充字典：
    -遍歷給定的二維數組，將元素按照對角線索引添加到對應的 deque 中。由於對角線上的元素需要逆序輸出，因此使用 appendleft 方法將元素添加到 deque 的開頭。

3.構建最終結果：
    -初始化一個列表 trav，用於存儲最終的遍歷結果。
    -遍歷字典中的每一個 deque，並將其元素添加到 trav 中。

時間複雜度分析：
總體時間複雜度為 O(N)。

空間複雜度分析：
需要額外的空間來存儲字典和最終結果，空間複雜度為 O(N)。
"""
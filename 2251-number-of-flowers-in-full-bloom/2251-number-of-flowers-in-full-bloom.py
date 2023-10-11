from typing import List
from bisect import bisect_right, bisect_left

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # 分別取出所有花的開始和結束日期，並排序
        start = sorted([s for s, e in flowers])
        end = sorted([e for s, e in flowers])
        
        # 對於每一個人的到達時間，計算這時有多少花正在盛開
        # 花的盛開數量 = 在此時間之前開始盛開的花的數量 - 在此時間之前已經凋謝的花的數量
        return [bisect_right(start, t) - bisect_left(end, t) for t in people]

    """
給定一個 0 索引的 2D 整數陣列 Flowers，其中 Flowers[i] = [starti, endi] 表示第 i 朵花將從 starti 到 endi（含）盛開。
您還會獲得一個大小為 n 的 0 索引整數數組 people，其中 people[i] 是第 i 個人到達看花的時間。

傳回大小為 n 的整數數組answer，其中answer[i]是第i個人到達時盛開的花朵的數量。

解題思路是：

1. 分別對 flowers 中的起始和結束日期進行排序。
2. 遍歷每個人的到達時間，使用二分法計算此時正在盛開的花朵數量。

時間複雜度分析：
將 flowers 中的起始和結束日期排序的時間複雜度是 O(flogf)，其中 f 是 flowers 的長度。
對於每個人的到達時間，使用二分法查找的時間複雜度是 O(plogf)，其中 p 是 people 的長度。
所以總的時間複雜度是 O(flogf+plogf)。

空間複雜度分析：
我們使用了額外的 start 和 end 陣列，所以空間複雜度是 O(f)。
    """
from itertools import zip_longest

class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        # 使用split和map將版本號轉換為整數列表
        v1, v2 = list(map(int, v1.split('.'))), list(map(int, v2.split('.')))
        
        # 使用zip_longest同步比較兩個版本號
        for rev1, rev2 in zip_longest(v1, v2, fillvalue=0):
            if rev1 == rev2:
                continue
            # 返回版本號較大的版本
            return -1 if rev1 < rev2 else 1 
        
        # 所有子版本均相等
        return 0

"""
解題思路
1. 分割版本號：使用split函數以.分割版本號，並將每個子版本轉換為整數。
2. 同步比較：使用itertools.zip_longest函數對兩個版本號進行同步比較。如果一個版本號較短，則用0填充以保持同步。
3. 逐個比較：在同步遍歷子版本時比較它們的大小：
    -如果發現不同，則根據子版本的大小返回-1或1。
    -如果子版本相同，繼續比較下一個子版本。
4. 最終結果：如果所有子版本均相等，則返回0表示兩個版本號相同。


時間複雜度分析
時間複雜度：O(max(n, m))，其中n和m分別是兩個版本號的子版本數量。由於使用zip_longest，兩個版本號的子版本都將被遍歷一次。

空間複雜度分析
空間複雜度：O(n + m)，用於存儲版本號的分割結果。
"""
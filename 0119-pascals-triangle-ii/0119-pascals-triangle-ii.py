class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # 初始化結果為第一個元素1
        res = [1]
        # 上一個元素值
        prev = 1
        # 從第二個元素開始計算
        for k in range(1, rowIndex+1):
            # 利用公式計算當前元素值
            next_val = prev*(rowIndex - k + 1) // k
            res.append(next_val)
            # 更新上一個元素值
            prev = next_val
        return res
    
    
    
"""
時間複雜度：O(n)，其中n是行索引。
空間複雜度：O(1)。除了最後的結果外，我們只使用了常數的額外空間。
"""
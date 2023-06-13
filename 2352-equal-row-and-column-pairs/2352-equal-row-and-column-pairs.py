class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #用一個dict記錄下row長怎樣，之後開始掃column之後比對裡面有沒有
        m = defaultdict(int)  # 創建一個預設值為整數的字典，用於儲存每行的出現次數
        cnt = 0  # 初始化計數器

        for row in grid:  # 遍歷每一行
            m[str(row)] += 1  # 增加該行的出現次數
        
        for i in range(len(grid[0])):  # 遍歷每一列
            col = []  # 創建一個列表來儲存當前列的元素
            for j in range(len(grid)):
                col.append(grid[j][i])  # 將當前列的元素添加到列表中
            cnt += m[str(col)]  # 如果該列與某一行相等，則將計數器遞增相應的次數
        return cnt  # 返回計數器的值

"""
時間複雜度：
O(n^2)，其中 n 為矩陣的邊長。因為我們需要遍歷整個矩陣。

空間複雜度：
O(n)，其中 n 為矩陣的行數。我們需要一個字典來存儲每行的出現次數。

"""
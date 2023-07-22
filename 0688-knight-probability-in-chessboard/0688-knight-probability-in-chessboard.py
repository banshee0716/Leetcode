from functools import cache

class Solution:
    def __init__(self):
        self.n = 0  # 初始化棋盤大小
        self.k = 0  # 初始化移動次數
        self.states = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]  # 騎士的8種走法

    @cache
    def is_valid(self, x, y):
        if 0 <= x < self.n and 0 <= y < self.n:  # 檢查座標是否在棋盤內
            return True
        return False

    @cache
    def solve(self, x, y, k):
        if k == 0:  # 基礎情況：如果k為0，則騎士必在棋盤上
            return 1
        rate = 0
        for dx, dy in self.states:  # 遍歷每一種走法
            n_x, n_y = x + dx, y + dy
            if not self.is_valid(n_x, n_y):  # 檢查新座標是否在棋盤內
                continue
            rate += 0.125 * self.solve(n_x, n_y, k - 1)  # 算出每一步的概率並加到總概率上
        return rate

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        self.n = n  # 更新棋盤大小
        self.k = k  # 更新移動次數
        if k == 0:  # 如果k為0，只需要檢查初始座標是否在棋盤內
            return float(self.is_valid(row, column))
        return self.solve(row, column, k)  # 調用solve函數，並返回結果


"""
1. 首先，我們初始化一些變數，包括棋盤的大小n和騎士的移動次數k，以及騎士的八種走法。

2. 我們定義了一個函數is_valid，用於檢查騎士的座標是否在棋盤內。如果在棋盤內，則返回True；否則，返回False。

3. 函數solve用於計算騎士在k步後留在棋盤上的概率。如果k為0，則騎士必定在棋盤上，所以返回1。然後，我們遍歷騎士的每一種走法，並計算出每一種走法後的座標。如果這個座標在棋盤內，則我們遞迴調用solve函數，並將騎士的走法概率（1/8）乘上在新座標上的騎士留在棋盤上的概率，然後將這個值加到總概率上。

4. 在主函數knightProbability中，我們更新了棋盤的大小和騎士的移動次數，然後調用solve函數並返回其結果。

時間複雜度為O(N^2 * K)，這是因為我們要在N^2的棋盤上進行深度優先搜索，而最大深度為K。
空間複雜度為O(N^2 * K)，這是因為我們需要存儲在每個位置上，每一步的概率。這裡，我們使用了functools庫中的cache裝飾器來做記憶化搜索，以減少重複計算，優化了時間和空間複雜度。
"""

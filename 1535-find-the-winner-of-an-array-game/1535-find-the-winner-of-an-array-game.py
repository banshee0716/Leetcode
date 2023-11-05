from typing import List

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # 如果k為1，則贏家為前兩個玩家中的較強者
        if k == 1:
            return max(arr[0], arr[1])
        
        # 如果k大於陣列長度，則贏家為最強的玩家
        if k > len(arr):
            return max(arr)
        
        # 初始化當前贏家和連勝次數
        current_winner = arr[0]
        consecutive_wins = 0
        
        # 遍歷陣列中的玩家
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                # 如果當前贏家繼續勝利，增加連勝次數
                consecutive_wins += 1
            else:
                # 如果當前玩家輸了，更新當前贏家並重設連勝次數
                current_winner = arr[i]
                consecutive_wins = 1
                
            # 如果連勝次數達到k，返回當前贏家
            if consecutive_wins == k:
                return current_winner
        
        # 如果沒有玩家連勝k次，返回最後的當前贏家
        return current_winner

        
        
        """
時間複雜度分析：
在最壞的情況下，遍歷一次陣列中的所有元素，時間複雜度為O(n)，其中n是陣列arr的長度。

空間複雜度分析：
這段代碼只使用了固定的額外空間來儲存current_winner和consecutive_wins變量，因此空間複雜度為O(1)。
        """
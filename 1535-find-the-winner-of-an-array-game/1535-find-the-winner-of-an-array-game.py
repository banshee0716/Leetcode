class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k == 1:
            return max(arr[0], arr[1])
        
        if k> len(arr):
            return max(arr)
        
        current_winner = arr[0]
        consecutive_wins = 0
        for i in range(1, len(arr)):
            if current_winner > arr[i]:
                consecutive_wins += 1
            else:
                current_winner = arr[i]
                consecutive_wins = 1
                
            if consecutive_wins == k:
                return current_winner
            
        return current_winner
                
        
        
        """
給定一個由不同整數組成的整數陣列 arr 和一個整數 k。

將在陣列的前兩個元素（即 arr[0] 和 arr[1]）之間進行遊戲。在每一輪遊戲中，我們將 arr[0] 與 arr[1] 進行比較，較大的整數獲勝並保持在位置 0，較小的整數移動到數組的末尾。當一個整數連續 k 輪獲勝時，遊戲結束。

傳回將贏得比賽的整數。

這場比賽一定會有勝者。
        """
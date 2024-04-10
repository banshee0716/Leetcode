from typing import List
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()  # 將牌按遞增順序排序
        
        n = len(deck)
        result = [0] * n  # 初始化結果陣列
        indices = deque(range(n))  # 初始化一個隊列來存儲索引
        
        for card in deck:
            idx = indices.popleft()  # 從隊列頂部取出索引
            result[idx] = card  # 將當前牌放到結果陣列的正確位置
            if indices:
                indices.append(indices.popleft())  # 將使用過的索引移動到隊列的末尾
        
        return result

        
        
        """
給你一個整數陣列。有一副牌，每張牌都有一個唯一的整數。第 i 張牌上的整數是牌組[i]。

您可以按照您想要的任何順序訂購套牌。最初，所有牌面朝下（未揭開）放在一副牌中。

您將重複執行以下步驟，直到翻開所有牌：
    1.取出牌堆最上面的牌，展示它，然後將其從牌堆中取出。
    2.如果這副牌中還有牌，則將這副牌最上面的下一張牌放到這副牌的底部。
    3.如果還有未揭開的牌，則返回步驟 1。否則，停止。


傳回牌組的順序，此順序將依升序顯示牌。

請注意，答案中的第一個條目被認為是牌組的頂部。

解題思路
解決這個問題的關鍵在於反向操作。首先對牌進行排序，確保結果陣列是按遞增順序排列的。
然後，使用一個隊列來模擬抽牌和放回牌堆底部的過程。從排序後的牌堆開始，每次將一張牌放到結果陣列的正確位置，並在需要時將索引移動到隊列的末尾。

時間複雜度分析
對deck進行排序的時間複雜度為O(NlogN)，其中N是deck的長度。
遍歷排序後的deck並進行重排的時間複雜度為O(N)。
總的時間複雜度為O(NlogN)。

空間複雜度分析
需要額外的空間來存儲結果陣列和索引隊列，空間複雜度為O(N)。

"""
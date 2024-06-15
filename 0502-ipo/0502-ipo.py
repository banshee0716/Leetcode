import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # 將資本和利潤配對並根據資本金額排序
        projects = sorted(zip(capital, profits))
        # 創建最大堆，用於存儲可以選取的項目的利潤
        max_heap = []
        i = 0
        
        for _ in range(k):
            # 把所有當前資金可以承受的項目的利潤加入最大堆
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            
            # 如果沒有可選的項目，則提前終止
            if not max_heap:
                break
            # 選取一個最大利潤項目進行投資
            w -= heapq.heappop(max_heap)
        
        # 返回投資結束後的總資金
        return w

    
    """
假設 LeetCode 即將開始 IPO。為了以好的價格將股份出售給創投公司，LeetCode 希望在 IPO 之前能進行一些增資項目。由於其資源有限，在首次公開發行之前最多只能完成 k 個不同的專案。幫助 LeetCode 設計在完成最多 k 個不同項目後最大化其總資本的最佳方法。

給您 n 個項目，其中第 i 個項目具有純利潤利潤 [i]，並且啟動它所需的最低資本為 Capital[i]。

最初，你有w資本。當您完成專案時，您將獲得其純利潤，並將該利潤添加到您的總資本中。

**從給定項目中選擇最多 k 個不同項目的列表，以最大化您的最終資本，並返回最終最大化的資本。**

答案保證適合 32 位元有符號整數。

解題思路：
資料準備：首先，將所有項目依照所需資本從小到大排序，每個項目是一個包含所需資本和可能獲得利潤的二元組。
優先隊列使用：利用一個最大堆來保持目前可投資的項目的利潤。這樣每次都可以優先投資利潤最大的項目。
資金增長迭代：按照所能承受的最大資本，不斷將符合條件的項目利潤加入最大堆，然後從堆中取出最大元素增加到資金中。
迭代次數：最多重複k次，或者當沒有可投資的項目時結束。


時間複雜度：O(N log N + k log N)，其中N是項目數目。O(N log N)來自於排序，每次迭代中對堆的操作是O(log N)，最多進行k次。
空間複雜度：O(N)，用於存儲所有項目的排序列表和最大堆。
    """
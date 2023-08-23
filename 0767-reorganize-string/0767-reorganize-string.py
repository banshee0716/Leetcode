class Solution:
    def reorganizeString(self, s: str) -> str:
        # 使用 Counter 計算每個字符的出現次數
        count = Counter(s)
        # 建立一個最大堆來保存字符和其出現次數，注意我們使用-negative count以創建最大堆
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None  # 儲存前一次從堆中取出的字符和計數
        res = ""  # 結果字串

        while maxHeap or prev:
            # 如果僅有prev而堆為空，則無法重新組織字串
            if prev and not maxHeap:
                return ""
            # 從堆中取出計數最多的字符
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1  # 更新計數

            # 如果前一個字符存在，將其放回堆中
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # 如果當前字符的計數不為0，保存它以在下一次迭代中使用
            if cnt != 0:
                prev = [cnt, char]

        return res

        
        # 回傳任何一個可能的組合都可以
        
        
        
"""
解題思路：
計數：首先，我們需要計算每個字符出現的次數。為此，我們使用Counter。

最大堆：接下來，我們建立一個最大堆(max heap)來保存每個字符及其計數。堆中元素的順序是根據字符的出現次數來決定的。

重新組織：我們從最大堆中取出計數最多的字符，將它加到結果字串中，然後將其計數減1，並將其保存起來，以在下一次迭代中重新插入堆中。每次迭代時，我們都從堆中取出計數最多的字符，這確保了我們不會連續放置相同的字符。

時間複雜度: O(N log A)，其中 N 是字串的長度，A 是字符集的大小。這是因為每次從堆中插入或刪除元素的操作都需要 log A 的時間，而我們需要執行 N 次這樣的操作。

空間複雜度: O(A)，這裡的 A 是字符集的大小。因為我們需要存儲每個字符及其出現次數。
"""
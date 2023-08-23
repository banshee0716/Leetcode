class Solution:
    def reorganizeString(self, s: str) -> str:
        # 使用Counter計算每個字符的出現次數
        count = Counter(s)
        
        # 創建一個最大堆來存儲字符及其出現次數
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        res = ""
        
        # 當堆不為空或者還有暫存的字符時，持續處理
        while maxHeap or prev:
            # 如果只有暫存的字符，則無法組織字符串，返回空字符串
            if prev and not maxHeap:
                return ""
            
            # 從最大堆中取出出現次數最多的字符
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            # 如果有暫存的字符，將其放回堆中
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            # 如果當前字符還有剩餘，暫存起來
            if cnt != 0:
                prev = [cnt, char]

        return res


"""
給定一個字符串 s，重新排列 s 的字符，使得任意兩個相鄰的字符不相同。

返回 s 的任何可能的重新排列，如果不可能則返回 

解題思路：
1. Counter 統計字符串中每個字符出現的次數。
2. 堆 (maxHeap) 存儲字符及其出現次數，使用 -cnt 因為 Python 的 heapq 默認是最小堆。
3. 最大堆中取出出現次數最多的字符，並將其加入結果字符串中。然後將這個字符的出現次數減一。
4. 保相同的字符不會相鄰，每次從堆中取出一個字符後，我們先不立即將它放回堆中，而是等到下一次再放回。

時間複雜度:

O(NlogA)，其中 N 是字符串的長度，A 是字母表的大小（在這裡是 26，因為只有小寫字母）。
空間複雜度:

O(A) - 我們用於存儲字符的出現次數。
    """
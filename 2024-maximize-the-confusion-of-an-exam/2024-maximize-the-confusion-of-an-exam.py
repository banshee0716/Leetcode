class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        maxf = 0  # 最頻繁的字符出現的次數
        ans = 0  # 窗口的大小
        count = collections.Counter()  # 儲存字符出現次數的Counter對象
        n = len(answerKey)

        for i in range(n):
            # 將字符放入Counter並更新最頻繁的字符出現的次數
            count[answerKey[i]] += 1
            maxf = max(maxf, count[answerKey[i]])

            # 如果窗口的大小減去最頻繁的字符出現的次數小於k，則擴大窗口
            if ans - maxf < k:
                ans += 1
            else:
                # 否則，窗口不變，並將左邊界的字符從Counter中移除
                count[answerKey[i - ans]] -= 1

        return ans

        
"""
解題思路使用了滑動窗口（Sliding Window）和哈希映射（Hash Map）來處理。
我們從左到右遍歷答案鍵，將每個字符放入Counter對象（也就是哈希映射）中並記錄最頻繁的字符出現的次數。
如果窗口的大小減去最頻繁的字符出現的次數小於k，我們可以將窗口擴大。否則，我們將左邊界的字符從Counter中移除，並且窗口不變。

時間複雜度為O(n)，其中n是答案鍵的長度。這是因為我們對答案鍵進行了一次遍歷。
空間複雜度為O(1)，因為Counter對象中最多只存儲了兩個字符的出現次數。
"""
from collections import defaultdict

class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # 使用字典保存每個字符的出現位置
        seenCharAt = defaultdict(list)
        # 使用集合保存找到的回音子字符串，避免重複
        res = set()

        # 遍歷整個字符串
        for i, char in enumerate(text):
            # 如果當前字符之前出現過
            if char in seenCharAt:
                # 檢查每一個先前的出現位置
                for prevPos in seenCharAt[char]:
                    # 計算子字符串的長度
                    suffixLen = i - prevPos
                    # 比較兩個子字符串是否相同
                    if text[prevPos:i] == text[i:i+suffixLen]:
                        # 將找到的回音子字符串添加到集合中
                        res.add(text[prevPos:i+suffixLen])
            # 將當前字符的位置添加到字典中
            seenCharAt[char].append(i)
        
        # 返回不同的回音子字符串的數量
        return len(res)

"""
回音子字符串定義為某個子字符串可以被分為兩個相同的部分。

解題思路
1. 為了找到所有可能的回音子字符串，我們需要遍歷整個字符串。
2. 使用seenCharAt字典保存每個字符的出現位置。
3. 當遍歷字符串時，每遇到一個字符，就去查詢此字符之前出現的位置。因為如果目前的子字符串是一個回音子字符串，則它的前半部分必定在先前的某個位置。
4. 對於找到的每一個先前的位置，比較從那個位置到目前位置的子字符串和從目前位置開始的下一段子字符串是否相同。如果相同，那麼我們找到了一個回音子字符串。
5. 使用一個集合res保存找到的回音子字符串，這樣可以避免重複。
6. 最後，返回集合的大小，這就是不同的回音子字符串的數量。


時間複雜度: 最壞情況下為 O(n^3)，其中 n 是 text 的長度。這是因為我們需要遍歷字符串的每個字符，並對於每個字符，我們可能要查看其所有先前的位置，並在某些情況下使用O(n)的時間來比較子字符串。

空間複雜度: O(n^2)。這是因為在最壞情況下，res集合可能需要存儲所有可能的回音子字符串，且seenCharAt字典會存儲每個字符的所有位置。
"""
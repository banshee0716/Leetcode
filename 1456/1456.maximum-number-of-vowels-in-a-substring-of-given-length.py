#
# @lc app=leetcode id=1456 lang=python3
#
# [1456] Maximum Number of Vowels in a Substring of Given Length
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = j = vowels = 0  # 初始化結果、左邊界指標和元音數量變數
        for i, c in enumerate(s):  # 遍歷字符串s的每個字符和其索引
            vowels += c in 'aeiou'  # 如果當前字符是元音，則將元音數量加1
            if i - j + 1 > k:  # 檢查當前子字符串的長度是否大於k， 若大於k，則檢查左邊界字符是否為元音，若是則將元音數量減1
                vowels -= s[j] in 'aeiou' 
                j += 1  # 將左邊界指標右移一位
            if i - j + 1 == k:  # 當當前子字符串長度等於k時,更新最大元音數量
                res = max(res, vowels) 
        return res  # 返回最大元音數量

'''
時間複雜度：O(n)，
其中n是字符串s的長度。這個演算法需要遍歷整個字符串一次，因此時間複雜度為O(n)。

空間複雜度：O(1)。
在這個演算法中，我們只使用了常數個變數，例如res、j和vowels，因此空間複雜度為O(1)。
'''
# @lc code=end


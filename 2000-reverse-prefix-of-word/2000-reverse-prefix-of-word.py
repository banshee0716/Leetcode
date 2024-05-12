class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # 找到字符ch在字串word中的索引位置
        index = word.find(ch)
        # 如果字符存在於字串中
        if index != -1:
            # 反轉word從開頭到字符ch的部分，並將其與剩餘字串結合
            return word[:index+1][::-1] + word[index+1:]
        
        # 如果字符不存在，返回原字串
        return word

    
    """
給定一個索引為 0 的字串 word 和一個字元 ch，反轉從索引 0 開始到第一次出現 ch（包括）的索引結束的單字段。如果單字 ch 不存在，則不執行任何操作。
例如，如果 word = "abcdefd" 且 ch = "d"，則應反轉從 0 開始到 3（含）結束的段。結果字串將為“dcbaefd”。
傳回結果字串。

解題思路
這道題的核心是使用字符串操作來實現以下步驟：

1. 查找字符：使用str.find()方法查找給定字符ch在字串word中第一次出現的位置。
2. 反轉前綴：如果字符存在，則將該字符及其之前的所有字符進行反轉。
3. 組合字串：將反轉的前綴與剩餘的字串結合。

時間複雜度分析
時間複雜度：O(n)，其中n是字符串word的長度。在最壞的情況下，find()函數需要遍歷整個字符串來尋找字符ch。

空間複雜度分析
空間複雜度：O(n)，在執行反轉操作時，可能需要一個額外的空間來存儲反轉後的字符串部分。
    """
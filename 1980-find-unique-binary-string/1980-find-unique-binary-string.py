class Solution:
    def findDifferentBinaryString(self, binaryStrings: List[str]) -> str:
        result = []

        # 遍歷每個二進位字符串
        for i in range(len(binaryStrings)):
            # 獲取相同索引位置上的字符
            current_character = binaryStrings[i][i]

            # 將相反的二進位值添加到結果字符串中
            result.append('1' if current_character == '0' else '0')

        # 返回連接後的新二進位字符串
        return ''.join(result)
"""
解題思路：

1. 對角線方法：
    -遍歷給定的二進制字串列表，對於每個字串，取出其在對角線位置（即索引 i）的字符。
    -將此字符取反（0 變 1，1 變 0），然後將其添加到結果字串中。
    -這樣可以保證對於列表中的每個字串，在對角線位置至少有一個字符是不同的，從而保證生成的二進制字串不在列表中。
    
2. 實現步驟：
    -初始化一個空的列表 result 來存儲結果字串的每個字符。
    -遍歷二進制字串列表，對於每個字串的對角線位置，取反並添加到 result 中。
    -使用 join 函數將 result 中的字符連接成一個完整的二進制字串。
    
時間複雜度分析：
遍歷二進制字串列表的時間複雜度為 O(n)，其中 n 為列表的長度。

空間複雜度分析：
需要一個列表來存儲結果字串的字符，空間複雜度為 O(n)。
"""
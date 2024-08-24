class Solution:
    def nearestPalindromic(self, numberStr: str) -> str:
        number = int(numberStr)  # 將輸入的字串轉換為整數
        if number <= 10:  # 處理10以下的數字情況
            return str(number - 1)
        if number == 11:  # 處理11的特殊情況
            return "9"

        length = len(numberStr)  # 取得數字的長度
        leftHalf = int(numberStr[:(length + 1) // 2])  # 取得數字的左半部分
        
        # 生成可能的回文候選數列表
        palindromeCandidates = [
            self.generatePalindromeFromLeft(leftHalf - 1, length % 2 == 0),  # 左半部分減1生成的回文
            self.generatePalindromeFromLeft(leftHalf, length % 2 == 0),  # 左半部分生成的回文
            self.generatePalindromeFromLeft(leftHalf + 1, length % 2 == 0),  # 左半部分加1生成的回文
            10**(length - 1) - 1,  # 最小的n位數回文（例如99）
            10**length + 1  # 最大的n位數回文（例如1001）
        ]

        nearestPalindrome = 0  # 用於存儲最近的回文數
        minDifference = float('inf')  # 初始化最小差值為無窮大

        # 遍歷所有回文候選數並找到距離最近的回文
        for candidate in palindromeCandidates:
            if candidate == number:  # 忽略與原數字相同的候選數
                continue
            difference = abs(candidate - number)  # 計算候選數與原數字的差值
            if difference < minDifference or (difference == minDifference and candidate < nearestPalindrome):
                minDifference = difference  # 更新最小差值
                nearestPalindrome = candidate  # 更新最近的回文數

        return str(nearestPalindrome)  # 返回最近的回文數字串

    def generatePalindromeFromLeft(self, leftHalf: int, isEvenLength: bool) -> int:
        palindrome = leftHalf  # 從左半部分開始構建回文數
        if not isEvenLength:  # 如果數字長度為奇數，去掉中間的數字
            leftHalf //= 10
        while leftHalf > 0:  # 將左半部分翻轉並附加到回文的末尾
            palindrome = palindrome * 10 + leftHalf % 10
            leftHalf //= 10
        return palindrome  # 返回生成的回文數

    """
解題思路：
特別處理簡單案例： 如果數字小於等於10，最近的回文數就是它減1。如果數字為11，最近的回文數是9。
生成候選回文數： 對於較大的數字，我們首先生成數字的前半部分（leftHalf），然後根據這個前半部分生成三個回文數，分別是leftHalf減1、leftHalf和leftHalf加1生成的回文數。此外，還有兩個特殊的回文候選數是最小的n位數減1和最大的n位數加1（例如99和1001）。
比較與選擇最近的回文數： 將所有生成的回文數候選與原數字進行比較，找到與原數字差值最小的回文數作為結果。

時間複雜度：
生成候選回文數的時間複雜度是 O(n)，其中 n 是數字的長度。對於每個候選回文數，我們需要花費 O(n) 時間來生成，總共有5個候選者，因此總時間複雜度為 O(n)。

空間複雜度：
空間複雜度主要來自於儲存候選回文數和執行過程中的臨時變量。這些變量的空間複雜度是常數級別 O(1)，所以總的空間複雜度為 O(1)。

    """
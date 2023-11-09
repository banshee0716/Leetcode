class Solution:
    def countHomogenous(self, s: str) -> int:
        # 初始化結果、當前計數和字符串長度
        res, count, n = 0, 1, len(s)
        
        # 遍歷字符串
        for i in range(1, n):
            # 如果當前字符與前一個字符相同，增加計數
            if s[i] == s[i - 1]:
                count += 1
            else:
                # 如果計數大於1，計算同源子串數量並加到結果中
                if count > 1:
                    res += (count * (count - 1) // 2)
                # 重置計數
                count = 1
                
        # 檢查最後一段字符序列
        if count > 1:
            res += (count * (count - 1) // 2)
            
        # 返回總同源子串數量，每個字符本身也是一個同源子串，所以要加上n，並對10^9+7取模
        return (res + n) % (10**9 + 7)

# 使用black格式化後的代碼與上述代碼在格式上已經符合標準

    
    
    
        """
時間複雜度分析：

遍歷字符串s的時間複雜度為O(n)，其中n為字符串s的長度。
空間複雜度分析：

這段代碼使用了固定大小的額外空間來儲存res、count和n，因此空間複雜度為O(1)。
        """
class Solution:
    def minimumCost(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n-1):
            if s[i] != s[i + 1]:
                if i + 1 <= n - i - 1:
                    ans += i + 1
                else:
                    ans += n - i - 1
        return ans
"""
給定一個長度為 n 的 0 索引二進製字符串 s，您可以在其上應用兩種類型的操作：

選擇索引 i 並將索引 0 到索引 i（包括兩者）的所有字符反轉，成本為 i + 1
選擇索引 i 並將索引 i 中的所有字符反轉為索引 n - 1（包含兩者），成本為 n - i

返回使字符串中所有字符相等的最小成本。

反轉字符意味著如果其值為“0”，則變為“1”，反之亦然。
"""
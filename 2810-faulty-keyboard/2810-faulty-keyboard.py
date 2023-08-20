class Solution:
    def finalString(self, s: str) -> str:
        ans = ""
        for i in s:
            print(i)
            if i == "i":
                ans = ans[::-1]
            else:
                ans += i
        return ans
        
        """
您的筆記本電腦鍵盤有故障，每當您在其上鍵入字符“i”時，它都會反轉您所寫的字符串。輸入其他字符可以按預期工作。

給定一個索引為 0 的字符串 s，然後使用有問題的鍵盤鍵入 s 的每個字符。

返回將出現在筆記本電腦屏幕上的最終字符串。
        """
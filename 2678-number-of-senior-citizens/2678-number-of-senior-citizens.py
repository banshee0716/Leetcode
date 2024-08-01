class Solution:
    def countSeniors(self, details: List[str]) -> int:
        res = 0
        for i in details:
            if int(i[11:13]) > 60:
                res += 1
                
        return res
        
        
        

"""
您將獲得一個 0 索引的字串詳細資訊數組。詳細資訊的每個元素都提供有關壓縮為長度為 15 的字串的給定乘客的資訊。

前十個字元由乘客的電話號碼組成。
下一個字元表示該人的性別。
以下兩個字元用於表示該人的年齡。
最後兩個字符決定分配給該人的座位。

返回嚴格年齡在 60 歲以上的乘客人數。
"""
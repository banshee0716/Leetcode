class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            if str(i) * 3 in num:
                return str(i) *3
        return ''
        
        
        
    """
給定一個表示大整數的字串 num。如果滿足以下條件，則整數是好的：

    -它是num的一個長度為3的子字串。
    -它僅由一個唯一的數字組成。
    -以字串形式傳回最大的好整數，如果不存在這樣的整數，則傳回空字串「」。

筆記：

    -子字串是字串中連續的字元序列。
    -num 中可能有前導零或一個好的整數。
    """
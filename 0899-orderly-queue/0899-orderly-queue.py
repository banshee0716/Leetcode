class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
            #如果k>1的話,也就是每次都會把最前面k個不斷重排，最後的結果就會是sort之後的值
        return min(s[i:]+s[:i]for i in range(len(s)))
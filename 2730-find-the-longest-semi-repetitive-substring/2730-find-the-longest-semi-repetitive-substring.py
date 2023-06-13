class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        #s = '52233'
        s = s[0] + s + s[-1]                                    # s = '5522333'

        arr = [i for i in range(len(s)-1) if s[i] == s[i+1]]    # ans = [0, 2, 4, 5]
        
        return max ((y - x for x,y in zip(arr, arr[2:])),       # return max(4-0, 5-2) = 4
                                         default = len(s)-2)
        
        
        
        
        """
        給定一個由 0 到 9 的數字組成的 0 索引字符串 s。
如果在 t 中最多有一對連續的相同數字，則字符串 t 稱為半重複字符串。例如，0010、002020、0123、2002 和 54944 是半重複的，而 00101022 和 1101234883 則不是。

返回 s 中最長的半重複子串的長度。

子字符串是字符串中連續的非空字符序列。
        """
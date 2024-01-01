class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(reverse = True)
        s.sort(reverse = True)
        res, i , j = 0 ,0,0
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                res+=1
                i+=1
                j+=1
            else:
                i+=1
        return res
    
    """
假設您是一位很棒的父母，想給您的孩子一些餅乾。但是，您最多應該給每個孩子一塊餅乾。

每個孩子 i 都有貪婪因子 g[i]，它是孩子能夠滿足的 cookie 的最小大小；每個 cookie j 的大小為 s[j]。如果 s[j] >= g[i]，我們可以將 cookie j 指派給子 i，而子 i 將是內容。您的目標是最大化內容子項的數量並輸出最大數量。
    """
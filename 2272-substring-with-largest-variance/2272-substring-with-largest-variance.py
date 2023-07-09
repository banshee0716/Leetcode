import collections
import string
from typing import List

class Solution:
    def largestVariance(self, s: str) -> int:
        # 創建一個字典，鍵為字符，值為該字符在字符串中的所有索引
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        
        ans = 0
        # 遍歷每一對不同的字符
        for x, chr1 in enumerate(string.ascii_lowercase):
            for chr2 in string.ascii_lowercase[x+1:]:
                # 如果兩個字符相同，或者其中一個字符不在字典中，則跳過
                if chr1 == chr2 or chr1 not in d or chr2 not in d:
                    continue
                
                # 初始化變量
                prefix = i = p1 = p2 = 0
                hi = hi_idx = lo = lo_idx = 0
                n1, n2 = len(d[chr1]), len(d[chr2])
                
                # 使用兩個指針遍歷兩個字符的索引列表
                while p1 < n1 or p2 < n2:
                    if p1 < n1 and p2 < n2:
                        if d[chr1][p1] < d[chr2][p2]:
                            prefix, p1 = prefix+1, p1+1
                        else:
                            prefix, p2 = prefix-1, p2+1
                    elif p1 < n1:        
                        prefix, p1 = prefix+1, p1+1
                    else:
                        prefix, p2 = prefix-1, p2+1
                    
                    # 更新最高值和最低值
                    if prefix > hi:
                        hi, hi_idx = prefix, i
                    if prefix < lo:
                        lo, lo_idx = prefix, i
                    
                    # 更新答案
                    ans = max(ans, min(prefix-lo, i-lo_idx-1))
                    ans = max(ans, min(hi-prefix, i-hi_idx-1)) 
                    i += 1 
        
        return ans

"""
1. 我們首先遍歷字符串，用一個字典 d 儲存每個字符與其在字符串中的所有索引。

2. 然後我們遍歷每一對不同的字符 chr1 和 chr2。如果 chr1 和 chr2 都在字典 d 中，我們使用兩個指針 p1 和 p2 分別遍歷兩個字符的索引列表。

3. 對於每一個索引，如果它是 chr1 的索引，我們就讓 prefix 加一，否則讓 prefix 減一。然後我們更新最高值 hi 和最低值 lo，以及它們的索引 hi_idx 和 lo_idx。

4. 最後，我們計算並更新答案 ans，它是當前的 prefix 與 lo 的差值，以及當前的 hi 與 prefix 的差值中的較小值。這兩個差值分別表示目前 chr1 的數量與 chr2 的數量的最大差值，以及 chr2 的數量與 chr1 的數量的最大差值。

時間複雜度
為 O(n^2)，其中 n 是字符的數量。這是因為我們需要遍歷每一對不同的字符，並且對每一對字符都需要進行 O(n) 時間的操作。這裡 n 為字符串的長度。

空間複雜度
為 O(n)，其中 n 為字符的種類數量乘以每種字符出現的平均次數。因為我們需要用一個字典來保存每個字符的索引列表。在最壞的情況下，每種字符都會出現，且出現次數都相等，所以空間複雜度為 O(n)。
"""
import collections
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        mp = Counter(arr)
        v = list(mp.values())
        cnt = 0
        
        v.sort()
        for i in range(len(v)):
            if k > v[i]:
                k -= v[i]
                v[i] = 0
            else:
                v[i] -= k
                k = 0
            if v[i] != 0:
                cnt += 1
                
        return cnt
    
"""
解題思路
統計每個數字的出現次數：
    -使用collections.Counter或Counter從collections模塊來統計數組中每個數字的出現次數。

排序出現次數：
    -將出現次數存儲在一個列表v中，然後對這個列表進行升序排序，以便先處理出現次數最少的數字。

刪除元素：
    -遍歷排序後的出現次數列表v。
    -對於每個出現次數，如果k大於當前的出現次數，則將k減去這個出現次數，並將當前出現次數設為0（表示該數字已完全刪除）。
    -否則，從當前出現次數中減去k（表示部分或全部刪除該數字），並將k設為0。

計數剩餘的不同數字：
    -繼續遍歷出現次數列表，如果當前出現次數不為0，則將計數器cnt加1。

返回結果：
    -返回計數器cnt的值，即為剩餘的最少不同整數的數量。
"""
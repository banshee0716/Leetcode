class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 2
        for i in range(len(arr)):
            for j in range (i+1,len(arr)):
                a, b, l = arr[i], arr[j], 2 #元素，元素，長度
                while a + b in s:#計算斐波納契有沒有在集合裡面
                    a, b, l = b, a+b, l+1
                
                res = max(l,res)
                
        return res if res > 2 else 0
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 儲存結果的列表
        arr = []
        # 當前組合
        nums = [0] * k
        # 回溯函數，pos表示當前處理到的位置，cur表示當前的數字
        def backTracking(pos, cur):
            # 如果已經選取了k個數字，則加入到結果中
            if pos == k:
                arr.append(nums[:])
                return 
            # 從cur開始選取數字，選取範圍為[cur, n-k+pos+2)
            for i in range(cur, n-k+pos+2):
                nums[pos] = i
                # 進入下一層選取
                backTracking(pos+1, i+1)
        # 從第一個數字開始選取
        backTracking(0, 1)
        return arr

            
"""
nums 是當前的組合。
pos 是 nums 中的當前位置
cur 是當前號碼

在函數回溯中：
如果 pos == k，我們就知道我們得到了其中一個組合。
如果 pos != k，我們可以嘗試所有可能的數字來適應當前位置，然後再次調用回溯。

時間複雜度為O(C(n, k))，因為我們需要遍歷所有的可能組合，這裡的C(n, k)表示從n中選取k的組合數。
空間複雜度為O(k)，因為我們需要一個長度為k的列表來保存當前的組合。
"""
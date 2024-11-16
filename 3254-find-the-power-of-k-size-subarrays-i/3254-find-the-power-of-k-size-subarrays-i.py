class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        if k == 1:
            return nums[:]
        if n < k:
            return result
        diff = [nums[i + 1] - nums[i] for i in range(n - 1)]
        bad = 0
        
        for i in range(k - 1):
            if diff[i] != 1:
                bad += 1
        for i in range(n - k + 1):
            if bad == 0:
                result.append(nums[i + k - 1])
            else:
                result.append(-1)
            if i + k - 1 < n - 1:
                if diff[i] != 1:
                    bad -= 1
                if diff[i + k - 1] != 1:
                    bad += 1
            else:
                if diff[i] != 1:
                    bad -= 1
        
        return result
    
    
    
    
    """
時間複雜度：O(n)
預處理差分陣列需要 O(n) 的時間。
初始化第一個窗口的 bad 值需要 O(k) 的時間，因為 k≤n，所以這部分最多也是 O(n)。

滑動窗口的過程中，每個窗口的更新和檢查都在 O(1) 的時間內完成，共有 n−k+1 個窗口，總共 O(n) 的時間。

空間複雜度：O(n)
差分陣列 diff 需要 O(n) 的空間。
結果陣列 result 需要 O(n) 的空間。
    """
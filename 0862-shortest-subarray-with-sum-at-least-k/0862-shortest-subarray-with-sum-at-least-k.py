class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSums = [0] * (n + 1)
        
        for i in range(n):
            prefixSums[i + 1] = prefixSums[i] + nums[i]
            
        result = n + 1
        deque_indices = deque()
        
        for i in range(n + 1):
            while deque_indices and prefixSums[i] - prefixSums[deque_indices[0]] >= k:
                result = min(result, i - deque_indices.popleft())
            while deque_indices and prefixSums[i] <= prefixSums[deque_indices[-1]]:
                deque_indices.pop()
            
            deque_indices.append(i)
            
        return result if result <= n else -1
        
        
        
    """
前綴和
首先，我們計算數組的前綴和數組 prefixSums，其中：prefixSums[i]=nums[0]+nums[1]+⋯+nums[i−1]
這樣，對於任意的子陣列 nums[i..j]，其和為： =prefixSums[j+1]−prefixSums[i]
我們的目標是找到最短的 (j - i)，使得 prefixSums[j + 1] - prefixSums[i] >= k。

單調隊列
我們需要一個高效的方法來找到所有滿足上述條件的 (i, j)，並找到其中最短的 (j - i)。
這裡我們使用一個單調遞增的雙端隊列 deque 來存儲前綴和的索引。我們保持隊列中的索引對應的前綴和值是單調遞增的。這樣可以確保我們能夠在 O(n) 的時間內找到符合條件的最短子陣列。

具體步驟
初始化：
計算前綴和數組 prefixSums，長度為 n + 1，其中 prefixSums[0] = 0。
初始化一個結果變量 result = n + 1，表示最短長度。
初始化一個雙端隊列 deque。

遍歷前綴和數組：
對於每個位置 i（從 0 到 n）：
檢查條件一：當 deque 不為空，且 prefixSums[i] - prefixSums[deque[0]] >= k：
更新 result = min(result, i - deque[0])。
移除隊首元素 deque.popleft()。
保持隊列單調性：當 deque 不為空，且 prefixSums[i] <= prefixSums[deque[-1]]：
移除隊尾元素 deque.pop()。
將當前索引 i 添加到隊尾 deque.append(i)。

返回結果：
如果 result <= n，返回 result。
否則，返回 -1，表示沒有找到符合條件的子陣列。

為什麼這樣做有效？
單調性：我們保持隊列中的前綴和索引對應的值是單調遞增的，這樣可以確保當我們找到一個新的 prefixSums[i] 時，能夠快速找到最早的、使得差值達到 k 的索引。
效率：由於每個索引最多被加入和移除一次，整個過程的時間複雜度為 O(n)。

複雜度分析
時間複雜度：O(n)
計算前綴和需要 O(n) 的時間。
主循環中，每個索引 i 只會被加入和彈出 deque 一次，因此總的循環時間為 O(n)。

空間複雜度：O(n)
前綴和數組 prefixSums 需要 O(n) 的空間。
雙端隊列 deque 最多包含O(n) 個元素。
    """
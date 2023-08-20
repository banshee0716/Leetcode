from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        # 初始化完整子陣列的數量為0
        complete = 0
        n = len(nums)
        # 原始陣列中的唯一元素數量
        k = len(set(nums))
        count = defaultdict(int)
        i = 0
        for j in range(n):
            # 更新當前元素的計數
            count[nums[j]] += 1
            # 檢查當前子陣列是否是完整的
            while len(count) == k:
                # 增加完整子陣列的數量
                complete += n-j
                # 縮小窗口的大小
                count[nums[i]] -= 1
                # 如果某個元素的計數為0，則從字典中刪除它
                if not count[nums[i]]:
                    count.pop(nums[i])
                i += 1
        
        return complete

        """
給定一個由正整數組成的數組 nums。

如果滿足以下條件，我們稱數組的子數組為完整數組：
    -子數組中不同元素的數量等於整個數組中不同元素的數量。

返回完整子數組的數量。
子數組是數組的連續非空部分。

思路
1. 滑動窗口法 (Sliding Window): 考慮使用滑動窗口的技巧。定義 i 和 j 分別為子陣列的起始和結束位置。窗口的範圍是從 i 到 j。
2. 我們使用 count 這個字典來記錄當前子陣列中每個元素的數量。
3. 當子陣列中的唯一元素數量等於原始陣列中的唯一元素數量時，我們知道我們找到了一個完整子陣列。然後，考慮到子陣列 i 到 j 是完整的，從 i 到 n-1 的所有子陣列都是完整的。所以對於每個這樣的 j，我們可以添加 n-j 個完整子陣列。
4. 之後，我們會縮小窗口的大小，也就是增加 i 的值，並適當調整 count。

時間複雜度: O(n)，其中 n 是 nums 的長度。儘管我們有兩個循環，但每個元素僅被處理兩次：一次是由外部循環，一次是由內部循環。

空間複雜度: O(n)，在最壞情況下，我們可能需要存儲所有不同的元素。
        """
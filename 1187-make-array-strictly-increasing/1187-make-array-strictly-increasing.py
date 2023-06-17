class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        # 初始化 dp 字典，設置一個虛擬前導數值 -1，不需要任何替換
        dp = {-1:0}
        # 將 arr2 排序
        arr2.sort()
        # 遍歷 arr1
        for i in arr1:
            # 使用一個臨時的字典 tmp 儲存可能的 dp 狀態
            tmp = collections.defaultdict(lambda: float('inf'))
            # 對於當前 dp 的每個狀態
            for key in dp:
                # 如果 arr1 的當前值 i 大於 dp 狀態的 key
                # 則可以將 i 直接接在 key 後面
                # 更新 tmp[i] 的狀態為 dp[key]
                if i > key:
                    tmp[i] = min(tmp[i],dp[key])
                # 使用二分查找在 arr2 中找到剛好大於 key 的數字的位置
                loc = bisect.bisect_right(arr2,key)
                # 如果該位置不越界，則可以將 arr2[loc] 接在 key 後面
                # 更新 tmp[arr2[loc]] 的狀態為 dp[key]+1
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]],dp[key]+1)
            # 用 tmp 更新 dp
            dp = tmp
        # 如果 dp 為空，則返回 -1，否則返回 dp 的最小值
        if dp:
            return min(dp.values())
        return -1
"""
時間複雜度為O(n^2*logn)，空間複雜度為O(n)，其中n是arr1的長度。
"""
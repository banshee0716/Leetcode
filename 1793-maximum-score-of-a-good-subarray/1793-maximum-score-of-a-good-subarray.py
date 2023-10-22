class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # 初始化左右邊界數組
        leftBoundary = [-1] * n  # 記錄左邊的下一個較小元素。
        rightBoundary = [n] * n  # 記錄右邊的下一個較小元素。

        leftStack = []  # 用於計算左邊界的單調棧。
        rightStack = []  # 用於計算右邊界的單調棧。

        # 計算從左側的下一個較小元素
        for i in range(n - 1, -1, -1):
            while leftStack and nums[leftStack[-1]] > nums[i]:
                leftBoundary[leftStack[-1]] = i
                leftStack.pop()
            leftStack.append(i)

        # 計算從右側的下一個較小元素
        for i in range(n):
            while rightStack and nums[rightStack[-1]] > nums[i]:
                rightBoundary[rightStack[-1]] = i
                rightStack.pop()
            rightStack.append(i)

        maxScore = 0  # 初始化最大得分為0

        # 計算良好子數組的最大得分
        for i in range(n):
            if leftBoundary[i] < k and rightBoundary[i] > k:
                subarrayScore = nums[i] * (rightBoundary[i] - leftBoundary[i] - 1)
                maxScore = max(maxScore, subarrayScore)  # 更新最大得分

        return maxScore  # 返回良好子數組的最大得分
    
    
"""
解題思路：

1. 我們使用了兩個單調棧來計算每個元素的左右邊界。
2. 左邊界表示該元素左側的下一個較小元素的索引；右邊界表示該元素右側的下一個較小元素的索引。
3. 然後，我們遍歷每個元素，確定該元素所在的子數組是否包含索引 k。如果包含，我們就計算該子數組的得分並更新最大得分。

時間複雜度：
由於我們只遍歷了每個元素一次，所以時間複雜度為 O(N)，其中 N 是數組 nums 的長度。

空間複雜度：
我們使用了兩個單調棧和兩個邊界數組，所以空間複雜度為 O(N)。
"""
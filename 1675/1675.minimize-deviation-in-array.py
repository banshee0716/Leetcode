#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#

# @lc code=start
class Solution:
    def minimumDeviation(self, nums):
        heap = []
        # 將數字轉換成最小的偶數和最大的數字組成的tuple加入heap中
        for num in nums:
            tmp = num
            while tmp % 2 == 0:
                tmp //= 2
            heap.append((tmp, max(num, tmp * 2)))

        # 取出heap中最大的數字作為Max
        Max = max(i for i, j in heap)
        heapify(heap)
        ans = float("inf")

        # 當heap中的元素數量等於nums的長度時，執行以下迴圈
        while len(heap) == len(nums):
            # 取出heap中最小的數字
            num, limit = heappop(heap)
            # 計算當前數字與最大數字之差
            ans = min(ans, Max - num)
            # 如果當前數字小於最大數字限制，將該數字乘以2後重新放入heap中
            if num < limit:
                heappush(heap, (num * 2, limit))
                # 更新最大數字
                Max = max(Max, num * 2)

        # 回傳答案
        return ans


# @lc code=end

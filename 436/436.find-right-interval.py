#
# @lc app=leetcode id=436 lang=python3
#
# [436] Find Right Interval
#

# @lc code=start
import bisect


class Solution:
    def findRightInterval(self, intervals):
        # 將區間結束位置、起始位置、原索引存入新列表ints中
        ints = sorted([[j, k, i] for i, [j, k] in enumerate(intervals)])
        # 將所有起始位置存入列表begs中
        begs = [i for i, _, _ in ints]
        # 初始化存放結果的列表out
        out = [-1] * len(begs)
        # 遍歷排序過的ints，對於每個區間，使用二分查找找到其右側最近的區間並將其原索引存入out中
        for i, j, k in ints:
            t = bisect.bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        # 返回結果
        return out


"""
時間複雜度：排序所需的時間複雜度為O(nlogn)，遍歷列表所需的時間複雜度為O(n)，二分查找所需的時間複雜度為O(logn)，因此總時間複雜度為O(nlogn)。
空間複雜度：除了存放結果的列表外，需要O(n)的額外空間來存儲排序後的區間結束位置、起始位置和原索引，因此空間複雜度為O(n)。"""


# @lc code=end

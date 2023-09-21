class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # 計算目標子數組和
        x = sum(nums) - x
        # 如果目標子數組和為0，則返回整個數組的長度
        if not x:
            return len(nums)
        # 初始化前綴和及其索引的字典
        seen = {0: -1}
        ans = prefix = 0
        for i, num in enumerate(nums):
            prefix += num
            # 如果當前前綴和減去目標和在字典中
            if prefix - x in seen:
                ans = max(ans, i - seen[prefix - x])
            # 將當前前綴和加入字典，僅當它是第一次出現時
            seen.setdefault(prefix, i)
        # 如果ans不為0，返回整個數組長度減去ans，否則返回-1
        return len(nums) - ans if ans else -1

"""
1. 先處理edge case：裡面的值直接超過
2. 用prefix的手法，去比較現在的值或者最後一個誰能夠精準的符合現況，如果他能夠讓ｘ更精準地符合到 0 的法則，就把他加入seen裡面。

時間複雜度：O(n)。我們只遍歷整個數組一次。
空間複雜度：O(n)。哈希表的大小最大為數組的長度。
"""
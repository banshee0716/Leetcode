class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        # 尋找中位數
        for count in range(0, (n + m) // 2 + 1):
            m2 = m1
            # 如果兩個數組都未遍歷完
            if i < n and j < m:
                # 選擇較小的數並前進
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            # 如果只有 nums1 未遍歷完
            elif i < n:
                m1 = nums1[i]
                i += 1
            # 如果只有 nums2 未遍歷完
            else:
                m1 = nums2[j]
                j += 1

        # 判斷 n + m 的奇偶性，返回對應的中位數
        if (n + m) % 2 == 1:
            return float(m1)
        else:
            return (float(m1) + float(m2)) / 2.0

        
"""

1. 初始化兩個指針 i 和 j，分別指向 nums1 和 nums2。
2. 使用 m1 和 m2 來儲存當前和前一個數。
3. 遍歷直到 (n + m) // 2 + 1，這樣確保我們遍歷到中位數的位置。
4. 在遍歷的過程中，比較 nums1[i] 和 nums2[j]，將較小的數存儲到 m1，並將指針向前移動。
5. 根據 n + m 的奇偶性返回中位數。

時間複雜度：O(m + n)。在最壞的情況下，我們可能需要遍歷所有的 nums1 和 nums2。
空間複雜度：O(1)。我們只使用了常數的額外空間。
"""
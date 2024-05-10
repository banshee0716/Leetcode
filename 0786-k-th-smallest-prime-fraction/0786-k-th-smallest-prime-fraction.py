from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        left, right = 0.0, 1.0

        while left < right:
            mid = (left + right) / 2
            count = 0
            max_fraction = 0
            numerator = 0
            denominator = 1

            j = 1
            for i in range(n):
                while j < n and arr[i] > arr[j] * mid:
                    j += 1
                count += n - j
                if j < n and arr[i] / arr[j] > max_fraction:
                    max_fraction = arr[i] / arr[j]
                    numerator, denominator = arr[i], arr[j]

            if count < k:
                left = mid + 1e-10
            elif count > k:
                right = mid
            else:
                return [numerator, denominator]

        return [numerator, denominator]

        
        """
    給定一個已排序的整數數組 arr，其中包含 1 和素數，其中 arr 的所有整數都是唯一的。您還將獲得一個整數 k。
對於每個 i 和 j（其中 0 <= i < j < arr.length），我們考慮分數 arr[i] / arr[j]。
傳回所考慮的第 k 個最小分數。以大小為 2 的整數陣列形式傳回答案，其中 answer[0] == arr[i] 且 answer[1] == arr[j]。

解題思路
這個問題可以通過二分搜索法來解決，其中使用了類似於「搜尋有序矩陣」的策略。

初始化範圍：設定初始的二分搜索範圍，left = 0 (代表最小可能的分數) 和 right = 1 (代表最大可能的分數)。
二分搜索：在範圍 [left, right] 內使用二分搜索找到可能的第 k 小的分數。
計數和更新：對於每個中間值 mid，計算總共有多少個分數小於或等於 mid。同時記錄當前最大的分數和其索引。
檢查並縮小範圍：如果找到的分數個數恰好為 k，則找到所需的分數。如果個數大於 k，則需要將 right 更新為 mid 縮小範圍；如果小於 k，則更新 left 為 mid。

時間複雜度
時間複雜度：O(n log n * logM)，其中 n 是數組 arr 的長度，logM 是對值域進行二分搜索的深度。
二分搜索次數：取決於值域的精度和範圍，通常是 log(1 / 精確度)。

空間複雜度
空間複雜度：O(1)，除了給定的輸入外，只使用了常數空間存儲臨時變量和計數。
        """
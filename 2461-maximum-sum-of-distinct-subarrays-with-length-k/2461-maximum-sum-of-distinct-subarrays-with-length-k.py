class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        elements = set()
        current_sum = 0
        max_sum = 0
        begin = 0

        for end in range(n): 
            if nums[end] not in elements:
                current_sum += nums[end]
                elements.add(nums[end])

                if end - begin + 1 == k:
                    if current_sum > max_sum:
                        max_sum = current_sum
                    
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
            else:
                while nums[begin] != nums[end]:
                    current_sum -= nums[begin]
                    elements.remove(nums[begin])
                    begin += 1
                
                begin += 1

        return max_sum
    
"""
方法概述
滑動窗口：我們可以使用滑動窗口的方法來遍歷數組，維護一個長度為 k 的窗口，並確保窗口內的元素都是不同的。
哈希集（Set）：使用一個哈希集合來跟蹤當前窗口內的元素，方便檢查是否有重複的元素。
具體步驟
初始化：

定義兩個指針 left 和 right，分別表示窗口的左邊界和右邊界。
初始化變量：
current_sum：當前窗口內元素的總和。
max_sum：滿足條件的子陣列的最大總和，初始為 0。
element_set：用於存儲當前窗口內的元素。
遍歷數組：

從 right = 0 開始遍歷到 n - 1：
將 nums[right] 加入到 current_sum 中。
檢查 nums[right] 是否已存在於 element_set 中：
如果已存在，則需要移動 left 指針，並從 element_set 中移除 nums[left]，同時更新 current_sum，直到 nums[right] 不在 element_set 中。
將 nums[right] 加入到 element_set 中。
如果當前窗口的大小超過了 k，則需要縮小窗口：
從 element_set 中移除 nums[left]，更新 current_sum，並將 left 指針右移一位。
如果當前窗口的大小正好為 k，且元素都是不同的：
更新 max_sum，取當前的 current_sum 和 max_sum 的較大值。
返回結果：

如果找到滿足條件的子陣列，返回 max_sum。
否則，返回 0。
注意事項
由於我們需要確保窗口內的元素都是不同的，因此在添加新元素時，如果發現重複，需要移動左指針並更新集合和總和，直到沒有重複的元素為止。
我們需要維護窗口的大小為 k，因此當窗口大小超過 k 時，需要移除最左邊的元素。

複雜度分析
時間複雜度：O(n)
右指針 right 遍歷整個數組，每個元素最多訪問兩次（一次由右指針訪問，一次由左指針移動時訪問），因此總時間複雜度為線性的 O(n)。

空間複雜度：O(k)
需要一個集合 element_set 來存儲當前窗口內的元素，最多包含 k 個元素。
"""
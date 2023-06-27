class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        queue = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):  # 確保i和j都在數組的範圍內
                # 將數對的和以及數對的索引存入最小堆中
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])

        # 從數組的開始位置開始
        push(0, 0)
        pairs = []
        # 當堆中有元素並且我們還沒有找到k個數對時
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)  # 彈出堆中最小的元素
            pairs.append([nums1[i], nums2[j]])  # 將該元素加入結果中
            push(i, j + 1)  # 將下一個可能的數對加入堆中
            if j == 0:  # 如果我們正在處理的是第一個數組的元素
                push(i + 1, 0)  # 將下一個可能的數對加入堆中

        return pairs

        # 有n組，透過heap來儲存有可能的組合，設計一個儲存最多k個的max heap，如果對方大於這個數值就踢掉


"""
解題思路：

1. 我們首先將兩個數組的開始位置的數對以及他們的和放入一個最小堆中。

2. 然後我們從堆中彈出最小的元素，並將該元素加入結果中。

3. 我們將下一個可能的數對加入堆中。我們首先將與當前元素在第二個數組中相鄰的元素加入堆中，然後如果當前元素在第一個數組中的位置是0，我們還會將與當前元素在第一個數組中相鄰的元素加入堆中。

4. 我們重複以上步驟，直到我們找到k個最小的數對。

時間複雜度：
O(k log k)。我們需要從堆中彈出k個元素，每次彈出元素的時間複雜度都是O(log k)，因此總的時間複雜度是O(k log k)。

空間複雜度：
O(k)。我們在堆中存儲的元素最多為k個，因此空間複雜度為O(k)。

"""

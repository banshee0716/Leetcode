class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 初始化一個字典存儲每個數字出現的次數
        num_dict = {}

        # 遍歷 nums 中的每個數字，計算其出現次數
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1

        # 初始化一個最小堆
        heap = []

        # 遍歷字典中的數字和對應的出現次數
        for key, val in num_dict.items():
            # 將出現次數的負數和數字一起放入最小堆中
            # 這樣做是因為 heapq 模塊僅支持最小堆，我們需要最大堆來按出現次數排序
            heap.append((-val, key))
            print(heap)

        # 將列表轉換為最小堆
        heapq.heapify(heap)

        # 初始化一個列表存儲結果
        res = []

        # 從最小堆中彈出 k 個元素，並將數字添加到 res 列表中
        for _ in range(k):
            _, ans = heapq.heappop(heap)
            res.append(ans)

        # 返回結果列表
        return res


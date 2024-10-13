import heapq

class Solution:
    def smallestRange(self, nums):
        min_heap = []
        current_max = float('-inf')

        # 初始化堆和 current_max
        for list_index, num_list in enumerate(nums):
            value = num_list[0]
            heapq.heappush(min_heap, (value, list_index, 0))
            current_max = max(current_max, value)

        result_range = [min_heap[0][0], current_max]

        while True:
            current_min, list_index, element_index = heapq.heappop(min_heap)

            # 更新最小范围
            if current_max - current_min < result_range[1] - result_range[0] or \
               (current_max - current_min == result_range[1] - result_range[0] and current_min < result_range[0]):
                result_range = [current_min, current_max]

            # 检查列表是否有下一个元素
            if element_index + 1 < len(nums[list_index]):
                next_value = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
                current_max = max(current_max, next_value)
            else:
                # 当前列表已无更多元素，无法再找到包含所有列表元素的范围
                break

        return result_range

    
    
    """
复杂度分析：

时间复杂度： O(N log k)

其中 N 是所有列表中元素的总数，k 是列表的数量。
我们需要遍历所有的元素，每个元素可能会被加入和弹出堆，堆的大小为 k，因此每次操作的时间复杂度为 O(log k)。
总时间复杂度为 O(N log k)。
空间复杂度： O(k)

堆的大小最多为 k，因为每次堆中只包含每个列表的一个元素。
因此，空间复杂度为 O(k)。
示例演示：

假设有三个列表：

列表 0：[4, 10, 15, 24, 26]
列表 1：[0, 9, 12, 20]
列表 2：[5, 18, 22, 30]
初始化：

堆包含：
(4, 0, 0) 来自列表 0
(0, 1, 0) 来自列表 1
(5, 2, 0) 来自列表 2
current_max = max(4, 0, 5) = 5
最小范围初始为 [0, 5]
迭代过程：

第一次迭代：

弹出 (0, 1, 0)，current_min = 0
更新最小范围为 [0, 5]（长度为 5）
列表 1 的下一个元素是 9
将 (9, 1, 1) 压入堆
更新 current_max = max(5, 9) = 9
第二次迭代：

弹出 (4, 0, 0)，current_min = 4
更新最小范围为 [4, 9]（长度为 5）
列表 0 的下一个元素是 10
将 (10, 0, 1) 压入堆
更新 current_max = max(9, 10) = 10
第三次迭代：

弹出 (5, 2, 0)，current_min = 5
更新最小范围为 [5, 10]（长度为 5）
列表 2 的下一个元素是 18
将 (18, 2, 1) 压入堆
更新 current_max = max(10, 18) = 18
第四次迭代：

弹出 (9, 1, 1)，current_min = 9
更新最小范围为 [9, 18]（长度为 9），不优于当前最小范围
列表 1 的下一个元素是 12
将 (12, 1, 2) 压入堆
更新 current_max = max(18, 12) = 18
继续迭代：

持续更新堆和 current_max，直到某个列表没有更多元素。
最终结果：

通过以上过程，我们可以找到最小范围 [20, 24]，包含了所有列表中的元素。
关键点总结：

最小堆的使用： 我们使用最小堆来快速获取当前的最小值，并跟踪其所属的列表。
维护当前最大值： 每次插入新元素时，更新 current_max，确保范围包含所有列表的当前元素。
迭代终止条件： 当任何一个列表耗尽时，无法再找到包含所有列表的范围。
范围更新逻辑： 每次计算新的范围时，比较其长度和起点，确保找到最小的范围。
小提示：

为什么需要跟踪 current_max？

因为范围的上限由当前所有列表中最大的元素决定，我们需要确保范围 [current_min, current_max] 包含每个列表中的一个元素。
为什么堆中只需要存储当前元素？

我们只关心每个列表的当前最小元素，以便找到最小的可能范围。随着迭代，我们会更新这些元素。
    
    """
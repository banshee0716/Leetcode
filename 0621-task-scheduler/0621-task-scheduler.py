class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = collections.Counter(tasks)
        max_task_count = max(task_counts.values())
        tasks_with_max_count = sum(1 for task, count in task_counts.items() if count == max_task_count)
        intervals_needed = (max_task_count - 1) * (n + 1) + tasks_with_max_count
        
        return max(intervals_needed, len(tasks))
        
        
    """
您將獲得一組 CPU 任務，每個任務都由字母 A 到 Z 表示，以及冷卻時間 n。每個週期或間隔允許完成一項任務。
任務可以按任何順序完成，但有一個限制：由於冷卻時間的原因，相同的任務必須至少間隔 n 個間隔。

傳回完成所有任務所需的最小間隔數。


演算法思路
1. 計算每個任務的出現次數：首先，需要計算每個任務出現的次數，這可以通過一個哈希表（字典）來完成。

2. 找出出現次數最多的任務：理解這一點很重要，因為這將決定至少需要多少個間隔。出現次數最多的任務之間必須至少有n個間隔，這形成了完成所有任務的時間框架。

3. 計算間隔總數：以出現次數最多的任務為基準，計算至少需要的間隔數。如果有多個任務出現次數相同且為最大，這些任務可以在同一輪循環中交替進行，而不需要額外的冷卻時間。

4. 處理剩餘任務：在考慮了出現次數最多的任務後，需要將其他任務插入這些間隔中，如果可能的話，不增加額外的間隔數。


时间复杂度是O(N)，空间复杂度是O(1)。
    """
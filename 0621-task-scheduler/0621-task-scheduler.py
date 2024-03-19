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
    """
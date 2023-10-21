class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks, processorTime, ans = sorted(tasks), sorted(processorTime), 0
        for i in processorTime:
            ans = max(ans, i + max(tasks[-4:]))
            tasks = tasks[:-4]
            
        return ans
        
        
"""
您的n個處理器每個都有4個內核和n * 4個任務，需要執行每個核心，以使每個核心只能執行一個任務。

給定0個索引整數陣列processorTime 表示每個處理器首次可用的時間以及一個0個點數的整數數組tasks ，
代表執行每個任務所需的時間，返回所有任務的最小時間由處理器執行。

注意：每個核心都獨立於其他核心執行任務。
"""
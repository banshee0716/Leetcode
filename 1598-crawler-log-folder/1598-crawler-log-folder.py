class Solution:
    def minOperations(self, logs: List[str]) -> int:
        paths_stack: list[str] = []
        for log in logs:
            if log == "../":
                if paths_stack:
                    paths_stack.pop()
                    
            elif log != './':
                paths_stack.append(log)
        
        return len(paths_stack)
        
        
        
        """
每次使用者執行變更資料夾操作時，Leetcode 檔案系統都會保留一個日誌。

操作說明如下：

“../”：移動到目前資料夾的父資料夾。 （如果您已位於主資料夾中，請保留在同一資料夾中）。
“./”：保留在同一資料夾中。
"x/" ：移至名為 x 的子資料夾（該資料夾保證始終存在）。
您將獲得一個字串日誌列表，其中logs[i]是使用者在第i步驟執行的操作。

檔案系統在主資料夾中啟動，然後執行日誌中的操作。

傳回更改資料夾操作後傳回主資料夾所需的最少操作數。
        """
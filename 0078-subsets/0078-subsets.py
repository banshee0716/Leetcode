class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Ans = []
        n = len(nums)

        # Helper function
        def Helper(op, start_index):
            # base case
            if start_index == n:
                Ans.append(list(op))
                return
            
            # recursive case
            # choice 1: include the current element
            op.append(nums[start_index])
            Helper(op, start_index + 1)
            
            # backtracking step
            op.pop()
            
            # choice 2: exclude the current element
            Helper(op, start_index + 1)
        
        Helper([], 0)
        return Ans
    
    """
解題思路：
初始化：創建一個空列表 Ans 來存儲所有的子集。

遞歸函數 Helper：這個函數接受一個當前的子集 op 和一個起始索引 start_index，用來控制添加哪個元素到子集中。

基礎情況：當 start_index 等於 nums 的長度時，將 op 添加到 Ans 中，因為已經考慮完所有元素。
遞歸情況：將當前元素 nums[start_index] 加入到 op 中，然後遞歸調用 Helper 函數處理下一個元素。

回溯：將 op 最後一個元素移除（這模擬了不包括當前元素的情況）。
繼續遞歸調用 Helper 函數處理下一個元素，但這次是不包括當前元素。
啟動遞歸：從索引 0 開始，使用空列表開始遞歸。

時間和空間複雜度分析：
時間複雜度：O(N * 2^N)，其中 N 是數組 nums 的長度。對於每個元素，我們都有兩種選擇（包括或不包括）。因此，總的遞歸調用次數是 2 的 N 次方。
空間複雜度：O(N)，這是因為遞歸棧的最大深度是 N，這發生在當我們選擇包含所有元素的情況下。
    
    """
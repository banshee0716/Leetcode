import collections

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        left = 0
        max_length = 1
        n = len(nums)
        
        # 定義兩個雙端隊列，分別維護遞增和遞減序列
        increasing_q = collections.deque()
        decreasing_q = collections.deque()
        
        for right in range(n):
            # 維護遞增隊列
            while increasing_q and increasing_q[-1] > nums[right]:
                increasing_q.pop()
            increasing_q.append(nums[right])
            
            # 維護遞減隊列
            while decreasing_q and decreasing_q[-1] < nums[right]:
                decreasing_q.pop()
            decreasing_q.append(nums[right])
            
            # 如果當前窗口內最大值和最小值之差大於 limit，則調整左邊界
            while decreasing_q[0] - increasing_q[0] > limit:
                # 當前最大值和最小值的差大於 limit，需要縮小窗口
                if decreasing_q[0] == nums[left]:
                    decreasing_q.popleft()
                if increasing_q[0] == nums[left]:
                    increasing_q.popleft()
                left += 1
            
            # 更新最大子數組長度
            max_length = max(max_length, right - left + 1)
        
        return max_length

    
    """
解題思路：

1. 使用兩個雙端隊列（increasing_q 和 decreasing_q）來維護當前窗口內的最小值和最大值。這樣可以在常數時間內找到窗口內的最小值和最大值。
2. 滑動窗口從左至右遍歷數組：
    -當前元素插入到 increasing_q 和 decreasing_q 時，確保 increasing_q 是單調遞增的，decreasing_q 是單調遞減的。
    -每次插入後，檢查窗口內的最大值和最小值之差是否大於 limit。如果大於，則需要調整左邊界（left）以縮小窗口，直到窗口內的最大值和最小值之差不大於 limit。
3. 在調整窗口的過程中，不斷更新最大子數組長度。


時間複雜度：O(n)，每個元素最多進入和離開隊列一次。
空間複雜度：O(n)，需要用兩個雙端隊列來儲存元素。
    """
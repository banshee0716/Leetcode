class Solution:
    def checkRecord(self, n: int) -> int:
        # Initialize the DP table with -1, indicating uncomputed states
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        MOD = 10**9 + 7  # The modulus for the result

        def check_all_records(cur_ind, count_a, count_l) -> int:
            # If the entire record is processed, return 1 valid record
            if cur_ind == n:
                return 1
            # If the current state has been computed, return the stored value
            if dp[cur_ind][count_a][count_l] != -1:
                return dp[cur_ind][count_a][count_l]

            # If allowed, add a 'A' to the record
            with_a_next = 0
            if count_a == 0:
                with_a_next = check_all_records(cur_ind + 1, count_a + 1, 0)

            # If allowed, add a 'L' to the record
            with_l_next = 0
            if count_l < 2:
                with_l_next = check_all_records(cur_ind + 1, count_a, count_l + 1)
            
            # Add a 'P' to the record
            with_p_next = check_all_records(cur_ind + 1, count_a, 0)

            # Compute the total number of valid sequences from the current state
            total = (with_a_next + with_l_next + with_p_next) % MOD
            dp[cur_ind][count_a][count_l] = total
            return total

        # Start the computation from the first day with no 'A's and no consecutive 'L's
        return check_all_records(0, 0, 0)

    
    """
解題思路：
－狀態表示：temp[i][count_a][count_l] 表示考慮到第 i 天時，使用 count_a 次'A'和連續 count_l 次'L'的情況下的合法出勤記錄數。
－邊界條件：
　　－當 i 達到 n（天數），表示一個有效的序列完成，返回 1。
　　－若 temp[i][count_a][count_l] 已經計算過，直接返回其值。
－轉移方程：
　　－若當天缺席，則 count_a 加 1，count_l 重置為 0。
　　－若當天遲到，則 count_l 加 1，但要檢查是否超過連續兩次。
　　－若當天出席，則 count_l 重置為 0。    

時間與空間複雜度分析：
時間複雜度：O(n)，其中 n 是天數，因為每種狀態只被計算一次。
空間複雜度：O(n)，用於存儲遞歸過程中的狀態
    """
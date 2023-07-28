class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        # 初始化動態規劃陣列
        dp = [0] * n

        # 從後向前遍歷數字陣列
        for i in range(n - 1, -1, -1):
            dp[i] = nums[i]
            for j in range(i + 1, n):
                # 更新 dp[j] 為選擇數字陣列開頭或結尾的數字後的最大分數差
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        # 如果 dp[n-1] 大於或等於 0，則先手玩家可以贏得遊戲
        return dp[n - 1] >= 0

"""
1. 給定一個整數數組 nums。兩個玩家正在使用此數組玩遊戲：玩家 1 和玩家 2。

2. 玩家 1 和玩家 2 輪流進行，玩家 1 首先開始。雙方玩家都以 0 分開始遊戲。
在每一回合，玩家從數組的任一端取出一個數字（即 nums[0] 或 nums[nums.length - 1]），這會減少數組加 1。
玩家將所選數字添加到他們的分數中。當數組中不再有元素時遊戲結束。

3. 如果玩家 1 能夠贏得比賽，則返回 true。如果兩個玩家的分數相等，那麼玩家 1 仍然是獲勝者，您也應該返回 true。您可能會假設兩名玩家都處於最佳狀態，也就是雙方不會做出不合理的判斷。

在這個解決方案中，使用了動態規劃的思想來解決這個問題。定義一個dp陣列，其中dp[i]表示從i到n-1（包括兩端）的當前玩家與另一位玩家的分數之差的最大值，其中n是數字陣列的長度。

首先，遍歷數字陣列，對於每個i，都將dp[i]設置為nums[i]。然後，從i+1到n遍歷數字陣列，更新dp[j]為nums[i]-dp[j]和nums[j]-dp[j-1]的最大值，這表示當前玩家選擇數字陣列的開頭或結尾的數字。

最後，如果dp[n-1]大於或等於0，則返回True，表示先手玩家可以贏得遊戲；否則，返回False。

時間複雜度
是O(n^2)，其中n是數字陣列的長度。這是因為需要兩次遍歷數字陣列來更新dp陣列。

空間複雜度
是O(n)，這是因為創建了一個長度為n的dp陣列來儲存每個位置的最大分數差。
"""
from typing import List

MOD = 10**9 + 7

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        # 對arr進行排序
        arr.sort()
        # 使用集合s存儲arr中的元素
        s = set(arr)
        # 初始化dp字典，每個數字自己可以形成一個二叉樹
        dp = {x: 1 for x in arr}
        
        # 遍歷arr中的每個數字i
        for i in arr:
            # 再次遍歷arr中的每個數字j
            for j in arr:
                # 如果j大於i的平方根，則跳出內層循環
                if j > i**0.5:
                    break
                # 如果i能被j整除，且i除以j的結果也在集合s中
                if i % j == 0 and i // j in s:
                    # 如果i除以j的結果等於j，則dp[i]增加dp[j] * dp[j]
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    # 否則，dp[i]增加dp[j] * dp[i // j] * 2
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    # 每次更新dp[i]後，對MOD取模以防止溢出
                    dp[i] %= MOD
        
        # 將dp字典中的所有值相加，再對MOD取模，得到最終答案
        return sum(dp.values()) % MOD
"""
時間複雜度分析：
外層循環遍歷arr中的每個數字i，內層循環最多遍歷到i的平方根，所以時間複雜度是O(n * sqrt(m))，其中n是arr的長度，m是arr中最大的數。

空間複雜度分析：
使用了一個集合s和一個字典dp，空間複雜度是O(n)
"""
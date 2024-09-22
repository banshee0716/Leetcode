class Solution:
    def findKthNumber(self, n, k):
        def calcSteps(n, curr, next):
            steps = 0
            while curr <= n:
                steps += min(n + 1, next) - curr
                curr *= 10
                next *= 10
            return steps

        curr = 1
        k -= 1  # 第一个数字已经是 1

        while k > 0:
            steps = calcSteps(n, curr, curr + 1)
            if steps <= k:
                # 跳过当前前缀下的所有数字，移动到下一个兄弟节点
                curr += 1
                k -= steps
            else:
                # 深入子节点
                curr *= 10
                k -= 1  # 减去当前节点占用的一个位置

        return curr

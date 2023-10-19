class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # 定義兩個指針，分別指向 s 和 t 的末尾
        i, j = len(s) - 1, len(t) - 1
        skip_s, skip_t = 0, 0  # 記錄每個字串中 # 的數量

        # 當其中一個指針還沒移動到起始位置時，繼續比較
        while i >= 0 or j >= 0:
            # 找到 s 中下一個有效字符的位置
            while i >= 0:
                if s[i] == '#':
                    skip_s += 1
                    i -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    i -= 1
                else:
                    break

            # 找到 t 中下一個有效字符的位置
            while j >= 0:
                if t[j] == '#':
                    skip_t += 1
                    j -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    j -= 1
                else:
                    break

            # 比較 s 和 t 中的字符
            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False
            # 如果其中一個字串已遍歷完，但另一個字串還有有效字符，則返回 False
            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True
"""
時間複雜度為 O(N + M)（N 和 M 分別為 s 和 t 的長度），
空間複雜度為 O(1)（常數空間）。
"""
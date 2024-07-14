from typing import Dict, List
from collections import Counter


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # Initialize stack with an empty Counter for the outermost level
        stack: List[Counter] = [Counter()]
        i, n = 0, len(formula)

        while i < n:
            if formula[i] == "(":
                # Start a new nested level with an empty Counter
                stack.append(Counter())
                i += 1
            elif formula[i] == ")":
                # Process the closing parenthesis
                top = stack.pop()
                i += 1
                # Parse the multiplier after the closing parenthesis
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplier = int(formula[i_start:i] or 1)
                # Multiply and merge the counts with the parent level
                for element, count in top.items():
                    stack[-1][element] += count * multiplier
            else:
                # Process an atom
                i_start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                element = formula[i_start:i]
                # Parse the count for this atom
                i_start = i
                while i < n and formula[i].isdigit():
                    i += 1
                count = int(formula[i_start:i] or 1)
                # Update the count in the current level
                stack[-1][element] += count

        # Get the final counts
        result = stack[0]
        # Sort elements alphabetically and format the output
        return "".join(
            f"{element}{result[element] if result[element] > 1 else ''}"
            for element in sorted(result)
        )

"""

這是 LeetCode 第 726 題「原子的數量」的解決方案。以下是詳細的問題解決方法：
該解決方案採用棧和字典的組合來處理化學式。主要思路如下：

-使用棧來處理嵌套的括號結構。每個棧元素是一個字典，用於存儲當前層級的原子計數。
-遍歷化學式字符串，根據不同的字符類型進行相應的處理：
    a. 遇到左括號 '('，創建新的字典並推入棧中。
    b. 遇到右括號 ')'，處理括號內的原子計數，並將結果合併到上一層。
    c. 遇到原子名稱，解析原子名稱和數量，更新當前字典。
-最後，對結果進行排序並格式化輸出。

時間複雜度：
O(N * log(N))，其中 N 是化學式的長度。
遍歷化學式需要 O(N) 時間。
最後的排序操作需要 O(K * log(K)) 時間，其中 K 是不同原子的數量（最壞情況下 K = N/2）。
因此，總體時間複雜度為 O(N * log(N))。

空間複雜度：
O(N)，其中 N 是化學式的長度。
在最壞情況下（深度嵌套的括號），棧可能包含 O(N) 個元素。
每個 Counter 對象最多包含 O(N) 個元素。
因此，總體空間複雜度為 O(N)。
"""
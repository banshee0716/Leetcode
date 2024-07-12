from typing import List


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substrings(stack: List[str], target: str, score: int) -> int:
            """Remove target substrings from the stack and return the score."""
            result = 0
            new_stack = []
            for char in stack:
                if char == target[1] and new_stack and new_stack[-1] == target[0]:
                    result += score
                    new_stack.pop()
                else:
                    new_stack.append(char)
            return result, new_stack

        # Determine which substring has higher priority based on score
        if y > x:
            high_priority, high_score = "ba", y
            low_priority, low_score = "ab", x
        else:
            high_priority, high_score = "ab", x
            low_priority, low_score = "ba", y

        total_score = 0

        # First pass: remove high priority substrings
        high_priority_score, remaining_chars = remove_substrings(s, high_priority, high_score)
        total_score += high_priority_score

        # Second pass: remove low priority substrings
        low_priority_score, _ = remove_substrings(remaining_chars, low_priority, low_score)
        total_score += low_priority_score

        return total_score
    
    
    """
解題思路如下：

首先確定哪個子字串（"ab" 或 "ba"）能得到更高的分數，將其稱為 "top" 子字串。
第一次遍歷：移除所有 "top" 子字串，因為它們能提供更高的分數。
第二次遍歷：移除剩餘的另一種子字串。

這種方法之所以有效，是因為無論移除順序如何，能夠移除的子字串總數是固定的。通過優先移除高分值的子字串，我們可以確保獲得最高分數。

時間複雜度：
O(n)，其中 n 是字符串 s 的長度。
我們對字符串進行兩次遍歷，每次遍歷的時間複雜度都是 O(n)。

空間複雜度：
O(n)，其中 n 是字符串 s 的長度。
在最壞情況下，我們可能需要存儲整個字符串的字符（當沒有子字符串可以被移除時）。

    """
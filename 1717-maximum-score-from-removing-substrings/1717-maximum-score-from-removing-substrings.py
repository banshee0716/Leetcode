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
class Solution:
    def findTheLongestSubstring(self, s):
        vowels = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        state_to_index = {0: -1}
        mask = 0
        max_length = 0

        for i, char in enumerate(s):
            if char in vowels:
                mask ^= 1 << vowels[char]

            if mask in state_to_index:
                max_length = max(max_length, i - state_to_index[mask])
            else:
                state_to_index[mask] = i

        return max_length

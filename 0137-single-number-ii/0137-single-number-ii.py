class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)

        for x in nums:
            count[x] += 1

        for x, freq in count.items():
            if freq == 1:
                return x

        return -1


"""
就是簡單的建立一個hash map之後，再透過hash map的特性來找出只出現一次的數字
"""

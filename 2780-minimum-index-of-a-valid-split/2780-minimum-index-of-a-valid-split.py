class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        def most_frequent(data):
            # 建立 Counter 物件以計算每個數字的出現次數
            counter = Counter(data)
            
            # 初始化最大次數和最頻繁的數字
            max_count = -1
            max_item = None

            # 遍歷字典中的每一個項目
            for item, count in counter.items():
                # 如果找到更高的計數，則更新 max_item 和 max_count
                if count > max_count:
                    max_count = count
                    max_item = item

            return max_item, max_count

        # 找出數字出現最頻繁的數字和它的計數
        dom, cnt = most_frequent(nums) 
        left, right = 0, cnt
        for i in range(n):
            if nums[i] == dom:
                left += 1
                right -= 1
            if left * 2 > i + 1 and right * 2 > n - (i + 1):
                return i
        
        return -1
    
# O(N) 
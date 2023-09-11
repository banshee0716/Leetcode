class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        # 建立一個字典來保存組和一個列表來保存結果
        groups = {}
        result = []
        
        # 遍歷每個人的組大小
        for i, size in enumerate(groupSizes):
            # 如果該組大小還未在字典中，則添加它
            if size not in groups:
                groups[size] = []
            # 將該人的索引添加到相應大小的組中
            groups[size].append(i)
            
            # 如果該組的大小與組大小相符，則將該組添加到結果中
            if len(groups[size]) == size:
                result.append(groups[size])
                # 清空該大小的組列表以便之後的添加
                groups[size] = []
                
        # 返回結果
        return result

"""
解題思路：
1. 使用一個字典 groups 來保存每個大小的組。鍵是組的大小，值是該組的成員索引。
2. 遍歷 groupSizes，對於每個人（他們的索引和他們的組大小）：
    - 如果該組大小還未出現在字典中，則在字典中為該組大小建立一個新的空列表。
    - 將該人的索引添加到相應大小的組中。
    - 檢查該組的長度是否與組大小相等。如果是，則將該組添加到結果中，並清空該大小的組列表以便之後的添加。
3. 返回結果列表。

時間複雜度：O(n)。我們只遍歷了一次 groupSizes，其中 n 是 groupSizes 的長度。

空間複雜度：O(n)。在最壞的情況下，groups 字典和 result 列表可以存儲所有的人。
"""
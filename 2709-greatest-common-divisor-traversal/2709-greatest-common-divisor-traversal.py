class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        def find_set_leader(disjoint_set, x):
            if disjoint_set[x] == x:
                return x
            disjoint_set[x] = find_set_leader(disjoint_set, disjoint_set[x])
            return disjoint_set[x]

        def union_sets(disjoint_set, set_size, x, y):
            x_leader = find_set_leader(disjoint_set, x)
            y_leader = find_set_leader(disjoint_set, y)
            if x_leader == y_leader:
                return
            if set_size[x_leader] < set_size[y_leader]:
                disjoint_set[x_leader] = y_leader
                set_size[y_leader] += set_size[x_leader]
            else:
                disjoint_set[y_leader] = x_leader
                set_size[x_leader] += set_size[y_leader]

        num_elements = len(nums)
        if num_elements == 1:
            return True

        disjoint_set = [i for i in range(num_elements)]
        set_size = [1] * num_elements
        factor_first_occurrence = {}

        for i, num in enumerate(nums):
            divisor = 2
            while divisor * divisor <= num:
                if num % divisor == 0:
                    if divisor in factor_first_occurrence:
                        union_sets(disjoint_set, set_size, i, factor_first_occurrence[divisor])
                    else:
                        factor_first_occurrence[divisor] = i
                    while num % divisor == 0:
                        num //= divisor
                divisor += 1
            if num > 1:
                if num in factor_first_occurrence:
                    union_sets(disjoint_set, set_size, i, factor_first_occurrence[num])
                else:
                    factor_first_occurrence[num] = i

        return set_size[find_set_leader(disjoint_set, 0)] == num_elements

"""
解題思路
構建圖：
    -將問題轉化為圖的遍歷問題。如果兩個數的最大公約數大於1，則這兩個數之間有一條邊。
    -首先，對每個數字分解質因數，建立兩個映射：一個是從質數到索引的映射prime2index，另一個是從索引到質數的映射index2prime。

深度優先搜索（DFS）：
    -從索引0開始，使用DFS遍歷整個圖。遍歷過程中，標記訪問過的索引和質數。
    -對於每個訪問的索引，遍歷其對應的所有質數，並對這些質數對應的所有索引進行DFS遍歷。

檢查是否所有索引都被訪問：
    -完成DFS後，檢查是否所有的索引都被訪問過。如果是，則返回true，表示可以遍歷所有數字對；否則返回false。
    
時間複雜度
    -分解質因數的時間複雜度為O(N*sqrt(M))，其中N是數組nums的長度，M是nums中最大數字的大小。
    -DFS的時間複雜度為O(V+E)，其中V是圖中頂點的數量（即nums的長度N），E是圖中邊的數量。在最壞情況下，每個數字都與其他所有數字相連，那麼E為O(N^2)。

空間複雜度
    -需要額外的空間來存儲prime2index和index2prime映射，以及DFS過程中的訪問標記，空間複雜度為O(N)。
"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        sorted_lst = []

        for x in arr2:
            while x in arr1:
                sorted_lst.append(x)
                arr1.remove(x)

        return(sorted_lst+sorted(arr1))
    
    """
給定兩個陣列 arr1 和 arr2，arr2 的元素是不同的，並且 arr2 中的所有元素也在 arr1 中。

將 arr1 的元素排序，使得 arr1 中項目的相對順序與 arr2 中的項目的相對順序相同。未出現在arr2中的元素應以升序放置在arr1的末端。
    """
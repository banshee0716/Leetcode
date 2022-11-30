class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        # Get the occurrences of each number. (also remove duplicated numbers)
        Number_Occurrences = Counter(arr)

        Unique_Occurrences = set(Number_Occurrences.values())

        # return Truen if each unique number has a unique occurrence
        return len(Number_Occurrences.keys()) == len(Unique_Occurrences)
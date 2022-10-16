class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        hashmap = {}
        for i in range(len(list1)):   #step 1
            hashmap[list1[i]] = i
        
        res = []

        minsum = float("inf")   #step 2
        
        for j in range(len(list2)):    #step 3
            if list2[j] in hashmap:
                Sum = j + hashmap[list2[j]]    #step 3a
                
                if Sum < minsum:   #step 3b
                    minsum = Sum
                    res = []
                    res.append(list2[j])
                elif Sum == minsum:     #step 3c
                    res.append(list2[j])
        return res
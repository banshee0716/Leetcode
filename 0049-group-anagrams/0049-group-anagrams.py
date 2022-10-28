class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}
        for word in strs:
            sortWord = ''.join(sorted(word))
            if sortWord not in h:
                h[sortWord] = [word]
            else:
                h[sortWord].append(word)
        
        final = []
        for val in h.values():
            final.append (val)
        
        return final
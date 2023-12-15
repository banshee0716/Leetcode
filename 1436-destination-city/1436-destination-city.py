class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        source = set()
        dest = set()
        for l in paths:
            source.add(l[0])
            dest.add(l[1])
        return list(dest - source)[0]
        
        source = set()
        dest = set()
        for l in paths:
            source.add(l[0])
            dest.add(l[1])
        return list(dest - source)[0]
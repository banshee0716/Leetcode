class Solution(object):
    def equationsPossible(self, equations):
        def find(x):
            if x != uf[x]: uf[x] = find(uf[x])
            return uf[x]
        uf = {a: a for a in string.lowercase}
        for a, e, _, b in equations:
            if e == "=":
                uf[find(a)] = find(b)
        return not any(e == "!" and find(a) == find(b) for a, e, _, b in equations)
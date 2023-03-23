class Solution:
    def makeConnected(self, n, connections):
        if len(connections) < n - 1:
            return -1
        s = ''.join(map(chr, range(n)))
        for a, b in connections:
            s = s.replace(s[a], s[b])
        return len(set(s)) - 1
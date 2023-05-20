class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
	    root = {}
	
	# xr = x/parent(x), pr = parent(x)/root(x), update xr to xr*pr = x/root(x)
	    def find(x):
		    p, xr = root.setdefault(x, (x, 1.0))
		    if x != p:
			    r, pr = find(p)
			    root[x] = (r, xr*pr)
		    return root[x]

	# if root(x) = root(y), equations "x / y" doable as (x/root(x)) / (y/root(y)) = xr / yr
	    def union(x, y, ratio):
		    px, xr, py, yr = *find(x), *find(y)
		    if not ratio:
			    return xr / yr if px == py else -1.0
		    if px != py:
			    root[px] = (py, yr/xr*ratio)

	    for (x, y), v in zip(equations, values):
		    union(x, y, v)
	    return [union(x, y, 0) if x in root and y in root else -1.0 for x, y in queries]
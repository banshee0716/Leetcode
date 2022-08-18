func minSetSize(arr []int) int {
   c := make([]int, 100001)
	r, l := 0, len(arr)

	for _, i := range arr {
		c[i]++
	}

	sort.Slice(c, func(i, j int) bool {
		return c[i] > c[j]
	})

	for i := 0; i < len(c) && c[i] != 0; i++ {
		l -= c[i]
		r++
		if l <= len(arr)/2 {
			return r
		}
	}
	
	return len(arr)
}
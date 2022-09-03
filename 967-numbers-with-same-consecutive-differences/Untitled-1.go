//967-numbers-with-same-consecutive-differences
func numsSameConsecDiff(N int, K int) []int {
	cur := []int{1, 2, 3, 4, 5, 6, 7, 8, 9}
	for i := 0; i < N-1; i++ {
		tmp := []int{}
		for _, v := range cur {
			n := v % 10
			if n+K < 10 {
				tmp = append(tmp, v*10+n+K)
			}
			if n >= K && K > 0 {
				tmp = append(tmp, v*10+n-K)
			}
		}
		cur = tmp
	}
	return cur
}
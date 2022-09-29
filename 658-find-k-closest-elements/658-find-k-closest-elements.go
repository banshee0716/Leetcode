func findClosestElements(arr []int, k int, x int) []int {
    if len(arr) <= k{
        return arr
    }
    if arr[0] >=x {
        return arr[:k]
    }
    if arr[len(arr)-1] <= x {
		return arr[len(arr)-k:]
	}
    var mid int
	lo, hi := 0, len(arr)-1
	for lo <= hi {
		mid = lo + (hi-lo)/2
		if arr[mid] == x {
			break
		}
		if arr[mid] > x {
			hi = mid - 1
		} else {
			lo = mid + 1
		}
	}
	begin, end := max(0, mid-k-1), min(len(arr)-1, mid+k+1)

	for end-begin+1 != k {
		if x-arr[begin] <= arr[end]-x {
			end--
		} else {
			begin++
		}
	}

	return arr[begin : end+1]
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
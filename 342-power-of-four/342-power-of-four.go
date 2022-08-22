func isPowerOfFour(n int) bool {
    if n<1 || n & (n-1) != 0{
        return false
    }
    return 1 == n % 3
}
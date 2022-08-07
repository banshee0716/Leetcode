func countVowelPermutation(n int) int {
    var mod int64 = 1000000007
    var a , e, i, o, u int64 = 1, 1, 1, 1, 1
    for p:=1;p<n; p++ {
        aNew := (e+i+u) % mod
        eNew := (a+i) % mod
        iNew := (e+o) % mod
        oNew := i % mod
        uNew := (i+o) % mod
        a, e,i,o,u = aNew, eNew, iNew, oNew, uNew
    }
    return int((a+e+i+o+u)%mod)
}
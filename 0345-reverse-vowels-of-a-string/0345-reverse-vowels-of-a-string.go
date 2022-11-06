func reverseVowels(s string) string {
    tmp := []byte(s)
    left := 0
    right := len(s)-1
    for left < right{
        if !(isVowel(s[left])){
            left++
            continue
        }else if !(isVowel(s[right])){
            right--
            continue
        }
        tmp[left], tmp[right] = tmp[right], tmp[left]
        left++
        right--
    }
    return string(tmp)
    
}
func isVowel(c byte) bool {
    if c < 'a' { c += 32 }
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
}
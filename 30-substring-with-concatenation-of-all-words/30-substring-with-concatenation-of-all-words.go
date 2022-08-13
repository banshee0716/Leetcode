func findSubstring(s string, words []string) []int {
    res := []int{}
    if len(words) == 0 {
        return res
    }
    mapWords := map[string]int{}
    for _,w := range words {
        mapWords[w]++
    }
    wordLen := len(words[0])
    for i:=0; i<=len(s)-wordLen*len(words); i++ {
        found := 0
        seenWords := map[string]int{}
        for k := i; k <= len(s) - wordLen; k += wordLen {
            word := s[k:k+wordLen]
            needWords,ok := mapWords[word]
            if ok {
                seen, ok := seenWords[word]
                if !ok || seen < needWords {
                    seenWords[word]++
                } else {
                    break
                }
                found++
                if found == len(words) {
                    res = append(res, i)
                    break
                }
            } else {
                break
            }
        } 
    }
    return res
}
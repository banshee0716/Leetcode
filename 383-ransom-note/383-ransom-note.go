func canConstruct(ransomNote string, magazine string) bool {
    for _, v := range(ransomNote){
        if strings.Count(ransomNote,string(v))>strings.Count(magazine,string(v)){
            return false
        }
    }
    return true
}
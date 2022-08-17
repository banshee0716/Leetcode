func uniqueMorseRepresentations(words []string) int {
    letter := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    m := make(map[string]int)
    for _, v := range(words){
        s := ""
        for _,i := range(v){
            s += letter[i-'a']
        }
        m[s]++
    }
    return len(m)
}
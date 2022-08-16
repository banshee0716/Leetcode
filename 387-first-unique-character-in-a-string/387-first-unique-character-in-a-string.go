func firstUniqChar(s string) int {
    m := make([]int,26) //英文字母的hash map
    for _,v := range(s){
        m[int(v-'a')] ++
    }
    for i,v := range(s){
        if m[int(v-'a')] == 1{
            return i
        }
    }
    return -1
}
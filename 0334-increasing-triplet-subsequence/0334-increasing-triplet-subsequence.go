func increasingTriplet(nums []int) bool {
    if len(nums)<3{
        return false
    }
    Smallest, SecSmall := 2<<32, 2<<32
    for _, v := range nums{
        if v <= Smallest{
            Smallest = v
        }else if v <= SecSmall{
            SecSmall = v
        }else{
            return true
        }
    }
    return false
}
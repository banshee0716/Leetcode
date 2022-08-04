func mirrorReflection(p int, q int) int {
    x, y := gcd(p, q)  //gcd - greatest common divisor, get x, y based on p, q and their gcd
    
    x %= 2 //locate x back to squar 1
    y %= 2 //locate y back to squar 1
    
    if x == 0 && y == 1 {
        return 2
    } else if x == 1 && y == 1 || x == 0 && y == 0 {
        return 1
    } else {
        return 0
    }
}

func gcd(p, q int) (int, int) {
    x := p
    y := q
    for p % q != 0 {
        temp := p % q
        p = q
        q = temp
    }
    return x / q, y / q 
}
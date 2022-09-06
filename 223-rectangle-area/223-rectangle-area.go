func computeArea(ax1 int, ay1 int, ax2 int, ay2 int, bx1 int, by1 int, bx2 int, by2 int) int {
    first  := area(ax1, ay1, ax2, ay2)
    second := area(bx1, by1, bx2, by2)
    
    leftOverlap  := max(ax1, bx1)
    downOverlap  := max(ay1, by1)
    
    rightOverlap := min(ax2, bx2)
    upOverlap    := min(ay2, by2)
    
    overlap := area(leftOverlap, downOverlap, rightOverlap, upOverlap)
    
    return first + second - overlap
}

func area(left, down, right, up int) int {
    if left > right || down > up{
        return 0
    }
    return (right - left) * (up - down)
}

func max(a, b int)int{
    if a < b{
        return b
    }
    return a
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
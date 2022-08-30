func rotate(matrix [][]int)  {
    left := 0
    right := len(matrix)-1
    
    for left < right{
        top, bottom := left, right
        for i := 0; i < right-left; i++{
            topLeft := matrix[top][left+i]//計算現在的位置
            //旋轉每個位置
            matrix[top][left+i] =  matrix[bottom-i][left]
            matrix[bottom-i][left] = matrix[bottom][right-i]
            matrix[bottom][right-i] = matrix[top+i][right]
			matrix[top+i][right] = topLeft
        }
        left++
        right--
        //進入裡面那個圈
    }
}

//n*n要轉n-1次
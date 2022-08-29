func numIslands(grid [][]byte) int {
    result := 0
    for i, row := range grid{
        for j, value := range row{
            if value == '1'{
                visit(&grid,i,j)
                result += 1
            }
        }
    }
    return result
}
func visit(grid *[][]byte, i int , j int){
    m, n := len(*grid),len((*grid)[0])
    if (i>=m) || (i<0) || (j>=n) || (j<0) || ((*grid)[i][j] == '0'){
        return 
    }//如果超出圖形區域，或是確認為０就返回
    (*grid)[i][j] = '0'//走訪過就弄為0
    visit(grid,i-1,j)
    visit(grid,i+1,j)
    visit(grid,i,j-1)
    visit(grid,i,j+1)
}
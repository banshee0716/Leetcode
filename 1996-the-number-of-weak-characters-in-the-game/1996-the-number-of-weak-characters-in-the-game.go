func numberOfWeakCharacters(properties [][]int) int {
    sort.Slice(properties, func(i, j int) bool {
		if properties[i][0] == properties[j][0] {
			return properties[i][1] < properties[j][1] // defence asc
		}
		return properties[i][0] > properties[j][0] // attack desc
	}) // sort by attack desc and defense asec 
    
    weakCounter := 0
	maxDefenseBefore := 0 // till now
    
    for i := 0; i < len(properties); i++{
        if properties[i][1] < maxDefenseBefore{
            weakCounter++
        }else if properties[i][1]>maxDefenseBefore{
            maxDefenseBefore = properties[i][1]
        }//else: current defense even with maxDefense - skipping
    }
    return weakCounter
}
func maxProfit(prices []int) int {
    if len(prices)<1{
        return 0
    }
    maxprofit := 0
    minPurchase := prices[0]
    for _,price := range(prices){
        if price < minPurchase{
            minPurchase = price
        }else if (price-minPurchase) > maxprofit{
            maxprofit = price - minPurchase
        }
    }
    return maxprofit
}
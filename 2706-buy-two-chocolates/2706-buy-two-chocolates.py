class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        first_min = second_min = maxsize

        for p in prices:
            if p < first_min:
                second_min, first_min = first_min, p
            elif p < second_min:
                second_min = p

        min_price = first_min + second_min
        return money - min_price if min_price <= money else money
    
    
"""
給你一個整數數組價格，代表商店中各種巧克力的價格。您還會獲得一個整數錢，它代表您的初始金額。

您必須購買兩塊巧克力，這樣您還有一些非負的剩餘資金。您希望最小化您購買的兩種巧克力的價格總和。

退還購買兩塊巧克力後剩餘的金額。如果你無法在不負債的情況下購買兩塊巧克力，那就退錢。請注意，餘數必須是非負數。
"""
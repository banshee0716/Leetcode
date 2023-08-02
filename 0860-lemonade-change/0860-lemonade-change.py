class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        L, B = len(bills), {5: 0, 10: 0, 20: 0}
        
        for i in range(L):
            if bills[i] == 10:
                if B[5] == 0:
                    return False
                else:
                    B[5] -= 1

            elif bills[i] == 20:
                if B[10] != 0 and B[5] != 0:
                    B[10] -= 1
                    B[5] -= 1
                elif B[5] >= 3:
                    B[5] -= 3
                else:
                    return False
            B[bills[i]] += 1

        return True

"""
在檸檬水攤上，每杯檸檬水售價 5 美元。顧客排隊向您購買，並一次訂購一件（按照賬單指定的順序）。
每個顧客只能購買一份檸檬水，並用 5 美元、10 美元或 20 美元的鈔票付款。您必須向每個客戶提供正確的零錢，以便客戶支付 5 美元進行淨交易。

請注意，一開始您手頭沒有任何零錢。

給定一個整數數組 bills，其中 bills[i] 是第 i 個客戶支付的賬單，如果您能為每個客戶提供正確的零錢，則返回 true，否則返回 false。
"""
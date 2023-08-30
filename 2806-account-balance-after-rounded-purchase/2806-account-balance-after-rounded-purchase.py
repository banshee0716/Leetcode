class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        return (104 -purchaseAmount)//10*10
        
        
        
    """
最初，您的銀行賬戶餘額為 100 美元。

您將獲得一個整數purchaseAmount，代表您將花費的美元購買金額。

在您要進行購買的商店，購買金額將四捨五入到最接近的 10 倍數。換句話說，您支付一個非負金額 roundedAmount，這樣 roundedAmount 是 10 的倍數，abs(roundedAmount - buyAmount ) 被最小化。

如果有多個最接近的 10 倍數，則選擇最大的倍數。

返回一個整數，表示您從商店購買了價值 buyAmount 美元的商品後的帳戶餘額。

注意：本題中0被認為是10的倍數。
    """
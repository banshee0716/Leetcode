class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        n = len(customers)
        ans = 0
        for i in range(n):
            if grumpy[i] == 0:
                ans += customers[i]
        
        unsatis = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                unsatis += customers[i]
        
        max_ = unsatis
        for i in range(minutes, n):
            if grumpy[i - minutes] == 1:
                unsatis -= customers[i - minutes]
            if grumpy[i] == 1:
                unsatis += customers[i]
            max_ = max(max_, unsatis)
        
        return ans + max_
        
        
        """
有一個書店老闆，他的書店營業時間為n分鐘。每分鐘都有一定數量的顧客進入商店。給定一個長度為 n 的整數數組customers，其中customers[i] 是在第i 分鐘開始時進入商店的客戶數量，以及所有這些客戶在該分鐘結束後離開的數量。

有幾分鐘，書店老闆脾氣暴躁。給定一個二進制數組 grumpy，其中如果書店老闆在第 i 分鐘內脾氣暴躁，則 grumpy[i] 為 1，否則為 0。

當書店老闆脾氣暴躁時，那一分鐘的顧客就不滿意，反之，他們就滿意。

書店老闆知道一個秘密技巧，可以讓自己連續幾分鐘不脾氣暴躁，但只能用一次。

返回全天可以滿足的最大客戶數量。
        """
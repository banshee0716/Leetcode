class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        def f(x):
            if (veganFriendly == 1 and x[2] == 1 and x[3] <= maxPrice and x[4] <= maxDistance) or (veganFriendly == 0 and x[3] <= maxPrice and x[4] <= maxDistance):
                return True
            else:
                return False
        
        y = list(filter(f,restaurants))
        y.sort(key=lambda a:a[0],reverse=True)
        y.sort(key=lambda a:a[1],reverse=True)
        return [i[0] for i in y]
        
        
"""
給定餐廳數組，其中restaurants[i] = [idi, ratingi, veganFriendlyi,pricei,distancei]。您必須使用三個過濾器來過濾餐廳。

veganFriendly 過濾器要么為 true（意味著您應該只包含 veganFriendlyi 設置為 true 的餐廳），要么為 false（意味著您可以包含任何餐廳）。此外，您還有過濾器 maxPrice 和 maxDistance，它們分別是您應考慮的餐廳價格和距離的最大值。

返回過濾後的餐廳 ID 數組，按評分從高到低排序。對於相同評分的餐廳，按照id從高到低排序。為簡單起見，當 veganFriendlyi 和 veganFriendly 為 true 時取值 1，為 false 時取值 0。
"""
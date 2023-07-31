class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        sum = 0
        x = 0
        y = 0
        while mainTank >= 5:
            x = mainTank // 5
            y = mainTank % 5
            if additionalTank >= x:
                mainTank = y + x
                
            elif additionalTank >= 0:
                mainTank = y + additionalTank
                
            else:
                mainTank = y
            additionalTank = additionalTank - x
            
            sum = sum + x * 5 * 10

        return sum + mainTank * 10

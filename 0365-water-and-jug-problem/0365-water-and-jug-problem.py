class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if (jug1Capacity + jug2Capacity < targetCapacity):
            return 0 
        
        return targetCapacity % math.gcd(jug1Capacity, jug2Capacity) == 0
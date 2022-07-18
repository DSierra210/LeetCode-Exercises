class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        elif num < 2:
            return False
        
        first = 2
        last = num
        
        while first <= last:
            midpoint = (first + last) // 2

            if midpoint ** 2 == num:
                return True
            elif midpoint **2 > num:
                last = midpoint - 1
            else:
                first = midpoint + 1
        
        return False

# Example 1:
# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:
#
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        if x==1:
            return 1
        while low < high:
            mid = int((high+low) / 2)
            if low == mid or high == mid:
                return low
            elif mid * mid == x:
                return mid
            elif mid * mid > x:
                high = mid
            elif mid * mid < x:
                low = mid
        return low

sol = Solution()
x= 1
result = sol.mySqrt(x)
print(result)

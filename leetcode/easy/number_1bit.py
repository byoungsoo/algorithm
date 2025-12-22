# Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).
from math import remainder


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n >= 1:
            if (n%2) == 1:
                count += 1
            n //= 2
        return count



sol = Solution()
n = 2147483645
result = sol.hammingWeight(n)
print(result)
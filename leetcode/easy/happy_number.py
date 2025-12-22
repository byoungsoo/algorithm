# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.



class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        num = n
        while True:
            total = 0
            s.add(num)
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10

            if total == 1:
                return True
            elif total in s:
                return False
            num = total

sol = Solution()
n = 19
result = sol.isHappy(n)
print(result)
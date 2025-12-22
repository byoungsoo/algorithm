class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n = n//2
        if n == 1:
            return True


sol = Solution()
n = 1
result = sol.isPowerOfTwo(n)
print(result)

# An integer n is a power of two, if there exists an integer x such that n == 2x.


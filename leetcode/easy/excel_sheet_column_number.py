class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0

        for c in columnTitle:
            val = ord(c) - 64
            total = total * 26 + val

        return total

sol = Solution()
columnTitle = "AB"
result = sol.titleToNumber(columnTitle)
print(result)

# The point is that [previous_num * (based-num) + current_num].
# For example, 10 based number system. 120 is 1*10+2 and 12*10+0
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500`
# M             1000

class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        i = 0
        size = len(s)
        while i < size:

            if i == size-1:
                result += roman[s[i]]
                break

            current = roman[s[i]]
            next = roman[s[i+1]]
            if current >= next:
                result += current
            else:
                result += (next - current)
                i += 1
            i+=1
        return result

sol = Solution()
s = "LVIII"

result = sol.romanToInt(s)
print(result)

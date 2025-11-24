class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        pre_val = 0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        for char in reversed(s):
            cur_val = roman[char]

            if cur_val >= pre_val:
                result += cur_val
            else:
                result -= cur_val

            pre_val = cur_val
        return result




sol = Solution()

s = "MCMXCIV"

# V I C X M C M
result = sol.romanToInt(s)
print(result)
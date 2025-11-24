# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:

        num_str = ""
        result = []
        for digit in digits:
            num_str += str(digit)

        num = int(num_str)+1
        num_str = str(num)

        for char in num_str:
            result.append(int(char))

        return result


sol = Solution()

digits = [1,9,9,9,9,9,9,9,9]
print(sol.plusOne(digits))
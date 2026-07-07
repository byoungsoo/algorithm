class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if not s or numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        current_row = 0
        direction = 1

        for char in s:
            rows[current_row].append(char)
            current_row += direction
            if current_row == numRows-1 or current_row==0:
                direction *= -1

        result_string = ""
        for row_list in rows:
            result_string += "".join(row_list)
        return result_string


sol = Solution()
s = "PAYPALISHIRING"
numRows = 4
result = sol.convert(s, numRows)
print(result)

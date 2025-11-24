class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            result = [[1]]
            return result
        result = [[1] for _ in range(numRows)]
        for cur_row in range(1, numRows):
            p1 = 0
            p2 = 0
            for p2 in range(0, cur_row-1):
                p2 = p1 + 1
                result[cur_row].append(result[cur_row - 1][p1] + result[cur_row - 1][p2])
                p1 += 1
            result[cur_row].append(result[cur_row - 1][p2])
            cur_row += 1
        return result


sol = Solution()
numRows = 30
res = sol.generate(numRows)
print(res)


# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

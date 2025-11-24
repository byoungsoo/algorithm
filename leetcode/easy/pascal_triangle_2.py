class Solution:
    def getRow(self, rowIndex: int) -> list[int]:

        if rowIndex == 0:
            return [1]

        temp = [1]
        for cur_row in range(0, rowIndex):
            cur_list = [1]
            p1 = 0
            p2 = 0
            for p2 in range(0, cur_row):
                p2 = p1 + 1
                cur_list.append(temp[p1] + temp[p2])
                p1 += 1
            cur_list.append(temp[p2])
            temp = cur_list

        return temp



sol = Solution()

rowIndex = 3

result = sol.getRow(rowIndex)
print(result)



class Solution:
    def reverseBits(self, n: int) -> int:
        binary_num = bin(n)[2:].zfill(32)
        reverse_num = ""
        for c in reversed(binary_num):
            reverse_num += c

        reverse_decimal = int(reverse_num, 2)
        return reverse_decimal


sol = Solution()
n = 2147483644
result = sol.reverseBits(n)
print(result)


# 00000010100101000001111010011100
# 00000010100101000001111010011100
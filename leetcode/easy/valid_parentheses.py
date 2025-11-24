class Solution:
    def isValid(self, s: str) -> bool:

        valid = True
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in mapping:
                if stack and stack[-1]  == mapping[char]:
                    stack.pop()
                else: return False

            else:
                stack.append(char)

        if stack:
            return False

        return True



sol = Solution()


# s = "()[]{}"
s = "([{)}]"
# s = "()"
result = sol.isValid(s)
print(result)
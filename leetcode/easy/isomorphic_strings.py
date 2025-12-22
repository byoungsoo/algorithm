class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        o_map = {}
        r_map = {}
        for idx, char in enumerate(s):
            if char in o_map:
                if o_map[char] != t[idx]:
                    return False
            elif t[idx] in r_map:
                if r_map[t[idx]] != char:
                    return False
            else:
                o_map[char] = t[idx]
                r_map[t[idx]] = char
        return True



sol = Solution()
s = "badc"
t = "baba"

result = sol.isIsomorphic(s,t)
print(result)
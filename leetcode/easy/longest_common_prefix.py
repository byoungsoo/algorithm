# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"


# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        common = ""
        strs.sort()

        firstWord = strs[0]
        lastWord = strs[-1]

        index = 0
        firstWordSize = len(firstWord)
        lastWordSize = len(lastWord)

        while index < firstWordSize and index < lastWordSize:
            firstWordChar = firstWord[index]
            lastWordChar = lastWord[index]

            if firstWordChar == lastWordChar:
                common += firstWordChar
                index += 1
            else:
                return common

        return common





sol = Solution()
strs = ["dog","racecar","car"]

result = sol.longestCommonPrefix(strs)

print(result)


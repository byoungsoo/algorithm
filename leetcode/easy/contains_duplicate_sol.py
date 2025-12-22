class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set((nums))) != len(nums)


sol = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
result = sol.containsDuplicate(nums)
print(result)
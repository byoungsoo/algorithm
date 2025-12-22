class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()

        for num in nums:
            if num in s:
                return True
            else:
                s.add(num)
        return False



sol = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
result = sol.containsDuplicate(nums)
print(result)
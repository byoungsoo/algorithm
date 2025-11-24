# You must implement a solution with a linear runtime complexity and use only constant extra space.
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.


class Solution:
    def singleNumber(self, nums: list[int]) -> int:

        res = 0
        for val in nums:
            res ^= val
        return res


sol = Solution()
nums = [2,2,1]
result = sol.singleNumber(nums)
print(result)


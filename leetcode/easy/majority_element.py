class Solution:
    def majorityElement(self, nums: list[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        major = nums[0]
        count = 0
        for cur in nums:
            if major == cur:
                count += 1
            else:
                count -= 1
            if count <= 0:
                major = cur
                count = 1
        return major

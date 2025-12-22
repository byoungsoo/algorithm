class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:

        num_map = {}
        for idx, num in enumerate(nums):
            if num in num_map:
                prev_idx = num_map[num]
                if abs(prev_idx - idx) <= k:
                    return True
            num_map[num] = idx
        return False



sol = Solution()
nums = [1,2,3,1]
k = 3
result = sol.containsNearbyDuplicate(nums, k)
print(result)



# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# abs(i - j) <= k
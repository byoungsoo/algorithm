#Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index = []
        origin = nums.copy()
        nums.sort()
        print(nums)
        left=0
        right=len(nums)-1

        while left<right:
            current_sum = nums[left]+nums[right]
            if current_sum == target:
                index.append(origin.index(nums[left]))
                if nums[left] == nums[right]:
                    index.append(origin.index(nums[right], origin.index(nums[left])+1))
                else:
                    index.append(origin.index(nums[right]))
                break
            elif current_sum < target:
                left+=1
            elif current_sum > target:
                right-=1
        return index


# Input: nums = [2,7,11,15], target = 9
nums = [3,3]
target = 6
# nums = [-1,-2,-3,-4,-5]
# target = -8

sol = Solution()
result = sol.twoSum(nums, target)

print(result)


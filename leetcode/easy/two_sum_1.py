class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        left = 0
        index=[]
        while left < len(nums):
            x = nums[left]
            y = target - x
            if y in nums:
                index.append(left)
                if x == y:
                    index.append(nums.index(y, left+1))
                else:
                    index.append(nums.index(y))
                break
            left +=1
        return index


# Input: nums = [2,7,11,15], target = 9

# nums = [2,7,11,15]
# target = 18
# nums = [3, 3]
# target = 6
# nums = [-1,-2,-3,-4,-5]
# target = -8
nums = [3,2,4]
target = 6

sol = Solution()
result = sol.twoSum(nums, target)

print(result)


class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]

        sp = 0
        p1 = 0
        p2 = 1

        res = []
        while p2 < len(nums):
            if nums[p1]+1 != nums[p2]:
                if sp == p1:
                    val = str(nums[sp])
                    res.append(val)
                else:
                    val = str(nums[sp]) + "->" + str(nums[p1])
                    res.append(val)
                sp = p2
            p1 += 1
            p2 += 1

        if sp == p1:
            val = str(nums[sp])
            res.append(val)
        else:
            val = str(nums[sp]) + "->" + str(nums[p1])
            res.append(val)
        return res

sol = Solution()
nums = [0,1,2,4,5,7]

result = sol.summaryRanges(nums)
print(result)
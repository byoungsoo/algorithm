
class Solution:

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for index, x in enumerate(nums):
            y = target -x
            if y in num_map:
                return [num_map[y], index]
            num_map[x]=index
        return []


sol = Solution()

# --- 테스트 케이스 ---
print(f"Example 1: {sol.twoSum(nums=[2, 7, 11, 15], target=9)}")
# 예상 출력: [0, 1]

print(f"Example 2: {sol.twoSum(nums=[3, 2, 4], target=6)}")
# 예상 출력: [1, 2] 또는 [2, 1] (순서는 상관없음)

print(f"Example 3: {sol.twoSum(nums=[3, 3], target=6)}")
# 예상 출력: [0, 1]


# "정렬된 배열에서 ~" -> 투 포인터, 이진 탐색
# "값이 있는지 빠른 검색 / (값, 인덱스) / 빈도수" -> 해시 맵 (딕셔너리)
# "모든 경우 탐색 / 최단 거리" -> BFS/DFS


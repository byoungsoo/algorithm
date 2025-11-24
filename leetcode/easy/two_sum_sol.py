def twoSum(nums: list[int], target: int) -> list[int]:
    # 숫자와 그 인덱스를 저장할 해시 맵 (Python에서는 딕셔너리)을 선언합니다.
    # key: 배열의 숫자, value: 해당 숫자의 인덱스
    num_map = {}

    # nums 배열을 한 번 순회합니다.
    for index, x in enumerate(nums):
        # 현재 숫자 (num)에 대해, 목표 값 (target)에서 현재 숫자를 뺀 값 (complement)을 찾습니다.
        y = target - x

        # 만약 complement가 이미 num_map에 있다면,
        # 이는 complement와 현재 num을 더하면 target이 된다는 의미입니다.
        if y in num_map:
            # num_map[complement]는 complement 값의 인덱스이고, i는 현재 num의 인덱스입니다.
            # 문제에서 요구하는 두 인덱스를 반환합니다.
            return [num_map[y], index]

        # complement가 num_map에 없다면, 현재 num을 num_map에 저장하여
        # 이후의 숫자가 현재 num을 complement로 찾을 수 있도록 합니다.
        num_map[x] = index

    # 문제의 제약 조건에 따르면 "Only one valid answer exists." 이므로
    # 이 부분의 코드가 실제로 실행될 일은 없습니다.
    # 하지만 모든 경로에 대한 반환 값이 있도록 예외 처리를 해둘 수 있습니다.
    return []


# --- 테스트 케이스 ---
print(f"Example 1: {twoSum(nums=[2, 7, 11, 15], target=9)}")
# 예상 출력: [0, 1]

print(f"Example 2: {twoSum(nums=[3, 2, 4], target=6)}")
# 예상 출력: [1, 2] 또는 [2, 1] (순서는 상관없음)

print(f"Example 3: {twoSum(nums=[3, 3], target=6)}")
# 예상 출력: [0, 1]
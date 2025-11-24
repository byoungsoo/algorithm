
def binary_search(arr: list[int], target: int):
    print("test")
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = int((low + high) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1



arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

binary_search(arr, target)


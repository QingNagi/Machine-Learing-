def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1   # 以防偶数无法运行
        elif li[mid] < val:
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(li, 4))

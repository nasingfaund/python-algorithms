def merge(a, b):
    left = right = 0
    result = []
    while left < len(a) and right < len(b):
        if a[left] <= b[right]:
            result.append(a[left])
            left += 1
        else:
            result.append(b[right])
            right += 1

    while left < len(a):
        result.append(a[left])
        left += 1
    while right < len(b):
        result.append(b[right])
        right += 1

    return result


def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    middle = len(alist) // 2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])
    return merge(left, right)


alist = [5, 4, 3, 2]
assert merge_sort(alist) == [2, 3, 4, 5]

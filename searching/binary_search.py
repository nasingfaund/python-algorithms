def binary_search(alist, value):
    first = 0
    last = len(alist) - 1

    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == value:
            return True
        if value < alist[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False


alist = [1, 2, 3, 4, 5, 6]
assert binary_search(alist, 6) is True
assert binary_search(alist, 1) is True
assert binary_search(alist, 10) is False

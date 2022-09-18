def partition(alist, low, high):
    pivot = alist[floor(low + high) // 2]

    while low < high:
        while alist[low] < pivot:
            low += 1
        while alist[high] > pivot:
            high -= 1
        alist[low], alist[high] = alist[high], alist[low]
    return high


def _quick_sort(alist, low, high):
    if low >= high:
        return
    pi = partition(alist, low, high)
    _quick_sort(alist, low, pi)
    _quick_sort(alist, pi + 1, high)


def quick_sort(alist):
    _quick_sort(alist, 0, len(alist) - 1)


alist = [8, 5, 4, 3, 2, 1]

print(quick_sort(alist))
assert quick_sort(alist) == [1, 2, 3, 4, 5, 8]

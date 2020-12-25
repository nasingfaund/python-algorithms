"""
https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html
"""

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


def binary_search_rec(nums, target):
    mid = len(nums) // 2
    if not nums:
        return False

    if nums[mid] == target:
        return True

    if target < nums[mid]:
        return binary_search_rec(nums[:mid], target)
    else:
        return binary_search_rec(nums[mid+1:], target)


alist = [1, 2, 3, 4, 5, 6]
assert binary_search(alist, 6) is True
assert binary_search(alist, 1) is True
assert binary_search(alist, 10) is False


assert binary_search_rec(alist, 6) is True
assert binary_search_rec(alist, 1) is True
assert binary_search_rec(alist, 10) is False

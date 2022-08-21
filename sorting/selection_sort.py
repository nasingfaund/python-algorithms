def selection_sort(alist):
    for i in range(len(alist) - 1):
        _min_index = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[_min_index]:
                _min_index = j

        temp = alist[i]
        alist[i] = alist[_min_index]
        alist[_min_index] = temp

    return alist


alist = [4, 10, 0, 1, 23, 15]
print(selection_sort(alist))

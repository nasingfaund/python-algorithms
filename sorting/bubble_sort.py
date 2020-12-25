def bubble_sort(alist):
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            if alist[i] > alist[j]:
                temp = alist[j]
                alist[j] = alist[i]
                alist[i] = temp
    return alist


assert bubble_sort([8, 10, 4, 1, 7, 3, 7]) == [1, 3, 4, 7, 7, 8, 10]

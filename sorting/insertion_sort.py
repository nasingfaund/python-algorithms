def insertion_sort(alist):
    for i in range(len(alist) - 1):
        if alist[i] > alist[i + 1]:
            index = i
            while alist[index] > alist[index + 1]:
                temp = alist[index]
                alist[index] = alist[index + 1]
                alist[index + 1] = temp
                if index != 0:
                    index -= 1
                else:
                    break
    return alist


assert insertion_sort([15, 5, 1, 0, 10, 8]) == [0, 1, 5, 8, 10, 15]


alist = [[1, 1, 1], [0, 0, 1], [1, 0, 0]]


def transitive_closure(alist):
    for i in range(len(alist)):
        for j in range(len(alist)):
            for k in range(len(alist)):
                alist[j][k] = alist[j][k] or alist[j][i] and alist[i][k]
    return alist

def find_intersection(a, b):
    res = []
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if a[i] == b[j]:
                res.append(a[i])
    return res


a = [1, 7, 9, 3, 8]
b = [3, 5, 0, 6, 7]

assert find_intersection(a, b) == [7, 3]

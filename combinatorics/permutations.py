# Steinhaus–Johnson–Trotter algorithm (also called 'plain changes')


# Sweep first element back and forth to insert it into every
# position in each perm of the other elements

alist = [1, 2, 3]


def find_permutations(alist):
    res = []
    temp = list(alist)

    while True:
        for i in range(len(temp) - 1):
            temp[i + 1], temp[i] = temp[i], temp[i + 1]
            if temp in res:
                return res
            res.append(list(temp))

# result 
# [[2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2], [1, 3, 2], [1, 2, 3]]

def gen_sub_sets(alist):
    res = []
    for i in range(0, 2 ** len(alist)):
        frm_str = bin(i)[2:].zfill(len(alist))
        subset = []
        for j in range(0, len(frm_str)):
            if int(frm_str[j]) != 0:
                subset.append(alist[j])
        res.append(subset)
    return res


alist = [1, 2, 3]
# result: [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]

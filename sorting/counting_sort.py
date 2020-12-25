def counting_sort(nums):
    k = max(nums)
    count = [0] * (k + 1)

    for i in range(len(nums)):
        count[nums[i]] += 1

    total = 0
    for i in range(k + 1):
        count[i], total = total, count[i] + total

    output = [0] * len(nums)
    for i in range(len(nums)):
        output[count[nums[i]]] = nums[i]
        count[nums[i]] += 1
    return output


nums = [2, 0, 2, 1, 1, 0]

assert counting_sort(nums) == [0, 0, 1, 1, 2, 2]


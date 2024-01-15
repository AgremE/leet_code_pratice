def bs_one(matrix, cur_ind, high, low):
    if matrix[cur_ind] == 1:
        # go left
        high = cur_ind - 1
        if matrix[high] != 1:
            return cur_ind
        if high <= low:
            if matrix[high] == 1:
                return high
            return cur_ind
    elif matrix[cur_ind] == 0:
        # go right
        low = cur_ind + 1
        if high <= low:
            if matrix[low] == 1:
                return low
            return -1
    cur_ind = (low + high) // 2
    return bs_one(matrix, cur_ind, high, low)


# test_1 = [1, 1, 1, 1, 1, 1, 1]
test_2 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
test_3 = [0, 1, 1, 1]

# print(bs_one(test_1, test_1, (len(test_1)) // 2, len(test_1), 0))
# print(bs_one(test_2, (len(test_2)) // 2, len(test_2), 0))
print(bs_one(test_3, (len(test_3)) // 2, len(test_3), 0))

def climbStairs(n: int) -> int:
    result = 0
    n_1 = 2
    n_2 = 1
    if n == 1 or n == 2 or n == 3:
        return n
    for i in range(n - 2):
        result = n_1 + n_2
        n_2 = n_1
        n_1 = result
    return result


print(climbStairs(4))

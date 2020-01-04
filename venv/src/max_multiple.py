def max_multiple(divisor, bound):
    val = 0
    for x in range(1,bound+1):
        if x % divisor == 0:
            if x > val:
                val = x
    return val

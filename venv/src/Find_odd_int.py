def find_it(seq):

    numbers = {}
    for x in seq:
        numbers[x] = 0

    for i in seq:
        numbers[i] = numbers.get(i) + 1

    for j in seq:
        if (numbers.get(j)) % 2 != 0:
            oddNumber = j

    return oddNumber
# ------------------------------------------------------------------------------------------------------------------------


# From Code wars..

# def find_it(seq):
#     for i in seq:
#         if seq.count(i)%2!=0:
#             return i

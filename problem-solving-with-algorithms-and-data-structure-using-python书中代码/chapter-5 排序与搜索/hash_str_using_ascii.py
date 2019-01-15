def hash(astring, tablesize):
    sum_ = 0
    for pos in range(len(astring)):
        sum_ = sum_ + ord(astring[pos])
    return sum_ % tablesize



print(hash('abcd', 11))

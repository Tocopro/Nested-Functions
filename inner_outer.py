
# outer function

def outer_func(a, b):
    sq = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # calling inner function from outer function
    add = addition(a, b)
    # add 5 tp result
    return add + 5


result = outer_func(2, 4)
print(result)

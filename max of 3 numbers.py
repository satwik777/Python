def max_numbers(x,y):
    if x > y:
        return x
    return y
def max_numbers3(x,y,z):
    return max_numbers(x,max_numbers(y,z))
print(max_numbers3(3, 4, 6))
print(max_numbers(4,5))
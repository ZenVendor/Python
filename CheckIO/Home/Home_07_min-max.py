def min(*args, **kwargs):



print(min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]))

def max(*args, **kwargs):
    return max(*args, key=kwargs.get("key", None))

#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert max(3, 2) == 3, "Simple case max"
#     assert min(3, 2) == 2, "Simple case min"
#     assert max([1, 2, 0, 3, 4]) == 4, "From a list"
#     assert min("hello") == "e", "From string"
#     assert C == 5.6, "Two maximal items"
#     assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
#     print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

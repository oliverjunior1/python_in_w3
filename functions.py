# def my_function():
#     print('Hello from a function')
# my_function()

# def my_function(fname):
#     print(fname + ' Refsnes')
# my_function('Emil')
# my_function('Tobias')
# my_function('Linus')

# def my_function(country = 'Norway'):
#     print('Iam from ' + country)
# my_function('Sweden')
# my_function('India')
# my_function()
# my_function('Brazil')

# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print('\n\nRecursion Example Results')
tri_recursion(6)

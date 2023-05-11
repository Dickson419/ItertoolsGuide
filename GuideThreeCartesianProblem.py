import itertools

"""The traditional method"""
numbers_1 = [1, 2, 3]
numbers_2 = [4, 5, 6]
product = []

def traditionalSolution():
    for i in numbers_1:
        for j in numbers_2:
            product.append((i,j))
    print(product)

def withItertools():
    print(list(itertools.product(numbers_1, numbers_2))) #list() used to display results

withItertools()





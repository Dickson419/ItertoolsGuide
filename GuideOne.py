import itertools

"""
Using itertools for advanced iteration
Some normal Python first...
"""

"""Count to 5000"""
# i = 0
# while True:
#     print(i)
#     i += 5
#     if i == 5000:
#         break

"""This could also be"""
# for i in range(0, 5000, 5):
#     print(i)

"""Into a list"""
print(list(range(0, 5000, 5)))

"""Itertools can be used as a generator"""
counter = itertools.count(0,5)
print(next(counter))
print(next(counter))
print(next(counter))




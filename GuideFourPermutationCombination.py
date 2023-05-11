import itertools

"""Demonstrate the use of combination and permutations with itertools"""

#How can i arrange these elements?
# Permutations = length, number of elements, factorial i.e 5! = 5x4x3x2x1 = 120. 10! = 3,628,800
letters = ["A", "B", "C", "D"]
print(list(itertools.permutations(letters)))

#combinations - how many unique combinations are there? Order does not matter so abc is the same as cba
print(list(itertools.combinations(letters, 3)))

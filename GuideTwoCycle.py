import itertools

"""Keep iterating over a list in order"""

"""as normal Python"""
stuff = ["a", 12, 4.5, False, 17]

# while True:
#     for item in stuff:
#         print(item)

"""With itertools"""
def cycleOne():
    for i in itertools.cycle(stuff):
        print(i)

def cycleTwo():
    myCycle = itertools.cycle(stuff)
    print(next(myCycle))
    print(next(myCycle))

def cycleThree():
    a = len(stuff)
    myCycle = itertools.cycle(stuff)
    for i in range(a):
        print(next(myCycle))

cycleTwo()
cycleThree()

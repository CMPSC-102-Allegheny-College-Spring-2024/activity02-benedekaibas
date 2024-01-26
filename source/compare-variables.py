"""Demonstrate strange outcomes when comparing variables."""


def firstQuestion():
# is 1.0 equal to 1.1?
    if 1.0 == 1.1:
        print("1.0 is the same as 1.1")
    else:
        print("1.0 is not the same as 1.1")

def secondQuestion():
# is 1.0 equal to 1?
    if 1.0 == 1:
        print("1.0 is the same as 1.0")
    else:
        print("1.0 is not the same as 1.0")

def thridQiestion():
# is .33333 + .33333 + .33333 == 1?
    if .33333 + .33333 + .33333 == 1:
        print(".33333 + .33333 + .33333 is equal to 1")
    else:
        print(".33333 + .33333 + .33333 is not equal to 1")

def fourthQuestion():
# is .33333333333 + .33333333333 + .3333333333 == 1?
    if .33333333333 + .33333333333 + .3333333333 == 1:
        print(".33333333333 + .33333333333 + .3333333333 is equal to 1")
    else:
        print(".33333333333 + .33333333333 + .3333333333 is not equal to 1")

def fifthQuestion():
# what is the value of 1/3 as a decimal number?
    print(f"The value of 1/3 is {(1/3)}")

def sixthQuestion():
# is 0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 == 1?
    if 0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 == 1:
        print("0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is equal to 1")
    else:
        print("0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is not equal to 1")

def seventhQuestion():
# is 1/3 + 1/3 + 1/3 == 1?
    if (1/3) + (1/3) + (1/3) == 1:
        print("1/3 + 1/3 + 1/3 is equal 1")
    else:
        print("1/3 + 1/3 + 1/3 is not equal 1")


if __name__ == "__main__":
    firstQuestion()
    secondQuestion()
    thridQiestion()
    fourthQuestion()
    fifthQuestion()
    sixthQuestion()
    seventhQuestion()

"""
After running all the functions I got the following output:
    1.0 is not the same as 1.1
    1.0 is the same as 1.0
    .33333 + .33333 + .33333 is not equal to 1
    .33333333333 + .33333333333 + .3333333333 is not equal to 1
    The value of 1/3 is 0.3333333333333333
    0.3333333333333333 + 0.3333333333333333 + 0.3333333333333333 is equal to 1
    1/3 + 1/3 + 1/3 is equal 1

"""
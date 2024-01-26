"""Demonstrate the limitations of using different variables"""
def feasible_number_i():
    feasible_number = 2**2**8
    print(f"The value of a feasible number is {feasible_number}")
    print()

def another_feasible_number_i():
    another_feasible_number = 2**2**10
    print(f"The value of another feasible number is {another_feasible_number}")
    print()

# ncomment this line and run it!
# Make sure that this line is commented-out when run in GitHub Actions
def less_feasible_number_i():
    less_feasible_number = 2**2**100
    print(f"The value of a less feasible number is {less_feasible_number}")
    print()


if __name__ == "__main__":
    feasible_number_i()
    another_feasible_number_i()
    less_feasible_number_i()
import sys

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return(3 * number + 1)

def test(n):
    try:
        n = int(n)
    except ValueError:
        print("Invalid (that's not an integer!)")
        sys.exit()
    if n == 0:
        print("We're done here!")
        sys.exit()
    while n != 1:
        print(collatz(n))
        n = collatz(n)        

n = input("Type in an integer: ")

test(n)
# returns the nth Fibonacci number using recursion.
def fibonacci(n):
    # base case
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    # recursive case: sum of previous two number
    return fibonacci(n - 1) + fibonacci(n - 2)

# calculates the Greatest Common Divisor of two numbers using Euclid's algorithm.
def gcd(a, b):
    # base case remainder is 0
    if b == 0:
        return a

    # recursive case: gcd(b, remainder of a/b)
    return gcd(b, a % b)


def compareTo(s1, s2):
    # base case: if both strings are empty
    if len(s1) == 0 and len(s2) == 0:
        return 0
        
    # if one string is empty
    if len(s1) == 0:
        return -1
    if len(s2) == 0:
        return 1
        
   # compare first characters
    if s1[0] < s2[0]:
        return -1
    if s1[0] > s2[0]:
        return 1
        
    # if first characters match, recursively compare rest
    return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    print("testing fibonacci:")
    for i in range(10):
        print(f"fibonacci({i}) = {fibonacci(i)}")

    print("\n testing gcd:")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"gcd(54, 24) = {gcd(54, 24)}")

    print("\n testing compareTo:")
    print(f"compareTo('cat', 'cat') = {compareTo('cat', 'cat')}")  
    print(f"compareTo('dog', 'fish') = {compareTo('dog', 'fish')}")  
    print(f"compareTo('zebra', 'lion') = {compareTo('zebra', 'lion')}") 

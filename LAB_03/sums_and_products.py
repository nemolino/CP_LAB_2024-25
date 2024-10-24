def sum_in_range(n):
    return (n * (n+1)) // 2


def product_in_range(n):
    factorial = 1
    for i in range(2,n+1):
        factorial *= i
    return factorial


n = int(input("Insert a positive integer n : "))
if n <= 0:
    print("ERROR : n must be positive!")
else:
    op = input("Insert 's' or 'p' : ")
    if op == "s": 
        print("The sum of the integers in 1 ...", n, "is", sum_in_range(n))
    elif op == "p":
        print("The product of the integers in 1 ...", n, "is", product_in_range(n))
    else:
        print("ERROR : invalid character!")
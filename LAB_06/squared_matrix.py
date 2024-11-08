from random import randint


def generate_random_matrix(n):
    """
    Takes a positive integer n.
    Returns a square matrix of random integers in [0,9] that has size n 
    """
    M = []
    for _ in range(n):
        M.append([])
        for _ in range(n):
            x = randint(0,9)    # randint(a,b) returns a random integer in [a,b]
            M[-1].append(x)
    return M


def print_matrix(M):
    """
    Takes a matrix M.
    Pretty-prints M. 
    """
    n = len(M)
    print("[")
    for i in range(n):
        for el in M[i]:
            print(f"{el:5d}", end='')
        print()
    print("]")


def square(M):
    """
    Takes a matrix M.
    Returns a new matrix that is M * M. 
    """
    n = len(M)
    M_squared = []
    for i in range(n):
        M_squared.append([])
        for j in range(n):

            ### here we are building x = M_squared[i][j]
            x = 0
            for k in range(n):
                x += M[i][k] * M[k][j] 
            ###

            M_squared[-1].append(x)

    return M_squared


### MAIN ######################################################################


while True:
    n = int(input("Insert matrix size : "))
    if n > 0:
        break
    else:
        print(f"The size", n, "is invalid\n")

M = generate_random_matrix(n)
print("\nM = ")
print_matrix(M)

M_squared = square(M)
print("\nM^2 = ")
print_matrix(M_squared)
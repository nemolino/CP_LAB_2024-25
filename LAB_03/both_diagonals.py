def draw_matrix_with_asterisks_on_both_diagonals(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == (n-1-i): 
                print("* ", end='')
            else:
                print("- ", end='')
        print()


n = int(input("Insert a positive integer n : "))
if n <= 0:
    print("ERROR : n must be positive!")
else:
    draw_matrix_with_asterisks_on_both_diagonals(n)
def draw_matrix_with_asterisks_on_main_diagonal(n):
    for i in range(n):
        row = ("- " * i) + "* " + ("- " * (n-i-1))
        print(row)


# another equivalent version that uses nested for loops
# def draw_matrix_with_asterisks_on_main_diagonal(n):
#     for i in range(n):
#         for j in range(n):
#             if i == j: 
#                 print("* ", end='')
#             else:
#                 print("- ", end='')
#         print()


n = int(input("Insert a positive integer n : "))
if n <= 0:
    print("ERROR : n must be positive!")
else:
    draw_matrix_with_asterisks_on_main_diagonal(n)
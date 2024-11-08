NUM_ROWS = 5
NUM_COLS = 26

M = []
for _ in range(NUM_ROWS):
    M.append([])
    for _ in range(NUM_COLS):
        M[-1].append([])

VOWELS = ['a', 'e', 'i', 'o', 'u']

count = 0
f = open('words.txt')
for line in f:
    word = line.strip()

    first_letter = word[0]
    if first_letter not in VOWELS: 
        count += 1
    else:
        index_row = VOWELS.index(first_letter)
        second_letter = word[1]
        index_col = ord(second_letter)-ord('a')
        M[index_row][index_col].append(word)

f.close()

print("There are", count, "words that do not start with a vowel\n")
for i in range(NUM_ROWS):
    print(VOWELS[i], ": {")
    for j in range(NUM_COLS):
        if M[i][j]:
            second_letter = chr(ord('a')+j)
            words_joined_by_commas = ', '.join(sorted(M[i][j]))
            print("\t", second_letter, ": {", words_joined_by_commas, "}")
    print("}")
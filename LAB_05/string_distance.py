def is_alphabetical(c):
    """
    Takes a character c.
    Returns True if c is alphabetical, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')


def contains_only_alphabetical_chars(s):
    """
    Takes a string s.
    Returns True if s contains only alphabetical characters , False otherwise
    """
    for char in s:
        if not is_alphabetical(char):
            return False
    return True


def remove_non_alphabetical_chars(s):
    """
    Takes a string s.
    Returns a new string that is the result of removing the non-alphabetical characters from s.
    The order of the alphabetical ones is preserved.
    """
    new_s = ""
    for char in s:
        if is_alphabetical(char):
            new_s += char
    return new_s


def distance_between_words(w1, w2):
    """
    Takes a string w1 and a string w2.
    Requires that w1 and w2 have the same length and only contain alphabetical characters.
    Returns the distance between w1 and w2.
    """
    w1 = w1.lower()
    w2 = w2.lower()
    distance = 0
    for i in range(len(w1)):
        distance += abs(ord(w1[i])-ord(w2[i]))
    return distance


### MAIN ######################################################################

x_min_length, x_max_length = 3, 10
while True:
    x = input("Insert a string : ")
    if x_min_length <= len(x) <= x_max_length and contains_only_alphabetical_chars(x):
        break
    else:
        print(f"The string '{x}' is invalid")

# the distance between 'a' and 'z'
max_distance = 25   
# distance between x and another words will never be greater than min_distance
min_distance = max_distance * x_max_length   
min_distance_word = None

f = open('words.txt')
for line in f:
    word = line.strip()
    cleaned_word = remove_non_alphabetical_chars(word)
    if len(x) == len(cleaned_word):
        distance = distance_between_words(x,cleaned_word)
        if distance < min_distance:
            min_distance = distance
            min_distance_word = word
f.close()

print("Lowest distance from '", x, "' is ", min_distance, " and it is given by the word '", min_distance_word, "'", sep='')
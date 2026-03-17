# Function to check whether
# First and last characters of the words match
def check_match(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            lst.append(word)
            ctr += 1
            lst.append(word)

    print("List of words with matching first and last same\n,",
lst)
    return ctr


count = check_match(["abc", "xyz", "aba", "1221"])
print("Count of words with matching first and last same:",
count)
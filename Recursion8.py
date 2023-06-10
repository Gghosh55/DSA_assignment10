def countConsonants(s):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0

    def helper(string):
        nonlocal count
        if len(string) == 0:
            return

        if string[0] in consonants:
            count += 1

        helper(string[1:])

    helper(s)
    return count

# Test the function
string = "abc de"
string1 = "geeksforgeeks portal"
print(f"Total consonants: {countConsonants(string)}")
print(f"Total consonants: {countConsonants(string1)}")

def countSubstrings(s):
    count = 0
    n = len(s)

    for i in range(n):
        count += 1
        j = i - 1
        k = i + 1

        while j >= 0 and k < n and s[j] == s[k]:
            count += 1
            j -= 1
            k += 1

    return count

# Test the function
print(countSubstrings("abcab"))
print(countSubstrings("aba"))

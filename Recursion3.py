def printSubsets(s, current_set, index):
    if index == len(s):
        print(current_set)
        return
    printSubsets(s, current_set + s[index], index + 1)


    printSubsets(s, current_set, index + 1)

def subsets(s):
    printSubsets(s, "", 0)

subsets("abc")
subsets("abcd")


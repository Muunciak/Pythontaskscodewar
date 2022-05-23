def array_diff(a, b):
    #your code here
    for i in a.copy():
        if i in b:
            a.pop(a.index(i))
    return a
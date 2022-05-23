def alphabet_position(text):
    n = []
    for x in text:
        if ord(x) - 96 > 0:
            n.append(ord(x) - 96)
        elif ord(x) - 96 < 0:
            if ord(x) == 32 or ord(x) == 46 or ord(x) == 39:
                pass
            else:
                n.append((ord(x)-96)+32)
    print(str(n)[1:-1])


alphabet_position("The sunset sets at twelve o' clock.")
def disemvowel(string_):
    vowels = 'a', 'e', 'i', 'o', 'u', 'w', 'y', 'A', 'E', 'I', 'O', 'U', 'W', 'Y'
    for i in vowels:
        string_ = string_.replace(i, '')
    return string_


print(disemvowel("This website is for losers LOL! "))

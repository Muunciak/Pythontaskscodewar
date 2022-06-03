import random

while True:
    char = ['"', '#', '$', '%', '&', '(', ')', '*', '+', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'W', 'Y', 'X', 'Z']
    wish = int(input('What number of characters you want to have in password?'))
    password = ""
    for i in range(wish):
        data = random.choice(char)
        password = password + data
    print(password)
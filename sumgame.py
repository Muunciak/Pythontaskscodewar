from random import randint
score = 1
while True:
    a = randint(1, 50)
    b = randint(1, 50)
    c = a + b
    question_mark_position = randint(1, 3)
    print('Type the answer: ')

    match question_mark_position:
        case 1:
            print(f' ? + {b} = {c}')
            correct_answer = a
        case 2:
            print(f' {a} + ? = {c}')
            correct_answer = b
        case 3:
            print(f' {a} + {b} = ?')
            correct_answer = c

    your_answer = int(input())
    if your_answer == correct_answer:
        print('Correct! :)')
        print(f'Your score is: {score}')
        score += 1
        if score == 50:
            print("I think you are unstoppable B)")
    else:
        print('Incorrect. :(')
        break
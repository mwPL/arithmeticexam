import random


def easy():
    correct = 0
    for i in range(5):
        x = random.randint(2, 9)
        op = random.choice(['+', '-', '*'])
        y = random.randint(2, 9)
        print(f'{str(x)} {op} {str(y)}')
        while True:
            guess = input()
            if guess == '' or guess[0] not in '-0123456789':
                print('Incorrect format.')
            elif len(guess) > 1 and not guess[1:].isdigit():
                print('Incorrect format.')
            else:
                break
        if op == '+':
            result = x + y
        elif op == '-':
            result = x - y
        elif op == '*':
            result = x * y
        if int(guess) == result:
            print('Right!')
            correct += 1
        else:
            print('Wrong!')
    return correct


def hard():
    correct = 0
    for i in range(5):
        x = random.randint(11, 29)
        print(x)
        while True:
            try:
                guess = int(input())
                if guess == x * x:
                    print('Right!')
                    correct += 1
                    break
                else:
                    print('Wrong!')
                    break
            except ValueError:
                print('Wrong format! Try again')
    return correct


while True:
    print('Which level do you want? Enter a number:')
    print('1 - simple operations with numbers 2-9')
    print('2 - integral squares of 11-29')
    choice = input()
    if choice == '1':
        correct = easy()
        break
    elif choice == '2':
        correct = hard()
        break
    else:
        print('Incorrect format.')
print(f"Your mark is {correct}/5. Would you like to save the result? Enter yes or no.")
answer = input()
if answer in ['yes', 'YES', 'Yes', 'y']:
    print('What is your name?')
    name = input()
    level = 'level 1 (simple operations with numbers 2-9)' if choice == '1' else 'level 2 (integral squares of 11-29)'
    myfile = open('results.txt', 'a')
    s = f"{name}: {correct}/5 in {level}."
    myfile.write(s)
    myfile.close()
    print('The results are saved in "results.txt".')
else:
    exit()



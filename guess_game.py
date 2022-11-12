import random
def guess_game():
    x = random.randint(0,5)
    guess = int(input('enter a guess number: '))
    user_lifeline = 0
    while user_lifeline < 5:
        if x == guess:
            print('number guessed correctly', user_lifeline)
            break
        else:
            print('number not guessed correctly')
        user_lifeline += 1
        guess= int(input('enter a guess_number: '))
guess_game()


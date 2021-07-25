import random

def play():
    user = input("Choose -- 'R' for Rock, 'P' for Paper, 'S' for Scissors : \n").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'IT\'s a tie!!!'

    if is_win(user, computer):
        return 'You Won!!!'

    return "You Lost!!!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
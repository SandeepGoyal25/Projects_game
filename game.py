import random
def gameWin(computer, you):
    if computer == you:
        return None
    
    elif computer == 'R':
        if you == 'S':
            return False
        elif you == 'P':
            return True
    
    elif computer == 'S':
        if you == 'P':
            return False
        elif you == 'R':
            return True
    
    elif computer == 'P':
        if you == 'R':
            return False
        elif you == 'S':
            return True

print("Computer Turn: Rock(R), Paper(P) or Scissor(S)?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 'R'
if randNo == 2:
    computer = 'S'
if randNo == 3:
    computer = 'P'

you = input("Your Turn: Rock(R), Paper(P) or Scissor(S)?")
a = gameWin(computer, you)

print(f"Computer choose {computer}")
print(f"You choose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Loose!")

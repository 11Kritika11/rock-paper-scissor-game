import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False

print("Comp turn: rock(r) paper(p) or scissor(s) : ")

randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn: rock(r) paper(p) or scissor(s) : ")
print(f"Computer choose : {comp}")
print(f"You choose : {you}")

a = gameWin(comp, you)

if a == None:
    print("The game is a tie")
elif a:
    print("Congratulations!! You win the game ")
else:
    print("You loose the game :(")


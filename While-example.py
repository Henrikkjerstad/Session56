import random
lives = 3
while lives:
    print("You have", lives, "lives left.")
    # roll the dice
    dice = random.randint(1,6)
    print("you rolled a", dice)
    # Check if you win
    if dice == 6:
        print("\n\nYOU WIN!\n\n")
        break
    lives -= 1
else:
    print("\n\nYOU LOSE!\n\n")

print("Thank you for playing. Goodbye.")
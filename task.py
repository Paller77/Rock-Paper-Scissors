import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def rock_paper_scissor():
    print("Welcome to the Rock-Paper-Scissors game!")
    selection = input("Choose your fighter!\nType 0 for Rock, 1 for Paper, 2 for Scissors!\n")
    selection = int(selection)

    if selection == 0:
        print(rock)
    elif selection == 1:
        print(paper)
    elif selection == 2:
        print(scissors)
    else:
        print("This fighter can not be chosen! Please restart the game with [CTRL + ENTER!]")
        exit()

    print("Computer's fighter:")

    comp_fighters = [rock, paper, scissors]
    comp_selection_index = random.randrange(len(comp_fighters))

    if comp_selection_index == 0:
        print(rock)
    elif comp_selection_index == 1:
        print(paper)
    elif comp_selection_index == 2:
        print(scissors)

    if selection == 0 and comp_selection_index == 0:
        print("DRAW!")
    elif selection == 1 and comp_selection_index == 0:
        print("YOUR FIGHTER WON!")
    elif selection == 2 and comp_selection_index == 0:
        print("YOUR FIGHTER LOST!")
    elif selection == 0 and comp_selection_index == 1:
        print("YOUR FIGHTER LOST!")
    elif selection == 1 and comp_selection_index == 1:
        print("DRAW!")
    elif selection == 2 and comp_selection_index == 1:
        print("YOUR FIGHTER WON!")
    elif selection == 0 and comp_selection_index == 2:
        print("YOUR FIGHTER WON!")
    elif selection == 1 and comp_selection_index == 2:
        print("YOUR FIGHTER LOST!")
    elif selection == 2 and comp_selection_index == 2:
        print("DRAW!")

while input("Do you want to play Rock-Paper-Scissors? ('y' or 'n')") == "y":
    print("\n"*40)
    rock_paper_scissor()
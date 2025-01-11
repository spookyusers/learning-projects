import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        num_die = int(input('How many? Enter whole number: '))
        die_list = []
        for n in range(num_die):
            die_list.append(random.randint(1,6))
        die_tuple = tuple(die_list)
        print(die_tuple)
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else:
        print('Invalid choice!')
exit()

# Code without user choosing number of die to roll
# while True:
#     choice = input('Roll the dice? (y/n): ').lower()
#     if choice == 'y':
#         die1 = random.randint(1,6)
#         die2 = random.randint(1,6)
#         print(f'({die1},{die2})')
#     elif choice == 'n':
#         print('Thanks for playing!')
#         break
#     else:
#         print('Invalid choice!')
# exit()

# Example thought process
# Loop
    # Ask: roll how many dice? (enter number or exit)
    # If user enters number
        # Loop
            # create a die
            # generate a random number 1,6
            # add die to list
        # Turn list into tuple
        # Print
    # If user enters exit
        # Print thank you message
        # break
    # If invalid input
        # Print invalid input!
# Exit

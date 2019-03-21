import random


# this function gets how many die are being rolled and how many sides the die have
def get_die():
    die_num = 0
    die_type = 0
    # while loop ensures the user enters a minimum of 1 for the number of die and sides
    while die_type < 1 and die_num < 1:
        try:
            die_num = int(input("Please enter how many die you would like to roll: "))
            if die_num < 1:
                print("Die type must be greater than 0!")
                die_num = 0
            if die_num > 0:
                die_type = int(input("Please enter the number of sides: "))
                if die_type < 1:
                    print("Die type must be greater than 0!")
                    die_type = 0
            # returns the values once the user has entered valid numbers for the input
            if die_num > 0 and die_type > 0:
                return die_num, die_type
        except ValueError:
            print("Must enter a number!")


# this function stores the dice rolls in an empty list then prints the results in a beautiful manner
def roll_die(user_die):
    die_results = []
    # appends a dice roll to die_results as many times as the user entered rolls
    for num in range(0, user_die[0]):
        die_results.append(random.randint(1, user_die[1]))
    print("Results: " + str(die_results))
    print("Sum total: " + str(sum(die_results)) + "\n")

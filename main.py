import random
import main_functions

while True:
    user_die = main_functions.get_die()
    print("User die: " + str(user_die))

    cont = input("Continue?: ")
    if cont.lower() not in ("no", "n", "0"):
        break

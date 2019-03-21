import main_functions

while True:
    user_die = main_functions.get_die()
    main_functions.roll_die(user_die)
    cont = input("Continue?: ")
    if cont.lower() in ("no", "n", "0"):
        break
    print("")

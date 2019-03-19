

def get_die():
    die_num = 0
    die_type = 0
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
            if die_num >= 1 and die_type >= 1:
                return die_num, die_num
        except ValueError:
            print("Must enter a number!")

print("Welcome!\nThink of a number between 1 and 1000 and we'll tell you if it's even or odd\n")
def odd_or_even():
    continue_asking = True;
    val = input("What number are you thinking of? ")

    if val:
        if val.isnumeric():
            if 1 <= int(val) <= 1000:
                remainder = int(val) % 2
                if remainder == 0:
                    print("That's an even number! Have another?")
                else:
                    print("That's an odd number! Have another?")
            else:
                print("Please input a number between 1 and 1000")

            print("Type in a string to quit\n")
        else:
            continue_asking = False
    else:
        print("Please input a value\n")

    if continue_asking:
        odd_or_even()

odd_or_even()
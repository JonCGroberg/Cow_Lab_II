import functools
import sys

from dragon import Dragon
from heifer_generator import HeiferGenerator


def main():
    # If no arguments are passed, exit the program
    if len(sys.argv) == 0:
        exit()

    # Get the first argument passed
    arg1 = sys.argv[1]

    # If the first character of the first argument is '-', it's a flag
    if arg1[0] == '-':
        # If the flag is 'l', list all available cows
        if arg1[1:] == 'l':
            cows = stringify_cows(HeiferGenerator.get_cows())
            print("Cows available: " + cows)

            # If the flag is 'n', generate a cow with a specific name and message
        elif arg1[1:] == 'n':
            cow_name = sys.argv[2]
            message = concat(sys.argv[3:])
            cow = find_cow(cow_name)

            # If the cow is found, print the message and the image of the cow
            if cow:
                print(message)
                print(cow.get_image())
                if isinstance(cow, Dragon):
                    can_breathe_fire = "can" if cow.can_breathe_fire() else "cannot"
                    print(f"This dragon {can_breathe_fire} breathe fire.")

            else:
                print("Could not find " + cow_name + " cow!")
        elif arg1[1:] == "f":
            pass

    else:
        # print everything if one of the special commands is not found
        message = concat(sys.argv[1:])
        default_cow = HeiferGenerator.get_cows()[0]
        print(message)
        print(default_cow.get_image())


def stringify_cows(cows):
    # turn to a list of strings
    cow_name_list = list(map(lambda cow: cow.get_name(), cows))
    # concat the strings and return
    return concat(cow_name_list)


# concat but add a space between
def concat(list):
    return functools.reduce(lambda a, b: a + " " + b, list)


# return the cow with name x if it exists, none otherwise
def find_cow(name):
    for item in HeiferGenerator.get_cows():
        if item.get_name() == name:
            return item
    return None


if __name__ == "__main__":
    main()

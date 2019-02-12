from wheatclass import *
from potatoclass import *

def display_menu():
    print()
    print("Which crop do you want to create")
    print()
    print("1. Potato")
    print("2. Wheat")
    print()
    print("Please select an option from above menu")

def select_option():
    option_valid = False
    while not option_valid:
        try:
            choice = int(input("Option Selected: "))
            if choice in (1,2):
                option_valid = True
            else:
                print ("Enter Valid option")
        except ValueError:
            print ("Enter Valid option")
    return choice

def create_crop():
    display_menu()
    choice = select_option()
    if choice == 1:
        new_crop = Potato()
    elif choice == 2:
        new_crop = Wheat()
    return new_crop

def main():
    new_crop = create_crop()
    manage_crop(new_crop)

if __name__ == '__main__':
    main()

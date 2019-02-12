from Cow import *
from Sheep import *

#Animal Display Menu
def display_menu():
    print ("Choose which animal you want to create: ")
    print ()
    print ("1.Cow")
    print ("2.Sheep")
    print()

#Function for chosing Option
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

#Animal Creation Fn

def create_animal():
    display_menu()
    choice = select_option()
    if choice == 1:
        print()
        name = input("Enter name of Cow: ")
        new_animal = Cow(name)
    elif choice == 2:
        print()
        name = input("Enter name of Sheep: ")
        new_animal = Sheep(name)
    return new_animal

#Main Function
def main():
    new_animal = create_animal()
    animal_manage(new_animal)

if __name__ == '__main__':
    main()

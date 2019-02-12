from Cow_Class import *
from Sheep_Class import *
from Potato_Class import *
from Wheat_Class import *
import random

class Field:
    """A Class to stimulate Field which Contain Plants and Animals ."""
    #constructor
    def __init__(self, max_animals, max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops

    def plant_crop(self,crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False

    def add_animal(self,animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False

    def harvest_crop(self,position):
        return self._crops.pop(position)

    def remove_animal(self,position):
        return self._animals.pop(position)

    def report_contents(self):
        crop_report = []
        animal_report = []
        for crop in self._crops:
            crop_report.append(crop.report())
        for animal in self._animals:
            animal_report.append(animal.report())
        return {'Crops' : crop_report , 'Animals': animal_report}

    def report_need(self):
        food = 0
        light = 0
        water = 0
        for crop in self._crops:
            needs = crop.needs()
            if needs['light_need'] > light:
                light = needs['light_need']
            if needs['water_need'] > water:
                water = needs['water_need']
        for animal in self._animals:
            needs = animal.needs()
            food = food + needs['food need']
            if needs['water need'] > water:
                water = needs['water need']
        return {'Food' : food, 'Light' : light, 'Water': water}

    def grow(self,food,light,water):
        #grow the crop (Light and Water available to all the crops in same amount)
        if (len(self._crops)>0):
            for crop in self._crops:
                crop.grow(light,water)
        #grow the animals (water available to all the animals in same amount)
        #but food is total that must be shared
        if (len(self._animals)>0):
            #get total amount of food required in the Field
            food_required = 0
            for animal in self._animals:
                needs = animal.needs()
                food_required += needs['food need']
            #if we have more food available than is required work out the additional_food
            if food > food_required:
                additional_food = food - food_required
                food = food_required
            else:
                additional_food = 0
            #Grow each animal
            for animal in self._animals:
                #get the animals food needs
                needs = animal.needs()
                if food >= needs['food need']:
                    #remove food for this animal from total
                    food = food - needs['food need']
                    feed = needs['food need']
                    #see if there is additional_food left
                    if additional_food > 0:
                        #remove food from additional_food for this animal
                        additional_food -= 1
                        #add this to the feed given to animal
                        feed += 1
                    animal.grow(feed,water)



def auto_grow(field,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        food = random.randint(1,100)
        #Grow the Field
        field.grow(food,light,water)

def manual_grow(field):
    #Get Food Value
    valid = False
    while not valid:
        try:
            food = int(input("Please enter food value(1-100): "))
            if 1<=food<=100:
                valid = True
            else:
                print ("Value entered not valid please enter value between 1-100")
        except ValueError:
            print ("Value entered not valid please enter value between 1-100")
    #Get Water Value
    valid = False
    try:
        water = int(input("Please enter water value(1-10): "))
        if 1<=water<=10:
            valid = True
        else:
            print ("Value entered not valid please enter value between 1-10")
    except ValueError:
        print ("Value entered not valid please enter value between 1-10")

    #Get Light Value
    valid = False
    while not valid:
        try:
            light = int(input("Please enter light value(1-10): "))
            if 1<=light<=10:
                valid = True
            else:
                print ("Value entered not valid please enter value between 1-10")
        except ValueError:
            print ("Value entered not valid please enter value between 1-10")
    field.grow(food,light,water)




def display_crops(crop_list):
    print()
    print("The following are the crops in field: ")
    pos = 1
    for crop in crop_list:
        print("{0:>2}. {1}".format(pos,crop.report()))
        pos += 1

def display_animals(animal_list):
    print()
    print("The following are thr animals in the field: ")
    pos = 1
    for animal in animal_list:
        print("{0:>2}. {1}".format(pos,animal.report()))
        pos += 1

def select_crop(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a crop: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def select_animal(length_list):
    valid = False
    while not valid:
        selected = int(input("Please select a animal: "))
        if selected in range(1,length_list+1):
            valid = True
        else:
            print("Please select a valid option")
    return selected - 1

def harvest_crop_from_field(field):
    display_crops(field._crops)
    selected_crop = select_crop(len(field._crops))
    return field.harvest_crop(selected_crop)

def remove_animal_from_field(field):
    display_animals(field._animals)
    selected_animal = select_animal(len(field._animals))
    return field.remove_animal(selected_animal)

def display_crop_menu():
    print ()
    print("Which crop do you like to plant?: ")
    print("1. Potato")
    print("2. Wheat")
    print()
    print("0. I dont want to plant crop return me to main menu")
    print()
    print("Please select an action from Above menu")

def display_animal_menu():
    print ()
    print("Which animal do you like to buy?: ")
    print("1. Cow")
    print("2. Sheep")
    print()
    print("0. I dont want to buy animal return me to main menu")
    print()
    print("Please select an action from Above menu")

def display_main_menu():
    print()
    print("1. Plant a new crop")
    print("2. Harvest a crop")
    print()
    print("3. Buy a new animal")
    print("4.Slaughter a animal")
    print()
    print("5. Grow field manually over 1 day")
    print("6. Grow Field automatically over 30 days")
    print()
    print("7. Report Field Status")
    print()
    print("0. Exit Field")
    print()
    print("Please select an action from Above menu")

def get_menu_choice(lower,upper):
    valid = False
    while not valid:
        try:
            choice = int(input("Option selected: "))
            if lower <= choice <= upper:
                valid = True
            else:
                print("Please select a valid option "+lower +"-"+upper)
        except ValueError:
            print("Please select a valid option "+lower +"-"+upper)
    return choice

def plant_crop_in_field(field):
    display_crop_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        if field.plant_crop(Potato()):
            print()
            print ("Potato planted")
            print()
        else:
            print()
            print("No space in your field to plant potato")
            print()
    if choice == 2:
        if field.plant_crop(Wheat()):
            print()
            print ("Wheat planted")
            print()
        else:
            print()
            print("No space in your field to plant wheat")
            print()

def add_animal_to_field(field):
    display_animal_menu()
    choice = get_menu_choice(0,2)
    if choice == 1:
        print()
        name=input(("What is the name of the cow: "))
        print()
        if field.add_animal(Cow(name)):
            print()
            print ("Cow added to herd")
            print()
        else:
            print()
            print("No space in your field to add cow")
            print()
    if choice == 2:
        print()
        name=input(("What is the name of the sheep: "))
        print()
        if field.add_animal(Sheep(name)):
            print()
            print ("Sheep added to herd")
            print()
        else:
            print()
            print("No space in your field to add sheep")
            print()


def manage_field(field):
    print ("Welcome to your field management Program")
    print()
    exit = False
    while not exit:
        display_main_menu()
        option = get_menu_choice(0,7)
        print()
        if option == 1:
            plant_crop_in_field(field)
        elif option == 2:
            removed_crop = harvest_crop_from_field(field)
            print("You harvested the crop: {0}".format(removed_crop))
        elif option == 3:
            add_animal_to_field(field)
        elif option == 4:
            removed_animal = remove_animal_from_field(field)
            print("You butchered the animal: {0}".format(removed_animal))
        elif option == 5:
            manual_grow(field)
        elif option == 6:
            auto_grow(field,30)
        elif option == 7:
            print(field.report_contents())
        elif option == 0:
            exit = True
            print()
    print ("Bye Bye ! See you again thanks for using field management program")
#Main Function of Field Class
def main():
    new_field = Field(5,2)
    manage_field(new_field)

if __name__ == '__main__':
    main()

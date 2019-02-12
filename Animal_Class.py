import random
class Animal:
    """A Class of Generic Animal ."""
    #constructor for animal class
    def __init__(self,growth_rate,food_need,water_need,name):
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Baby"
        self._type = "Generic"
        self._name = name

    #Method Which Returns need for animal to grow
    def needs(self):
        return {'food need' : self._food_need, 'water need': self._water_need}
    #Method which return current report of the animal
    def report(self):
        return {'Name' : self._name, 'Weight': self._weight, 'Days Growing': self._days_growing, 'Status' : self._status, 'type': self._type}

    #Private Method for updating status
    def _update_status(self):
        if self._weight > 20:
            self._status = "Old"
        elif self._weight > 15:
            self._status = "Adult"
        elif self._weight > 10:
            self._status = "Teen"
        elif self._weight > 5:
            self._status = "Kid"
        elif self._weight > 0:
            self._status = "Baby"

    #Method for Growing
    def grow(self,food,water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        self._days_growing += 1
        self._update_status()

# Auto Growth Testing Function
def auto_grow(animal,days):
    for day in range(days):
        food = random.randint(1,10)
        water = random.randint(1,10)
        animal.grow(food,water)

#For Manual Growth of Animal Day by Day doesnt make sense but we are doing
#this for learning compromising reality
def manual_grow(animal):
    #get values of food and water from user
    valid = False
    while not valid:
        try:
            food = int(input("Please enter food value(1-10): "))
            if 1<=food<=10:
                valid = True
            else:
                print ("Value entered not valid please enter value between 1-10")
        except ValueError:
            print ("Value entered not valid please enter value between 1-10")
    valid = False
    try:
        water = int(input("Please enter water value(1-10): "))
        if 1<=water<=10:
            valid = True
        else:
            print ("Value entered not valid please enter value between 1-10")
    except ValueError:
        print ("Value entered not valid please enter value between 1-10")

    #grow the animal
    animal.grow(food,water)

#Menu Display Function
def display_menu():
    print()
    print("1.Manually Grow")
    print("2.Auto Grow for 30 days")
    print("3.Get Report")
    print("0.Exit from Program")

#For to choose Valid Choice
def get_menu_choice():
    valid = False
    while not valid:
        try:
            option_chosen = int(input("Enter option from above menu: "))
            if 0<=option_chosen<=3:
                valid = True
            else:
                print("Choose valid option")
                print()
        except ValueError:
            print("Choose valid option")
    return option_chosen

#Animal Management Function
def animal_manage(animal):
    noexit = True
    print ("This is Animal Management")
    print ()
    while noexit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(animal)
            print()
        elif option == 2:
            auto_grow(animal,30)
            print()
        elif option == 3:
            print(animal.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print ("Thanks for using Animal Corporation")

#Main Function
def main():
    new_animal = Animal(2,3,5,"Ramudu")
    animal_manage(new_animal)

if __name__ == '__main__':
    main()

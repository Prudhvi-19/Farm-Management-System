import random

class Crop:
    """A Generic Crop Class ."""
    #constructor
    def __init__(self, growth_rate,light_need, water_need):
        #set attributes to initial Values

        self._growth = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

        #The Above attirbutes are prefixed with underscore to indicate that
        #they should not be acessed directly from out with class (private attributes)

        #CLASS METHODS
    def needs(self):
        #return a dictionary containing light and water needed
        return {'light_need' : self._light_need, 'water_need' : self._water_need}

    def report(self):
        #return a dictionary reporting tyoe,status,growth, days growing
        return {'type': self._type, 'status' : self._status, 'growth' : self._growth,'days growing': self._days_growing}

    def _update_status(self):
        #updates status of the crop based on growth
        #this is private method only acessed with in class
        if self._growth > 15:
            self._status = "Old"
        elif self._growth >10:
            self._status = "Mature"
        elif self._growth >5:
            self._status = "Young"
        elif self._growth >0:
            self._status = "Seedling"
        else:
            self._status = "Seed"

    def grow(self,light,water):
        if light >= self._light_need and water >=self._water_need:
            self._growth = self._growth + self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update status
        self._update_status()


#Auto Grow Function To Grow Crop for number of Days automatically
#Auto Grow is Testing Function
def auto_grow(crop,days):
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)

#Manually Provide Light and Water Values . Means we manually growing the crop
#Manual Grow is also Testing Function
def manual_grow(crop):
    #get values of light and water from user
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
    valid = False
    try:
        water = int(input("Please enter water value(1-10): "))
        if 1<=water<=10:
            valid = True
        else:
            print ("Value entered not valid please enter value between 1-10")
    except ValueError:
        print ("Value entered not valid please enter value between 1-10")

    #grow the crop
    crop.grow(light,water)

#Menu Display Function
def display_menu():
    print("1.Grow Manually over 1 day")
    print("2.Grow automatically over 30 days")
    print("3.Get Report")
    print("0.Exit Testing Program")

#Menu Choice Function
def get_menu_choice():
    option_valid = False
    while not option_valid:
        try:
            choice=int(input("Option Selected: "))
            print()
            if 0<=choice<=3:
                option_valid = True
            else:
                print ("Please Select Valid Option")
        except ValueError:
            print ("Please Select Valid Option")
            print()
    return choice

#Manage Crop Function
def manage_crop(crop):
    print ("This is Crop Management Program")
    print()
    noexit = True
    while noexit:
        display_menu()
        option = get_menu_choice()
        if option == 1:
            manual_grow(crop)
            print()
        elif option ==2:
            auto_grow(crop,30)
            print()
        elif option == 3:
            print (crop.report())
            print()
        elif option == 0:
            noexit = False
            print()
    print ("Thank for using Crop Management Program")


def main():
    #instantiation of class(crop)
    new_crop = Crop(2,6,3)
    manage_crop(new_crop)

if __name__ == '__main__':
    main()

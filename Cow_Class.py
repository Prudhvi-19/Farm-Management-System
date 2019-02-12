from Animal_Class import *
class Cow(Animal):
    """Cow Sub Class ."""
    def __init__(self,name):
        #Assume Ideal Cows that is every cow on same care behaves same so initial values are given
        super().__init__(2,3,6,name)
        self._type = "Cow"

    #override animal weight function in cow
    def grow(self,food,water):
        if food >= self._food_need and water>= self._water_need:
            if self._status == "Baby" and water >self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Kid" and water >self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        #increment days growing
        self._days_growing += 1
        #update the status
        self._update_status()

#Main function of sub class this is just for Testing
def main():
    new_cow = Cow("Ramudu")
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())
    manual_grow(new_cow)
    print(new_cow.report())

if __name__ == '__main__':
    main()

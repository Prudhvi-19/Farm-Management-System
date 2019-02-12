from Animal_Class import *
class Sheep(Animal):
    """Sheep Subclass  ."""
    #constructor
    def __init__(self, name):
        #Default Values of sheep to grow
        super().__init__(3,5,5,name)
        self._type = "Sheep"

#Main function for Testing
def main():
    new_sheep = Sheep("Jack")
    print(new_sheep.report())

if __name__ == '__main__':
    main()

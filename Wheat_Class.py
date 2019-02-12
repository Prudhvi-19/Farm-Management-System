from Crop_class import *

class Wheat(Crop):
    """Wheat Crop Class ."""
    def __init__(self):
        #call parent class set default values of wheat
        super().__init__(3,4,7)
        self._type = "Wheat"
def main():
    wheat_crop = Wheat()

if __name__ == '__main__':
    main()

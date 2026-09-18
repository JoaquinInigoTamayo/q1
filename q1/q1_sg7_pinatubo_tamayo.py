class Glassware:
    pass

class Beaker(Glassware):
    def __init__(self, number):
        self.number = number
    def __del__(self):
        print("Beaker", self.number, "is lost")

class Tray:
    def __init__(self):
        print("Tray is created")
        self.beaker1 = Beaker(1)
        print("Beaker 1 is placed on tray")

        self.beaker2 = Beaker(2)
        print("Beaker 2 is placed on tray")

        self.beaker3 = Beaker(3)
        print("Beaker 3 is placed on tray")

        self.beaker4 = Beaker(4)
        print("Beaker 4 is placed on tray")

        self.beaker5 = Beaker(5)
        print("Beaker 5 is placed on tray")
    def __del__(self):
        beaker1 = self.beaker1
        beaker2 = self.beaker2
        beaker3 = self.beaker3
        beaker4 = self.beaker4
        beaker5 = self.beaker5
        del self.beaker1
        del self.beaker2
        del self.beaker3
        del self.beaker4
        del self.beaker5
        print("Tray is gone")
        del beaker1
        del beaker2
        del beaker3
        del beaker4
        del beaker5

tray = Tray()
del tray

class mammal:
    def mammal_info(self):
        print("Mammals can give direct birth ")

class wingedanimal:
    def winged_animal_info(self):
        print("Winged animals can fly")

class bat(mammal, wingedanimal):
    pass

b1 = bat()
b1.mammal_info()  # Inherited from mammal class
b1.winged_animal_info()  # Inherited from wingedanimal class
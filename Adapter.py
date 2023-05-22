class Constructor:
    def construieste(self, tip, locatie):
        pass

class ConstructorAvansat:
    def construieste_casa(self, locatie):
        pass

    def construieste_zgaraie_nor(self, locatie):
        pass

class ConstructorCasa(ConstructorAvansat):
    def construieste_casa(self, locatie):
        print(f"Se construiește o casă în zona {locatie}!")

    def construieste_zgaraie_nor(self, locatie):
        pass

class ConstructorZgaraieNor(ConstructorAvansat):
    def construieste_zgaraie_nor(self, locatie):
        print(f"Se construiește un zgârie-nori în zona {locatie}!")

    def construieste_casa(self, locatie):
        pass

class AdaptatorConstructor(Constructor):
    def __init__(self, tip):
        if tip.lower() == "casa":
            self.constructor_avansat = ConstructorCasa()
        elif tip.lower() == "zgaraienor":
            self.constructor_avansat = ConstructorZgaraieNor()

    def construieste(self, tip, locatie):
        if tip.lower() == "casa":
            self.constructor_avansat.construieste_casa(locatie)
        elif tip.lower() == "zgaraienor":
            self.constructor_avansat.construieste_zgaraie_nor(locatie)

class ImplementareConstructor(Constructor):
    def __init__(self):
        self.adaptator_constructor = None

    def construieste(self, tip, locatie):
        if tip.lower() == "casa" or tip.lower() == "zgaraienor":
            self.adaptator_constructor = AdaptatorConstructor(tip)
            self.adaptator_constructor.construieste(tip, locatie)
        else:
            print(f"Tipul de construcție '{tip}' nu este valid.")

# Utilizare
implementare_constructor = ImplementareConstructor()
implementare_constructor.construieste("casa", "Centru oraș")
implementare_constructor.construieste("zgaraienor", "Centru oraș")
implementare_constructor.construieste("zgaraienor", "Periferie")
implementare_constructor.construieste("hotel", "Centru oraș")

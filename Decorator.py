class Calculator:
    def asambleaza(self):
        pass

class CalculatorDeBaza(Calculator):
    def asambleaza(self):
        print("Asamblarea unui calculator de bază.", end='')

class DecoratorCalculator(Calculator):
    def __init__(self, calculator):
        self.calculator = calculator

    def asambleaza(self):
        self.calculator.asambleaza()

class CalculatorGaming(DecoratorCalculator):
    def asambleaza(self):
        super().asambleaza()
        print(" Adăugarea caracteristicilor unui calculator de gaming! ", end='')

class CalculatorDeLucru(DecoratorCalculator):
    def asambleaza(self):
        super().asambleaza()
        print(" Adăugarea caracteristicilor unui calculator de lucru! ", end='')

# Utilizare
calculator_gaming = CalculatorGaming(CalculatorDeBaza())
calculator_gaming.asambleaza()
print("\n")

calculator_de_lucru = CalculatorDeLucru(CalculatorGaming(CalculatorDeBaza()))
calculator_de_lucru.asambleaza()

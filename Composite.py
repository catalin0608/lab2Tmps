class Angajat:
    def __init__(self, nume, pozitie, salariu):
        self.nume = nume
        self.pozitie = pozitie
        self.salariu = salariu
        self.colegi = []

    def adauga_coleg(self, coleg):
        self.colegi.append(coleg)

    def elimina_coleg(self, coleg):
        self.colegi.remove(coleg)

    def get_colegi(self):
        return self.colegi

    def __str__(self):
        return "Angajat: | Nume: " + self.nume + ", Pozitie: " + self.pozitie + ", Salariu: " + str(self.salariu) + " |"

class StackAbuseJavaDesignPatterns:
    def main(self):
        angajat1 = Angajat("David", "Programator", 1500)
        angajat2 = Angajat("Scott", "CEO", 3000)
        angajat3 = Angajat("Andrew", "Manager", 2000)
        angajat4 = Angajat("Scott", "Intretinitor", 500)
        angajat5 = Angajat("Juliette", "Marketing", 1000)
        angajat6 = Angajat("Rebecca", "Vanzari", 2000)
        angajat7 = Angajat("Chris", "Programator", 1750)
        angajat8 = Angajat("Ivan", "Programator", 1200)

        angajat3.adauga_coleg(angajat1)
        angajat3.adauga_coleg(angajat7)
        angajat3.adauga_coleg(angajat8)

        angajat1.adauga_coleg(angajat7)
        angajat1.adauga_coleg(angajat8)

        angajat2.adauga_coleg(angajat3)
        angajat2.adauga_coleg(angajat5)
        angajat2.adauga_coleg(angajat6)

        print(angajat2)
        for angajat_sef in angajat2.get_colegi():
            print(angajat_sef)

            for angajat in angajat_sef.get_colegi():
                print(angajat)

# Utilizare
aplicatie = StackAbuseJavaDesignPatterns()
aplicatie.main()

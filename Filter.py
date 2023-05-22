class Angajat:
    def __init__(self, nume, sex, pozitie):
        self.nume = nume
        self.sex = sex
        self.pozitie = pozitie

class Criteriu:
    def indeplineste(self, lista_angajati):
        pass

class CriteriuMasculin(Criteriu):
    def indeplineste(self, lista_angajati):
        angajati_masculini = []
        for angajat in lista_angajati:
            if angajat.sex.lower() == "masculin":
                angajati_masculini.append(angajat)
        return angajati_masculini

class CriteriuFeminin(Criteriu):
    def indeplineste(self, lista_angajati):
        angajati_feminini = []
        for angajat in lista_angajati:
            if angajat.sex.lower() == "feminin":
                angajati_feminini.append(angajat)
        return angajati_feminini

class CriteriuSenior(Criteriu):
    def indeplineste(self, lista_angajati):
        angajati_seniori = []
        for angajat in lista_angajati:
            if angajat.pozitie.lower() == "senior":
                angajati_seniori.append(angajat)
        return angajati_seniori

class CriteriuJunior(Criteriu):
    def indeplineste(self, lista_angajati):
        angajati_juniori = []
        for angajat in lista_angajati:
            if angajat.pozitie.lower() == "junior":
                angajati_juniori.append(angajat)
        return angajati_juniori

class CriteriuSi(Criteriu):
    def __init__(self, primul_criteriu, al_doilea_criteriu):
        self.primul_criteriu = primul_criteriu
        self.al_doilea_criteriu = al_doilea_criteriu

    def indeplineste(self, lista_angajati):
        angajati_primul_criteriu = self.primul_criteriu.indeplineste(lista_angajati)
        return self.al_doilea_criteriu.indeplineste(angajati_primul_criteriu)

class CriteriuSau(Criteriu):
    def __init__(self, primul_criteriu, al_doilea_criteriu):
        self.primul_criteriu = primul_criteriu
        self.al_doilea_criteriu = al_doilea_criteriu

    def indeplineste(self, lista_angajati):
        angajati_primul_criteriu = self.primul_criteriu.indeplineste(lista_angajati)
        angajati_al_doilea_criteriu = self.al_doilea_criteriu.indeplineste(lista_angajati)

        for angajat in angajati_al_doilea_criteriu:
            if angajat not in angajati_primul_criteriu:
                angajati_primul_criteriu.append(angajat)

        return angajati_primul_criteriu

angajati = [
    Angajat("David", "masculin", "senior"),
    Angajat("Scott", "masculin", "senior"),
    Angajat("Rhett", "masculin", "junior"),
    Angajat("Andrew", "masculin", "junior"),
    Angajat("Susan", "feminin", "senior"),
    Angajat("Rebecca", "feminin", "junior"),
    Angajat("Mary", "feminin", "junior"),
    Angajat("Juliette", "feminin", "senior"),
    Angajat("Jessica", "feminin", "junior"),
    Angajat("Mike", "masculin", "junior"),
    Angajat("Chris", "masculin", "junior")
]

criteriu_masculin = CriteriuMasculin()
criteriu_feminin = CriteriuFeminin()
criteriu_senior = CriteriuSenior()
criteriu_junior = CriteriuJunior()
criteriu_senior_feminin = CriteriuSi(criteriu_senior, criteriu_feminin)
criteriu_junior_sau_masculin = CriteriuSau(criteriu_junior, criteriu_masculin)

print("Angajații de sex masculin:")
for angajat in criteriu_masculin.indeplineste(angajati):
    print(f"Nume: {angajat.nume}, Sex: {angajat.sex}, Poziție: {angajat.pozitie}")

print("\nAngajații de sex feminin:")
for angajat in criteriu_feminin.indeplineste(angajati):
    print(f"Nume: {angajat.nume}, Sex: {angajat.sex}, Poziție: {angajat.pozitie}")

print("\nAngajații de sex feminin și poziție senior:")
for angajat in criteriu_senior_feminin.indeplineste(angajati):
    print(f"Nume: {angajat.nume}, Sex: {angajat.sex}, Poziție: {angajat.pozitie}")

print("\nAngajații de sex masculin sau poziție junior:")
for angajat in criteriu_junior_sau_masculin.indeplineste(angajati):
    print(f"Nume: {angajat.nume}, Sex: {angajat.sex}, Poziție: {angajat.pozitie}")

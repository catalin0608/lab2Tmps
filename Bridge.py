class APIHranire:
    def hraneste(self, de_cate_ori_pe_zi, cantitate, tip_hrana):
        pass

class CaineMare(APIHranire):
    def hraneste(self, de_cate_ori_pe_zi, cantitate, tip_hrana):
        print("Hranire câine mare, de " + str(de_cate_ori_pe_zi) + " ori pe zi, cu " +
              str(cantitate) + " g de " + tip_hrana)

class CaineMic(APIHranire):
    def hraneste(self, de_cate_ori_pe_zi, cantitate, tip_hrana):
        print("Hranire câine mic, de " + str(de_cate_ori_pe_zi) + " ori pe zi, cu " +
              str(cantitate) + " g de " + tip_hrana)

class Animal:
    def __init__(self, api_hranire):
        self.api_hranire = api_hranire

    def hraneste(self):
        pass

class Caine(Animal):
    def __init__(self, de_cate_ori_pe_zi, cantitate, tip_hrana, api_hranire):
        super().__init__(api_hranire)
        self.de_cate_ori_pe_zi = de_cate_ori_pe_zi
        self.cantitate = cantitate
        self.tip_hrana = tip_hrana

    def hraneste(self):
        self.api_hranire.hraneste(self.de_cate_ori_pe_zi, self.cantitate, self.tip_hrana)

# Utilizare
caine_mare = Caine(3, 500, "Carne", CaineMare())
caine_mic = Caine(2, 250, "Granule", CaineMic())

caine_mare.hraneste()
caine_mic.hraneste()

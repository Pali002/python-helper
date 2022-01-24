from dolgozo import Dolgozo

class Juta:
    def __init__(self):
        self.file_name = "dolgozok.txt"
    def file_read(self):
        fp = open(self.file_name, "r", encoding="utf-8")
        self.lines = fp.readlines()
        fp.close()
    
    def convert_content(self):
        self.dolgozok = []
        for line in self.lines:
            (az, nev, anyjaneve, telepules, cim, fizetes,
            jutalom, belepes, szuletes, szulhely) = line.split(";")

            dolgozo = Dolgozo(az, nev, anyjaneve, telepules, cim, int(fizetes), int(jutalom), belepes, szuletes, szulhely)
            self.dolgozok.append(dolgozo)

    def jutalmak_osszeg(self):
        osszeg = 0
        for dolgozo in self.dolgozok:
            osszeg = osszeg + dolgozo.jutalom
        print("Jutalmak osszege:", osszeg)
    def fizetesek_osszege(self):
        fizetes = 0
        for dolgozo in self.dolgozok:
           fizetes = fizetes + dolgozo.fizetes
        print("Fizetések osszege:", fizetes)

juta = Juta()
juta.file_read()
juta.convert_content()
juta.jutalmak_osszeg()
juta.fizetesek_osszege()

#crop.py
#Zentai Pál, 2022.01.21, Szoft-I-N
from typing import List
from cropModel import CropModel

class Crop:
    def __init__(self):
        self.file_name = 'termes.txt'
        self.crops: List[CropModel] = []

    def read_content(self):
        fp = open(self.file_name, 'r', encoding='utf-8')
        self.lines = fp.readlines() 
        fp.close()
    
    def convert_content(self):        
        for line in self.lines[1:]:
            (id, name, place, size, cropyield, year) = line.split(':')
            cropModel = CropModel(
                id, 
                name, 
                place, 
                int(size),
                float(cropyield.replace(",", ".")), 
                int(year)
                )
            self.crops.append(cropModel)

    # Földterület összesen
    def total_land(self):
        osszeg = 0
        for crop in self.crops:
            osszeg += crop.size
        print("Földterület összesen:", osszeg, "hektár")

    # Hány tonna búza termés volt összesen?
    def sum_wheat(self):
        osszeg = 0
        for crop in self.crops:
            if crop.name == "búza":
                osszeg += crop.cropyield
            print("Összesen:", osszeg, "tonna")

    # 300-nál több termés esetén név és termés legyen kiírtva
    def more_then_three_hundred(self):
        sep = "----------------------------"
        print(sep)
        print("300-nál több termés:")
        for crop in self.crops:
            if crop.cropyield > 300:
                print(crop.name, crop.cropyield)
        print(sep)

    # Hány területen termelnek árpát?
    def area_barley(self):
        darab = 0
        for crop in self.crops:
            if crop.name == "árpa":
                darab += 1
        print(darab, "területen termelnek árpát")

    # Hány terület nagyobb mint 80 hektár?
    def area_larger_eighty(self):
        hektar = 0
        for crop in self.crops:
            if crop.size > 80:
                hektar += 1
        print(hektar, "területen nagyobb mint 80 tonna")

    # Milyen gabona termett a "Csendes" nevű területen?
    def which_crop_on_csendes(self):
        for crop in self.crops:
            if crop.place == "Csendes":
                print("A Csendes területen termelt gabona:",crop.name)
    
    # Melyik területről lett a legkevesebb búzatermés?
    def which_place_wheat_min(self):
        min_crop = self.crops[0]
        for crop in self.crops:
            if crop.cropyield < min_crop.cropyield:
                min_crop = crop
        print("Legkevesebb búza termés innen:", min_crop.place)

crop = Crop()
crop.read_content()
crop.convert_content()
crop.total_land()
crop.sum_wheat()
crop.more_then_three_hundred()
crop.area_barley()
crop.area_larger_eighty()
crop.which_crop_on_csendes()
crop.which_place_wheat_min()
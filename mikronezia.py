########################################
#
# Zentai Pál
# 2022-01-12
# Szoft I N
#
########################################


from country import Country

class Mikronezia:
    def __init__(self):
        self.countries = []
        self.sep = ':'
        
    def read_content(self):
        file_name = 'countries.txt'
        fp = open(file_name, 'r', encoding="utf-8")
        self.lines = fp.readlines()
        fp.close()

    def convert_content(self):
        for line in self.lines[1::]:            
            (id, name, area, population) = line.split('#')
            country = Country(id, name, int(area), int(population))
            self.countries.append(country)

    # Legnépesebb ország
    def most_populated(self):
        max_country = self.countries[0]
        for country in self.countries[1:]:
            if country.population > max_country.population:
                max_country = country
        print("Legnépesebb ország:", max_country.name,
            max_country.population)

    # Legkisebb területű ország
    def smallest_area(self):
        min_country = self.countries[0]
        for country in self.countries[1:]:
            if country.area < min_country.area:
                min_country = country
        print("Legkisebbb területű ország adatai:",
        min_country.id,
        min_country.name,
        min_country.area,
        min_country.population)

    # 99 ezernél kisebb népesség
    def less_than_ninety_nine_thousand(self):
        print("99000-nél kisebb népességű országok:")
        for country in self.countries:
            if country.population < 99000:
                print(country.name,
                country.population)

    # Hány 500 négyeztkilométernél nagyobb területi ország van?
    def more_than_five_hunderd_area(self):
        darab = 0
        for country in self.countries:
            if country.area > 500:
                darab += 1
        print("500km2-nél nagyobb országok:", darab)

    # Hány ország nevében szerepel a "sziget" szó?
    def island_word_in_name(self):
        darab = 0
        for country in self.countries:
            if "sziget" in country.name:
                darab += 1
        print("A sziget szerepel:", darab, "darab")

    # Az országok területe összesen
    def sum_areas(self):
        osszeg = 0
        for country in self.countries:
            osszeg += country.area
        print("Össz terület:", osszeg, "km^2")

    # Az országok népességének átlaga
    def population_average(self):
        darab = len(self.countries)
        osszeg = 0
        for country in self.countries:
            osszeg = osszeg + country.population
        atlag = osszeg / darab
        print("Népeség átlag: %.2f" % atlag)

    # Állapítsuk meg, hogy egyszavas, vagy nem, a név
    def is_one_word(self, country):
        if "-" in country.name:
            return False
        else:
            return True
        

    def write_a_country(self, fp, country):
        fp.write(country.id)
        fp.write(self.sep)
        fp.write(country.name)
        fp.write(self.sep)
        fp.write(str(country.area))
        fp.write(self.sep)
        fp.write(str(country.population))
        fp.write('\n')


    def write_one_word(self):
        fp = open('oneword.txt', 'w')
        for country in self.countries:
            if self.is_one_word(country):
                self.write_a_country(fp, country)
        fp.close()

#mikronezia osztály vége

mikro = Mikronezia()
mikro.read_content()
mikro.convert_content()
mikro.most_populated()
mikro.smallest_area()
mikro.less_than_ninety_nine_thousand()
mikro.more_than_five_hunderd_area()
mikro.island_word_in_name()
mikro.sum_areas()
mikro.population_average()
mikro.write_one_word()

#res = mikro.is_one_word(mikro.countries[1])
#print("res:", res)
class City:
    def __init__(self, cityname, regionname, countryname, numberofcitiziens, zipcode, areacode):
        self.cityname = cityname
        self.regionname = regionname
        self.countryname = countryname
        self.numberofcitiziens = numberofcitiziens
        self.zipcode = zipcode
        self.areacode = areacode

    def getfulladress(self):
        print(f"Názov mesta je: {self.cityname}, nachadza sa v  kraji: {self.regionname}, v state: {self.countryname}, ma {self.numberofcitiziens} obyvatelov. Postove smerove cilso je {self.zipcode} a area code je {self.areacode}")

bratislava = City("Bratislava","Bratislavsky","Slovakia",500000,82105,50)
bratislava.getfulladress()
Humenne = City("Humenne","Presovsky","Slovakia",35000,"06601,5)
Humenne.getfulladress()
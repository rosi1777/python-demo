class Animal:

    def __init__(self, nama, jenis, umur):
        self.__name = nama
        self.__type = jenis
        self.__age = umur

    @property
    def setname(self):
        pass

    @property
    def getname(self):
        pass

    @property
    def settype(self):
        pass

    @property
    def gettype(self):
        pass

    @property
    def setage(self):
        pass

    @property
    def getage(self):
        pass

    @setname.setter
    def setname(self, value):
        self.__name = value

    @getname.getter
    def getname(self):
        return self.__name
    
    @settype.setter
    def settype(self, value):
        self.__type = value

    @gettype.getter
    def gettype(self):
        return self.__type

    @setage.setter
    def setage(self, value):
        self.__age = value

    @getage.getter
    def getage(self):
        return self.__age


class Cat(Animal):

    def __init__(self, nama, jenis, umur, warnabulu):
        super().__init__(nama, jenis, umur)
        self.__furcolor = warnabulu

    @property
    def setfurcolor(self):
        pass

    @property
    def getfurcolor(self):
        pass

    @setfurcolor.setter
    def setfurcolor(self, value):
        self.__furcolor = value

    @getfurcolor.getter
    def getfurcolor(self):
        return self.__furcolor

    def walk(self):
        return self.getname + " is walking"

    def sleep(self):
        return self.getname + " is sleeping"

cat1 = Cat("Simba", "Aggora", 2, "Black")

#print(cat1.__dict__)
#print("==============================")
#cat1.setname = input("Masukkan nama untuk diperbarui = ")
#cat1.settype = input("Masukkan jenis untuk diperbarui = ")
#cat1.setage = int(input("Masukkan umur untuk diperbarui = "))
#cat1.setfurcolor = input("Masukkan warna bulu untuk diperbarui = ")
#print("==============================")
#print(cat1.__dict__)
#print(cat1.walk())
print(cat1.getname)
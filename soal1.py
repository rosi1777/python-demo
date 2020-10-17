class Tabung:

    counter = 0
    phi = 3.14

    def __init__(self, jariJari, tinggi):
        self.r = jariJari
        self.t = tinggi

        Tabung.counter += 1

    def volume(self):
        vol = self.phi * self.r * self.r * self.t
        return vol

    def luasPermukaan(self):
        lp = 2 * self.phi * self.r * (self.r + self.t)
        return lp

    def luasSelimut(self):
        ls = 2 * self.phi * self.r * self.t
        return ls


tabung1 = Tabung(7, 17)
tabung2 = Tabung(2, 7)
print("volume = ", tabung1.luasPermukaan())
print("Jumlah objek yang dibuat :", Tabung.counter)

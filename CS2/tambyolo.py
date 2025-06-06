class Ticket:
    def __init__(self, Name = "", City = "", SukingTindahan = ""):
        self.Name = Name
        self.City = City
        self.SukingTindahan = SukingTindahan
    
    def __str__(self):
        return "{0} from {1}".format(self.Name, self.City)
    
    def __repr__(self):
        return "{0} from {1}".format(self.Name, self.City)
    
class Tambyolo:
    def __init__(self):
        self.container = []
    
    def add(self, t):
        if type(t) == Ticket:
            self.container.append(t)
        else:
            raise TypeError from self
    
    def __str__(self):
        return "Number of tickets: {0}".format(len(self.container))

    def draw(self):
        try:
            ticket = self.container.pop()
        except IndexError:
            ticket = None
        return ticket
    
A = Ticket("Juan Dela Cruz", "Manila", "Aling Nena's Tindahan")
B = Ticket("Paulina Bauntista", "San Ildefonso", "Manang Biday's Corner Store")
C = Ticket("Esteban Cargador", "Argao", "ABC Sari-Sari Store")
D = Ticket("Silka al-Falani", "Iligan City", "7-11")

Box = Tambyolo()
Box.add(A)
Box.add(B)
Box.add(C)
Box.add(D)
print(str(Box))
print(Box.draw())
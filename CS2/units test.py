class unitMeter:
    # Allow to specify quantity in the unit of the class, or specify it in meters
    def __init__(self, value = 0.0, fromMeters = None):
        self.conversionFactor = 1.0     # conversion rate to and from meters
        self.displayName = "m"          # what unit to display when printed out
        
        if fromMeters is not None:
            self.innerValue = fromMeters
        else:
            self.innerValue = value
    
    # Display the quantity and units
    def __str__(self):
        return "{0} {1}".format(self.innerValue * self.conversionFactor, self.displayName)
    
    # Handle adding two units together
    def __add__(self, other):
        return unitMeter((self.inMeters + other.inMeters) * self.conversionFactor)
    
    # Handle subtracting two units from each other
    def __sub__(self, other):
        return unitMeter((self.inMeters - other.inMeters) * self.conversionFactor)
    
    # Preferred way to retrieve the inner properties of a class
    @property
    def inMeters(self):
        return self.innerValue
    
    # Preferred way to set the inner properties of a clas
    @inMeters.setter
    def inMeters(self, value):
        self.innerValue = value
    
    @property
    def value(self):
        return self.innerValue * self.conversionFactor

    @value.setter
    def value(self, newValue):
        self.innerValue = newValue / self.conversionFactor

class unitMillimeter(unitMeter):
    def __init__(self, value=0, fromMeters=None):
        super().__init__(value / 1000, fromMeters)
        self.displayName = "mm"
        self.conversionFactor = 1000

    # Handle adding two units together
    def __add__(self, other):
        return unitMillimeter((self.inMeters + other.inMeters) * self.conversionFactor)
    
    # Handle subtracting two units from each other
    def __sub__(self, other):
        return unitMillimeter((self.inMeters - other.inMeters) * self.conversionFactor)

L1 = unitMeter(1.0)
L2 = unitMillimeter(1500.0)
print(L1)
print(L2)
print(L2+L1)
# Implementing classes

# Class definition
class Smartphone:

    # Constructor
    def __init__(self, name, model, vendor, year):
        # Attributes
        self.name = name
        self.model = model
        self.vendor = vendor
        self.year = year
    
    # Methods
    def call(self):
        return f"Making a call"
    def connect_internet(self):
        print("Browsing the internet")

# Inheritance
class Tablet(Smartphone):
    # constructor
    def __init__(self, name, model, vendor, year, size):
        super().__init__(name, model, vendor, year)
        self.size = size

# Instanciation of the class
phone = Smartphone("Iphone16", "oir349", "Apple", 2025)
print(phone.name, phone.vendor, phone.year)

tablet1 = Tablet("ipad", "oqwie933", "Apple", 2014, 10)
print(tablet1.name, tablet1.vendor, tablet1.year, tablet1.size)
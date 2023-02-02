class Length :
    def __init__(self) :
        self.feet = 0
        self.inches = 0

    def SetLength(self) :
        self.feet = int(input("Enter feet : "))
        self.inches = int(input("Enter inches : "))

    def getLength(self) :
        return (self.feet, self.inches)

    def __len__(self) :
        return (self.feet + (self.inches / 12))
    
    def __add__(self, other) :
        a = self.feet + other.feet
        b = self.inches + other.inches

        return (a, b)

L1 = Length()
L2 = Length()
L3 = Length()

L1.SetLength()
print("L1 data : ", L1.getLength())
L2.SetLength()

a = L1 + L2
print(tuple(a))
class arithmetic:
    def Add(self, m, n):
        c = m + n
        return c
    def Sub(self, m, n):
        c = m - n
        return c

x = int(input('no 1 : '))
y = int(input('no 2 : '))

ob = arithmetic()

a = ob.Add(x, y)
b = ob.Sub(x, y)

print(f"sum : {a}, diff = {b}")
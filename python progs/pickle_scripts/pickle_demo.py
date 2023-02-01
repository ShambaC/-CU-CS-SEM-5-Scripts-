import pickle

dic1 = {'A' : 1, 'B' : 2}
print(f"Original dictionary : {dic1}")

# String pickling
# Pickling
Str1 = pickle.dumps(dic1)
print(f"Pickled String : {Str1}")

# Unpickling
dic = pickle.loads(Str1)
print(f"Unpickled data : {dic}")

# Reseting
dic = None

# File pickling
# Pickling
with open('dumped', 'wb') as wf :
    pickle.dump(dic1, wf)

# Unpickling
with open('dumped', 'rb') as rf :
    dic = pickle.load(rf)
    print(f"\nUnpickled data from file : {dic}")

# Class object pickling
# Class definition
class User() :
    def __init__(self, Name, Id) :
        self.Name = Name
        self.Id = Id

    def __str__(self) :
        return(f"Name : {self.Name}, ID : {self.Id}")

# Class object
U1 = User("ABC", 123)

# Pickling
with open('ClassPickle', 'wb') as wf:
    pickle.Pickler(wf).dump(U1)

# Unpickling
with open('ClassPickle', 'rb') as rf :
    U2 = pickle.Unpickler(rf).load()
    print(f"\nUnpickled class obj : {U2}")
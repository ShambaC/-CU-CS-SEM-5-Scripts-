class A:
    def display(self):
        print("This is class A")
        
class B(A):
    def display(self):
        print("This is class B")

class C(A):
    def display(self):
        print("This is class c")

    def call_parent(self) :
        super().display()
    
    b=B()
    b.display()

c = C()
c.call_parent()
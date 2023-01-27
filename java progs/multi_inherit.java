interface A
{
    void display();
}

interface B
{
    void meow();
}

class C implements A, B
{
    public void display()
    {
        System.out.println("Display");
    }

    public void meow()
    {
        System.out.println("Meow");
    }
}

public class multi_inherit
{
    public static void main(String args[])
    {
        A ob1 = new C();
        B ob2 = new C();
        C ob3 = new C();

        ob1.display();
        ob2.meow();

        ob3.display();
        ob3.meow();
    }
}

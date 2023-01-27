class DemoClass
{
    static int a = 4;
    static int b;

    static
    {
        b = 69;
    }

    static float f = 1.4f;

    static void meth()
    {
        System.out.println("Static method !");
    }

    static void meth(int i)
    {
        System.out.println("num : " + i);
    }
}

class Demo2 extends DemoClass
{
    static int a = 5;

    static void meth()
    {
        System.out.println("Static method in demo2");
    }
}

public class StaticDemo extends DemoClass
{
    public static void main(String args[])
    {
        System.out.println(a);
        System.out.println(Demo2.a);
        System.out.println(b);

        meth();
        meth(69);

        Demo2.meth();
        Demo2 ob = new Demo2();
        ob.meth();
    }   
}

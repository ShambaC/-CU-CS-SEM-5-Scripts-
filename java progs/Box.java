import java.util.*;

public class Box
{
    float length, breadth, height;

    Box(float length, float breadth, float height)
    {
        this.length = length;
        this.breadth = breadth;
        this.height = height;
    }

    Box(Box B)
    {
        this.length = B.length;
        this.breadth = B.breadth;
        this.height = B.height;
    }

    float Volume()
    {
        return length * breadth * height;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        float l, b, h;

        System.out.print("Enter the length : ");
        l = sc.nextFloat();
        System.out.print("Enter the breadth : ");
        b = sc.nextFloat();
        System.out.print("Enter the height : ");
        h = sc.nextFloat();

        Box box = new Box(l, b, h);
        Box ob = new Box(box);

        sc.close();

        float vol = ob.Volume();

        System.out.println("Volume of the box is : " + vol);
    }
}

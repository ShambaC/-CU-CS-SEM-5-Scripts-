import java.util.*;

class Square
{
    double side;

    Square()
    {

    }

    Square(double side)
    {
        this.side = side;
    }

    double getVolume()
    {
        double vol = this.side * this.side * this.side;
        return vol;
    }
}

class Cylinder extends Square
{
    double height;

    Cylinder()
    {

    }

    Cylinder(double r, double h)
    {
        super.side = r;
        this.height = h;
    }

    double getVolume()
    {
        double vol = 3.14 * super.side * super.side * this.height;
        return vol;
    }
}

public class shapes
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        double radius, height, side;

        System.out.print("Enter the side of Cube : ");
        side = sc.nextDouble();

        System.out.print("Enter the radius of Cylinder : ");
        radius = sc.nextDouble();
        System.out.print("Enter the height of Cylinder : ");
        height = sc.nextDouble();

        Square S = new Square(side);
        Cylinder C = new Cylinder(radius, height);
        
        sc.close();

        System.out.println("Volume of Cube : " + S.getVolume());
        System.out.println("Volume of Cylinder : " + C.getVolume());
    }
}

import my_pack.MyPoint;

class MyTriangle
{
    MyPoint v1, v2, v3;

    MyTriangle(int x1, int y1, int x2, int y2, int x3, int y3)
    {
        v1 = new MyPoint(x1, y1);
        v2 = new MyPoint(x2, y2);
        v3 = new MyPoint(x3, y3);
    }

    MyTriangle(MyPoint P1, MyPoint P2, MyPoint P3)
    {
        v1 = new MyPoint(P1.x, P1.y);
        v2 = new MyPoint(P2.x, P2.y);
        v3 = new MyPoint(P3.x, P3.y);
    }

    public String toString()
    {
        return("MyTriangle [ v1 = (" + v1.x + ", " + v1.y + "), v2 = (" + v2.x + ", " + v2.y + "), v3 = (" + v3.x + ", " + v3.y + ")]");
    }

    public double Perimeter()
    {
        double dis1 = v1.distance(v2);
        double dis2 = v1.distance(v3);
        double dis3 = v2.distance(v3);

        return dis1 + dis2 + dis3;
    }

    public void printType()
    {
        double dis1 = v1.distance(v2);
        double dis2 = v1.distance(v3);
        double dis3 = v2.distance(v3);

        if(dis1 == dis2 && dis2 == dis3)
        {
            System.out.println("The triangle is equilateral");
        }
        else if(dis1 == dis2 || dis2 == dis3 || dis1 == dis3)
        {
            System.out.println("The triangle is isosceles");
        }
        else
        {
            System.out.println("The triangle is scalene");
        }
    }
}

public class TriangleDriver
{
    public static void main(String args[])
    {
        MyTriangle T1 = new MyTriangle(2, 3, 1, 2, 3, 1);
        System.out.println(T1);

        System.out.println("Perimeter : " + T1.Perimeter());
        T1.printType();
    }
}

class MyPoint
{
    int x, y;

    MyPoint()
    {
        x = y = 0;
    }

    MyPoint(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public void setXY(int x, int y)
    {
        this.x = x;
        this.y = y;
    }

    public int[] getXY()
    {
        int[] a = new int[] {this.x, this.y};
        return a;
    }

    public String toString()
    {
        String s = "(" + this.x + ", " + this.y + ")";
        return s;
    }

    public double distance(int x, int y)
    {
        double dis = Math.sqrt(Math.pow((this.x - x), 2) + Math.pow((this.y - y), 2));
        return dis;
    }
}

public class PointDriver
{
    public static void main(String args[])
    {
        MyPoint M1 = new MyPoint();
        MyPoint M2 = new MyPoint(3, 5);

        int points1[] = new int[2];
        points1 = M1.getXY();
        System.out.println("Points of M1 : (" + points1[0] + ", " + points1[1] + ")");

        System.out.println("Points of M2 : " + M2);

        System.out.println("Setting points of M1 to (1, 2)");
        M1.setXY(1, 2);
        System.out.println("New points of M1 : " + M1);

        double dis = M2.distance(1, 2);
        System.out.println("Distance of M2 from (1, 2) is : " + dis);
    }
}
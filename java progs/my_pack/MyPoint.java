package my_pack;

public class MyPoint
{
    public int x, y;

    public MyPoint()
    {
        x = y = 0;
    }

    public MyPoint(int x, int y)
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

    public double distance()
    {
        double dis = Math.sqrt((x*x) + (y*y));
        return dis;
    }

    public double distance(int x, int y)
    {
        double dis = Math.sqrt(Math.pow((this.x - x), 2) + Math.pow((this.y - y), 2));
        return dis;
    }

    public double distance(MyPoint P)
    {
        int points[] = P.getXY();
        int PointX = points[0];
        int PointY = points[1];

        double dis = Math.sqrt(Math.pow((this.x - PointX), 2) + Math.pow((this.y - PointY), 2));
        return dis;
    }
}

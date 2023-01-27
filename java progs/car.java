import java.util.*;

interface engine
{
    void SpeedUp(int val);
    void ChangeGear(int val);
}

class vehicle implements engine
{
    int speed, gear;

    vehicle(int speed, int gear)
    {
        this.speed = speed;
        this.gear = gear;
    }

    public void SpeedUp(int val)
    {
        System.out.println("Original Speed : " + this.speed);
        this.speed += val;
        System.out.println("Changed Speed : " + this.speed);
    }

    public void ChangeGear(int val)
    {
        System.out.println("Original Gear : " + this.gear);
        this.gear = val;
        System.out.println("Current gear : " + this.gear);
    }
}

public class car
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int speed, gear;
        System.out.print("Enter the speed : ");
        speed = sc.nextInt();
        System.out.print("Enter the gear : ");
        gear = sc.nextInt();

        engine E = new vehicle(speed, gear);
        int speedup, gearchange;
        System.out.print("Enter the speed up : ");
        speedup = sc.nextInt();
        System.out.print("Enter the changed gear : ");
        gearchange = sc.nextInt();

        E.SpeedUp(speedup);
        E.ChangeGear(gearchange);

        sc.close();
    }
}

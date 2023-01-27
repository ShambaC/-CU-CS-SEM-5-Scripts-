import java.util.*;

abstract class Employee
{
    abstract void salary();
    abstract void display();
}

class manager extends Employee
{
    float basic, HRA, DA, Net;

    manager(float basic)
    {
        this.basic = basic;
    }

    void salary()
    {
        HRA = basic * 10 / 100;
        DA = basic * 73 / 100;
        Net = basic + HRA + DA;
    }

    void display()
    {
        System.out.println("Net salary is : " + Net);
    }
}

class clerk extends Employee
{
    float basic, HRA, DA, Net;

    clerk(float basic)
    {
        this.basic = basic;
    }

    void salary()
    {
        HRA = basic * 10 / 100;
        DA = basic * 73 / 100;
        Net = basic + HRA + DA;
    }

    void display()
    {
        System.out.println("Net salary is : " + Net);
    }
}

public class abstract_run
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the basic salary for manager : ");
        float base = sc.nextFloat();

        Employee E1 = new manager(base);
        E1.salary();
        E1.display();

        System.out.print("Enter the basic salary for clerk : ");
        base = sc.nextFloat();

        Employee E2 = new clerk(base);
        E2.salary();
        E2.display();

        sc.close();
    }
}

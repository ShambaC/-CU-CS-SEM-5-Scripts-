import java.util.*;

public class Employee
{
    double PF, Salary, Base;

    Employee()
    {
        
    }

    Employee(double Base)
    {
        this.Base = Base;
    }

    Employee(Employee E)
    {
        this.Base = E.Base;
    }

    Employee Calculate()
    {
        PF = Base * 0.12;
        Salary = Base + PF;

        Employee E = new Employee();
        E.PF = PF;
        E.Base = this.Base;
        E.Salary = Salary;

        return E;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the base salary : ");
        double base = sc.nextDouble();

        Employee E1 = new Employee(base);
        Employee E2 = new Employee(E1);
        sc.close();

        E2 = E2.Calculate();
        System.out.println("Salary : " + E2.Salary);
    }
}

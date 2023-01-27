import java.util.*;

class Person
{
    Scanner sc = new Scanner(System.in);
    String name, address;

    Person()
    {

    }

    void setPerson()
    {
        String n, add;
        System.out.print("Enter the name : ");
        n = sc.nextLine();
        System.out.print("Enter the address : ");
        add = sc.nextLine();


        this.name = n;
        this.address = add;
    }

    void tostring()
    {
        System.out.println("Person [ Name = " + this.name + " , Address : " + this.address);
    }
}

class Student extends Person
{
    String program, year;
    double fees;

    Student()
    {

    }

    void setStudent()
    {
        super.setPerson();

        String p, y;
        double f;
        System.out.print("Enter the program : ");
        p = sc.nextLine();
        System.out.print("Enter the year : ");
        y = sc.nextLine();
        System.out.print("Enter the fees : ");
        f = sc.nextDouble();

        sc.nextLine();

        this.program = p;
        this.year = y;
        this.fees = f;
    }

    void tostring()
    {
        System.out.println("Person [ Name = " + super.name + ", Address : " + super.address + ", Program : " + this.program + ", Year : " + this.year + ", Fees : " + this.fees);
    }
}

class Staff extends Person
{
    String School;
    double Pay;

    Staff()
    {

    }

    void setStaff()
    {
        super.setPerson();

        String s;
        double p;

        System.out.print("Enter the school : ");
        s = sc.nextLine();
        System.out.print("Enter the pay : ");
        p = sc.nextDouble();

        sc.nextLine();

        this.School = s;
        this.Pay = p;
    }

    void tostring()
    {
        System.out.println("Person [ Name = " + super.name + ", Address : " + super.address + ", School : " + this.School + ", Pay : " + this.Pay );
    }
}


public class Inherit
{
    public static void main(String args[])
    {
        Person P = new Person();
        Student S = new Student();
        Staff St = new Staff();

        System.out.println("---PERSON CLASS---");
        P.setPerson();
        P.tostring();

        System.out.println("---STUDENT CLASS---");
        S.setStudent();
        S.tostring();

        System.out.println("---STAFF CLASS---");
        St.setStaff();
        St.tostring();
    }
}
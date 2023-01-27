import java.util.*;

public class Student
{
    String name, dept;
    int roll;

    Student(String name, String dept, int roll)
    {
        this.name = name;
        this.dept = dept;
        this.roll = roll;
    }

    boolean isEqual(Student S1, Student S2)
    {
        // if(this.name.equals(S.name) && this.dept.equals(S.dept) && this.roll == S.roll)
        // {
        //     return true;
        // }

        // return false;

        return S1.name.equals(S2.name) && S1.dept.equals(S2.dept) && S1.roll == S2.roll;
    }

    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter details for first student :");
        System.out.print("Enter name : ");
        String n = sc.nextLine();
        System.out.print("Enter department : ");
        String d = sc.nextLine();
        System.out.print("Enter roll : ");
        int r = sc.nextInt();

        //To take the carriage return input and avoid skipping the next input
        sc.nextLine();

        Student S1 = new Student(n, d, r);

        System.out.println("Enter details for second student :");
        System.out.print("Enter name : ");
        n = sc.nextLine();
        System.out.print("Enter department : ");
        d = sc.nextLine();
        System.out.print("Enter roll : ");
        r = sc.nextInt();

        Student S2 = new Student(n, d, r);

        sc.close();

        System.out.println("Checking if the two entries are equal !");
        boolean check = S1.isEqual(S1, S2);
        if(check)
        {
            System.out.println("The two entries are equal !");
        }
        else
        {
            System.out.println("The two entries are not equal !");
        }
    }
}

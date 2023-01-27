import java.util.*;

public class Register
{
    int cap, top;
    String stud[] = new String[100];   
    
    Register(int max)
    {
        cap = max;
        top = -1;
    }

    void Push(String n)
    {
        if (top == cap - 1)
        {
            System.out.println("OVERFLOW");
            return;
        }

        stud[++top] = n;
        System.out.println(stud[top] + " Added");
    }

    void Pop()
    {
        if(top == -1)
        {
            System.out.println("$$");
            return;
        }

        System.out.println(stud[top--] + " Removed");
    }

    void Display()
    {
        if(top == -1)
        {
            System.out.println("No data");
            return;
        }

        System.out.println("Displaying the data : ");
        for(int i = top; i >= 0; i--)
        {
            System.out.println(stud[i]);
        }
    }

    public static void main(String args[])
    {
        int count;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the number of names you want to add [max 100] : ");
        count = sc.nextInt();
        Register Rr = new Register(count);

        while(true)
        {
            System.out.println("Choose operation : \n1. Push\n2. Pop\n3. Display\n4. Exit");
            System.out.print("Enter your choice : ");
            int ch = sc.nextInt();
            sc.nextLine();

            switch(ch)
            {
                case 1:
                    String str;
                    System.out.print("Enter the name : ");
                    str = sc.nextLine();
                    Rr.Push(str);
                    break;
                case 2:
                    Rr.Pop();
                    break;
                case 3:
                    Rr.Display();
                    break;
                case 4:
                    sc.close();
                    System.exit(0);
                    break;
                default:
                    System.out.println("Wrong choice !");
            }
        }
    }
}

import java.util.*;

public class StringRegion
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String s1, s2;

        System.out.print("Enter the first string : ");
        s1 = sc.nextLine();
        System.out.print("Enter the second string : ");
        s2 = sc.nextLine();

        int start1, num, start2;
        System.out.print("Enter the starting index for first string to check : ");
        start1 = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter the starting index for second string to check : ");
        start2 = sc.nextInt();
        sc.nextLine();
        System.out.print("Enter the number of characters to check : ");
        num = sc.nextInt();

        boolean res = s1.regionMatches(false, start1, s2, start2, num);

        if(res)
        {
            System.out.print("Region matches !");
        }
        else
        {
            System.out.print("Regions dont match !");
        }

        sc.close();
    }
}

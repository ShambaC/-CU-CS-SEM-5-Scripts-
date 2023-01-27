import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class string_perm
{
    static Scanner sc = new Scanner(System.in);

    public static void showPerm(String str1, String newStringtoPrint)
    {
        if(newStringtoPrint.length() == str1.length())
        {
            System.out.println(newStringtoPrint);
            return;
        }

        for(int i = 0; i < str1.length(); i++)
        {
            showPerm(str1, newStringtoPrint + str1.charAt(i));
        }
    }

    public static void main(String args[])
    {
        System.out.print("Enter the string : ");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;

        try
        {
            str = br.readLine();
            showPerm(str, "");
        }
        catch(IOException e)
        {
            System.out.println("Cannot Read");
        }
        // String str = sc.nextLine();
    }
}

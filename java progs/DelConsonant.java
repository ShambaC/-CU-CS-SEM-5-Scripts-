import java.util.*;

public class DelConsonant
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        String str, str2 = "";

        System.out.print("Enter the string : ");
        str = sc.nextLine();

        int size = str.length();

        sc.close();

        for(int i = 0; i < size; i++)
        {
            Character ch = str.charAt(i);
            
            if(Character.isLetter(ch))
            {
                if(ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' && ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U')
                {
                    continue;
                }

                str2 += ch;
            }
            else
            {
                str2 += ch;
            }
        }

        System.out.println("New String : " + str2);
    }
}

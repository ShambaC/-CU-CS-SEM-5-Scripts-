import java.util.*;

public class TheString
{
    String str;
    int len, wordcount = 1, cons = 0;

    TheString(String ds)
    {
        str = ds;
        len = str.length();
    }

    void countFreq()
    {
        for(int i = 0; i < len; i++)
        {
            if(str.charAt(i) == ' ')
            {
                wordcount++;
            }

            Character ch = new Character(str.charAt(i));

            if(ch.isLetter(ch))
            {
                if(ch != 'a' && ch != 'e' && ch != 'i' && ch != 'o' && ch != 'u' && ch != 'A' && ch != 'E' && ch != 'I' && ch != 'O' && ch != 'U')
                {
                    cons++;
                }
            }
        }
    }

    void Display()
    {
        System.out.println("The entered string : " + str);
        System.out.println("The number of words in the string are : " + wordcount);
        System.out.println("The number of consonants in the string are : " + cons);
    }

    public static void main(String args[])
    {
        String input;
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the string : ");
        input = sc.nextLine();

        TheString STR = new TheString(input);

        STR.countFreq();
        STR.Display();
    }
}

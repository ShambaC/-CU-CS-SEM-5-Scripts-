import java.util.*;

class NegativeSizeException extends Exception
{
    int num;

    NegativeSizeException(int i)
    {
        num = i;
    }

    public String toString()
    {
        return "Exception occured ! Negative number entered : " + num;
    }
}

public class CustomExcep
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the size of the array : ");
        int size = sc.nextInt();
        int Arr[] = new int[size];

        System.out.println("Enter elements : ");
        for(int i = 0; i < size; i++)
        {
            Arr[i] = sc.nextInt();
            try
            {
                if(Arr[i] < 0)
                {
                    int temp = i;
                    i--;
                    throw new NegativeSizeException(Arr[temp]);
                }
            }
            catch(NegativeSizeException e)
            {
                System.out.println(e);
            }
        }

        sc.close();
    }    
}

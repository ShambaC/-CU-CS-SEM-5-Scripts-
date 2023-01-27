import java.util.*;

public class SumPair
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        int array[] = new int[10];
        int size, sum;

        System.out.print("Enter the size of the array : ");
        size = sc.nextInt();

        System.out.println("Enter the array elements : ");
        for(int i = 0; i < size; i++)
        {
            array[i] = sc.nextInt();
        }

        System.out.print("Enter the sum : ");
        sum = sc.nextInt();

        for(int i = 0; i < size; i++)
        {
            for(int j = i + 1; j < size - 1; j++)
            {
                int add = array[i] + array[j];
                if(sum == add)
                {
                    System.out.println("Pair : " + array[i] + ", " + array[j]);
                }
            }
        }

    }
}

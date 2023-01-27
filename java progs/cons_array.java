import java.util.*;

public class cons_array
{
    public static int[] sortArr(int Arr[])
    {
        int size = Arr.length;
        
        for(int i = 0; i < size - 1; i++)
        {
            for(int j = i + 1; j < size; j++)
            {
                if(Arr[i] > Arr[j])
                {
                    int temp = Arr[i];
                    Arr[i] = Arr[j];
                    Arr[j] = temp;
                }
            }
        }

        return Arr;
    }   
    
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the size of the array : ");
        int size = sc.nextInt();
        int Arr[] = new int[size];

        System.out.println("Enter the data : ");
        for(int i = 0; i < size; i++)
        {
            Arr[i] = sc.nextInt();
        }
        sc.close();

        Arr = sortArr(Arr);

        int tmpSize = 1, largeSize = 1;

        for(int i = 0; i < size - 1; i++)
        {
            if(Arr[i + 1] - Arr[i] == 1)
            {
                tmpSize++;
                continue;
            }
            if(tmpSize > largeSize)
            {
                largeSize = tmpSize;
                tmpSize = 1;
            }
        }
        if(tmpSize > largeSize)
        {
            largeSize = tmpSize;
            tmpSize = 1;
        }

        System.out.println("The largest sequence of consecutive numbers is of the size : " + largeSize);
    }
}

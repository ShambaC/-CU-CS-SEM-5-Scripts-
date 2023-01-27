import java.util.Scanner;

public class arrayop
{
    static Scanner sc = new Scanner(System.in);
    static int array[] = new int[20], size;

    public static void Insert()
    {
        int i, pos, val;

        System.out.print("Enter the position to be inserted : ");
        pos = sc.nextInt();
        System.out.print("\nEnter the value to be inserted : ");
        val = sc.nextInt();    
        
        for(i = size; i > pos; i--)
        {
            array[i] = array[i - 1];
        }

        array[pos] = val;
        size++;

        System.out.println("\nThe array now is : ");
        for(i = 0; i < size; i++)
        {
            System.out.println(array[i] + " ");
        }
    }

    public static void Remove()
    {
        int i, element, pos = 0, flag = 0;

        System.out.print("\nEnter the element to be removed : ");
        element = sc.nextInt();
        
        for(i = 0; i < size; i++)
        {
            if(array[i] == element)
            {
                pos = i;
                flag = 1;
                break;
            }
        }

        if(flag == 0)
        {
            System.out.println("\nElement not found !");
        }
        else
        {
            for(i = pos; i < size - 1; i++)
            {
                array[i] = array[i+1];
            }
        }
        size--;

        System.out.println("\nThe array now is : ");
        for(i = 0; i < size; i++)
        {
            System.out.println(array[i] + " ");
        }        
    }

    public static void RmDup()
    {
        int i, j;

        for(i = 0; i < size - 1; i++)
        {
            for(j = i + 1; j < size; j++)
            {
                if(array[i] == array [j])
                {
                    array[j] = -1;
                }
            }
        }

        for(i = 0; i < size; i++)
        {
            if(array[i] == -1)
            {
                int pos = i;
                for( j = pos; j < size - 1; j++)
                {
                    array[j] = array[j + 1];
                }
                size--;
            }
        }

        System.out.println("\nThe current size of array is : " + size);

        System.out.println("The array now is : ");
        for(i = 0; i < size; i++)
        {
            System.out.println(array[i] + " ");
        }
    }

    public static void Sort()
    {
        int i, j, mid = size/2, temp;

        for(i = 0; i < mid - 1; i++)
        {
            for(j = i + 1; j < mid; j++)
            {
                if(array[i] > array[j])
                {
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }                
            }
        }

        for(i = mid; i < size - 1; i++)
        {
            for(j = i + 1; j < size; j++)
            {
                if(array[i] < array[j])
                {
                    temp = array[i];
                    array[i] = array[j];
                    array[j] = temp;
                }
            }
        }

        System.out.println("\nThe array now is : \n");
        for(i = 0; i < size; i++)
        {
            System.out.println(array[i] + " ");
        }
    }

    public static void main(String args[])
    {
        int choice = 1, i;
        

        System.out.print("Enter the size of the array : ");
        size = sc.nextInt();

        System.out.println("Enter array data :");
        for(i = 0; i < size; i++)
        {
            array[i] = sc.nextInt();
        }

        do
        {
            System.out.println("Available methods : \n1.Insert\n2.Remove\n3.Remove Duplicate\n4.Sort Half\n5.Exit\nEnter your choice : ");
            choice = sc.nextInt();

            switch(choice)
            {
                case 1:
                    Insert();
                    break;
                case 2:
                    Remove();
                    break;
                case 3:
                    RmDup();
                    break;
                case 4:
                    Sort();
                    break;
                case 5:
                    System.exit(0);
                    break;
                default:
                    System.out.println("\nWrong choice !!");
            }
        }while(choice != 5);
    }
}

import java.util.*;

public class Array2Dmin
{
    public static void main(String args[])
    {
        int array[][] = new int[10][10], row, column, i, j, temp;
        int rowmin[] = new int[10], colmin[] = new int[10];
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the row of the array : ");
        row = sc.nextInt();
        System.out.print("Enter the column of the array : ");
        column = sc.nextInt();

        //Input
        System.out.print("\nEnter the matrix : \n");
        for(i = 0; i < row; i++)
        {
            for(j = 0; j < column; j++)
            {
                array[i][j] = sc.nextInt();
            }
        }

        //min elements of rows and columns
        for(i = 0; i < row; i++)
        {
            temp = array[i][0];
            for(j = 0; j < column; j++)
            {
                if(temp > array[i][j])
                {
                    temp = array[i][j];
                }
            }
            rowmin[i] = temp;
        }

        for(i = 0; i < column; i++)
        {
            temp = array[0][i];
            for(j = 0; j < row; j++)
            {
                if(temp > array[j][i])
                {
                    temp = array[j][i];
                }
            }
            colmin[i] = temp;
        }

        System.out.println("minimum elements of rows : ");
        for(i = 0; i < row; i++)
        {
            System.out.print(rowmin[i] + " ");
        }

        System.out.println("\nminimum elements of column : ");
        for(i = 0; i < column; i++)
        {
            System.out.print(colmin[i] + " ");
        }
    }
}

public class ExceptDemo
{
    public static void main(String args[])
    {
        try
        {
            int n = 5;
            int arr[] = {1, 2, 3};

            //double c = n / 0;
            int ele = arr[5];
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.print("Array out of bounds : " + e);
        }
        catch(ArithmeticException e)
        {
            System.out.print("Divide by zero : " + e);
        }
    }
}

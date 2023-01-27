public class Array2D {
    public static void main(String args[])
    {
        int arr[][] = new int[4][];

        //init
        arr[0] = new int[1];
        arr[1] = new int[2];
        arr[2] = new int[3];
        arr[3] = new int[4];

        int i, j, k = 0;

        for(i = 0; i < 4; i++)
        {
            for(j = 0; j < i+1; j++)
            {
                System.out.print(k++ + " ");
            }
            System.out.println();
        }
    }
}

public class palindrome
{
    public static void main(String args[])
    {
        try
        {
            String original = args[0];
            String reversed = "";

            for(int i = original.length() - 1; i >= 0; i--)
            {
                reversed += original.charAt(i);
            }

            if(original.equalsIgnoreCase(reversed))
            {
                System.out.println("Palindrome, " + reversed);
            }
            else
            {
                System.out.println("Not Palindrome");
            }
        }
        catch(ArrayIndexOutOfBoundsException e)
        {
            System.out.println("No arguments passed");
        }
    }    
}

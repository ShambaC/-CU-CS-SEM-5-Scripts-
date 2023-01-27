public class reverse_word
{
    public static void main(String args[])
    {
        String original = "Tiyasha is so cute";
        String Words[] = original.split(" ");
        String reverse_string = "";

        for(int i = 0; i < Words.length; i++)
        {
            StringBuffer sbr = new StringBuffer(Words[i]);
            sbr.reverse();
            reverse_string += sbr + " ";
        }

        System.out.println("Original string : " + original + "\nString with words reversed : " + reverse_string);
    }
}

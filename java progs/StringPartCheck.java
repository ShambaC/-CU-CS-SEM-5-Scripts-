public class StringPartCheck
{
    public static void main(String args[])
    {
        String s = "This is orange juice";
        String term = "orange";
        String s2 = "";

        String[] words = s.split(" ");

        System.out.println("Original sentemce : " + s);

        for(int i = 0; i < words.length; i++)
        {
            if(words[i].equalsIgnoreCase(term))
            {
                s2 += "apple";
            }
            else
            {
                s2 += words[i];
            }

            s2 += " ";
        }

        System.out.println("New sentemce : " + s2);
    }
}

import java.util.*;

public class BookDriver
{
    static int c=0;
    public static Book[] BooksWithPriceRange(double min, double max, Book b[])
    {
        int size = b.length;
        Book booksInRange[] = new Book[size];
        for(int i=0;i<size;i++)
        {
            if(b[i].getPrice()>=min && b[i].getPrice()<=max)
            {
                booksInRange[c]=b[i];
                c++;

            }
        }
        return booksInRange;
    }
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("Enter the number of book:");
        int n=sc.nextInt();
        Book books[]=new Book[n];
        int i;
        for(i=0;i<n;i++)
        {
            System.out.println("Enter the details of book "+(i+1)+": ");
            System.out.println("Enter the id of the book: ");
            int id=sc.nextInt();
            System.out.println ("Enter the price of the book: ");
            double price=sc.nextDouble();
            sc.nextLine();
            System.out.println("Enter the author of the book: ");
            String author=sc.nextLine();
            System.out.println("Enter the title of the book: ");
            String title=sc.nextLine();
            books[i]=new Book(id,price,author,title);
        }

        System.out.println("Enter the minimum price for range: ");
        double min=sc.nextDouble();
         System.out.println("Enter the maximum price for range: ");
        double max=sc.nextDouble();

        System.out.println("The books with price in the range "+min+" to "+max+": ");
        Book b[]=BooksWithPriceRange(min,max,books);
        System.out.println("id\tprice\tauthor\ttitle");
        for(i=0;i<c;i++)
        {
            System.out.println(b[i].getId()+"\t"+b[i].getPrice()+"\t"+b[i].getAuthor()+"\t"+b[i].getTitle());
        }

    }    
}

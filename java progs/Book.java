public class Book
{
    private int id;
    private double price;
    private String author;
    private String title;

    Book(int id, double price, String author, String title)
    {
        this.id = id;
        this.price = price;
        this.author = author;
        this.title = title;
    }
    public int getId()
    {
        return(this.id);
    }
    public double getPrice()
    {
        return(this.price);
    }
    public String getAuthor()
    {
        return(this.author);
    }
    public String getTitle()
    {
        return(this.title);
    }
}
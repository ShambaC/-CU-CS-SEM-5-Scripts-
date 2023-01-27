package ishani;

public class person2
{
    String name;
    String address;

    person2() //default constructor
    {
        name="";
        address="";
    }

    void setPerson(String name, String addr)
    {
        this.name=name;
        this.address=addr;
    }
    public String toString()
    {
        return("Person[name="+this.name+", address="+this.address+"]");
    }
     public static void main(String args[])
    {
        person2 p=new person2();
        p.setPerson("Abc","Delhi");
        System.out.println(p.toString());  
    }
}

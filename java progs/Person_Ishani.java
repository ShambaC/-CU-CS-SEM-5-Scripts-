class Person_Ishani
{
    String name;
    String address;

    Person_Ishani() //default constructor
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
}
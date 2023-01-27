class Staff_Ishani extends Person_Ishani
{
    String school;
    double pay;

    Staff_Ishani()
    {
        super();
        school="";
        pay=0.0;
        name="";
        address="";

    }

    void setStaff(String school, double pay, String name, String address)
    {
        this.school=school;
        this.pay=pay;
        this.name=name;
        this.address=address;
    }

    public String toString()
    {
        return("Person[name="+this.name+", address="+this.address+", school="+this.school+", pay="+this.pay+"]");
    }
}
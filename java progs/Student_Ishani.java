class Student_Ishani extends Person_Ishani 
{
    String program;
    String year;
    double fees;

    Student_Ishani()
    {
        super();
        program="";
        year="";
        fees=0.0;
    }

    void setStudent(String program, String year, double fees, String name, String address)
    {
        this.program=program;
        this.year=year;
        this.fees=fees;
        setPerson(name, address);
    }  

    public String toString()
    {
        return("Person[name="+this.name+", address="+this.address+", program="+this.program+",year="+ this.year+", fees="+this.fees+"]");
    }
}
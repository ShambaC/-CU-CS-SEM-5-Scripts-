package ishani;

public class student2 extends person2
{
    String program;
    String year;
    double fees;

    student2()
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
        return("Person[name=" + name + ", address=" + address + ", program=" + this.program + ",year=" + this.year + ", fees=" + this.fees + "]");
    }
     public static void main(String args[])
    {
        
        student2 st=new student2();
       
        st.setStudent("ComputerScience","2022",18000.00, "Xyz","Kolkata");
        System.out.println(st.toString());
        
    }    
}

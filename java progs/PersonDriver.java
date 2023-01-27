public class PersonDriver
{
    public static void main(String args[])
    {
        Person_Ishani p=new Person_Ishani();
        Student_Ishani st=new Student_Ishani();
        Staff_Ishani stf=new Staff_Ishani();

        p.setPerson("Abc","Delhi");
        System.out.println(p.toString());

        st.setStudent("ComputerScience","2022",18000.00, "Xyz","Kolkata");
        System.out.println(st.toString());
        stf.setStaff("DMHSS",36000.65,"Fgh","Mumbai");
        System.out.println(stf.toString());
    }
}

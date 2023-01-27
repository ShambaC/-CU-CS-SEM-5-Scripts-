import java.util.*;
class person{
String name,address;
int age;
person(String n,String a)
{
name=n;
address=a;
}
void tostring()
{
System.out.println("The name of the person is:"+name);
System.out.println("The address of the person is:"+address);
}
}
class student extends person{
String program,year;
double fees;
student(String p,String y,double f,String n,String a)
{
super(n, a);
program=p;
year=y;
fees=f;
}

void tostring()
{
System.out.println("The name of the person is:"+name);
System.out.println("The address of the person is:"+address);
System.out.println("The name of the program of the person is:"+program);
System.out.println("The year of the person is:"+year);
System.out.println("The fees of the person is:"+fees);
}
}
class staff extends person{
String school;
double pay;
staff(String n,String a,String s,double py)
{
super(n, a);
school=s;
pay=py;
}
void tostring()
{
System.out.println("The name of the person is:"+name);
System.out.println("The address of the person is:"+address);
System.out.println("The name of the school of the person is:"+school);
System.out.println("The payment is:"+pay);
}
}
class experiment{
public static void main(String args[])
{
person ob = new person( "ANIL","AHEMDABAD");
ob.tostring();
student ob1= new student("BSC","FINALYEAR",20000,"AVIK","RAIGANG");
ob1.tostring();
staff ob2= new staff( "AHELI","KOLKATA","CARMELCONVENT",30000);
ob2.tostring();
}
}


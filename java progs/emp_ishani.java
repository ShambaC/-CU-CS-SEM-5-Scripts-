import java.util.*;

abstract class Employee1
{
	double basic,da,hra,pf,gross,net;
	abstract void set_basic(double basic);
	abstract void set_allowance(double da,double hra,double pf);
	abstract void sal_calculate();
	abstract void display();
	
}
class manager extends Employee1
{
	//Overridden method
	void set_basic(double basic)
    {
		// TODO Auto-generated method stub
		this.basic=basic;
	}
	//Overridden method
	void set_allowance(double da, double hra, double pf)
    {
		// TODO Auto-generated method stub
		this.da=da;
		this.hra=hra;
		this.pf=pf;
	}
	//Overridden method
	void sal_calculate()
    {
		// TODO Auto-generated method stub
		gross=basic*(1+da+hra);
		net=gross-(basic*pf);
	}
	//Overridden method
	void display()
    {
		System.out.println("The Net Salary of the Manager is: "+net);
	}
}
class clerk extends Employee1 {
	//Overridden method
	void set_basic(double basic) {
		// TODO Auto-generated method stub
		this.basic=basic;
	}
	//Overridden method
	void set_allowance(double da, double hra, double pf){
		// TODO Auto-generated method stub
		this.da=da;
		this.hra=hra;
		this.pf=pf;
	}
	//Overridden method
	void sal_calculate(){
		// TODO Auto-generated method stub
		gross=basic*(1+da+hra);
		net=gross-(basic*pf);
	}
	//Overridden method
	void display(){
	System.out.println("The Net Salary of the Clerk is: "+net);
	}
}

public class emp_ishani {
	public static void main(String[] args){
		// TODO Auto-generated method stub
		double basicsal;
		Scanner sc=new Scanner(System.in);
		manager obj=new manager();
		System.out.println("Enter the Basic Salary of the Manager:  ");
		basicsal=sc.nextInt();
		obj.set_basic(basicsal);
		obj.set_allowance(1.10, 0.30, 0.24);
		obj.sal_calculate();
		obj.display();
		clerk obj2=new clerk();
		System.out.println("Enter the Basic Salary of the Clerk:  ");
		basicsal=sc.nextInt();
		obj2.set_basic(basicsal);
		obj2.set_allowance(0.90, 0.20, 0.16);
		obj2.sal_calculate();
		obj2.display();
	}
}

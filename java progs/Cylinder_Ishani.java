import java.util.*;
class Square{
	double side;
	Square(){
		side=0;
	}
	Square(double side){ 
		this.side=side;
	}
	double getVolume(){
		double v = side*side*side;
		return v;
	}
}
public class Cylinder_Ishani extends Square{
	double h;
	Cylinder_Ishani(double h, double side){
		super(side);
		this.h = h;
	}
	//Overridden method getVolume()
	public double getVolume(){
		double v = 3.14*super.side*super.side*h;
		return v;
	}
	public static void main(String args[]){
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the value for height : ");
		double hei = sc.nextDouble();
		System.out.println("Enter the value for side : ");
		double s = sc.nextDouble();
		Cylinder ob = new Cylinder(hei, s);
		Square sq=new Square(s);
		System.out.println("Volume of cylinder is : " + ob.getVolume());
		System.out.println("Volume of square is : " + sq.getVolume());
	}
}


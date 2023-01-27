import java.util.Scanner;

public class temp_box {
	int length,breadth,height;

	temp_box(int l,int b,int h)
	{
	length=l;
	breadth=b;
	height=h;

	}
	temp_box(temp_box ob)
	{
	length=ob.length;
	breadth=ob.breadth;
	height=ob.height;
	}
	public int volume()
	{
	return length*breadth*height;

	}

	public static void main(String args[])
	{
	Scanner sc=new Scanner(System.in);
	System.out.println("Enter the length,breadth and height of the box: ");
	int l=sc.nextInt();
	int b=sc.nextInt();
	int h=sc.nextInt();
	temp_box ob1=new temp_box(l,b,h);
	temp_box ob2=new temp_box(ob1);
	System.out.println("The volume of the box is: "+ob2.volume());
	}
}
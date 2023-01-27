import java.util.Scanner;
public class array_Sorting 
{
	public static void main(String args[])
	{
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the size of the array:");
		int size=sc.nextInt();
		
		int arr[]=new int[size];
		System.out.println("Enter the elements in the array:");
		int i,j,t;
		for(i=0;i<size;i++)
			arr[i]=sc.nextInt();
		int mid=(int)(size/2);
		
		for(i=0;i<mid;i++) // sorting the first half in ascending order
		{
			for(j=i;j<mid;j++)
			{
				if(arr[j]<arr[i])
				{
					t=arr[i];
					arr[i]=arr[j];
					arr[j]=t;
				}
			}
		}
			
		for(i=mid;i<size;i++) // sorting the second half in descending order
		{
			for(j=i;j<size;j++)
			{
				if(arr[i]<arr[j])
				{
					t=arr[i];
					arr[i]=arr[j];
					arr[j]=t;
				}
			}
		}
		System.out.println("The sorted array is as follows:");
		for(i=0;i<size;i++)
			System.out.print(arr[i]+"\t");	
		

	}
}
import java.util.Scanner;
import java.util.Arrays;
public class array { 
	
	public static int[] insert(int size, int arr[], int x, int pos) {
    	int i;
        int newarr[]=new int[size+1];
        for(i = 0;i<size+1;i++) {
        	if(i<pos-1)
        		newarr[i]=arr[i];
            else if(i==pos-1)
            	newarr[i]=x;
            else
            	newarr[i]=arr[i-1];
        	}
        return newarr;
     }
	
	public static int[] removeTheElement(int[] arr, int size, int index) {
		// If the array is empty
        // or the index is not in array range
        // return the original array
        if(arr==null || index<0 || index>=arr.length) {
        	return arr;
        }
        
        // Create another array of size one less
        int[] anotherArray=new int[arr.length-1];
 
        // Copy the elements except the index
        // from original array to the other array
        for(int i=0,k=0;i<arr.length;i++) {
        	// if the index is
            // the removal element index
            if(i==index) {
            	continue;
            }
 
            // if the index is not
            // the removal element index
            anotherArray[k++]=arr[i];
        }
 
        // return the resultant array
        return anotherArray;
    }
	
	public static int removeDuplicateElements(int arr[], int size) {
		int i,j=0,k;
		for (i=0;i<size;i ++) {  
	        for (j=i+1;j<size;j++) {  
	        	// use if statement to check duplicate element  
	            if (arr[i]==arr[j]) {  
	            	// delete the current position of the duplicate element  
	                for (k=j;k<size-1;k++) {  
	                	arr[k]=arr[k+1];  
	                }  
	                // decrease the size of array after removing duplicate element  
	                size--;  
	                  
	            // if the position of the elements is changes, don't increase the index j  
	                j--;      
	            }  
	        }  
	    } 
		return j;
	}
	public static void printOrder(int arr[], int n) {
		// sorting the array
		int i,j,temp;
		for(i=0;i<n-1;i++) {
			for(j=0;j<n/2;j++) { 
				if(arr[j]>arr[j+1]) {
					temp=arr[j];
	                arr[j]=arr[j+1];
	                arr[j+1]=temp;
	            }
	        }

	        for(j=n/2;j<n-1;j++) {
	        	if(arr[j]<arr[j+1]) {
	        		temp=arr[j];
	                arr[j]=arr[j+1];
	                arr[j+1]=temp;
	            }
	        }
	    }

	    for(i=0;i<n;i++)
	    	System.out.print(arr[i]+" ");

	   
	   
	}
    public static void main(String[] args) {
    	int i;
        Scanner sc=new Scanner(System.in);  
        System.out.println("Enter the array range:\n");  
        int size=sc.nextInt();  
        int[] arr=new int[size];  
        System.out.println("Enter the elements of the array:\n");  

        for( i=0; i<size; i++) {  
        	arr[i] = sc.nextInt();  
        }
        // print the original array
        System.out.println("Initial Array:\n"+Arrays.toString(arr));
        String ch="";
        do
        {
        	System.out.println("\nEnter your Choice: \n1. Insert new element in Array\n2. Delete specific element from array\n"
		    +"3. Remove duplicate element from array\n4. Sort The array\n");  
            int w=sc.nextInt(); 
            switch(w)
            {
                 case 1:
                 {
                	 System.out.print("Enter the position where you want to insert:\t");
	                 int pos=sc.nextInt();
	                 System.out.println("Enter the value of element to be inserted:\t");
	                 int x=sc.nextInt();
	                 arr=insert(size,arr,x,pos);
	                 System.out.println("\nArray with "+x+" inserted at position "+pos+ ":\n"+Arrays.toString(arr));
	                 break;
	             }
                 case 2:
                 {
                	 System.out.print("Enter the index of element you want to delete:\t");
	                 int index=sc.nextInt();
	                 arr=removeTheElement(arr,size,index);
                     System.out.println("\nArray without "+index+Arrays.toString(arr));
	                 break;	
                 }
                 case 3:
                 {
                	 size=removeDuplicateElements(arr,size);  
	                 System.out.println("The array after reomving duplicate values::\n ");
	                 for(i=0;i<size;i++) 
	                	 System.out.print(+arr[i]+" ");  
	                 break;
                 }
                 case 4:
                 {
                	 System.out.println("The sorted array is:");
                	 printOrder(arr,size);
	                 break;
                 }
                 default:
                 {
                	 System.out.print("Not valid option");
	                 break;
                 }
            }
            System.out.print("\nDo you want to continue(y/Y):\n");
            ch=sc.next();
        }while(ch.equals("y")||ch.equals("Y"));
    }
}	



class NewThread implements Runnable
{
    Thread t;

    NewThread()
    {
        t = new Thread(this, "Child thread");
        System.out.println("child thread name : " + t);
    }

    public void run()
    {
        try
        {
            for(int i = 5; i > 0; i--)
            {
                System.out.println("child count : " + i);
                Thread.sleep(500);
            }
        }
        catch(InterruptedException e)
        {
            System.out.println("Error in child thread");
        }

        System.out.println("Exiting child thread");
    }
}

public class ThreadDemo
{
    public static void main(String args[])
    {
        NewThread nt = new NewThread();

        System.out.println("Before child start");

        nt.t.start();

        System.out.println("After child start");

        try
        {
            for(int i = 5; i > 0; i--)
            {
                System.out.println("Main thread count : " + i);
                Thread.sleep(1000);
            }
        }
        catch(InterruptedException e)
        {
            System.out.println("error in main thread");
        }

        System.out.println("Exiting main thread");
    }
}

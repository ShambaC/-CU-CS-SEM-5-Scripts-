class NewThread implements Runnable
{
    String name;
    Thread t;

    NewThread(String s)
    {
        name = s;
        t = new Thread(this, name);
        System.out.println("New thread : " + t);
    }

    public void run()
    {
        try
        {
            for(int i = 5; i > 0; i--)
            {
                System.out.println(name + " : " + i);
                Thread.sleep(1000);
            }
        }
        catch(InterruptedException e)
        {
            System.out.println(name + "Interrupted");
        }

        System.out.println(name + "Exiting");
    }
}

public class DemoJoin
{
    public static void main(String args[])
    {
        NewThread t1 = new NewThread("One");
        NewThread t2 = new NewThread("Two");
        NewThread t3 = new NewThread("Three");

        //Start the threads
        t1.t.start();
        t2.t.start();
        t3.t.start();

        System.out.println("Thread One is alive : " + t1.t.isAlive());
        System.out.println("Thread Two is alive : " + t2.t.isAlive());
        System.out.println("Thread Three is alive : " + t3.t.isAlive());

        try
        {
            System.out.println("Waiting for threads to finish !");
            t1.t.join();
            t2.t.join();
            t3.t.join();
        }
        catch(InterruptedException e)
        {
            System.out.println("Main thread interrupted");
        }

        System.out.println("Thread One is alive : " + t1.t.isAlive());
        System.out.println("Thread Two is alive : " + t2.t.isAlive());
        System.out.println("Thread Three is alive : " + t3.t.isAlive());

        System.out.println("Main thread exiting");
    }
}

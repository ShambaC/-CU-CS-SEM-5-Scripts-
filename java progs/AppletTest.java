import java.awt.event.*;
import java.awt.*;

public class AppletTest extends Frame
{
    public AppletTest()
    {
        addWindowListener(new WindowAdapter(){
            public void windowClosing(WindowEvent we) {
                System.exit(0);
            }
        });
    }

    public void paint(Graphics g)
    {
        g.setColor(Color.RED);
        g.drawString("WELCOME", 20, 100);
        g.drawRect(20, 150, 60, 50);

        int x[] = {20, 40, 60};
        int y[] = {250, 210, 250};

        g.drawPolygon(x, y, 3);
    }

    public static void main(String args[])
    {
        AppletTest appwin = new AppletTest();
        
        appwin.setSize(new Dimension(370, 700));
        appwin.setTitle("Demo app");
        appwin.setVisible(true);
    }
}

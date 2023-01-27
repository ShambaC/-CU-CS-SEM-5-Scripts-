import java.awt.*;
import java.applet.Applet;

@Deprecated
public class LegacyApp extends Applet
{
    public void paint(Graphics g)
    {
        g.setColor(Color.CYAN);
        g.drawString("WELCOME", 20, 20);
        g.drawRect(20, 150, 60, 50);
    }
}

import javax.swing.*;
import java.awt.*;

public class MultiTabExample {
    public static void main(String[] args) {
        // Create the main frame
        JFrame frame = new JFrame("Multi-Tab Example");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Create a tabbed pane
        JTabbedPane tabbedPane = new JTabbedPane();

        // Create panels for each tab
        JPanel tab1 = new JPanel();
        tab1.add(new JLabel("Welcome to DASHBOARD!"));
        tab1.add(new JButton("Button 1"));
        tabbedPane.addTab("Dashboard", tab1);
        tabbedPane.addTab("Timetable", new MainAppSwing());
        tabbedPane.addTab("Goals", new GoalTrackingApp());
        tabbedPane.addTab("Attendance", new AttendanceTrackerGUI());
        tabbedPane.addTab("Energy", new EnergyHealthUI());
        
        

        // Add the tabbed pane to the frame
        frame.add(tabbedPane);

        // Make the frame visible
        frame.setVisible(true);
    }
}
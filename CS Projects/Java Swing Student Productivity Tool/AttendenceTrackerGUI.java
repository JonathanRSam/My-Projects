import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class AttendanceTrackerGUI extends JPanel {
    // Define components
    private AttendanceTracker attendanceTracker;
    private JTextField totalClassesField;
    private JTextField attendanceGoalField;
    private JLabel attendanceStatusLabel;
    private JButton markAttendanceButton;
    private JButton checkAttendanceButton;

    public AttendanceTrackerGUI() {
        // Setup and add components
        setLayout(new BorderLayout());

        // Initialize GUI components
        totalClassesField = new JTextField(10);
        attendanceGoalField = new JTextField(10);
        attendanceStatusLabel = new JLabel("Attendance Status: ");
        
        markAttendanceButton = new JButton("Mark Attendance");
        checkAttendanceButton = new JButton("Check Attendance Status");
        JButton setGoalButton = new JButton("Set Goal and Start");

        // Panel for inputs
        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(3, 2));
        inputPanel.add(new JLabel("Total Classes:"));
        inputPanel.add(totalClassesField);
        inputPanel.add(new JLabel("Attendance Goal (%):"));
        inputPanel.add(attendanceGoalField);
        inputPanel.add(setGoalButton);

        // Panel for actions
        JPanel actionPanel = new JPanel();
        actionPanel.add(markAttendanceButton);
        actionPanel.add(checkAttendanceButton);
        actionPanel.add(attendanceStatusLabel);

        // Add panels to the panel
        add(inputPanel, BorderLayout.NORTH);
        add(actionPanel, BorderLayout.CENTER);

        // Initially disable action buttons until goal is set
        markAttendanceButton.setEnabled(false);
        checkAttendanceButton.setEnabled(false);

        // Action listeners
        setGoalButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int totalClasses = Integer.parseInt(totalClassesField.getText());
                int goal = Integer.parseInt(attendanceGoalField.getText());
                attendanceTracker = new AttendanceTracker(totalClasses);
                attendanceTracker.setAttendanceGoal(goal);

                // Enable action buttons
                markAttendanceButton.setEnabled(true);
                checkAttendanceButton.setEnabled(true);
                
                attendanceStatusLabel.setText("Goal set. Start marking attendance!");
            }
        });

        markAttendanceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                attendanceTracker.markAttendance();
                attendanceStatusLabel.setText("Attendance marked for " + attendanceTracker.getClassesAttended() + " out of " + attendanceTracker.getTotalClasses() + " classes.");
            }
        });

        checkAttendanceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                attendanceTracker.checkAttendanceStatus();
                float attendancePercentage = attendanceTracker.calculateAttendance();
                String status = attendancePercentage >= attendanceTracker.getAttendanceGoal() ? "Goal met!" : "Goal not met.";
                attendanceStatusLabel.setText("Attendance: " + attendancePercentage + "% - " + status);
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Attendance Tracker");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(400, 300);
            frame.setLocationRelativeTo(null);

            AttendanceTrackerGUI panel = new AttendanceTrackerGUI();
            frame.add(panel);

            frame.setVisible(true);
        });
    }
}

// Your AttendanceTracker class (unchanged)
class AttendanceTracker {
    private int attendanceGoal;
    private int totalClasses;
    private int classesAttended;
    
    public AttendanceTracker(int totalClasses) {
        this.totalClasses = totalClasses;
        this.classesAttended = 0;
    }

    public void setAttendanceGoal(int goal) {
        this.attendanceGoal = goal;
    }
    
    public void markAttendance() {
        if (classesAttended < totalClasses) {
            classesAttended++;
            System.out.println("Attendance marked!");
        } else {
            System.out.println("All sessions are marked.");
        }
    }
    
    public float calculateAttendance() {
        return (float) classesAttended / totalClasses * 100;
    }

    public void checkAttendanceStatus() {
        float attendancePercentage = calculateAttendance();
        System.out.println("Attendance Percentage: " + attendancePercentage + "%");
        if (attendancePercentage >= attendanceGoal) {
            System.out.println("Attendance goal met.");
        } else {
            System.out.println("Attendance goal not met.");
        }
    }

    public int getTotalClasses() {
        return totalClasses;
    }

    public int getClassesAttended() {
        return classesAttended;
    }

    public int getAttendanceGoal() {
        return attendanceGoal;
    }
}


/* import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

class AttendanceTrackerGUI extends JFrame {
    // Define components
    private AttendanceTracker attendanceTracker;
    private JTextField totalClassesField;
    private JTextField attendanceGoalField;
    private JLabel attendanceStatusLabel;
    private JButton markAttendanceButton;
    private JButton checkAttendanceButton;

    public AttendanceTrackerGUI() {
        // Setup and add components
        setTitle("Attendance Tracker");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        // Initialize GUI components
        totalClassesField = new JTextField(10);
        attendanceGoalField = new JTextField(10);
        attendanceStatusLabel = new JLabel("Attendance Status: ");
        
        markAttendanceButton = new JButton("Mark Attendance");
        checkAttendanceButton = new JButton("Check Attendance Status");
        JButton setGoalButton = new JButton("Set Goal and Start");

        // Panel for inputs
        JPanel inputPanel = new JPanel();
        inputPanel.setLayout(new GridLayout(3, 2));
        inputPanel.add(new JLabel("Total Classes:"));
        inputPanel.add(totalClassesField);
        inputPanel.add(new JLabel("Attendance Goal (%):"));
        inputPanel.add(attendanceGoalField);
        inputPanel.add(setGoalButton);

        // Panel for actions
        JPanel actionPanel = new JPanel();
        actionPanel.add(markAttendanceButton);
        actionPanel.add(checkAttendanceButton);
        actionPanel.add(attendanceStatusLabel);

        // Add panels to the frame
        setLayout(new BorderLayout());
        add(inputPanel, BorderLayout.NORTH);
        add(actionPanel, BorderLayout.CENTER);

        // Initially disable action buttons until goal is set
        markAttendanceButton.setEnabled(false);
        checkAttendanceButton.setEnabled(false);

        // Action listeners
        setGoalButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                int totalClasses = Integer.parseInt(totalClassesField.getText());
                int goal = Integer.parseInt(attendanceGoalField.getText());
                attendanceTracker = new AttendanceTracker(totalClasses);
                attendanceTracker.setAttendanceGoal(goal);

                // Enable action buttons
                markAttendanceButton.setEnabled(true);
                checkAttendanceButton.setEnabled(true);
                
                attendanceStatusLabel.setText("Goal set. Start marking attendance!");
            }
        });

        markAttendanceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                attendanceTracker.markAttendance();
                attendanceStatusLabel.setText("Attendance marked for " + attendanceTracker.getClassesAttended() + " out of " + attendanceTracker.getTotalClasses() + " classes.");
            }
        });

        checkAttendanceButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                attendanceTracker.checkAttendanceStatus();
                float attendancePercentage = attendanceTracker.calculateAttendance();
                String status = attendancePercentage >= attendanceTracker.getAttendanceGoal() ? "Goal met!" : "Goal not met.";
                attendanceStatusLabel.setText("Attendance: " + attendancePercentage + "% - " + status);
            }
        });
    }


    

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            AttendanceTrackerGUI frame = new AttendanceTrackerGUI();
            frame.setVisible(true);
        });
    }
}

// Your AttendanceTracker class
class AttendanceTracker {
    private int attendanceGoal;
    private int totalClasses;
    private int classesAttended;
    
    public AttendanceTracker(int totalClasses) {
        this.totalClasses = totalClasses;
        this.classesAttended = 0;
    }

    public void setAttendanceGoal(int goal) {
        this.attendanceGoal = goal;
    }
    
    public void markAttendance() {
        if (classesAttended < totalClasses) {
            classesAttended++;
            System.out.println("Attendance marked!");
        } else {
            System.out.println("All sessions are marked.");
        }
    }
    
    public float calculateAttendance() {
        return (float) classesAttended / totalClasses * 100;
    }

    public void checkAttendanceStatus() {
        float attendancePercentage = calculateAttendance();
        System.out.println("Attendance Percentage: " + attendancePercentage + "%");
        if (attendancePercentage >= attendanceGoal) {
            System.out.println("Attendance goal met.");
        } else {
            System.out.println("Attendance goal not met.");
        }
    }

    public int getTotalClasses() {
        return totalClasses;
    }

    public int getClassesAttended() {
        return classesAttended;
    }

    public int getAttendanceGoal() {
        return attendanceGoal;
    }
} */
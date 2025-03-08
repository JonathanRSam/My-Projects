import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.HashMap;
import java.util.Map;

public class MainAppSwing extends JPanel {

    private static final String[] DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    private static final Map<String, JTextField> timetableMap = new HashMap<>();
    private static final DefaultTableModel examModel = new DefaultTableModel(new String[]{"Subject", "Date", "Priority"}, 0);

    private static final Color CLASS_COLOR = new Color(173, 216, 230);  
    private static final Color STUDY_COLOR = new Color(144, 238, 144); 
    private static final Color PLAY_COLOR = new Color(255, 182, 193);
    private static final Color REST_COLOR = new Color(255, 255, 224);   

    public MainAppSwing() {
        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JPanel timetableGrid = createTimetableGrid();
        JPanel examSection = createExamSection();

        JScrollPane scrollPane = new JScrollPane(this);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

        add(timetableGrid);
        add(examSection);
    }

    private JPanel createTimetableGrid() {
        JPanel grid = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        for (int i = 0; i < DAYS.length; i++) {
            gbc.gridx = i + 1;
            gbc.gridy = 0;
            grid.add(new JLabel(DAYS[i]), gbc);
        }

        for (int row = 1; row <= 9; row++) {
            gbc.gridx = 0;
            gbc.gridy = row;
            grid.add(new JLabel("Period " + row), gbc);  
            for (int col = 0; col < DAYS.length; col++) {
                JTextField cell = createEditableCell("Classroom/Subject");
                gbc.gridx = col + 1;
                grid.add(cell, gbc);
                String cellKey = DAYS[col] + row;
                timetableMap.put(cellKey, cell);
            }
        }

        JButton updateButton = new JButton("Update Timetable for Free Time");
        updateButton.addActionListener(e -> updateTimetableForActivities());
        gbc.gridx = 0;
        gbc.gridy = 10;
        gbc.gridwidth = DAYS.length + 1;
        grid.add(updateButton, gbc);

        return grid;
    }

    private JTextField createEditableCell(String placeholder) {
        JTextField cell = new JTextField(10);
        cell.setToolTipText(placeholder);
        cell.addActionListener(e -> {
            String text = cell.getText().toLowerCase();
            if (text.contains("study")) {
                cell.setBackground(STUDY_COLOR);
            } else if (text.contains("play")) {
                cell.setBackground(PLAY_COLOR);
            } else if (text.contains("rest")) {
                cell.setBackground(REST_COLOR);
            } else {
                cell.setBackground(CLASS_COLOR);
            }
        });
        return cell;
    }

    private void updateTimetableForActivities() {
        for (Map.Entry<String, JTextField> entry : timetableMap.entrySet()) {
            JTextField cell = entry.getValue();
            if (cell.getText().trim().isEmpty()) {
                cell.setText("Rest");
                cell.setBackground(REST_COLOR);
            }
        }
    }

    private JPanel createExamSection() {
        JPanel examPanel = new JPanel();
        examPanel.setLayout(new BoxLayout(examPanel, BoxLayout.Y_AXIS));

        JTable examTable = new JTable(examModel);
        JScrollPane tableScrollPane = new JScrollPane(examTable);

        JTextField subjectField = new JTextField(10);
        JTextField dateField = new JTextField(10);
        JTextField priorityField = new JTextField(10);

        JButton addExamButton = new JButton("Add Exam");
        addExamButton.addActionListener((ActionEvent e) -> {
            String subject = subjectField.getText();
            String date = dateField.getText();
            String priority = priorityField.getText();

            if (!subject.isEmpty() && !date.isEmpty() && !priority.isEmpty()) {
                examModel.addRow(new String[]{subject, date, priority});
                subjectField.setText("");
                dateField.setText("");
                priorityField.setText("");
            }
        });

        JButton removeExamButton = new JButton("Remove Selected Exam");
        removeExamButton.addActionListener(e -> {
            int selectedRow = examTable.getSelectedRow();
            if (selectedRow != -1) {
                examModel.removeRow(selectedRow);
            }
        });

        JPanel inputPanel = new JPanel();
        inputPanel.add(new JLabel("Subject:"));
        inputPanel.add(subjectField);
        inputPanel.add(new JLabel("Date:"));
        inputPanel.add(dateField);
        inputPanel.add(new JLabel("Priority:"));
        inputPanel.add(priorityField);
        inputPanel.add(addExamButton);
        inputPanel.add(removeExamButton);

        examPanel.add(tableScrollPane);
        examPanel.add(inputPanel);

        return examPanel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Student Timetable and Exam Manager");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(800, 600);
            frame.setLocationRelativeTo(null);

            MainAppSwing mainPanel = new MainAppSwing();
            frame.add(mainPanel);
            frame.setVisible(true);
        });
    }
}


/* import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.util.HashMap;
import java.util.Map;

public class MainAppSwing extends JFrame {

    private static final String[] DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    private static final Map<String, JTextField> timetableMap = new HashMap<>();
    private static final DefaultTableModel examModel = new DefaultTableModel(new String[]{"Subject", "Date", "Priority"}, 0);

    private static final Color CLASS_COLOR = new Color(173, 216, 230);  
    private static final Color STUDY_COLOR = new Color(144, 238, 144); 
    private static final Color PLAY_COLOR = new Color(255, 182, 193);
    private static final Color REST_COLOR = new Color(255, 255, 224);   

    public MainAppSwing() 
    {
        setTitle("Student Timetable and Exam Manager");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(800, 600);
        setLocationRelativeTo(null);

        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS));
        mainPanel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        JPanel timetableGrid = createTimetableGrid();
        JPanel examSection = createExamSection();

        JScrollPane scrollPane = new JScrollPane(mainPanel);
        scrollPane.setVerticalScrollBarPolicy(JScrollPane.VERTICAL_SCROLLBAR_ALWAYS);

        mainPanel.add(timetableGrid);
        mainPanel.add(examSection);

        add(scrollPane);
    }

    private JPanel createTimetableGrid() {
        JPanel grid = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(5, 5, 5, 5);

        for (int i = 0; i < DAYS.length; i++) {
            gbc.gridx = i + 1;
            gbc.gridy = 0;
            grid.add(new JLabel(DAYS[i]), gbc);
        }

        for (int row = 1; row <= 9; row++) {
            gbc.gridx = 0;
            gbc.gridy = row;
            grid.add(new JLabel("Period " + row), gbc);  
            for (int col = 0; col < DAYS.length; col++) {
                JTextField cell = createEditableCell("Classroom/Subject");
                gbc.gridx = col + 1;
                grid.add(cell, gbc);
                String cellKey = DAYS[col] + row;
                timetableMap.put(cellKey, cell);
            }
        }

        JButton updateButton = new JButton("Update Timetable for Free Time");
        updateButton.addActionListener(e -> updateTimetableForActivities());
        gbc.gridx = 0;
        gbc.gridy = 10;
        gbc.gridwidth = DAYS.length + 1;
        grid.add(updateButton, gbc);

        return grid;
    }

    private JTextField createEditableCell(String placeholder) {
        JTextField cell = new JTextField(10);
        cell.setToolTipText(placeholder);
        cell.addActionListener(e -> {
            String text = cell.getText().toLowerCase();
            if (text.contains("study")) {
                cell.setBackground(STUDY_COLOR);
            } else if (text.contains("play")) {
                cell.setBackground(PLAY_COLOR);
            } else if (text.contains("rest")) {
                cell.setBackground(REST_COLOR);
            } else {
                cell.setBackground(CLASS_COLOR);
            }
        });
        return cell;
    }

    private void updateTimetableForActivities() {
        for (Map.Entry<String, JTextField> entry : timetableMap.entrySet()) {
            JTextField cell = entry.getValue();
            if (cell.getText().trim().isEmpty()) {
                cell.setText("Rest");
                cell.setBackground(REST_COLOR);
            }
        }
    }

    private JPanel createExamSection() {
        JPanel examPanel = new JPanel();
        examPanel.setLayout(new BoxLayout(examPanel, BoxLayout.Y_AXIS));

        JTable examTable = new JTable(examModel);
        JScrollPane tableScrollPane = new JScrollPane(examTable);

        JTextField subjectField = new JTextField(10);
        JTextField dateField = new JTextField(10);
        JTextField priorityField = new JTextField(10);

        JButton addExamButton = new JButton("Add Exam");
        addExamButton.addActionListener((ActionEvent e) -> {
            String subject = subjectField.getText();
            String date = dateField.getText();
            String priority = priorityField.getText();

            if (!subject.isEmpty() && !date.isEmpty() && !priority.isEmpty()) {
                examModel.addRow(new String[]{subject, date, priority});
                subjectField.setText("");
                dateField.setText("");
                priorityField.setText("");
            }
        });

        JButton removeExamButton = new JButton("Remove Selected Exam");
        removeExamButton.addActionListener(e -> {
            int selectedRow = examTable.getSelectedRow();
            if (selectedRow != -1) {
                examModel.removeRow(selectedRow);
            }
        });

        JPanel inputPanel = new JPanel();
        inputPanel.add(new JLabel("Subject:"));
        inputPanel.add(subjectField);
        inputPanel.add(new JLabel("Date:"));
        inputPanel.add(dateField);
        inputPanel.add(new JLabel("Priority:"));
        inputPanel.add(priorityField);
        inputPanel.add(addExamButton);
        inputPanel.add(removeExamButton);

        examPanel.add(tableScrollPane);
        examPanel.add(inputPanel);

        return examPanel;
    }

    public static void main(String[] args) 
    {
        SwingUtilities.invokeLater(() -> {
            MainAppSwing frame = new MainAppSwing();
            frame.setVisible(true);
        });
    }
} */
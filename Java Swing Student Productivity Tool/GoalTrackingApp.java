import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;
import java.util.ArrayList;

public class GoalTrackingApp extends JPanel {
    private GoalManager goalManager;
    private JPanel goalPanelContainer;

    public GoalTrackingApp() {
        goalManager = new GoalManager();
        setupUI();
    }

    private void setupUI() {
        setLayout(new BorderLayout()); // Use BorderLayout for the panel layout

        // Container for goals
        goalPanelContainer = new JPanel();
        goalPanelContainer.setLayout(new BoxLayout(goalPanelContainer, BoxLayout.Y_AXIS));

        // Add Goal Button
        JButton addGoalButton = new JButton("Add New Goal");
        addGoalButton.addActionListener(e -> showAddGoalDialog());

        // Add components to the main panel
        add(addGoalButton, BorderLayout.NORTH);
        add(new JScrollPane(goalPanelContainer), BorderLayout.CENTER);

        refreshGoalsDisplay();
    }

    // Show dialog to add a new goal
    private void showAddGoalDialog() {
        JTextField goalNameField = new JTextField();
        JTextField targetField = new JTextField();
        JTextField deadlineField = new JTextField();

        JPanel dialogPanel = new JPanel(new GridLayout(3, 2));
        dialogPanel.add(new JLabel("Goal Name:"));
        dialogPanel.add(goalNameField);
        dialogPanel.add(new JLabel("Target Progress (%):"));
        dialogPanel.add(targetField);
        dialogPanel.add(new JLabel("Deadline (YYYY-MM-DD):"));
        dialogPanel.add(deadlineField);

        int result = JOptionPane.showConfirmDialog(this, dialogPanel, "Add New Goal", JOptionPane.OK_CANCEL_OPTION);
        if (result == JOptionPane.OK_OPTION) {
            try {
                String goalName = goalNameField.getText();
                int target = Integer.parseInt(targetField.getText());
                LocalDate deadline = LocalDate.parse(deadlineField.getText());

                Goal newGoal = new Goal(goalName, target, deadline);
                goalManager.addGoal(newGoal);
                refreshGoalsDisplay();
            } catch (Exception e) {
                JOptionPane.showMessageDialog(this, "Invalid input. Please check your entries.");
            }
        }
    }

    // Refresh the display of goals
    private void refreshGoalsDisplay() {
        goalPanelContainer.removeAll();
        for (Goal goal : goalManager.getGoals()) {
            JPanel goalPanel = createGoalPanel(goal);
            goalPanelContainer.add(goalPanel);
        }
        goalPanelContainer.revalidate();
        goalPanelContainer.repaint();
    }

    // Create a JPanel to display a goal and its tasks
    private JPanel createGoalPanel(Goal goal) {
        JPanel goalPanel = new JPanel(new BorderLayout());
        goalPanel.setBorder(BorderFactory.createTitledBorder(goal.getName()));

        // Progress bar
        JProgressBar progressBar = new JProgressBar(0, 100);
        progressBar.setValue(goal.getCurrentProgress());
        progressBar.setStringPainted(true);

        // Task list display
        JPanel taskPanel = new JPanel();
        taskPanel.setLayout(new BoxLayout(taskPanel, BoxLayout.Y_AXIS));
        for (Task task : goal.getTasks()) {
            JPanel taskItemPanel = createTaskPanel(goal, task, progressBar);
            taskPanel.add(taskItemPanel);
        }

        // Add Task button
        JButton addTaskButton = new JButton("Add Task");
        addTaskButton.addActionListener(e -> showAddTaskDialog(goal, progressBar));

        // Goal status
        JLabel statusLabel = new JLabel("Status: " + goal.getStatus());
        goalPanel.add(progressBar, BorderLayout.NORTH);
        goalPanel.add(new JScrollPane(taskPanel), BorderLayout.CENTER);
        goalPanel.add(statusLabel, BorderLayout.SOUTH);
        goalPanel.add(addTaskButton, BorderLayout.EAST);

        return goalPanel;
    }

    // Show dialog to add a new task to a specific goal
    private void showAddTaskDialog(Goal goal, JProgressBar progressBar) {
        String taskDescription = JOptionPane.showInputDialog(this, "Enter Task Description:");
        if (taskDescription != null && !taskDescription.isEmpty()) {
            Task newTask = new Task(taskDescription);
            goal.addTask(newTask);
            goal.updateProgress();
            refreshGoalsDisplay();
        }
    }

    // Create a JPanel for each task to allow completion toggling
    private JPanel createTaskPanel(Goal goal, Task task, JProgressBar progressBar) {
        JPanel taskPanel = new JPanel(new BorderLayout());

        JCheckBox taskCheckBox = new JCheckBox(task.getDescription(), task.isComplete());
        taskCheckBox.addActionListener(e -> {
            task.markComplete(taskCheckBox.isSelected());
            goal.updateProgress();
            progressBar.setValue(goal.getCurrentProgress());
            refreshGoalsDisplay();
        });

        taskPanel.add(taskCheckBox, BorderLayout.CENTER);
        return taskPanel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Goal Tracking App");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(500, 500);
            frame.setLocationRelativeTo(null);

            GoalTrackingApp appPanel = new GoalTrackingApp();
            frame.add(appPanel);

            frame.setVisible(true);
        });
    }
}



/* import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.time.LocalDate;
import java.util.ArrayList;

public class GoalTrackingApp {
    private JFrame frame;
    private GoalManager goalManager;
    private JPanel goalPanelContainer;

    public GoalTrackingApp() {
        goalManager = new GoalManager();
        setupUI();
    }

    private void setupUI() {
        frame = new JFrame("Goal Tracking App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);

        // Main panel layout
        goalPanelContainer = new JPanel();
        goalPanelContainer.setLayout(new BoxLayout(goalPanelContainer, BoxLayout.Y_AXIS));

        // Add Goal Button
        JButton addGoalButton = new JButton("Add New Goal");
        addGoalButton.addActionListener(e -> showAddGoalDialog());

        // Panel to hold everything
        JPanel mainPanel = new JPanel(new BorderLayout());
        mainPanel.add(addGoalButton, BorderLayout.NORTH);
        mainPanel.add(new JScrollPane(goalPanelContainer), BorderLayout.CENTER);

        frame.add(mainPanel);
        frame.setVisible(true);

        refreshGoalsDisplay();
    }

    // Show dialog to add a new goal
    private void showAddGoalDialog() {
        JTextField goalNameField = new JTextField();
        JTextField targetField = new JTextField();
        JTextField deadlineField = new JTextField();

        JPanel dialogPanel = new JPanel(new GridLayout(3, 2));
        dialogPanel.add(new JLabel("Goal Name:"));
        dialogPanel.add(goalNameField);
        dialogPanel.add(new JLabel("Target Progress (%):"));
        dialogPanel.add(targetField);
        dialogPanel.add(new JLabel("Deadline (YYYY-MM-DD):"));
        dialogPanel.add(deadlineField);

        int result = JOptionPane.showConfirmDialog(frame, dialogPanel, "Add New Goal", JOptionPane.OK_CANCEL_OPTION);
        if (result == JOptionPane.OK_OPTION) {
            String goalName = goalNameField.getText();
            int target = Integer.parseInt(targetField.getText());
            LocalDate deadline = LocalDate.parse(deadlineField.getText());

            Goal newGoal = new Goal(goalName, target, deadline);
            goalManager.addGoal(newGoal);
            refreshGoalsDisplay();
        }
    }

    // Refresh the display of goals
    private void refreshGoalsDisplay() {
        goalPanelContainer.removeAll();
        for (Goal goal : goalManager.getGoals()) {
            JPanel goalPanel = createGoalPanel(goal);
            goalPanelContainer.add(goalPanel);
        }
        goalPanelContainer.revalidate();
        goalPanelContainer.repaint();
    }

    // Create a JPanel to display a goal and its tasks
    private JPanel createGoalPanel(Goal goal) {
        JPanel goalPanel = new JPanel(new BorderLayout());
        goalPanel.setBorder(BorderFactory.createTitledBorder(goal.getName()));

        // Progress bar
        JProgressBar progressBar = new JProgressBar(0, 100);
        progressBar.setValue(goal.getCurrentProgress());
        progressBar.setStringPainted(true);

        // Task list display
        JPanel taskPanel = new JPanel();
        taskPanel.setLayout(new BoxLayout(taskPanel, BoxLayout.Y_AXIS));
        for (Task task : goal.getTasks()) {
            JPanel taskItemPanel = createTaskPanel(goal, task, progressBar);
            taskPanel.add(taskItemPanel);
        }

        // Add Task button
        JButton addTaskButton = new JButton("Add Task");
        addTaskButton.addActionListener(e -> showAddTaskDialog(goal, progressBar));

        // Goal status
        JLabel statusLabel = new JLabel("Status: " + goal.getStatus());
        goalPanel.add(progressBar, BorderLayout.NORTH);
        goalPanel.add(new JScrollPane(taskPanel), BorderLayout.CENTER);
        goalPanel.add(statusLabel, BorderLayout.SOUTH);
        goalPanel.add(addTaskButton, BorderLayout.EAST);

        return goalPanel;
    }

    // Show dialog to add a new task to a specific goal
    private void showAddTaskDialog(Goal goal, JProgressBar progressBar) {
        String taskDescription = JOptionPane.showInputDialog(frame, "Enter Task Description:");
        if (taskDescription != null && !taskDescription.isEmpty()) {
            Task newTask = new Task(taskDescription);
            goal.addTask(newTask);
            goal.updateProgress();
            refreshGoalsDisplay();
        }
    }

    // Create a JPanel for each task to allow completion toggling
    private JPanel createTaskPanel(Goal goal, Task task, JProgressBar progressBar) {
        JPanel taskPanel = new JPanel(new BorderLayout());

        JCheckBox taskCheckBox = new JCheckBox(task.getDescription(), task.isComplete());
        taskCheckBox.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                task.markComplete(taskCheckBox.isSelected());
                goal.updateProgress();
                progressBar.setValue(goal.getCurrentProgress());
                refreshGoalsDisplay();
            }
        });

        taskPanel.add(taskCheckBox, BorderLayout.CENTER);
        return taskPanel;
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(GoalTrackingApp::new);
    }
}
    */
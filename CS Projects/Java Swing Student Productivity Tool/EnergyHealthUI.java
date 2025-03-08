import java.time.LocalDate;
import javax.swing.*;
import java.awt.*;
import java.util.List;

public class EnergyHealthUI extends JPanel {
    private EnergyHealthTracker tracker;

    public EnergyHealthUI() {
        tracker = new EnergyHealthTracker();
        initializeUI();
    }

    private void initializeUI() {
        setLayout(new BorderLayout()); // Use BorderLayout for the panel layout

        // Input Panel
        JPanel inputPanel = new JPanel(new GridLayout(3, 2));
        JLabel energyLabel = new JLabel("Energy Level (1-10):");
        JTextField energyField = new JTextField(3);
        JLabel sleepLabel = new JLabel("Sleep Hours:");
        JTextField sleepField = new JTextField(3);
        JButton submitButton = new JButton("Submit");
        inputPanel.add(energyLabel);
        inputPanel.add(energyField);
        inputPanel.add(sleepLabel);
        inputPanel.add(sleepField);
        inputPanel.add(new JLabel()); // Empty cell for spacing
        inputPanel.add(submitButton);

        // Output Panel
        JTextArea recommendationsArea = new JTextArea(10, 40);
        recommendationsArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(recommendationsArea);

        // Graph and Report Panel
        JPanel analysisPanel = new JPanel();
        JButton showGraphButton = new JButton("Show Weekly Trends");
        JButton showReportButton = new JButton("Show Weekly Report");
        analysisPanel.add(showGraphButton);
        analysisPanel.add(showReportButton);

        // Adding Panels to the Main Panel
        add(inputPanel, BorderLayout.NORTH);
        add(scrollPane, BorderLayout.CENTER);
        add(analysisPanel, BorderLayout.SOUTH);

        // Submit Button Action
        submitButton.addActionListener(e -> {
            try {
                int energyLevel = Integer.parseInt(energyField.getText());
                double sleepHours = Double.parseDouble(sleepField.getText());
                tracker.addEntry(new EnergyHealthEntry(LocalDate.now(), energyLevel, sleepHours));

                recommendationsArea.setText(generateDailyRecommendations(energyLevel, sleepHours));
                energyField.setText("");
                sleepField.setText("");
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Please enter valid numbers for energy and sleep.");
            }
        });

        // Show Graph Button Action
        showGraphButton.addActionListener(e -> showWeeklyGraph(tracker.getLastWeekEntries()));

        // Show Report Button Action
        showReportButton.addActionListener(e -> {
            String report = tracker.generateWeeklyReport();
            recommendationsArea.setText(report);
        });
    }

    private String generateDailyRecommendations(int energyLevel, double sleepHours) {
        StringBuilder recommendations = new StringBuilder();

        if (energyLevel < 5) {
            recommendations.append("Low energy today. Consider light tasks or rest.\n");
        } else if (energyLevel > 7) {
            recommendations.append("Great energy! You can focus on challenging tasks.\n");
        }

        if (sleepHours < 6) {
            recommendations.append("Insufficient sleep. Aim for at least 6-8 hours.\n");
        } else if (sleepHours > 8) {
            recommendations.append("Oversleeping may lead to fatigue. Try balancing sleep.\n");
        } else {
            recommendations.append("Good sleep duration. Keep it up!\n");
        }

        return recommendations.toString();
    }

    private void showWeeklyGraph(List<EnergyHealthEntry> entries) {
        JFrame graphFrame = new JFrame("Weekly Trends");
        graphFrame.setSize(600, 400);
        graphFrame.setLayout(new BorderLayout());

        // Create a custom JPanel to draw the chart
        JPanel chartPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawBarChart(g, entries);
            }
        };
        chartPanel.setPreferredSize(new Dimension(500, 300));
        graphFrame.add(chartPanel, BorderLayout.CENTER);

        graphFrame.setVisible(true);
    }

    private void drawBarChart(Graphics g, List<EnergyHealthEntry> entries) {
        int barWidth = 40;
        int spaceBetweenBars = 10;
        int xStart = 50; // X position to start drawing
        int yStart = 250; // Y position for the baseline
        int maxHeight = 150; // Maximum height for the bars (used for scaling)

        // Calculate maximum energy level and sleep hours for scaling
        int maxEnergy = entries.stream().mapToInt(EnergyHealthEntry::getEnergyLevel).max().orElse(10);
        double maxSleep = entries.stream().mapToDouble(EnergyHealthEntry::getSleepHours).max().orElse(8);

        for (int i = 0; i < entries.size(); i++) {
            EnergyHealthEntry entry = entries.get(i);

            // Scale the energy and sleep data to fit the graph
            int energyHeight = (int) ((entry.getEnergyLevel() / (double) maxEnergy) * maxHeight);
            int sleepHeight = (int) ((entry.getSleepHours() / maxSleep) * maxHeight);

            // Draw energy bars
            g.setColor(Color.BLUE);
            g.fillRect(xStart + i * (barWidth + spaceBetweenBars), yStart - energyHeight, barWidth, energyHeight);

            // Draw sleep bars
            g.setColor(Color.GREEN);
            g.fillRect(xStart + i * (barWidth + spaceBetweenBars) + barWidth / 2, yStart - sleepHeight, barWidth,
                    sleepHeight);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame("Energy & Health Tracker");
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(700, 700);
            frame.setLocationRelativeTo(null);

            EnergyHealthUI panel = new EnergyHealthUI();
            frame.add(panel);

            frame.setVisible(true);
        });
    }
}


/* 
import java.time.LocalDate;
import javax.swing.*;
import java.awt.*;
import java.util.List;

public class EnergyHealthUI {
    private EnergyHealthTracker tracker;

    public EnergyHealthUI() {
        tracker = new EnergyHealthTracker();
        initializeUI();
    }

    private void initializeUI() {
        JFrame frame = new JFrame("Energy & Health Tracker");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(700, 700);
        frame.setLayout(new BorderLayout());

        // Input Panel
        JPanel inputPanel = new JPanel(new GridLayout(3, 2));
        JLabel energyLabel = new JLabel("Energy Level (1-10):");
        JTextField energyField = new JTextField(3);
        JLabel sleepLabel = new JLabel("Sleep Hours:");
        JTextField sleepField = new JTextField(3);
        JButton submitButton = new JButton("Submit");
        inputPanel.add(energyLabel);
        inputPanel.add(energyField);
        inputPanel.add(sleepLabel);
        inputPanel.add(sleepField);
        inputPanel.add(new JLabel()); // Empty cell for spacing
        inputPanel.add(submitButton);

        // Output Panel
        JTextArea recommendationsArea = new JTextArea(10, 40);
        recommendationsArea.setEditable(false);
        JScrollPane scrollPane = new JScrollPane(recommendationsArea);

        // Graph and Report Panel
        JPanel analysisPanel = new JPanel();
        JButton showGraphButton = new JButton("Show Weekly Trends");
        JButton showReportButton = new JButton("Show Weekly Report");
        analysisPanel.add(showGraphButton);
        analysisPanel.add(showReportButton);

        // Adding Panels to Frame
        frame.add(inputPanel, BorderLayout.NORTH);
        frame.add(scrollPane, BorderLayout.CENTER);
        frame.add(analysisPanel, BorderLayout.SOUTH);

        // Submit Button Action
        submitButton.addActionListener(e -> {
            try {
                int energyLevel = Integer.parseInt(energyField.getText());
                double sleepHours = Double.parseDouble(sleepField.getText());
                tracker.addEntry(new EnergyHealthEntry(LocalDate.now(), energyLevel, sleepHours));

                recommendationsArea.setText(generateDailyRecommendations(energyLevel, sleepHours));
                energyField.setText("");
                sleepField.setText("");
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(frame, "Please enter valid numbers for energy and sleep.");
            }
        });

        // Show Graph Button Action
        showGraphButton.addActionListener(e -> showWeeklyGraph(tracker.getLastWeekEntries()));

        // Show Report Button Action
        showReportButton.addActionListener(e -> {
            String report = tracker.generateWeeklyReport();
            recommendationsArea.setText(report);
        });

        frame.setVisible(true);
    }

    private String generateDailyRecommendations(int energyLevel, double sleepHours) {
        StringBuilder recommendations = new StringBuilder();

        if (energyLevel < 5) {
            recommendations.append("Low energy today. Consider light tasks or rest.\n");
        } else if (energyLevel > 7) {
            recommendations.append("Great energy! You can focus on challenging tasks.\n");
        }

        if (sleepHours < 6) {
            recommendations.append("Insufficient sleep. Aim for at least 6-8 hours.\n");
        } else if (sleepHours > 8) {
            recommendations.append("Oversleeping may lead to fatigue. Try balancing sleep.\n");
        } else {
            recommendations.append("Good sleep duration. Keep it up!\n");
        }

        return recommendations.toString();
    }

    private void showWeeklyGraph(List<EnergyHealthEntry> entries) {
        JFrame graphFrame = new JFrame("Weekly Trends");
        graphFrame.setSize(600, 400);
        graphFrame.setLayout(new BorderLayout());

        // Create a custom JPanel to draw the chart
        JPanel chartPanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                drawBarChart(g, entries);
            }
        };
        chartPanel.setPreferredSize(new Dimension(500, 300));
        graphFrame.add(chartPanel, BorderLayout.CENTER);

        graphFrame.setVisible(true);
    }

    private void drawBarChart(Graphics g, List<EnergyHealthEntry> entries) {
        int barWidth = 40;
        int spaceBetweenBars = 10;
        int xStart = 50; // X position to start drawing
        int yStart = 250; // Y position for the baseline
        int maxHeight = 150; // Maximum height for the bars (used for scaling)

        // Calculate maximum energy level and sleep hours for scaling
        int maxEnergy = entries.stream().mapToInt(EnergyHealthEntry::getEnergyLevel).max().orElse(10);
        double maxSleep = entries.stream().mapToDouble(EnergyHealthEntry::getSleepHours).max().orElse(8);

        for (int i = 0; i < entries.size(); i++) {
            EnergyHealthEntry entry = entries.get(i);

            // Scale the energy and sleep data to fit the graph
            int energyHeight = (int) ((entry.getEnergyLevel() / (double) maxEnergy) * maxHeight);
            int sleepHeight = (int) ((entry.getSleepHours() / maxSleep) * maxHeight);

            // Draw energy bars
            g.setColor(Color.BLUE);
            g.fillRect(xStart + i * (barWidth + spaceBetweenBars), yStart - energyHeight, barWidth, energyHeight);

            // Draw sleep bars
            g.setColor(Color.GREEN);
            g.fillRect(xStart + i * (barWidth + spaceBetweenBars) + barWidth / 2, yStart - sleepHeight, barWidth,
                    sleepHeight);
        }
    }

    public static void main(String[] args) {
        new EnergyHealthUI();
    }
}
*/
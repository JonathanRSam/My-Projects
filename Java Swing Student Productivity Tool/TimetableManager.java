import java.util.HashMap;
import java.util.Map;

public class TimetableManager {

    private static final String[] DAYS = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday"};
    private static Map<String, String> timetableMap = new HashMap<>();
    private static DefaultTableModel examModel = new DefaultTableModel(new String[]{"Subject", "Date", "Priority"}, 0);
  
    private static void initializeTimetable() 
    {
        for (String day : DAYS) {
            for (int period = 1; period <= 9; period++) {
                timetableMap.put(day + period, "Classroom/Subject");
            }
        }
    }

    private static void updateTimetableForActivities() 
    {
        for (Map.Entry<String, String> entry : timetableMap.entrySet()) {
            if (entry.getValue().trim().isEmpty()) {
                timetableMap.put(entry.getKey(), "Rest");
            }
        }
    }

    private static void displayTimetable() 
    {
        System.out.println("Timetable:");
        for (String day : DAYS) {
            System.out.print(day + ": ");
            for (int period = 1; period <= 9; period++) {
                System.out.print(timetableMap.get(day + period) + " ");
            }
            System.out.println();
        }
    }

    private static void addExam(String subject, String date, String priority) 
    {
        examModel.addRow(new String[]{subject, date, priority});
    }

    private static void displayExams() {
        System.out.println("Exams:");
        for (int i = 0; i < examModel.getRowCount(); i++) {
            System.out.println("Subject: " + examModel.getValueAt(i, 0) +
                               ", Date: " + examModel.getValueAt(i, 1) +
                               ", Priority: " + examModel.getValueAt(i, 2));
        }
    }

    private static class DefaultTableModel {
        public void addRow(Object[] rowData) {
            System.out.println("Added row: " + String.join(", ", rowData));
        }

        public int getRowCount() {
            return 1; 
        }

        public Object getValueAt(int row, int column) {
            switch (row) {
                case 0:
                    switch (column) {
                        case 0: return "Mathematics";
                        case 1: return "2023-10-05";
                        case 2: return "High";
                    }
                default:
                    return null;
            }
        }
    }
}
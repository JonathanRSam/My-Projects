import java.time.LocalDate;
import java.util.ArrayList;

class Goal {
    private String name;
    private int target; // Target progress percentage
    private int currentProgress;
    private LocalDate deadline;
    private String status; // "In Progress", "Completed", "Missed"
    private ArrayList<Task> tasks;

    public Goal(String name, int target, LocalDate deadline) {
        this.name = name;
        this.target = target;
        this.currentProgress = 0;
        this.deadline = deadline;
        this.status = "In Progress";
        this.tasks = new ArrayList<>();
    }

    public void addTask(Task task) {
        tasks.add(task);
        updateProgress(); // Recalculate progress when a new task is added
    }

    public void updateProgress() {
        int completedTasks = (int) tasks.stream().filter(Task::isComplete).count();
        currentProgress = (int) ((double) completedTasks / tasks.size() * 100);

        // Update status based on progress and deadline
        if (currentProgress >= target) {
            status = "Completed";
        } else if (LocalDate.now().isAfter(deadline)) {
            status = "Missed";
        } else {
            status = "In Progress";
        }
    }

    // Getters
    public String getName() { return name; }
    public int getCurrentProgress() { return currentProgress; }
    public String getStatus() { return status; }
    public LocalDate getDeadline() { return deadline; }
    public ArrayList<Task> getTasks() { return tasks; }
}
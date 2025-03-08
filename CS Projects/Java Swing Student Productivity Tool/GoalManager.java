import java.util.ArrayList;

class GoalManager {
    private ArrayList<Goal> goals;

    public GoalManager() {
        this.goals = new ArrayList<>();
    }

    public void addGoal(Goal goal) {
        goals.add(goal);
    }

    public void updateGoalProgress() {
        for (Goal goal : goals) {
            goal.updateProgress();
        }
    }

    public ArrayList<Goal> getGoals() { return goals; }
}

class Task {
    private String description;
    private boolean isComplete;

    public Task(String description) {
        this.description = description;
        this.isComplete = false;
    }

    // Mark the task complete or incomplete based on the checkbox state
    public void markComplete(boolean complete) {
        this.isComplete = complete;
    }

    // Getters
    public boolean isComplete() { return isComplete; }
    public String getDescription() { return description; }
}

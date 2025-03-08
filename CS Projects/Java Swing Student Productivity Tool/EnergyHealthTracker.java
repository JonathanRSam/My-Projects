import java.time.LocalDate;
import java.time.temporal.ChronoUnit;
import java.util.ArrayList;
import java.util.List;

public class EnergyHealthTracker {
    private ArrayList<EnergyHealthEntry> entries;

    public EnergyHealthTracker() {
        entries = new ArrayList<>();
    }

    public void addEntry(EnergyHealthEntry entry) {
        entries.add(entry);
    }

    public List<EnergyHealthEntry> getEntries() {
        return entries;
    }

    public double calculateAverageEnergyLevel() {
        int totalEnergy = 0;
        for (EnergyHealthEntry entry : entries) {
            totalEnergy += entry.getEnergyLevel();
        }
        return entries.size() > 0 ? totalEnergy / (double) entries.size() : 0;
    }

    public double calculateAverageSleepHours() {
        double totalSleep = 0;
        for (EnergyHealthEntry entry : entries) {
            totalSleep += entry.getSleepHours();
        }
        return entries.size() > 0 ? totalSleep / entries.size() : 0;
    }

    public List<EnergyHealthEntry> getLastWeekEntries() {
        LocalDate today = LocalDate.now();
        List<EnergyHealthEntry> lastWeekEntries = new ArrayList<>();
        for (EnergyHealthEntry entry : entries) {
            if (ChronoUnit.DAYS.between(entry.getDate(), today) <= 7) {
                lastWeekEntries.add(entry);
            }
        }
        return lastWeekEntries;
    }

    public String generateWeeklyReport() {
        List<EnergyHealthEntry> lastWeekEntries = getLastWeekEntries();
        if (lastWeekEntries.isEmpty()) {
            return "No data entered in the last week.";
        }

        double avgEnergy = lastWeekEntries.stream().mapToInt(EnergyHealthEntry::getEnergyLevel).average().orElse(0);
        double avgSleep = lastWeekEntries.stream().mapToDouble(EnergyHealthEntry::getSleepHours).average().orElse(0);

        StringBuilder report = new StringBuilder();
        report.append("Weekly Trends:\n");
        report.append(String.format("- Average Energy Level: %.2f\n", avgEnergy));
        report.append(String.format("- Average Sleep Hours: %.2f\n", avgSleep));

        if (avgEnergy < 5) {
            report.append("Energy levels were low. Consider lightening your workload.\n");
        } else if (avgEnergy > 7) {
            report.append("Great energy levels! Keep it up!\n");
        }

        if (avgSleep < 6) {
            report.append("Insufficient sleep recorded. Aim for 6-8 hours per night.\n");
        } else if (avgSleep > 8) {
            report.append("You may be oversleeping. Try balancing sleep and waking hours.\n");
        } else {
            report.append("Your sleep schedule is healthy. Well done!\n");
        }

        return report.toString();
    }
}

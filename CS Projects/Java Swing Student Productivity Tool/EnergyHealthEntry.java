import java.time.LocalDate;

public class EnergyHealthEntry {
    private LocalDate date;
    private int energyLevel;
    private double sleepHours;

    public EnergyHealthEntry(LocalDate date, int energyLevel, double sleepHours) {
        this.date = date;
        this.energyLevel = energyLevel;
        this.sleepHours = sleepHours;
    }

    public LocalDate getDate() {
        return date;
    }

    public int getEnergyLevel() {
        return energyLevel;
    }

    public double getSleepHours() {
        return sleepHours;
    }
}

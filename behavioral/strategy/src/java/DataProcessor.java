// Context
public class DataProcessor {
    private SortStrategy strategy;

    public void setStrategy(SortStrategy strategy) {
        this.strategy = strategy;
    }

    public void processData(int[] data) {
        this.strategy.sort(data);
    }
}
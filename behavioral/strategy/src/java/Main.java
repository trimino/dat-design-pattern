import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        DataProcessor dataProcessor = new DataProcessor();
        int[] data = {5, 2, 9, 1, 5, 6};

        // Using Quick Sort
        dataProcessor.setStrategy(new QuickSortStrategy());
        dataProcessor.processData(data);

        System.out.println("Quick Sort: " + Arrays.toString(data));
        data = new int[]{5, 2, 9, 1, 5, 6};

        // Using Merge Sort
        dataProcessor.setStrategy(new MergeSortStrategy());
        dataProcessor.processData(data);

        System.out.println("Merge Sort: " + Arrays.toString(data));
        data = new int[]{5, 2, 9, 1, 5, 6};

        // Using Bubble Sort
        dataProcessor.setStrategy(new BubbleSortStrategy());
        dataProcessor.processData(data);

        System.out.println("Bubble Sort: " + Arrays.toString(data));
    }
}

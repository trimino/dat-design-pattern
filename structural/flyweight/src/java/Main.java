import java.awt.*;



public class Main {
    static int CANVAS_SIZE = 500;
    static int TREES_TO_DRAW = 10;
    static int TREE_TYPES = 2;

    public static void main(String[] args) {
        Forest forest = new Forest();
        for (int i = 0; i < (double) (TREES_TO_DRAW / TREE_TYPES); i++) {
            forest.plantTree(random(0, CANVAS_SIZE), random(0, CANVAS_SIZE), "Summer Oak", Color.GREEN, "Oak texture sub");
            forest.plantTree(random(0, CANVAS_SIZE), random(0, CANVAS_SIZE), "Autumn Oak", Color.ORANGE, "Autumn Oak texture sub");
        }

        forest.setSize(CANVAS_SIZE, CANVAS_SIZE);
        forest.setVisible(true);

        int withFlyweight = ((TREES_TO_DRAW * 8 + TREE_TYPES * 30) / 1024 / 1024);
        int withoutFlyweight = ((TREES_TO_DRAW * 38) / 1024 / 1024);

        System.out.println(TREES_TO_DRAW + " trees drawn");
        System.out.println("-----------------------------");
        System.out.println("Memory usage: ");
        System.out.println("Tree size (8 bytes) * " + TREES_TO_DRAW);
        System.out.println("TreeTypes size (~30 bytes) * "  + TREE_TYPES);
        System.out.println("-----------------------------");
        System.out.println("Total With Flyweight: " + withFlyweight + "MB");
        System.out.println("Total Without Flyweight: " + withoutFlyweight + "MB");
    }

    private static int random(int min, int max) {
        return min + (int) (Math.random() * ((max - min) + 1));
    }
}

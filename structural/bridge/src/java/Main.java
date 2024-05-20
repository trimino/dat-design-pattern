public class Main {
    public static void main(String[] args) {
        ApplicationDatabase db = new ApplicationDatabase();
        db.connect();
        db.executeQuery("SELECT * from tableInMySqlDatabase;");
        db.disconnect();

        System.out.println("\nSwitching database...\n");

        db.switchDbImplementation();
        db.connect();
        db.executeQuery("SELECT * FROM orders;");
        db.disconnect();
    }
}
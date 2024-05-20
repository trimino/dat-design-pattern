// Concrete Implementation A
public class MySqlDriver implements DatabaseDriver {
    @Override
    public void connect() {
        System.out.println("Connecting to MYSQL database...");
    }

    @Override
    public void disconnect() {
        System.out.println("Disconnecting from MYSQL database...");
    }

    @Override
    public void executeQuery(String query) {
        System.out.println("Executing MYSQL query: " + query);
    }
}
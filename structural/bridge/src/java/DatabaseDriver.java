// Implementation Interface
public interface DatabaseDriver {
    void connect();
    void disconnect();
    void executeQuery(String query);
}
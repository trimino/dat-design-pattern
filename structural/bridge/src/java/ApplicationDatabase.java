// Client Interface
public class ApplicationDatabase {
    protected DatabaseDriver databaseDriver;
    private Boolean isMySql;

    public ApplicationDatabase() {
        this.databaseDriver = new MySqlDriver();
        this.isMySql = true;
    }

    public void connect() {
        databaseDriver.connect();
    }

    public void disconnect() {
        databaseDriver.disconnect();
    }

    public void executeQuery(String query) {
        databaseDriver.executeQuery(query);
    }

    public void switchDbImplementation() {
        if (this.isMySql) {
            this.databaseDriver = new PostgreSqlDriver();
            this.isMySql = false;
        }
        else {
            this.databaseDriver = new MySqlDriver();
            this.isMySql = true;
        }
    }
}
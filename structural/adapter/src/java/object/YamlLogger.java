// Adaptee YAML Implementation of Adaptee Interface
public class YamlLogger implements Logger {
    @Override
    public void log(String data) {
        System.out.println("Logging YAML data: ");
        System.out.println("message: " + data + " YAML");
    }
}
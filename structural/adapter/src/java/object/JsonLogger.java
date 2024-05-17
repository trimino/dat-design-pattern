// Adaptee JSON Implementation of Adaptee Interface
public class JsonLogger implements Logger {
    @Override
    public void log(String data) {
        System.out.println("Logging JSON data: ");
        System.out.println("{message: " + data + " JSON}");
    }
}
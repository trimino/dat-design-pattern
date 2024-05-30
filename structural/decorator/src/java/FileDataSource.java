import java.io.*;

// Concrete Implementation
public class FileDataSource implements DataSource {
    private final String name;

    public FileDataSource(String name) {
        this.name = name;
    }

    @Override
    public void writeData(String data) {
        File file = new File(this.name);
        try (OutputStream fos = new FileOutputStream(file)) {
            fos.write(data.getBytes(), 0, data.length());
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    @Override
    public String readData() {
        File file = new File(this.name);
        try (FileReader reader = new FileReader(file)) {
            char[] buffer = new char[(int) file.length()];
            reader.read(buffer);
            return new String (buffer);
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
            return null;
        }
    }
}
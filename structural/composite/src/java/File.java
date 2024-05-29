// Leaf or Primitive Component A/B
public class File extends FileSystemComponent {
    private final String name;

    public File(String name) {
        this.name = name;
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void display() {
        System.out.println("File: " + this.name);
    }
}
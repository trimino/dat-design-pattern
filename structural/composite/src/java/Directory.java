import java.util.ArrayList;
import java.util.List;

// Composite Component/Composite
public class Directory extends FileSystemComponent {
    private final String name;
    private final List<FileSystemComponent> components;

    public Directory(String name) {
        this.name = name;
        this.components = new ArrayList<>();
    }

    @Override
    public void add(FileSystemComponent component) {
        this.components.add(component);
    }

    @Override
    public void remove(FileSystemComponent component) {
        this.components.remove(component);
    }

    @Override
    public FileSystemComponent getChild(int idx) {
        return this.components.get(idx);
    }

    @Override
    public String getName() {
        return this.name;
    }

    @Override
    public void display() {
        System.out.println("Directory: " + this.name);
        for (FileSystemComponent component : this.components)
            component.display();
    }
}
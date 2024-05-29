// Client
public class Main {
    public static void main(String[] args) {
        FileSystemComponent file1 = new File("File1.txt");
        FileSystemComponent file2 = new File("File2.txt");
        FileSystemComponent file3 = new File("File3.txt");

        Directory directory1 = new Directory("Directory1");
        Directory directory2 = new Directory("Directory2");

        directory1.add(file1);
        directory1.add(file2);

        directory2.add(file3);
        directory2.add(directory1);

        directory2.display();
    }
}
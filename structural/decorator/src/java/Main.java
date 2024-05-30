public class Main {
    public static void main(String[] args) {
        String salaryRecords = "Name,Salary\nJohn Smith,100000\nSteven Jobs,912000";
        DataSourceDecorator encoded = new CompressionDecorator(
                new EncryptionDecorator(
                        new FileDataSource("OutputDemo.txt")
                )
        );

        encoded.writeData(salaryRecords);
        DataSource plain = new FileDataSource("OutputDemo.txt");

        System.out.println("- Input ----------------");
        System.out.println(salaryRecords + "\n");
        System.out.println("- Encoded ----------------");
        System.out.println(plain.readData() + "\n");
        System.out.println("- Decoded ----------------");
        System.out.println(encoded.readData());
    }
}
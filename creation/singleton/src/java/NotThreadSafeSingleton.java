public final class NotThreadSafeSingleton {
    private static NotThreadSafeSingleton instance;
    public String value;

    private NotThreadSafeSingleton(String value) {
        try {
            Thread.sleep(1000);
        } catch (InterruptedException ex) {
            System.out.println("Interrupted Exception");
        }

        this.value = value;
    }

    public static NotThreadSafeSingleton getInstance(String value) {
        if (instance == null)
            instance = new NotThreadSafeSingleton(value);
        return instance;
    }
}

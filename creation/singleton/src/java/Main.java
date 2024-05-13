// Code taken from refactorguru.com

public class Main {
    public static void main(String[] args) throws InterruptedException {
        System.out.println("If you see the same value, then singleton was reused (yay!)");
        System.out.println("If you see different values, then 2 singletons were created (boo!)");
        System.out.println("You may need to run the program multiple times to see the not thread safe!");
        System.out.println("Result: ");

        Thread threadFoo = new Thread(new ThreadFoo());
        Thread threadBar = new Thread(new ThreadBar());

        threadFoo.start();
        threadBar.start();

        threadFoo.join();
        threadBar.join();

        System.out.println();

        Thread notSafeFoo = new Thread(new NotSafeThreadFoo());
        Thread notSafeBar = new Thread(new NotSafeThreadBar());

        notSafeFoo.start();
        notSafeBar.start();
    }

    static class ThreadFoo implements Runnable {
        @Override
        public void run() {
            ThreadSafeSingleton threadSafeSingleton = ThreadSafeSingleton.getInstance("FOO");
            System.out.println(threadSafeSingleton.value);
        }
    }

    static class ThreadBar implements Runnable {
        @Override
        public void run() {
            ThreadSafeSingleton threadSafeSingleton = ThreadSafeSingleton.getInstance("BAR");
            System.out.println(threadSafeSingleton.value);
        }
    }

    static class NotSafeThreadFoo implements Runnable {
        @Override
        public void run() {
            NotThreadSafeSingleton notThreadSafeSingleton = NotThreadSafeSingleton.getInstance("FOO");
            System.out.println(notThreadSafeSingleton.value);
        }
    }

    static class NotSafeThreadBar implements Runnable {
        @Override
        public void run() {
            NotThreadSafeSingleton notThreadSafeSingleton = NotThreadSafeSingleton.getInstance("BAR");
            System.out.println(notThreadSafeSingleton.value);
        }
    }
}
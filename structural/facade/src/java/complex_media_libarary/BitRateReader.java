package complex_media_libarary;

public class BitRateReader {
    public static VideoFile read(VideoFile file, Codec codec) {
        System.out.println("BitRateReader: reading file...");
        return file;
    }

    public static VideoFile convert(VideoFile buffer, Codec codec) {
        System.out.println("BitRateReader: writing file...");
        return buffer;
    }
}
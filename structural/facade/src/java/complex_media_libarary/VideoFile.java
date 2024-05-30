package complex_media_libarary;

public class VideoFile {
    private final String name;
    private final String codecType;

    public VideoFile(String name) {
        this.name = name;
        this.codecType = name.substring(name.indexOf(".") + 1);
    }

    public String getCodecType() {
        return this.codecType;
    }

    public String getName() {
        return this.name;
    }
}
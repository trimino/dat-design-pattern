package media_library;

import java.util.HashMap;

// Common Interface
public interface ThirdPartyYouTubeLib {
    HashMap<String, Video> popularVideos();

    Video getVideo(String videoId);
}
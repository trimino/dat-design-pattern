package proxy;

import media_library.ThirdPartyYouTubeClass;
import media_library.ThirdPartyYouTubeLib;
import media_library.Video;

import java.util.HashMap;

// Proxy
public class YouTubeCacheProxy implements ThirdPartyYouTubeLib {
    private ThirdPartyYouTubeLib youtubeService;
    private HashMap<String, Video> cachePopular = new HashMap<>();
    private final HashMap<String, Video> cacheAll = new HashMap<>();

    public YouTubeCacheProxy() {
        this.youtubeService = new ThirdPartyYouTubeClass();
    }

    @Override
    public HashMap<String, Video> popularVideos() {
        if (this.cachePopular.isEmpty())
            this.cachePopular = youtubeService.popularVideos();
        else
            System.out.println("Retrieved list from cache");
        return this.cachePopular;
    }

    @Override
    public Video getVideo(String videoId) {
        Video video = this.cacheAll.get(videoId);
        if (video == null) {
            video = youtubeService.getVideo(videoId);
            this.cacheAll.put(videoId, video);
        } else {
            System.out.println("Retrieved video '" + videoId + "' from cache");
        }
        return video;
    }

    public void reset() {
        cachePopular.clear();
        cacheAll.clear();
    }
}

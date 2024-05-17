import java.util.regex.Matcher;
import java.util.regex.Pattern;

// Adapter Implementation of XmlLogger
public class XmlToJsonYamlAdapter implements XmlLogger {
    private Logger logger;

    public XmlToJsonYamlAdapter(Logger logger) {
        this.logger = logger;
    }

    @Override
    public void logXmlData(XmlData xmlData) {
        // Use a regular expression to find the content between the <message> tags
        Pattern pattern = Pattern.compile("<message>(.*?)</message>");
        Matcher matcher = pattern.matcher(xmlData.data);

        if (matcher.find()) {
            String messageContent = matcher.group(1);
            logger.log(messageContent);
        } else {
            System.out.println("Data is not XML formatted");
        }
    }

    @Override
    public void setLogger(Logger logger) {
        this.logger = logger;
    }
}
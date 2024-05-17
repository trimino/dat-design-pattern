import java.util.regex.Matcher;
import java.util.regex.Pattern;

// Adaptee using Inheritance
// Notice how the logXmlData is exactly the same as the XmlToJson
public class XmlToYamlAdapter extends YamlLogger implements XmlLogger {
    @Override
    public void logXmlData(XmlData xmlData) {
        // Use a regular expression to find the content between the <message> tags
        Pattern pattern = Pattern.compile("<message>(.*?)</message>");
        Matcher matcher = pattern.matcher(xmlData.data);

        if (matcher.find()) {
            String messageContent = matcher.group(1);
            super.log(messageContent);
        } else {
            System.out.println("Data is not XML formatted");
        }
    }
}
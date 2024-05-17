// Client
public class Main {
    public static void main(String[] args) {
        XmlLogger jsonLogger = new XmlToJsonAdapter();
        XmlLogger yamlLogger = new XmlToYamlAdapter();

        XmlData xmlToJson = new XmlData("<message>Hello I am a message from XML server being logged as</message>");
        XmlData xmlToYaml = new XmlData("<message>Hello I am a message from XML server being logged as</message>");

        jsonLogger.logXmlData(xmlToJson);
        System.out.println();
        yamlLogger.logXmlData(xmlToYaml);
    }
}
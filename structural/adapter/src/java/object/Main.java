public class Main {
    public static void main(String[] args) {
        Logger jsonLogger = new JsonLogger();
        Logger yamlLogger = new YamlLogger();

        XmlLogger xmlLogger = new XmlToJsonYamlAdapter(jsonLogger);
        XmlData responseFromServer1 = new XmlData(
                "<message>Hello I am a message from XML server being logged as</message>");
        xmlLogger.logXmlData(responseFromServer1);

        System.out.println();

        xmlLogger.setLogger(yamlLogger);
        XmlData responseFromServer2 = new XmlData(
                "<message>Hello I am a message from XML server being logged as</message>");
        xmlLogger.logXmlData(responseFromServer2);
    }
}
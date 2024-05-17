from abc import ABC, abstractmethod
from re import search

# Adaptee Interface (Represents existing system)
class Logger(ABC):
    @abstractmethod
    def log(data: str) -> None:
        pass

# Adaptee JSON Implementation of Adaptee Interface
class JsonLogger(Logger):
    def log(self, data: str) -> None:
        print("Logging JSON data: ")
        print(f"{{message: {data} JSON}}")

# Adaptee YAML Implementation of Adaptee Interface
class YamlLogger(Logger):
    def log(self, data: str) -> None:
        print("Logging YAML data: ")
        print(f"message: {data} YAML")

# Class to represent formatted XML data
class XmlData:
    def __init__(self, data: str) -> None:
        self.data = data

# Client/Target Interface
class XmlLogger(ABC):
    @abstractmethod
    def logXmlData(data: XmlData) -> None:
        pass

    @abstractmethod
    def setLogger(logger: Logger) -> None:
        pass

# Adapter
class XmlToJsonYamlAdapter(XmlLogger):
    def __init__(self, logger: Logger) -> None:
        super().__init__()
        self.logger = logger
    
    def logXmlData(self, xmlData: XmlData) -> None:
        # Use a regular expression to find the content between the <message> tags
        match = search(r'<message>(.*?)</message>', xmlData.data)
        if match:
            message_content = match.group(1)
            self.logger.log(message_content)
        else:
            print("No message tag found.")

    def setLogger(self, logger: Logger) -> None:
        self.logger = logger

# Client: main()
def main():
    jsonLogger: Logger = JsonLogger()
    yamlLogger: Logger = YamlLogger()

    xmlLogger: XmlLogger = XmlToJsonYamlAdapter(jsonLogger)
    xmlData: XmlData = XmlData("<message>Hello I am a message from XML server being logged as</message>")
    xmlLogger.logXmlData(xmlData)

    print()

    xmlLogger.setLogger(yamlLogger)
    xmlData = XmlData("<message>Hello I am a message from XML server being logged as</message>")
    xmlLogger.logXmlData(xmlData)

if __name__ == "__main__":
    main()
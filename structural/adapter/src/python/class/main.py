from abc import ABC, abstractmethod
from re import search

# Adaptee JSON Implementation of Adaptee Interface
class JsonLogger:
    def log(self, data: str) -> None:
        print("Logging JSON data: ")
        print(f"{{message: {data} JSON}}")

# Adaptee YAML Implementation of Adaptee Interface
class YamlLogger:
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

# Adapter
class XmlToJsonAdapter(JsonLogger):
    def logXmlData(self, xmlData: XmlData) -> None:
        # Use a regular expression to find the content between the <message> tags
        match = search(r'<message>(.*?)</message>', xmlData.data)
        if match:
            message_content = match.group(1)
            super().log(message_content)
        else:
            print("No message tag found.")

# Adapter
class XmlToYamlAdapter(YamlLogger):
    def logXmlData(self, xmlData: XmlData) -> None:
        # Use a regular expression to find the content between the <message> tags
        match = search(r'<message>(.*?)</message>', xmlData.data)
        if match:
            message_content = match.group(1)
            super().log(message_content)
        else:
            print("No message tag found.")

# Client: main()
def main():
    jsonLogger: XmlToJsonAdapter = XmlToJsonAdapter()
    yamlLogger: XmlToYamlAdapter = XmlToYamlAdapter()

    xmlData: XmlData = XmlData("<message>Hello I am a message from XML server being logged as</message>")
    jsonLogger.logXmlData(xmlData)

    print()

    xmlData = XmlData("<message>Hello I am a message from XML server being logged as</message>")
    yamlLogger.logXmlData(xmlData)

if __name__ == "__main__":
    main()
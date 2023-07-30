import tempfile,os
from datetime import datetime

class FileManager:
    def __init__(self):
        self.location = None
        
        self.changeLocation(tempfile.gettempdir() + "/fshare/")

    def changeLocation(self, path):
        if (not os.path.exists(path)):
            os.mkdir(path)
        self.location = path

    def getStrSize(self, filepath):
        size = os.path.getsize(filepath)
        if (size < 1000):
            return f"<1 KB"
        elif (size <= 1000*1000):
            return f"{size//1000} KB"
        elif (size <= 1000*1000*1000):
            return f"{size//1000_000} MB"
        else:
            return f"{size//1000_000_000} GB"

    def getFileData(self):
        data = []
        files = sorted( os.listdir(self.location), key= lambda item: os.path.getctime(f"{self.location}/{item}"), reverse=True )

        for file in files:
            file_created = datetime.fromtimestamp(os.path.getctime(f"{self.location}/{file}")).strftime("%Y/%m/%d %H:%M")
            file_size = self.getStrSize(f"{self.location}/{file}")

            item = [file, self.location, file_created, file_size]
            data.append(item)
        return data

    def removeFile(self, file):
        if (self.getFilePath(file)):
            os.remove(f"{self.location}/{file}")

    def saveFile(self, name, data):
        f = open(f"{self.location}/{name}", 'wb')
        f.write(data)
        f.close()
        print(f"{self.location}/{name}")

    def getFilePath(self, file):
        if (file not in os.listdir(self.location)):
            return None
        else:
            return f"{self.location}/{file}"
def readData():
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            return file.read().split("\n")
    except FileNotFoundError as error:
        print("nullo")
    return []

def readPartecipantiData():
    try:
        with open("partecipanti.txt", "r", encoding="utf-8") as file:
            return file.read().split("\n")
    except FileNotFoundError as error:
        print("nullo")
    return []

def showData(index):
    return readData()[index]


def createData(data, writeMode):
    try:
        with open("data.txt", writeMode, encoding="utf-8") as file:
            file.write(data)
    except FileNotFoundError as error:
        print("file non trovato")


def updateData(index, data):
    fileList = readData()
    fileList[int(index)]= data
    dataString = "\n".join(fileList)
    createData(dataString, "w")

def deleteData(index):
    fileList = readData()
    el = fileList.pop(index)
    dataString = "\n".join(fileList)
    createData(dataString, "w")
    return el

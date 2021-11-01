class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")
    dataOpen.write(siteURL+"\n")
    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')
    for dataShow in dataOpen:
      print(dataShow)
    dataOpen.close()
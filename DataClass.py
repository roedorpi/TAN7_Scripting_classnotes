from time import gmtime, strftime

class DataClass():

    def __init__(self, DataFile = 'test.csv'):
        self.datafile = DataFile
        self.responses = list()


    def dataupdate(self,StringToFile='',response=int()):
        tid = strftime("%a %d %b, %Y %H:%M:%S\n", gmtime())
        self.responses.append(response)
        with open(self.datafile,'a') as file:
            file.write(StringToFile + ',' + tid)
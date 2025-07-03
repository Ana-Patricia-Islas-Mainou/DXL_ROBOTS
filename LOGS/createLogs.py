def buildFileLogger(surfaceName, runName):
    # nombre de columnas
    header= ["t, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18\n"] # construir con motors[i].ID

    fn = "LOGS/" + surfaceName + "/" + runName + "_POSITION.csv";     posFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_SPEED.csv";        speFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_CURRENT.csv";      curFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_VOLTAGE.csv";      volFile = open(fn, "w")
    fn = "LOGS/" + surfaceName + "/" + runName + "_TEMPERATURE.csv";  temFile = open(fn, "w")

    posFile.writelines(header)
    speFile.writelines(header)
    curFile.writelines(header)
    volFile.writelines(header)
    temFile.writelines(header)

    return posFile, speFile, curFile, volFile, temFile

def closeFileLogger(files):
    for i in range(0,len(files)):
        files[i].close()

def writeToFIle(filename, data):
    filename.writelines(data)
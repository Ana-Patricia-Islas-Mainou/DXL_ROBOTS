from HUMANOID.HUMANOID_MOVEMENTS import *
from DXL_PROTOCOLS.DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *
from LOGS.createLogs import *

# DEFINE ROBOT ...
robot = HUMANOID_MOVEMENT("B32") # NOMBRE DE LA CARPETA CON POSES ROBOT
arms = [DXL_P2(1), DXL_P2(2),DXL_P2(3), DXL_P2(4), DXL_P2(5), DXL_P2(6)]


# CREATE FILES FOR LOGGER ...
surfaceName = "FLAT"
runName = "TEST2"

posFile, speFile, curFile, volFile, temFile = buildFileLogger(surfaceName, runName)
files = [posFile, speFile, curFile, volFile, temFile]


startCom() # START ROBOT COMMS ... 

# LET ARMS BE STILL DURING WALKING ...
for i in range(0,len(arms)):
    arms[i].setTorque(1)

### ESCRIBIR EL PROGRAMA PRINCIPAL AQUI --------------------------------------------------

robot.setMotorsTorque(1)

robot.start()
time.sleep(10)


#print([p, s,c,v,t])

#robot.Tpose()
tf = 0.6; radio = 2.5
Xzmp = 8.2; yzmp = 4.2
giro  =0; step = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]; s = len(step)
pAr, sAr, cAr, vAr, tAr = robot.walk_CartModel(Xzmp,  yzmp, radio, giro, tf, step, s, 1)

writeToFIle(posFile, pAr)
writeToFIle(speFile, sAr)
writeToFIle(curFile, cAr)
writeToFIle(volFile, vAr)
writeToFIle(temFile, tAr)

robot.start()

#robot.shutdown()
for i in range(0,len(arms)):
    arms[i].setTorque(0)
#robot.shutdown()"""

### --------------------------------------------------------------------------------------
 # NO ELIMINAR 
stopCom() # STOP ROBOT COMMS
closeFileLogger(files) # CLOSE LOGGER FILES
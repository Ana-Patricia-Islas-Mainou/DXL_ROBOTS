from HUMANOID.HUMANOID_MOVEMENTS import *
from DXL_PROTOCOLS.DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *

robot = HUMANOID_MOVEMENT("B32") # NOMBRE DE LA CARPETA CON POSES ROBOT
arms = [DXL_P2(1), DXL_P2(2),DXL_P2(3), DXL_P2(4), DXL_P2(5), DXL_P2(6)]

startCom() # NO ELIMINAR 

for i in range(0,len(arms)):
    arms[i].setTorque(1)

### ESCRIBIR EL PROGRAMA PRINCIPAL AQUI --------------------------------------------------

robot.setMotorsTorque(1)
#p, s, c, v, t = robot.moveRobotByQVals_Sync(p1s,1)
robot.start()


#print([p, s,c,v,t])

#robot.Tpose()
tf = 0.4; radio = 2.5
Xzmp = 8.5; yzmp = 4.8
giro  =0; step = [1,2,2,2,2,2,2,2,2,2,2,3]; s = len(step)
pAr, sAr, cAr, vAr, tAr = robot.walk_CartModel(Xzmp,  yzmp, radio, giro, tf, step, s, 1)

print(sAr)
print(cAr)
print(vAr)
print(tAr)

robot.start()

robot.shutdown()
for i in range(0,len(arms)):
    arms[i].setTorque(0)
#robot.shutdown()"""
stopCom()
### --------------------------------------------------------------------------------------
 # NO ELIMINAR 
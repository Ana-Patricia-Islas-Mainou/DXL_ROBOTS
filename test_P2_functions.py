from DXL_PROTOCOLS.DXL_PROTOCOL2.ROBOT_P2_FUNC import *
from time import sleep
robot = ROBOT_P2()

# Iniciar la comunicacion
startCom()

# Encender torque de los motores
robot.setMotorsTorque(1)
#robot.motors[0].setTorque(1)


"""
robot.qf = [2048]*18
robot.setMotorsPosition()
sleep(5)
print(robot.getMotorsPosition())"""


des_pos = [2048]*3
des_pos.append(0.3) # play time
des_pos.append(0) # pause

des_pos2 = [1081, 1805, 2123]
des_pos2.append(0.3) # play time
des_pos2.append(0) # pause

print(des_pos)
#print(des_pos2)


robot.moveRobotByQVals(home_vals)
#robot.moveRobotByQVals(des_pos2)

# NOTA SYNC READ NO SIRVE SI 1 MOTOR ESTA MAL
# NOTA PRIMERO MOVER SIN SYNC Y DESPUES CON SYNC 
p, s, c, v, t = robot.moveRobotByQVals_Sync(des_pos2,1)
print([p, s,c,v,t])
p, s, c, v, t = robot.moveRobotByQVals_Sync(des_pos,1)
print([p, s,c,v,t])
p, s, c, v, t = robot.moveRobotByQVals_Sync(des_pos2,1)
print([p, s,c,v,t])

des_pos[-1] = 0.2
p, s, c, v, t = robot.moveRobotByQVals_Sync(des_pos,1)
print([p, s,c,v,t])

robot.setMotorsTorque(0)

stopCom()
ROBOT_NAME  = "ROBOT_1"

from ROBOT_P2_FUNC import *
from time import sleep
robot = ROBOT_P2()

startCom()

robot.setMotorsTorque(1)

"""
robot.qf = [2048]*18
robot.setMotorsPosition()
sleep(5)
print(robot.getMotorsPosition())"""


des_pos = [2048]*18
des_pos.append(5) # play time
des_pos.append(0) # pause

des_pos2 = robot.getMotorsPosition()
des_pos2.append(5) # play time
des_pos2.append(0) # pause

robot.moveRobotByQVals(des_pos)
robot.moveRobotByQVals(des_pos2)
robot.setMotorsTorque(0)

print(des_pos)
stopCom()

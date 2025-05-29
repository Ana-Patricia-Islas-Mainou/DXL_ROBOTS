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

des_pos = [2048]*3
des_pos.append(0.4) # play time
des_pos.append(0) # pause

des_pos2 = [1081, 1805, 2123]
des_pos2.append(0.4) # play time
des_pos2.append(0) # pause

#print(des_pos)
#print(des_pos2)


robot.moveRobotByQVals(home_vals)
#robot.moveRobotByQVals(des_pos2)

# NOTA SYNC READ NO SIRVE SI 1 MOTOR ESTA MAL
robot.moveRobotByQVals_Sync(des_pos2)
robot.moveRobotByQVals_Sync(des_pos)
robot.moveRobotByQVals_Sync(des_pos2)
robot.moveRobotByQVals_Sync(des_pos)

robot.setMotorsTorque(0)

stopCom()


# vale la pena hacer esto???
t0 = time.time() # t0 calcs
pt = 0.5
elapsed = time.time() -t0

print("start wait")
while elapsed < pt:
    elapsed = time.time() -t0

print("stop wait")
print(elapsed)

"""
groupSyncRead = GroupSyncRead(portHandler, packetHandler, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)

# Add parameter storage for Dynamixel#1 present position value
dxl_addparam_result = groupSyncRead.addParam(13)
if dxl_addparam_result != True:
    print("[ID:%03d] groupSyncRead addparam failed" % 13)

# Add parameter storage for Dynamixel#2 present position value
dxl_addparam_result = groupSyncRead.addParam(15)
if dxl_addparam_result != True:
    print("[ID:%03d] groupSyncRead addparam failed" % 15)

dxl_comm_result = groupSyncRead.txRxPacket()
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))"""
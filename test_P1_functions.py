from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_Protocol1_Declarations import *
from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_MX.DXL_MX_Functions import *

#from DXL_PROTOCOLS.DXL_PROTOCOL1.ROBOT_P1_FUNC import *
from time import sleep

motor = DXL_MX_P1(20)

#robot = ROBOT_P1()
#robot.setMotorsTorque(1)
startCom()
motor.setTorque(1)

#robot.setMotorsTorque(1)
#robot.qf = [2048, 2048]
#robot.setMotorsPosition()
sleep(5)

motor.setTorque(0)
#robot.setMotorsTorque(0)

stopCom()
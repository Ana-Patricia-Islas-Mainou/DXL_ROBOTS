# HEADER AND DECLARATIONS FOR PROTOCOL 2
BAUDRATE                    = 2000000
PROTOCOL_VERSION            = 2.0
DEVICENAME                  = 'COM7'
#DEVICENAME                  = "/dev/ttyUSB0" #'COM7'

# CONTROL TABLE
ADDR_TORQUE_ENABLE          = 64
ADDR_GOAL_POSITION          = 116
ADDR_PRESENT_POSITION       = 132
ADDR_MOVING_SPEED           = 112

# BYTE SIZE INSTRUCTIONS
LEN_GOAL_POSITION           = 4
LEN_PRESENT_POSITION        = 4
LEN_MOVING_SPEED            = 4

# LIBRARIES
from dynamixel_sdk import *

# HANDLERS DEFINITION
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)
groupBulkWrite = GroupBulkWrite(portHandler, packetHandler)
groupBulkRead = GroupBulkRead(portHandler, packetHandler)

def startCom():
    if portHandler.openPort():
        print("Succeeded to open the port")
    else:
        print("Failed to open the port")
        print("Press any key to terminate...")

    if portHandler.setBaudRate(BAUDRATE):
        print("Succeeded to change the baudrate")
    else:
        print("Failed to change the baudrate")
        print("Press any key to terminate...")

def stopCom():
        portHandler.closePort()

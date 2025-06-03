from ROBOTS.ROBOT_P1_CONFIG import *

# CONTROL TABLE
MX_ADDR_TORQUE_ENABLE          = 24
MX_ADDR_GOAL_POSITION          = 30
MX_ADDR_PRESENT_POSITION       = 36
MX_ADDR_MOVING_SPEED           = 32

# BYTE SIZE INSTRUCTIONS
MX_LEN_GOAL_POSITION           = 2
MX_LEN_PRESENT_POSITION        = 2
MX_LEN_MOVING_SPEED            = 2

# LIBRARIES
from dynamixel_sdk import *

# HANDLERS DEFINITION
portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)
groupBulkWritePosition = GroupBulkWrite(portHandler, packetHandler)
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

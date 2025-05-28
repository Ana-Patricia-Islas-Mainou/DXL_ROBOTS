# HEADER AND DECLARATIONS FOR PROTOCOL 2
BAUDRATE                    = 2000000
PROTOCOL_VERSION            = 1.0
DEVICENAME                  = 'COM7'
#DEVICENAME                  = "/dev/ttyUSB0" #'COM7'

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

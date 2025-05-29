from DXL_PROTOCOL2.DXL_Protocol2_Declarations import *
from DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Conversions import *

class DXL_P2(DXL_P2_CONV):
    def __init__(self, ID):
        self.ID = ID
        self.torque = 0

    def setTorque(self, torque):
        self.torque = torque

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, self.ID, ADDR_TORQUE_ENABLE, self.torque)
        
        """
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Set Torque %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Set Torque %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            pass
            #if self.torque == 1: print(str(self.ID) + " Torque enabled correclty")
            #else: print(str(self.ID) + " Torque disabled correclty")
            """

    def setPosition(self, dxl_goal_position):
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, self.ID, ADDR_GOAL_POSITION, dxl_goal_position)
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Set Position %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Set Position %s" % packetHandler.getRxPacketError(dxl_error))

    def readPosition(self):
        self.present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, self.ID, ADDR_PRESENT_POSITION)
        """
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Read Position %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Read Position %s" % packetHandler.getRxPacketError(dxl_error))"""
    
    def getPosition(self):
        self.readPosition()
        return self.present_position
    
    def setSpeed(self, dxl_goal_speed):
        dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, self.ID, ADDR_MOVING_SPEED, dxl_goal_speed)
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Speed Set %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Speed Set %s" % packetHandler.getRxPacketError(dxl_error))

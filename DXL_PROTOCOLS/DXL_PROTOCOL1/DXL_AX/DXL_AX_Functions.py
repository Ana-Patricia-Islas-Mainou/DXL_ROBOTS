from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_Protocol1_Declarations import *
from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_AX.DXL_AX_Conversions import *

class DXL_AX_P1(DXL_AX_P1_CONV):
    def __init__(self, ID):
        self.ID = ID
        self.torque = 0

        # CONTROL TABLE
        self.ADDR_TORQUE_ENABLE          = 24
        self.ADDR_GOAL_POSITION          = 30
        self.ADDR_PRESENT_POSITION       = 36
        self.ADDR_MOVING_SPEED           = 32

        # BYTE SIZE INSTRUCTIONS
        self.LEN_GOAL_POSITION           = 2
        self.LEN_PRESENT_POSITION        = 2
        self.LEN_MOVING_SPEED            = 2
        
    def setTorque(self, torque):
        """
        Sets ON/OFF the Dynamixel Torque

        Parameters
        ----------
        int torque:
            must be 1 or 0. 1 for torque ON and 0 for torque OFF.
        
        int offset:
            motor offset in bits (0 deg value)   

        Returns
        -------
        None

        Raises
        ------
        Number Error
        """
        self.torque = torque

        dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, self.ID, self.ADDR_TORQUE_ENABLE, self.torque)
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Set Torque %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Set Torque %s" % packetHandler.getRxPacketError(dxl_error))
        else:
            if self.torque == 1: print(str(self.ID) + " Torque enabled correclty")
            else: print(str(self.ID) + " Torque disabled correclty")

    def setPosition(self, dxl_goal_position):
        """
        Writes the value on to Goal Position RAM table to move the motor

        Parameters
        ----------
        int dxl_goal_position:
            Dynamixel goal position in bits.
 
        Returns
        -------
        None

        Raises
        ------
        None
        """
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.ID, self.ADDR_GOAL_POSITION, dxl_goal_position)
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Set Position %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Set Position %s" % packetHandler.getRxPacketError(dxl_error))

    def readPosition(self):
        """
        Reads the value on the Present Position RAM table

        Parameters
        ----------
        None
 
        Returns
        -------
        None

        Raises
        ------
        None
        """
        self.present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, self.ID, self.ADDR_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Read Position %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Read Position %s" % packetHandler.getRxPacketError(dxl_error))
    
    def getPosition(self):
        """
        Reads and returns the dynamixel present position

        Parameters
        ----------
        None
 
        Returns
        -------
        int 
            present position in bits

        Raises
        ------
        None
        """
        self.readPosition()
        return self.present_position
    
    def setSpeed(self, dxl_goal_speed):
        """
        Writes the value to Present Speed RAM table

        Parameters
        ----------
        int dxl_goal_speed:
            Dynamixel goal speed in bits.
 
        Returns
        -------
        None

        Raises
        ------
        None
        """
        
        dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, self.ID, self.ADDR_MOVING_SPEED, dxl_goal_speed)
        if dxl_comm_result != COMM_SUCCESS:
            print(str(self.ID) + " Speed Set %s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print(str(self.ID) + " Speed Set %s" % packetHandler.getRxPacketError(dxl_error))

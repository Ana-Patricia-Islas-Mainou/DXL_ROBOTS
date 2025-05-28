from DXL_PROTOCOL2.DXL_Protocol2_Declarations import *
from DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *
from ROBOT_P2_CONFIG import *
from time import sleep

class ROBOT_P2(DXL_P2):

    def __init__(self, ROBOT_NAME):
         
        self.motors = motorConfig
        self.nMotors = numberOfMotors
        self.offsets = home_vals

        # DEFINE ARRAYS FOR ARTICULAR MOVEMENT
        self.q0 = home_vals # present position
        self.qf = home_vals # desiered position
        self.qVel = [1]*self.nMotors

        # DEFINE TIMMINGS
        self.playtime = 0
        self.pause = 0

    def moveRobotByQVals(self,qf):
        self.qf = qf
        self.playtime = qf[-2]

        self.getMotorsPosition() # get current pos
        self.calculateMotorsSpeed() # calc moving pos
        self.setMotorsSpeed() # set new moving speed
        self.setMotorsPosition() # set new goal pos
        sleep(self.playtime)

    def getMotorsPosition(self):
        qPos = []
        for i in range(0, self.nMotors):
            qPos.append(self.motors[i].getPosition())
        self.q0 = qPos
    
    """
    def setMotorsPosition(self):
        for i in range(0, self.nMotors):
            self.motors[i].setPosition(self.qf[i])"""
    
    def setMotorsPosition(self):
        for i in range(0, self.nMotors): # build the message
            param_goal_pos = [DXL_LOBYTE(DXL_LOWORD(self.qf[i])), DXL_HIBYTE(DXL_LOWORD(self.qf[i])),
                              DXL_LOBYTE(DXL_HIWORD(self.qf[i])), DXL_HIBYTE(DXL_HIWORD(self.qf[i]))]
            
            dxl_addparam_result = groupSyncWritePosition.addParam(self.motors[i].ID, param_goal_pos)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncWrite addparam failed" % self.motors[i].ID)

        dxl_comm_result = groupSyncWritePosition.txPacket() # send the message
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

        groupSyncWritePosition.clearParam() # clear comms

    """
    def setMotorsSpeed(self):
        for i in range(0, self.nMotors):
            self.motors[i].setSpeed(self.qVel[i])
        #print(self.qVel)"""
    
    def setMotorsSpeed(self):
        for i in range(0, self.nMotors): # build the message
            param_goal_speed = [DXL_LOBYTE(DXL_LOWORD(self.qf[i])), DXL_HIBYTE(DXL_LOWORD(self.qf[i])),
                              DXL_LOBYTE(DXL_HIWORD(self.qf[i])), DXL_HIBYTE(DXL_HIWORD(self.qf[i]))]
            
            dxl_addparam_result = groupSyncWriteSpeed.addParam(self.motors[i].ID, param_goal_speed)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncWrite addparam failed" % self.motors[i].ID)

        dxl_comm_result = groupSyncWriteSpeed.txPacket() # send the message
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

        groupSyncWritePosition.clearParam() # clear comms
    
    def setMotorsTorque(self,torque):
        qPos = []
        for i in range(0, self.nMotors):
            qPos.append(self.motors[i].setTorque(torque))

    def calculateMotorsSpeed(self): # cuello?? despues 
        qVel = []
        p0 = 0
        pf = 0
        for i in range(0, self.nMotors):
            
            p0 = self.bits2rad(self.q0[i], self.offsets[i])
            pf = self.bits2rad(self.qf[i], self.offsets[i]) 
            
            qVel.append(self.calcSpeedBits(p0,pf,self.playtime)) # cambiar qf18 por playtime
        self.qVel = qVel
        
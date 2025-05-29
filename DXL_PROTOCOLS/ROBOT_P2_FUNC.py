from DXL_PROTOCOL2.DXL_Protocol2_Declarations import *
from DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *

#from ROBOT_P2_CONFIG import ROBOT_NAME

#---------- aqui se debe colocar el if 
from ROBOT_P2_SPECS import * # elegir cual config cargar

from time import sleep

class ROBOT_P2(DXL_P2):

    def __init__(self):
         
        self.motors = motorConfig
        self.nMotors = numberOfMotors
        self.offsets = home_vals[0:self.nMotors]

        # DEFINE ARRAYS FOR ARTICULAR MOVEMENT
        self.q0 = home_vals[0:self.nMotors] # present position
        self.qf = home_vals[0:self.nMotors] # desiered position
        self.qVel = [1]*self.nMotors

        # DEFINE TIMMINGS
        self.playtime = 0
        self.pause = 0

        self.configGetMotorsPosition_Sync()

    def moveRobotByQVals(self,qf):
        self.qf = qf
        self.playtime = qf[-2]

        t0 = time.time() # t0 calcs
        self.getMotorsPosition() # get current pos
        self.calculateMotorsSpeed() # calc moving pos
        self.setMotorsSpeed() # SYNC set new moving speed
        self.setMotorsPosition() # SYNC set new goal pos
        tf = time.time() # tf calcs

        print("elapsed before playtime sleep: " + str(tf-t0))
        sleep((self.playtime - (tf-t0))) # stop for exactly the desiered time
        
        tf = time.time()
        print("elapsed after playtime : " + str(tf-t0))
        print("")
        
    def moveRobotByQVals_Sync(self,qf):
        self.qf = qf
        self.playtime = qf[-2]

        t0 = time.time() # t0 calcs
        self.getMotorsPosition_Sync() # get current pos
        self.calculateMotorsSpeed() # calc moving pos
        self.setMotorsSpeed() # SYNC set new moving speed
        self.setMotorsPosition() # SYNC set new goal pos
        tf = time.time() # tf calcs

        print("elapsed before playtime sleep: " + str(tf-t0))
        sleep((self.playtime - (tf-t0))) # stop for exactly the desiered time

        tf = time.time()
        print("elapsed after playtime : " + str(tf-t0))
        print("")

    def getMotorsPosition(self):
        qPos = []
        for i in range(0, self.nMotors):
            qPos.append(self.motors[i].getPosition())
        self.q0 = qPos
        return self.q0
    
    def configGetMotorsPosition_Sync(self):
        for i in range(0, self.nMotors):
            dxl_addparam_result = groupSyncReadPosition.addParam(self.motors[i].ID)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncRead addparam failed" % self.motors[i].ID)

    def getMotorsPosition_Sync(self):
        dxl_comm_result = groupSyncReadPosition.txRxPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        #else:print("READ OK")
        
        for i in range(0, self.nMotors):
            dxl_getdata_result = groupSyncReadPosition.isAvailable(self.motors[i].ID, 
                                 ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
            if dxl_getdata_result != True:
                print("[ID:%03d] groupSyncRead getdata failed" % self.motors[i].ID)
                #self.q0[i] = 0
            else: 
                self.q0[i] = groupSyncReadPosition.getData(self.motors[i].ID, 
                             ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)

        return self.q0
        
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
    
    def setMotorsSpeed(self):
        for i in range(0, self.nMotors): # build the message
            param_goal_speed = [DXL_LOBYTE(DXL_LOWORD(self.qVel[i])), DXL_HIBYTE(DXL_LOWORD(self.qVel[i])),
                              DXL_LOBYTE(DXL_HIWORD(self.qVel[i])), DXL_HIBYTE(DXL_HIWORD(self.qVel[i]))]
            
            dxl_addparam_result = groupSyncWriteSpeed.addParam(self.motors[i].ID, param_goal_speed)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncWrite addparam failed" % self.motors[i].ID)

        dxl_comm_result = groupSyncWriteSpeed.txPacket() # send the message
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))

        groupSyncWriteSpeed.clearParam() # clear comms
    
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
        
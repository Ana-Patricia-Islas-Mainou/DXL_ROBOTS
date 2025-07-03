from DXL_PROTOCOLS.DXL_PROTOCOL2.DXL_Protocol2_Declarations import *
from DXL_PROTOCOLS.DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *

from ROBOTS.ROBOT_P2_CONFIG import ROBOT_NAME

#---------- ADD ANOTHER ROBOT INSIDE THIS IF
if ROBOT_NAME == "BOGO3":
    from ROBOTS.BOGO3.BOGO3_SPECS import *
if ROBOT_NAME == "ROBOT_P2":
    from ROBOTS.ROBOT_P2_TEST.ROBOT_P2_SPECS import *
if ROBOT_NAME == "BOGO_H_LEEG_P2":
    from ROBOTS.ROBOT_HALF_LEG_P2.BOGO_HALF_LEG_P2_SPECS import *

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

        #self.configGetMotorsPosition_Sync()
        self.config_Sync()

    def moveRobotByQVals(self, qf, logger=0):
        self.qf = qf
        self.playtime = qf[-2]
        self.pause = qf[-1]

        t0 = time.time() # t0 calcs

        self.getMotorsPosition() # get current pos
        self.calculateMotorsSpeed() # calc moving pos
        self.setMotorsSpeed() # SYNC set new moving speed
        self.setMotorsPosition() # SYNC set new goal pos

        if logger:
            speedVals, currentVals, voltageVals, temperatureVals = self.getLogger()
        else: speedVals, currentVals, voltageVals, temperatureVals = 0,0,0,0
        
        tf = time.time() # tf calcs

        print("elapsed before playtime sleep_QVALS: " + str(tf-t0))                  # LOGGS
        sleep((self.playtime - (tf-t0))) # stop for exactly the desiered time
        
        #tf = time.time()                                                       # LOGGS
        #print("elapsed after playtime : " + str(tf-t0))                        # LOGGS
        #print("")                                                              # LOGGS
        sleep(self.pause)

        return self.q0, speedVals, currentVals, voltageVals, temperatureVals
        
    def moveRobotByQVals_Sync(self, qf, logger=0):
        q0 = self.qf
        print(self.q0)
        self.qf = qf
        print(self.qf)
        self.playtime = qf[-2]
        self.pause = qf[-1]
        
        t0 = time.time() # t0 calcs

        try:
            posVals = self.getMotorsPosition_Sync() # get current pos
        except:
            #self.getMotorsPosition()
            self.q0 = q0
            posVals = "0,"
            pass

        self.calculateMotorsSpeed() # calc moving pos
        self.setMotorsSpeed() # SYNC set new moving speed
        self.setMotorsPosition() # SYNC set new goal pos
        if logger:
            try:
                speedVals, currentVals, voltageVals, temperatureVals = self.getLogger()
            except:
                speedVals, currentVals, voltageVals, temperatureVals = "0, \n","0, \n","0, \n","0, \n"
        else: speedVals, currentVals, voltageVals, temperatureVals = 0,0,0,0
        tf = time.time() # tf calcs
        a = tf-t0
        b = self.playtime - a
        print("elapsed before playtime sleep: " + str(a))                  # LOGGS
        if b > 0:
            sleep(b) # stop for exactly the desiered time
        
        #tf = time.time()                                                       # LOGGS
        #print("elapsed after playtime : " + str(tf-t0))                        # LOGGS
        #print("")                                                              # LOGGS
        sleep(self.pause)

        posVals = posVals + "\n"
        return posVals, speedVals, currentVals, voltageVals, temperatureVals

    def getMotorsPosition(self):
        qPos = []
        qString = ""
        for i in range(0, self.nMotors):
            res = self.motors[i].getPosition()
            qPos.append(res)
            qString = qString + str(res) + ","
        self.q0 = qPos
        return qString
    
    def config_Sync(self):
        for i in range(0, self.nMotors):
            dxl_addparam_result = groupSyncReadPosition.addParam(self.motors[i].ID)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncRead POS addparam failed" % self.motors[i].ID)
            dxl_addparam_result = groupSyncReadSpeed.addParam(self.motors[i].ID)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncRead VEL addparam failed" % self.motors[i].ID)
            dxl_addparam_result = groupSyncReadCurrent.addParam(self.motors[i].ID)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncRead CUR addparam failed" % self.motors[i].ID)
            dxl_addparam_result = groupSyncReadVoltage.addParam(self.motors[i].ID)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncRead VOL addparam failed" % self.motors[i].ID)
            dxl_addparam_result = groupSyncReadtemperature.addParam(self.motors[i].ID)
            if dxl_addparam_result != True:
                print("[ID:%03d] groupSyncRead TMP addparam failed" % self.motors[i].ID)

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
        self.qString = ""
        for i in range(0, self.nMotors):
            dxl_getdata_result = groupSyncReadPosition.isAvailable(self.motors[i].ID, 
                                 ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
            if dxl_getdata_result != True:
                print("[ID:%03d] groupSyncRead getdata failed" % self.motors[i].ID)
                #self.q0[i] = 0
                raise Exception("Problem getting data")
            else: 
                res = groupSyncReadPosition.getData(self.motors[i].ID, 
                             ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
                self.q0[i] = res
                qString = qString + str(res) + ","

        return self.qString
    
    def getLogger(self):
        dxl_comm_result = groupSyncReadSpeed.txRxPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            raise Exception("Problem getting data")
        dxl_comm_result = groupSyncReadCurrent.txRxPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            raise Exception("Problem getting data")
        dxl_comm_result = groupSyncReadVoltage.txRxPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            raise Exception("Problem getting data")
        dxl_comm_result = groupSyncReadtemperature.txRxPacket()
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
            raise Exception("Problem getting data")

        speedVals = ""
        currentVals = ""
        voltageVals = ""
        temperatureVals=""

        for i in range(0, self.nMotors):

            # SPEED
            dxl_getdata_result = groupSyncReadSpeed.isAvailable(self.motors[i].ID, 
                                    ADDR_PRESENT_SPEED, LEN_PRESENT_SPEED)
            if dxl_getdata_result != True:
                print("[ID:%03d] groupSyncRead VEL getdata failed" % self.motors[i].ID)
                #self.q0[i] = 0
            else: 
                tmp = groupSyncReadSpeed.getData(self.motors[i].ID, 
                                ADDR_PRESENT_SPEED, LEN_PRESENT_SPEED)
                if tmp > 0x7fffffff: speedVals = speedVals + str(tmp - 4294967296) +", "
                else: speedVals = speedVals + str(tmp) + ", "
                
            # CURRENT
            dxl_getdata_result = groupSyncReadCurrent.isAvailable(self.motors[i].ID, 
                                    ADDR_PRESENT_CURRENT, LEN_PRESENT_CURRENT)
            if dxl_getdata_result != True:
                print("[ID:%03d] groupSyncRead CUR getdata failed" % self.motors[i].ID)
                #self.q0[i] = 0
            else: 
                tmp = groupSyncReadCurrent.getData(self.motors[i].ID, 
                                ADDR_PRESENT_CURRENT, LEN_PRESENT_CURRENT)
                if tmp >  0x7fff: currentVals = currentVals + str(tmp - 65536) + ", "
                else: currentVals = currentVals + str(tmp) + ", "
                
            # VOLTAGE
            dxl_getdata_result = groupSyncReadVoltage.isAvailable(self.motors[i].ID, 
                                    ADDR_PRESENT_VOLTAGE, LEN_PRESENT_VOLTAGE)
            if dxl_getdata_result != True:
                print("[ID:%03d] groupSyncRead VOL getdata failed" % self.motors[i].ID)
                #self.q0[i] = 0
            else: 
                voltageVals = voltageVals + str(groupSyncReadVoltage.getData(self.motors[i].ID, 
                                ADDR_PRESENT_VOLTAGE, LEN_PRESENT_VOLTAGE)) + ", "
                
            # TEMPERATURE
            dxl_getdata_result = groupSyncReadtemperature.isAvailable(self.motors[i].ID, 
                                    ADDR_PRESENT_TEMPERATURE, LEN_PRESENT_TEMPERATURE)
            if dxl_getdata_result != True:
                print("[ID:%03d] groupSyncRead VOL getdata failed" % self.motors[i].ID)
                #self.q0[i] = 0
            else: 
                temperatureVals = temperatureVals + str(groupSyncReadtemperature.getData(self.motors[i].ID, 
                                ADDR_PRESENT_TEMPERATURE, LEN_PRESENT_TEMPERATURE)) + ", "

        speedVals = speedVals + "\n"
        currentVals = currentVals +"\n"
        voltageVals = voltageVals + "\n"
        temperatureVals = temperatureVals + "\n"
        
        return speedVals, currentVals, voltageVals, temperatureVals

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
        
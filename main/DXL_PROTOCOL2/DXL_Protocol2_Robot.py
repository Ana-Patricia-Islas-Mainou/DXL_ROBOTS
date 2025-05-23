from DXL_PROTOCOL2.DXL_Protocol2_Functions import *
from DXL_PROTOCOL2.DXL_MX_X_Conversions import *
from time import sleep
class ROBOT_P2(DXL_P2):

    def __init__(self, ROBOT_NAME):

        # DEFINE OFFSETS FOR THE ROBOT CONFIG POS
        if ROBOT_NAME == "BOGOBOT 3.1":
            from BOGO_3_1.BOGO_3_1_positions import offsets
            from BOGO_3_1.BOGO_3_1_config import motorConfig, numberOfMotors

        if ROBOT_NAME == "BOGOBOT 3.2":
            from BOGO_3_2.BOGO_3_2_positions import offsets
            from BOGO_3_2.BOGO_3_2_config import motorConfig, numberOfMotors

        if ROBOT_NAME == "BOGOBOT 4":
            from BOGO_4.BOGO_4_positions import offsets
            from BOGO_4.BOGO_4_config import motorConfig, numberOfMotors

        if ROBOT_NAME == "TEST ROBOT":
            from TEST_robot_pos_conf import offsets, motorConfig, numberOfMotors
         
        self.motors = motorConfig
        self.nMotors = numberOfMotors
        self.offsets = offsets

        # DEFINE ARRAYS FOR ARTICULAR MOVEMENT
        self.q0 = offsets # present position
        self.qf = offsets # desiered position
        self.qVel = [1]*self.nMotors

        # DEFINE TIMMINGS
        self.playtime = 0
        # self.pause = 0

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
    
    def setMotorsPosition(self):
        for i in range(0, self.nMotors):
            self.motors[i].setPosition(self.qf[i])

    def setMotorsSpeed(self):
        for i in range(0, self.nMotors):
            self.motors[i].setSpeed(self.qVel[i])
        #print(self.qVel)
    
    def setMotorsTorque(self,torque):
        qPos = []
        for i in range(0, self.nMotors):
            qPos.append(self.motors[i].setTorque(torque))

    def calculateMotorsSpeed(self): # cuello?? despues 
        qVel = []
        p0 = 0
        pf = 0
        for i in range(0, self.nMotors):
            
            p0 = bits2rad(self.q0[i], self.offsets[i])
            pf = bits2rad(self.qf[i], self.offsets[i]) 
            
            qVel.append(calcSpeedBits(p0,pf,self.playtime)) # cambiar qf18 por playtime
        self.qVel = qVel
        
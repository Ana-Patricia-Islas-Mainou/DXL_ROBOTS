from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_Protocol1_Declarations import *
from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_MX.DXL_MX_Functions import *
from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_AX.DXL_AX_Functions import *

from ROBOTS.ROBOT_P1_CONFIG  import ROBOT_NAME

#---------- CARGAR LA CONFIGIRACION CORRECTA DEL ROBOT
if ROBOT_NAME == "ROBOT_P1":
    from ROBOTS.ROBOT_P1_TEST.ROBOT_P1_SPECS import *

from time import sleep

class ROBOT_P1():

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

    def moveRobotByQVals(self,qf):
        self.qf = qf
        self.playtime = qf[-2]
        self.pause = qf[-1]

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
        sleep(self.pause)
        
    def moveRobotByQVals_Sync(self,qf):
        self.qf = qf
        self.playtime = qf[-2]
        self.pause = qf[-1]

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
        sleep(self.pause)

    def getMotorsPosition(self):
        qPos = []
        for i in range(0, self.nMotors):
            qPos.append(self.motors[i].getPosition())
        self.q0 = qPos
        return self.q0
    
    def setMotorsPosition(self):
        for i in range(0, self.nMotors):
            self.motors[i].setPosition(self.qf[i])

    def setMotorsSpeed(self):
        for i in range(0, self.nMotors):
            self.motors[i].setSpeed(self.qVel[i])
    
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
        
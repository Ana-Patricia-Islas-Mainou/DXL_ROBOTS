from DXL_PROTOCOLS.DXL_PROTOCOL2.ROBOT_P2_FUNC import *
from HUMANOID.HUMANOID_KINEMATICS import *
from HUMANOID.ZMP_MODELS.CART_MODEL import *

class HUMANOID_MOVEMENT(ROBOT_P2):

    def __init__(self, ROBOT_NAME):
        
        if ROBOT_NAME == "BOGOBOT 3.1":
            from ROBOTS.BOGO3.B31.B31_POSES import  offsets

        if ROBOT_NAME == "BOGOBOT 3.2":
            from ROBOTS.BOGO3.B32.B32_POSES import offsets

        if ROBOT_NAME == "BOGOBOT 4":
            from ROBOTS.BOGO4.B4_POSES import  offsets
        super().__init__(ROBOT_NAME)

        self.offsets = offsets

    #def moveRobotByPose(self,pts,logger): # no esta terminado REVISAR IK BRAZOS
    #    qIK = IK_robot (pts,1,1) # new desiered position
    #    qf = self.qValsToBits(qIK,self.offsets)
    #    print(qf)
    
    def moveLegsByPose(self, pts, basePos):
        qIK = IK_robot (pts,1,0) #LEGS YES, ARMS NO
        legOffsets = self.offsets[6:18]
        qf = basePos[0:6] + self.qValsToBits(qIK,legOffsets)
        qf.append(pts[-2])
        qf.append(pts[-1])
        self.moveRobotByQVals(qf)

    def moveLegsByPose_Sync(self, pts, basePos, logger):
        qIK = IK_robot (pts,1,0) #LEGS YES, ARMS NO
        legOffsets = self.offsets[6:18]
        qf = basePos[0:6] + self.qValsToBits(qIK,legOffsets)
        qf.append(pts[-2])
        qf.append(pts[-1])
        self.moveRobotByQVals_Sync(qf, logger)

    def moveRobotByJacobian(self):
        pass

    def qValsToBits(self,qRad, offset):
        qBits = []
        for i in range(0, len(qRad)):
            qBits.append(self.rad2bits(qRad[i], offset[i]))
        return qBits
    
    def walk_CartModel(self, Xzmp,  yzmp, radio, giro, tf, step, s, offset):
        for i in range(0,s):
            t = 0
            dt = 0.1
            stop = t + tf
            #print("------------- inicio ciclo -----------")
            while (t < stop):
                pts = cartModel(Xzmp,yzmp,radio,giro,t,dt,tf,stop,i,step)
                print(pts)
                #print(pts)
                self.moveLegsByPose(pts, offset)
                # moveRobot_byPose(walk_TaskS)
                t = t + dt
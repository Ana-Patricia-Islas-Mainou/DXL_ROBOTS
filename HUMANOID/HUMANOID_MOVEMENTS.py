from DXL_PROTOCOLS.DXL_PROTOCOL2.ROBOT_P2_FUNC import *
from HUMANOID.HUMANOID_KINEMATICS import *
from HUMANOID.ZMP_MODELS.CART_MODEL import *

class HUMANOID_MOVEMENT(ROBOT_P2):

    def __init__(self, ROBOT_NAME):
        super().__init__()
        if ROBOT_NAME == "B31":
            from ROBOTS.BOGO3.B31.B31_POSES import  offsets, standPos_QVals, standPos_Pose, sitPos_QVals

        if ROBOT_NAME == "B32":
            from ROBOTS.BOGO3.B32.B32_POSES import offsets, standPos_QVals, standPos_Pose, sitPos_QVals 

        if ROBOT_NAME == "B4":
            from ROBOTS.BOGO4.B4_POSES import  offsets, standPos_QVals, standPos_Pose, sitPos_QVals
        
        #super().__init__(ROBOT_NAME)
        self.offsets = offsets
        self.standPos_Pose = standPos_Pose
        self.standPos_QVals = standPos_QVals
        self.sitPos_QVals = sitPos_QVals

    #### SPECIFIC ACTIONS ------------------------------------------------------------------
    #### -----------------------------------------------------------------------------------

    def start(self):
        self.setMotorsTorque(1)
        p, s, c, v, t = self.moveLegsByPose_Sync(self.standPos_Pose, 0,0,1)
        #print(s)

    def shutdown(self):
        self.moveRobotByQVals(self.sitPos_QVals)
        self.setMotorsTorque(0)

    def Tpose(self):
        self.moveRobotByQVals(self.offsets)
    
    def getUpBack():
        # perfom one time algorithm 
        pass

    def getUpFront():
        # perfom one time algorithm 
        pass

    def kickRight():
        # perfom one time algorithm 
        pass

    def kickLeft():
        # perfom one time algorithm 
        pass

    def walkCmdVel():
        # walking algorithms here
        pass

    def latRightWalk():
        # perfom one time algorithm 
        pass

    def latLeftWalk():
        # perfom one time algorithm 
        pass

    def oneTimeAlgorithm():
        pass



    ### DEFINITIONS TO PERFORM MOVEMENTS -------------------------------------------------
    ### ----------------------------------------------------------------------------------

    #def moveRobotByPose(self,pts,logger): # no esta terminado REVISAR IK BRAZOS
    #    qIK = IK_robot (pts,1,1) # new desiered position
    #    qf = self.qValsToBits(qIK,self.offsets)
    #    print(qf)

    def moveLegsByPose(self, pts, basePos, logger=0, t0=0.0): # privado???

        qIK = IK_robot (pts,1,0) #LEGS YES, ARMS NO
        legOffsets = self.offsets #[6:18] SE QUITA PORQUE EL ROBOT ESTÁ DEFINIDO COMO SOLO LAS PIERNAS
        #qf = basePos[0:6] + self._qValsToBits(qIK,legOffsets)
        qf = self._qValsToBits(qIK,legOffsets)
        qf.append(pts[-2])
        qf.append(pts[-1])
        #print(qf)
        p, s, c, v, t = self.moveRobotByQVals(qf, logger)
        return p, s, c, v, t

    def moveLegsByPose_Sync(self, pts, walk, extraMotor, logger=0): # privado???
        qIK = IK_robot (pts,1,0) #LEGS YES, ARMS NO
        
        legOffsets = self.offsets #[6:18] SE QUITA PORQUE EL ROBOT ESTÁ DEFINIDO COMO SOLO LAS PIERNAS
        #qf = basePos[0:6] + self._qValsToBits(qIK,legOffsets)
        qf = self._qValsToBits(qIK,legOffsets)
        qf.append(pts[-2])
        qf.append(pts[-1])
        #print(qf)
        p, s, c, v, t = self.moveRobotByQVals_Sync(qf, logger)
        return p, s, c, v, t

    def moveRobotByJacobian(self): # privado???
        pass

    def _qValsToBits(self,qRad, offset): # PRIV
        qBits = []
        for i in range(0, len(qRad)):
            qBits.append(self.rad2bits(qRad[i], offset[i]))
        return qBits
    
    #### WALKING ALGORITHMS ---------------------------------------------------------------
    #### ----------------------------------------------------------------------------------    
    
    def walk_CartModel(self, Xzmp,  yzmp, radio, giro, tf, step, s, logger=0):
        pAr, sAr, cAr, vAr, tAr = [], [], [], [], []
        tTot = 0 # LOGGER ONLY

        for i in range(0,s):
            t = 0
            dt = 0.1
            stop = t + tf
            
            #print("------------- inicio ciclo -----------")
            while (t < stop):
                #t0 = time.time() # for realtime calcs
                
                pts, extraMotor = cartModel(Xzmp,yzmp,radio,giro,t,dt,tf,stop,i,step)
                #print(pts)
                self.setMotorsTorque(1)
                p, s, c, v, tp = self.moveLegsByPose_Sync(pts, 1, extraMotor, logger)
                # moveRobot_byPose(walk_TaskS)
                t = t + dt
                tTot = tTot + dt # LOGGER ONLY

                if logger:
                    p = str(tTot) + ", " + p; 
                    s = str(tTot) + ", " + s
                    c = str(tTot) + ", " + c; v = str(tTot) + ", " + v
                    tp = str(tTot) + ", " + tp

                    pAr.append(p); sAr.append(s); cAr.append(c)
                    vAr.append(v); tAr.append(tp)
        
        return pAr, sAr, cAr, vAr, tAr
                
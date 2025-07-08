from DXL_PROTOCOLS.DXL_PROTOCOL2.ROBOT_P2_FUNC import *
from HUMANOID.HUMANOID_KINEMATICS import *
from HUMANOID.HUMANOID_JACOBIANS import *
from HUMANOID.ZMP_MODELS.CART_MODEL import *

import numpy as np

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

    def moveLegsByPose_Sync(self, pts, walk, extraMotor, logger=0, IK_NR =1): # privado???
        if IK_NR == 1:
            qIK = IK_robot (pts,1,0) #LEGS YES, ARMS NO
        else:
            qIK = self.NR_robot(pts) # MOVE LEGS WITH NEWTON RAPSHON
        
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
    

    ## 

    def NR_robot(self, pts):

        # define the pose setpoint vectors

        r_Leg_POSE_SETPOINT = np.zeros((6,1))
        r_Leg_POSE_SETPOINT[0,0] = pts[4] # x right leg REVISAR
        r_Leg_POSE_SETPOINT[1,0] = pts[5] # y right leg
        r_Leg_POSE_SETPOINT[2,0] = pts[6] # z right leg
        r_Leg_POSE_SETPOINT[3,0] = 0 # alpha
        r_Leg_POSE_SETPOINT[4,0] = 0 # theta
        r_Leg_POSE_SETPOINT[5,0] = pts[7] # gamma

        l_Leg_POSE_SETPOINT = np.zeros((6,1))
        l_Leg_POSE_SETPOINT[0,0] = pts[0] # x left leg
        l_Leg_POSE_SETPOINT[1,0] = pts[1] # y left leg
        l_Leg_POSE_SETPOINT[2,0] = pts[2] # z left leg
        l_Leg_POSE_SETPOINT[3,0] = 0 # alpha
        l_Leg_POSE_SETPOINT[4,0] = 0 # theta
        l_Leg_POSE_SETPOINT[5,0] = pts[3] # gamma

        # get the robot motor values from DXL
        m, q0 = self.getMotorsPosition()
        qR = [0.0]*12

        for i in range(0,len(q0)):
            qR[i] = self.bits2rad(q0[i], self.offsets[i])
        
        # divide the qR values for each leg
        qRight_Leg = [qR[6],qR[8],qR[10],qR[12],qR[14],qR[16]]  # q7 q9 q11q q13 q15 q17
        qLeft_Leg  = [qR[7],qR[9],qR[11],qR[13],qR[15],qR[17]] # q8 q10 q12q q14 q16 q18
        
        r_Leg_qNOW = np.zeros((6,1))
        r_Leg_qNOW[0,0] = qR[0]
        r_Leg_qNOW[1,0] = qR[2]
        r_Leg_qNOW[2,0] = qR[4]
        r_Leg_qNOW[3,0] = qR[6]
        r_Leg_qNOW[4,0] = qR[8]
        r_Leg_qNOW[5,0] = qR[10]

        l_Leg_qNOW = np.zeros((6,1))
        l_Leg_qNOW[0,0] = qR[1]
        l_Leg_qNOW[1,0] = qR[3]
        l_Leg_qNOW[2,0] = qR[5]
        l_Leg_qNOW[3,0] = qR[7]
        l_Leg_qNOW[4,0] = qR[9]
        l_Leg_qNOW[5,0] = qR[11]

        # use the forward kinematics to determine the current pose of the robot
        r_Leg_POSE = getRightLeg_POSE(qRight_Leg)
        l_Leg_POSE = getLeftLeg_POSE(qLeft_Leg)

        # get the jacobians for each leg
        r_Leg_JACOBIAN = rightLeg_Jacobian(qRight_Leg)
        l_Leg_JACOBIAN = leftLeg_Jacobian(qLeft_Leg)

        # invert the jacobians
        r_Leg_INV_JACO = np.linalg.inv(r_Leg_JACOBIAN)
        l_Leg_INV_JACO = np.linalg.inv(l_Leg_JACOBIAN)

        # calculate the error between the setpoint and the current pose
        r_Leg_ERROR = r_Leg_POSE - r_Leg_POSE_SETPOINT
        l_Leg_ERROR = l_Leg_POSE - l_Leg_POSE_SETPOINT

        # Serial.println("Current Values for Right Leg Error");
        # for (int i = 0; i<6; i = i+1){Serial.println(r_Leg_ERROR(i,0));}

        # Serial.println("Calculated Jacobian");
        # printJacobian6x6(r_Leg_JACOBIAN);

        # Serial.println("Inverted Jacobian");
        # printJacobian6x6(r_Leg_INV_JACO); r_Leg_qNOW - 
        
        # get the new values for the robot
        r_Leg_qNEW = r_Leg_qNOW - r_Leg_INV_JACO @ r_Leg_ERROR
        l_Leg_qNEW = l_Leg_qNOW - l_Leg_INV_JACO @ l_Leg_ERROR

        qF = [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
        
        # legs change to new pose
        # right leg
        qF[0] = r_Leg_qNEW[0,0] # cadera este puede girar
        qF[2] = r_Leg_qNEW[1,0] #- correctHip[0];
        qF[4] = r_Leg_qNEW[2,0]
        qF[6] = r_Leg_qNEW[3,0]
        qF[8] = r_Leg_qNEW[4,0]
        qF[10] = r_Leg_qNEW[5,0]# + ceil(correctHip[0]/5);

        # left leg
        qF[1] = l_Leg_qNEW[0,0] # cadera este puede girar
        qF[3] = l_Leg_qNEW[1,0] # + correctHip[1];
        qF[5] = l_Leg_qNEW[2,0]
        qF[7] = l_Leg_qNEW[3,0]
        qF[9] = l_Leg_qNEW[4,0]
        qF[11] = l_Leg_qNEW[5,0] # - ceil(correctHip[1]/5);

        return qF
    










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
                
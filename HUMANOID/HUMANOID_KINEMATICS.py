from math import *
import numpy as np

from ROBOTS.ROBOT_P2_CONFIG import ROBOT_NAME

#---------- ADD ANOTHER ROBOT INSIDE THIS IF
if ROBOT_NAME == "BOGO3":
    from ROBOTS.BOGO3.BOGO3_SPECS import *
if ROBOT_NAME == "BOGO4":
    from ROBOTS.BOGO4.BOGO4_SPECS import *

def IK_robot (pts, legs, arms):

    # Calcula la cinematica inversa de todas las cadenas del robot

    # piernas del robot
    L1 = L[0] 
    L2 = L[1] 
    L3 = L[2] 
    L4 = L[3]

    # brazos del robot
    D1 = L[4] 
    D2 = L[5] 
    D3 = L[6] 
    D4 = L[7]

    # IK PIERNAS ----------------------------------------------------
    # ---------------------------------------------------------------

    # IK robot pierna derecha ---------------------------------------

    # puntos deseados en el plano
    Px_alpha = pts[0] 
    Py_alpha = pts[1]  
    Pz_alpha = pts[2]  
    alpha = pts[3] 
    
    # nuevos puntos en el plano considerando la rotacion en z
    # q7
    q7 = alpha 
    c7 = cos(q7) 
    s7 = sin(q7)
    Px = Px_alpha*c7 - Py_alpha*s7
    Py = Px_alpha*s7 + Py_alpha*c7
    Pz = Pz_alpha

    #q13
    c13 = (Px**2 + Py**2 + Pz**2 - L3**2 - L4**2) / (2*L3*L4)
    c13 = max(-1,min(c13,1))
    q13 = - acos(c13) # + -  
    s13 = sin(q13)
    
    # q9
    q9 = atan2(-Py, -Pz) # o atan2(Py, Pz)
    c9 = cos(q9) 
    s9 = sin(q9)
    
    # q11
    q11 = atan2(Px, -Pz*c9 -Py*s9) - atan2(L4*s13, L3 + L4*c13)
    s11 = sin(q11) 
    c11 = cos(q11)
    q11 = atan2(s11, c11)
    
    # q15
    q15 = q13 + q11

    # q17
    q17 = q9
    
    # IK robot pierna izquierda ---------------------------------------

    # puntos deseados en el plano
    Px_alpha = pts[4]  
    Py_alpha = pts[5] 
    Pz_alpha = pts[6]  
    alpha = pts[7] 
    
    # nuevos puntos en el plano considerando la rotacion en z
    # q8
    q8 = alpha 
    c8 = cos(q8) 
    s8 = sin(q8)
    Px = Px_alpha*c8 - Px_alpha*s8
    Py = Py_alpha*s8 + Py_alpha*c8
    Pz = Pz_alpha

    #q14
    c14 = (Px**2 + Py**2 + Pz**2 - L3**2 - L4**2) / (2*L3*L4)
    c14 = max(-1,min(c14,1))
    q14 = acos(c14) # + -
    s14 = sin(q14)

    # q10
    q10 = atan2(-Py, -Pz) # o atan2(-Py, -Pz)
    c10 = cos(q10) 
    s10 = sin(q10)

    # q12
    q12 = atan2(-Px, -Pz*c10 -Py*s10) - atan2(L4*s14, L3 + L4*c14)
    s12 = sin(q12) 
    c12 = cos(q12)
    q12 = atan2(s12, c12)

    # q16
    q16 = q14 + q12
    # q18
    q18 = q10
  
    # IK BRAZOS ----------------------------------------------------
    # --------------------------------------------------------------

    # IK robot brazo derecho ---------------------------------------
    Px = pts[8]  
    Py = pts[9] 
    Pz = pts[10] 

    #q5
    c5 = (Px**2 + Py**2 + Pz**2 - D3**2 - D4**2) / (2*D3*D4)
    c5 = max(-1,min(c5,1))
    q5 = acos(c5) # + - Nota: debe ir positivo 
    s5 = sin(q5)
    
    # q1
    q1 = atan2(Px, -Pz)
    c1 = cos(q1) 
    s1 = sin(q1)
    
    # q3
    a = D4*s5 
    b = -D3-D4*c5 
    c = Py
    d = D4*s5 
    e = D3+D4*c5 
    f = -Pz*c1+Px*s1
    q3 = atan2(a*f-c*e,c*d-b*f) 
    s3 = sin(q3) 
    c3 = cos(q3)
    q3 = atan2(s3, c3)

    # IK robot brazo izquierdo -------------------------------------
    # puntos deseados en el plano
    Px = pts[11]  
    Py = pts[12]  
    Pz = pts[13] 

    #q6
    c6 = (Px**2 + Py**2 + Pz**2 - D3**2 - D4**2) / (2*D3*D4)
    c6 = max(-1,min(c6,1))
    q6 = acos(c6) # - para codo adentro
    s6 = sin(q6)
    
    # q2
    q2 = atan2(Px, Pz)
    c2 = cos(q2) 
    s2 = sin(q2)
    
    # q4
    a = -D4*s6 
    b = D3+D4*c6 
    c = -Py
    d = -D4*s6 
    e = -D3-D4*c6 
    f = Pz*c2+Px*s2
    q4 = atan2(a*f-c*e,c*d-b*f) 
    s4 = sin(q4) 
    c4 = cos(q4)
    q4 = atan2(s4, c4)

    # acomodados de cadera a pies
    if legs == 1 and arms == 1:
        q = [q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18]
    if legs == 1 and arms == 0:
        q = [q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18]
    if legs == 0 and arms == 1:
        q = [q1,q2,q3,q4,q5,q6]
    return q




def getRightLeg_POSE(qLeg):
    # piernas del robot
    L1 = L[0] 
    L2 = L[1] 
    L3 = L[2] 
    L4 = L[3]

    q7 = qLeg[0]
    q9 = qLeg[1]
    q11 = qLeg[2]
    q13 = qLeg[3]
    q15 = qLeg[4]
    q17 = qLeg[5]

    c7 = cos(q7)
    s7 = sin(q7)
    c9 = cos(q9)
    s9 = sin(q9)
    c11 = cos(q11)
    s11 = sin(q11)
    c13 = cos(q13)
    s13 = sin(q13)
    c15 = cos(q15)
    s15 = sin(q15)
    c17 = cos(q17)
    s17 = sin(q17)

    # Define the position and orientation vector
    legPose = np.zeros((6,1))

    # Calculate de position vector using FK [x;y;z]
    legPose[0,0] = L3*(c7*s11 - c11*s7*s9) + L4*(c13*(c7*s11 - c11*s7*s9) + s13*(c7*c11 + s7*s9*s11)) # x
    legPose[1,0] = - L3*(s7*s11 + c7*c11*s9) - L4*(c13*(s7*s11 + c7*c11*s9) + s13*(c11*s7 - c7*s9*s11)) # y
    legPose[2,0] = -c9*(L4*cos(q11 + q13) + L3*c11) # z

    # Calculate the orientation vector using Kajita's formula

    # rotation matrix
    r11 = s15*(c13*(c7*s11 - c11*s7*s9) + s13*(c7*c11 + s7*s9*s11)) + c15*(c13*(c7*c11 + s7*s9*s11) - s13*(c7*s11 - c11*s7*s9))
    r12 = s17*(s15*(c13*(c7*c11 + s7*s9*s11) - s13*(c7*s11 - c11*s7*s9)) - c15*(c13*(c7*s11 - c11*s7*s9) + s13*(c7*c11 + s7*s9*s11))) + c9*c17*s7
    r13 = c17*(s15*(c13*(c7*c11 + s7*s9*s11) - s13*(c7*s11 - c11*s7*s9)) - c15*(c13*(c7*s11 - c11*s7*s9) + s13*(c7*c11 + s7*s9*s11))) - c9*s7*s17

    r21 = - s15*(c13*(s7*s11 + c7*c11*s9) + s13*(c11*s7 - c7*s9*s11)) - c15*(c13*(c11*s7 - c7*s9*s11) - s13*(s7*s11 + c7*c11*s9))
    r22 = c7*c9*c17 - s17*(s15*(c13*(c11*s7 - c7*s9*s11) - s13*(s7*s11 + c7*c11*s9)) - c15*(c13*(s7*s11 + c7*c11*s9) + s13*(c11*s7 - c7*s9*s11)))
    r23 = - c17*(s15*(c13*(c11*s7 - c7*s9*s11) - s13*(s7*s11 + c7*c11*s9)) - c15*(c13*(s7*s11 + c7*c11*s9) + s13*(c11*s7 - c7*s9*s11))) - c7*c9*s17

    r31 = sin(q11 + q13 - q15)*c9
    r32 = cos(q11 + q13 - q15)*c9*s17 - c17*s9
    r33 = s9*s17 + cos(q11 + q13 - q15)*c9*c17

    # Determine if the matrix is diagonal
    ctrDiag = 0 # when this counter stays at 0 the matrix is diagonal

    if (r12 != 0): ctrDiag = ctrDiag+1
    if (r13 != 0): ctrDiag = ctrDiag+1
    if (r21 != 0): ctrDiag = ctrDiag+1
    if (r23 != 0): ctrDiag = ctrDiag+1
    if (r31 != 0): ctrDiag = ctrDiag+1
    if (r32 != 0): ctrDiag = ctrDiag+1

    k1 = 0
    k2 = 0
    k3 = 0

    if (ctrDiag == 0):
        # the matrix is diagonal
        k1 = (2*pi/2)*(r11 +1)
        k2 = (2*pi/2)*(r22 +1)
        k3 = (2*pi/2)*(r33 +1)
    
    else:
        # the matrix is not diagonal
        l1 = r32 - r23
        l2 = r13 - r31
        l3 = r21 - r12

        mag_l = sqrt(pow(l1,2) + pow(l2,2) + pow(l3,2))
        theta = atan2(mag_l, r11 + r22 + r33 -1)

        k1 = theta * (l1/mag_l)
        k2 = theta * (l2/mag_l)
        k3 = theta * (l3/mag_l)
        
    k1 = atan2(sin(k1), cos(k1))
    k2 = atan2(sin(k2), cos(k2))
    k3 = atan2(sin(k3), cos(k3))

    legPose[3,0] = k1
    legPose[4,0] = k2
    legPose[5,0] = k3

    #Serial.println("RIGHT LEG POSE");
    #for (int i = 0; i<6; i = i+1){
    #Serial.println(legPose(i,0));
    #}
    return legPose

def getLeftLeg_POSE(qLeg):
    # piernas del robot
    L1 = L[0] 
    L2 = L[1] 
    L3 = L[2] 
    L4 = L[3]

    q8 = qLeg[0]
    q10 = qLeg[1]
    q12 = qLeg[2]
    q14 = qLeg[3]
    q16 = qLeg[4]
    q18 = qLeg[5]

    c8 = cos(q8)
    s8 = sin(q8)
    c10 = cos(q10)
    s10 = sin(q10)
    c12 = cos(q12)
    s12 = sin(q12)
    c14 = cos(q14)
    s14 = sin(q14)
    c16 = cos(q16)
    s16 = sin(q16)
    c18 = cos(q18)
    s18 = sin(q18)

    # position and orientation vector
    legPose = np.zeros((6,1))

    # Calculate de position vector using FK [x;y;z]
    legPose[0,0] = - L3*(c8*s12 + c12*s8*s10) - L4*(c14*(c8*s12 + c12*s8*s10) + s14*(c8*c12 - s8*s10*s12))
    legPose[1,0] = L3*(s8*s12 - c8*c12*s10) + L4*(c14*(s8*s12 - c8*c12*s10) + s14*(c12*s8 + c8*s10*s12))
    legPose[2,0] = -c10*(L4*cos(q12 + q14) + L3*c12)

    # Calculate the orientation vector using Kajita's formula

    # rotation matrix
    r11 = sin(q16)*(cos(q14)*(cos(q8)*sin(q12) + cos(q12)*sin(q8)*sin(q10)) + sin(q14)*(cos(q8)*cos(q12) - sin(q8)*sin(q10)*sin(q12))) + cos(q16)*(cos(q14)*(cos(q8)*cos(q12) - sin(q8)*sin(q10)*sin(q12)) - sin(q14)*(cos(q8)*sin(q12) + cos(q12)*sin(q8)*sin(q10)))
    r12 = cos(q10)*cos(q18)*sin(q8) - sin(q18)*(sin(q16)*(cos(q14)*(cos(q8)*cos(q12) - sin(q8)*sin(q10)*sin(q12)) - sin(q14)*(cos(q8)*sin(q12) + cos(q12)*sin(q8)*sin(q10))) - cos(q16)*(cos(q14)*(cos(q8)*sin(q12) + cos(q12)*sin(q8)*sin(q10)) + sin(q14)*(cos(q8)*cos(q12) - sin(q8)*sin(q10)*sin(q12))))
    r13 = - cos(q18)*(sin(q16)*(cos(q14)*(cos(q8)*cos(q12) - sin(q8)*sin(q10)*sin(q12)) - sin(q14)*(cos(q8)*sin(q12) + cos(q12)*sin(q8)*sin(q10))) - cos(q16)*(cos(q14)*(cos(q8)*sin(q12) + cos(q12)*sin(q8)*sin(q10)) + sin(q14)*(cos(q8)*cos(q12) - sin(q8)*sin(q10)*sin(q12)))) - cos(q10)*sin(q8)*sin(q18)

    r21 = - sin(q16)*(cos(q14)*(sin(q8)*sin(q12) - cos(q8)*cos(q12)*sin(q10)) + sin(q14)*(cos(q12)*sin(q8) + cos(q8)*sin(q10)*sin(q12))) - cos(q16)*(cos(q14)*(cos(q12)*sin(q8) + cos(q8)*sin(q10)*sin(q12)) - sin(q14)*(sin(q8)*sin(q12) - cos(q8)*cos(q12)*sin(q10)))
    r22 = sin(q18)*(sin(q16)*(cos(q14)*(cos(q12)*sin(q8) + cos(q8)*sin(q10)*sin(q12)) - sin(q14)*(sin(q8)*sin(q12) - cos(q8)*cos(q12)*sin(q10))) - cos(q16)*(cos(q14)*(sin(q8)*sin(q12) - cos(q8)*cos(q12)*sin(q10)) + sin(q14)*(cos(q12)*sin(q8) + cos(q8)*sin(q10)*sin(q12)))) + cos(q8)*cos(q10)*cos(q18)
    r23 = cos(q18)*(sin(q16)*(cos(q14)*(cos(q12)*sin(q8) + cos(q8)*sin(q10)*sin(q12)) - sin(q14)*(sin(q8)*sin(q12) - cos(q8)*cos(q12)*sin(q10))) - cos(q16)*(cos(q14)*(sin(q8)*sin(q12) - cos(q8)*cos(q12)*sin(q10)) + sin(q14)*(cos(q12)*sin(q8) + cos(q8)*sin(q10)*sin(q12)))) - cos(q8)*cos(q10)*sin(q18)

    r31 = -sin(q12 + q14 - q16)*cos(q10)
    r32 = cos(q12 + q14 - q16)*cos(q10)*sin(q18) - cos(q18)*sin(q10)
    r33 = sin(q10)*sin(q18) + cos(q12 + q14 - q16)*cos(q10)*cos(q18)

    # Determine if the matrix is diagonal
    ctrDiag = 0; # when this counter stays at 0 the matrix is diagonal

    if (r12 != 0): ctrDiag = ctrDiag+1
    if (r13 != 0): ctrDiag = ctrDiag+1
    if (r21 != 0): ctrDiag = ctrDiag+1 
    if (r23 != 0): ctrDiag = ctrDiag+1 
    if (r31 != 0): ctrDiag = ctrDiag+1
    if (r32 != 0): ctrDiag = ctrDiag+1

    k1 = 0
    k2 = 0
    k3 = 0

    if (ctrDiag == 0):
        # the matrix is diagonal
        k1 = (2*pi/2)*(r11 +1)
        k2 = (2*pi/2)*(r22 +1)
        k3 = (2*pi/2)*(r33 +1)
        
    else:
        # the matrix is not diagonal
        l1 = r32 - r23
        l2 = r13 - r31
        l3 = r21 - r12

        mag_l = sqrt(pow(l1,2) + pow(l2,2) + pow(l3,2))
        theta = atan2(mag_l, r11 + r22 + r33 -1)

        k1 = theta * (l1/mag_l)
        k2 = theta * (l2/mag_l)
        k3 = theta * (l3/mag_l)
        

    k1 = atan2(sin(k1), cos(k1))
    k2 = atan2(sin(k2), cos(k2))
    k3 = atan2(sin(k3), cos(k3))

    legPose(3,0) = k1
    legPose(4,0) = k2
    legPose(5,0) = k3

    return legPose

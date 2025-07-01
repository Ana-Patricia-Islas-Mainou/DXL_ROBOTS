from math import *

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
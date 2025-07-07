from math import *

g = 980  
h = 1
hIK = 35

# CONSTANT DEFINITION BASED ON STEP TYPE ---------------------------------------------------
# FULL STEP 
def front( tf,  Xzmp):
    k1 = (-Xzmp)/(1-exp(sqrt(g/h)*tf))
    k2 = -k1*exp(sqrt(g/h)*tf)
    return k1, k2

# OPEN FRONT STEP 
def openFront( tf,  Xzmp):
    k1 = (-Xzmp*exp(sqrt(g/h)*tf)) / ((1-exp(sqrt(g/h)*tf))*(1+exp(sqrt(g/h)*tf)))
    k2 = -k1
    return k1, k2

# CLOSE FRONT STEP 
def closeFront( tf,  Xzmp):
    k1 = (-Xzmp) / ((1-exp(sqrt(g/h)*tf))*(1+exp(sqrt(g/h)*tf)))
    k2 = -k1*exp(2*sqrt(g/h)*tf)
    return k1, k2

# TRAYECTORY GENERATORS IN ALL AXES ---------------------------------------------------------
# FOOT TRAYECTORY IN Z
def pz(t, T, radio):
    z = -hIK +radio*(2/T)*sqrt(t*(T-t))
    return z

# ZMP TRAYECTORY IN Y
def py(t, tf, Yzmp):
    k1 = (-Yzmp)/(1+exp(sqrt(g/h)*tf))
    k2 = k1*exp(sqrt(g/h)*tf)
    return k1*exp(sqrt(g/h)*t) + k2*exp(-sqrt(g/h)*t) + Yzmp

# ZMP TRAYECTORY IN X
def px(t, k1, k2):
    a = k1*exp(sqrt(g/h)*t) + k2*exp(-sqrt(g/h)*t)
    return a

# CALCULATE ZMP TRAYECTORY BASED ON THE CASE
def zmpX_FwdCase(step, tf, Xzmp):
    if (step == 1): # open step
        #print("OPEN CASE")
        return openFront(tf, Xzmp)

    elif (step == 3): # close step
        #print("CLOSE CASE")
        return closeFront(tf, Xzmp)

    else:
        #print("WALK")
        return front(tf, Xzmp)

# SWITCH FOOT
def zmpY_foot(i,  yzmp):
    if (i%2 == 0):return -yzmp
    else: return yzmp

def sine_(t, a, x):
  w = pi/t
  return ceil(a * sin(w*x))

# CART MODEL ALGORITH 
def cartModel(Xzmp,yzmp,radio,giro,t,dt,tf,stop,i,step): #step[i] volver solo step
    #print(step[i])
    k1, k2 = zmpX_FwdCase(step[i], tf, Xzmp)
    Yzmp = zmpY_foot(i, yzmp)
    # pie fijo ---------------------------------
    # puntos del pie a la cadera
    yFijo = py(t, tf, Yzmp)
    xFijo = px(t, k1, k2)

    # puntos de la cadera al pie para pie fijo
    xFijo = -xFijo
    yFijo = -yFijo
    zFijo = -hIK

    # pie movil -------------------------------
    xMovil = 0
    yMovil = yFijo
    zMovil = pz(t, stop, radio)

    walk_TaskS = [0]*16
    extraMotor = [0,0]

    if (Yzmp > 0):# si yzmp es positivo usar pierna izq armar pose acorde
        # mover el centro de masa con la pierna izquierda 
        walk_TaskS[0] = xFijo # x left leg
        walk_TaskS[1] = yFijo # y left leg
        walk_TaskS[2] = zFijo # z left leg
        walk_TaskS[3] = giro  # alpha left leg
        extraMotor[1] = sine_(tf,35,t)

        # dar paso con la pierna derecha
        walk_TaskS[4] = xMovil # x right leg
        walk_TaskS[5] = yMovil # y right leg
        walk_TaskS[6] = zMovil # z right leg 
        walk_TaskS[7] = 0      # alpha right leg
        extraMotor[0] = 0
         
    else:
        # dar paso con la pierna izquierda
        walk_TaskS[0] = xMovil # x left leg
        walk_TaskS[1] = yMovil # y left leg
        walk_TaskS[2] = zMovil # z leftt leg  
        walk_TaskS[3] = 0      # alpha left let
        extraMotor[1] = 0

        # mover el centro de masa con la pierna derecha 
        walk_TaskS[4] = xFijo # x right leg
        walk_TaskS[5] = yFijo # y right leg
        walk_TaskS[6] = zFijo # z right leg
        walk_TaskS[7] = giro  # alpha right leg
        extraMotor[0] = sine_(tf,35,t)
        

    walk_TaskS[14] = dt
    walk_TaskS[15] = 0

    #print(walk_TaskS)
    return walk_TaskS, extraMotor
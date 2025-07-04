# BUILD DXL PROTOCOL 1 ROBOTS
from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_MX.DXL_MX_Functions import *

# MOTOR DECLARATION

DXL19 = DXL_MX_P1(19)
DXL20 = DXL_MX_P1(20)


# HARDWARE SPECS
motorConfig = [DXL19, DXL20]
numberOfMotors = len(motorConfig)

# POSICION EN HOME
home_vals = [2048,2048] #,2048,2048,2048,2048,1765,1800,2150,1946,2100,2000,2048,2048,2048,2048,2150,1946, 10, 20]
#home_vals = [2048,2048,2150,3,0]

# KINEMATIC SPECS
L = [0.53, 0.465, 18.5, 18.5, 0, 0, 20, 19] # Legs 4 numbers, Arms, 4 numbers

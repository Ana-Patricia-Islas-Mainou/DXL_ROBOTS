# ROBOT NAME:

# BUILD DXL PROTOCOL 2 ROBOTS

from DXL_PROTOCOLS.DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *

# MOTOR DECLARATION
DXL13 = DXL_P2(13)
DXL15 = DXL_P2(15)
DXL17 = DXL_P2(17)

# HARDWARE SPECS
motorConfig = [DXL13,DXL15,DXL17]
numberOfMotors = len(motorConfig)

# POSICION EN HOME
#            M1   M2   M3  PT D
home_vals = [2048,2048,2150,3,0]

# HUMANOID KINEMATIC SPECS
L = [0.53, 0.465, 18.5, 18.5, 0, 0, 20, 19] # Legs 4 numbers, Arms, 4 numbers


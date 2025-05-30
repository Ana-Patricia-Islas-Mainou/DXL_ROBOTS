from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_AX.DXL_AX_Functions import *
from DXL_PROTOCOLS.DXL_PROTOCOL1.DXL_MX.DXL_MX_Functions import *
from DXL_PROTOCOLS.DXL_PROTOCOL2.DXL_MX_X.DXL_MX_X_Functions import *

print("")

# PROTOCOL 1 CONVERSIONS

# VALIDATE FOR AX MOTOR WITH 0 DEG AT 512 BITS
home_AX = 512 # desiered position for 0 deg
motor_AX = DXL_AX_P1(1) # ID 1
print("TEST DXL AX CONVERSIONS")
print("   DXL AX ID: " + str(motor_AX.ID)) # get ID
print("   DXL AX DEG2BITS: " + str(motor_AX.deg2bits(0, home_AX))) # should show 512 (int)
print("   DXL AX BITS2DEG: " + str(motor_AX.bits2deg(512, home_AX))) # should show 0 (float)
print("   DXL AX BITS2RAD: " + str(motor_AX.bits2rad(512, home_AX))) # should show 0 (float)
print("   DXL AX RAD2BITS: " + str(motor_AX.rad2bits(0, home_AX))) # should show 512 (float)

print("")

# VALIDATE FOR MX MOTOR WITH 0 DEG AT 2048 BITS
home_MX = 2048 # desiered position for 0 deg
motor_MX = DXL_MX_P1(2) # ID 2
print("TEST DXL MX CONVERSIONS")
print("   DXL MX ID: " + str(motor_MX.ID)) # get ID
print("   DXL MX DEG2BITS: " + str(motor_MX.deg2bits(0,home_MX))) # should show 2048 (int)
print("   DXL MX BITS2DEG: " + str(motor_MX.bits2deg(2048,home_MX)))# should show 0 (float)
print("   DXL MX BITS2RAD: " + str(motor_MX.bits2rad(2048, home_MX))) # should show 0 (float)
print("   DXL MX RAD2BITS: " + str(motor_MX.rad2bits(0, home_MX))) # should show 512 (float)

print("")

# PROTOCOL 2 CONVERSIONS

home_MX_X = 2048 # desiered position for 0 deg
motor_MX_X = DXL_P2(3) # ID 3
print("TEST DXL MX-X CONVERSIONS")
print("   DXL MX-X ID: " + str(motor_MX_X.ID)) # get ID
print("   DXL MX-X DEG2BITS: " + str(motor_MX_X.deg2bits(0,home_MX_X))) # should show 2048 (int)
print("   DXL MX-X BITS2DEG: " + str(motor_MX_X.bits2deg(2048,home_MX_X)))# should show 0 (float)
print("   DXL MX-X BITS2RAD: " + str(motor_MX_X.bits2rad(2048, home_MX_X))) # should show 0 (float)
print("   DXL MX-X RAD2BITS: " + str(motor_MX_X.rad2bits(0, home_MX_X))) # should show 512 (float)

print("")
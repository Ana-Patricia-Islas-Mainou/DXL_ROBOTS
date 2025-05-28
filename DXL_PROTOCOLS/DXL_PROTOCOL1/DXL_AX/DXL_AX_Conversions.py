from math import *

class DXL_AX_P1_CONV:
  def deg2bits(self, deg, offset): # REVISAR
    return ceil(min(((deg/0.293255) + offset),1023))


  def rad2bits(self, rad, offset): # REVISAR
    return ceil(min((rad*(180.0/(0.293255 * pi)) + offset),1023))


  def bits2deg(self, bits, offset): # REVISAR
    return (bits-offset)*0.293255
  

  def bits2rad(self, bits, offset): # OK
    return (bits-offset)*((0.293255)*(pi/180.0))
  

  def calcSpeedBits(self, x0, xf, t): # OK
      rad_s = abs((xf-x0)/t)
      b = rad_s*(1/(0.1047 * 0.111)) #( rad/s->rpm * rpm->bits)

      a = min(b,1023)
      return ceil(max(1,a))
  
  def calcGradpSeg(self, posInicGrados, posFinGrados, seg): 
    gradPseg = ceil(abs(posFinGrados - posInicGrados)/seg)
    return gradPseg

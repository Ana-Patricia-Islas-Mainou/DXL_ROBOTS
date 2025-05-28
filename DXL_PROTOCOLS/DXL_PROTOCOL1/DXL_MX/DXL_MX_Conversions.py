from math import *

class DXL_MX_P1_CONV:
  def deg2bits(self, deg, offset): # OK
    return ceil(min(((deg/0.0879) + offset),4095))


  def rad2bits(self, rad, offset): # OK
    return ceil(min((rad*(180.0/(0.0879 * pi)) + offset),4095))


  def bits2deg(self, bits, offset): # OK
    return (bits-offset)*0.0879
  

  def bits2rad(self, bits, offset): # OK
    return (bits-offset)*((0.0879)*(pi/180.0))
  

  def calcSpeedBits(self, x0, xf, t): # OK
      rad_s = abs((xf-x0)/t)
      b = rad_s*(1/(0.1047 * 0.114)) #( rad/s->rpm * rpm->bits)

      a = min(b,4096)
      return ceil(max(1,a))
  

  def calcGradpSeg(self, posInicGrados, posFinGrados, seg): 
    gradPseg = ceil(abs(posFinGrados - posInicGrados)/seg)
    return gradPseg

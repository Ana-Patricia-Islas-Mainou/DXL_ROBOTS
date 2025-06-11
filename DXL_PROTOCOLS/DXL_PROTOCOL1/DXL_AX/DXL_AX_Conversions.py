from math import *

class DXL_AX_P1_CONV:
  def deg2bits(self, deg, offset): # REVISAR
    """
    Converts **degrees** to **bits** for Dynamixel
    AX using Protocol 1

    Parameters
    ----------
    float deg:
        degree value
    
    int offset:
        motor offset in bits (0 deg value)   

    Returns
    -------
    int
        degrees value expressed as bits

    Raises
    ------
    None
    """
    return ceil(min(((deg/0.293255) + offset),1023))


  def rad2bits(self, rad, offset): # REVISAR
    """
    Converts **radians** to **bits** for Dynamixel
    AX using Protocol 1

    Parameters
    ----------
    float rad:
        radians value
    
    int offset:
        motor offset in bits (0 rad value)   

    Returns
    -------
    int
        radians value expressed as bits

    Raises
    ------
    None
    """
    return ceil(min((rad*(180.0/(0.293255 * pi)) + offset),1023))


  def bits2deg(self, bits, offset): # REVISAR
    """
    Converts **bits** to **degrees** for Dynamixel
    AX using Protocol 1

    Parameters
    ----------
    int bits:
        bits value
    
    int offset:
        motor offset in bits (0 deg value)   

    Returns
    -------
    float
        bits value expressed as degrees

    Raises
    ------
    None
    """
    return (bits-offset)*0.293255
  

  def bits2rad(self, bits, offset): # OK
    """
    Converts **bits** to **radians** for Dynamixel
    AX using Protocol 1

    Parameters
    ----------
    int bits:
        degree value
    
    int offset:
        motor offset in bits (0 deg value)   

    Returns
    -------
    float
        bits value expressed as radians

    Raises
    ------
    None
    """
    return (bits-offset)*((0.293255)*(pi/180.0))
  

  def calcSpeedBits(self, x0, xf, t): # OK
    """
    Calculates the motor speed in bits per second

    Parameters
    ----------
    float x0:
        starting position in radians

    float xf:
        end position in radians

    float t:
        playtime 

    Returns
    -------
    int
        speed in rad/s expressed as bits

    Raises
    ------
    None
    """
    rad_s = abs((xf-x0)/t)
    b = rad_s*(1/(0.1047 * 0.111)) #( rad/s->rpm * rpm->bits)

    a = min(b,1023)
    return ceil(max(1,a))
  
  def calcGradpSeg(self, posInicGrados, posFinGrados, seg): 
    gradPseg = ceil(abs(posFinGrados - posInicGrados)/seg)
    return gradPseg

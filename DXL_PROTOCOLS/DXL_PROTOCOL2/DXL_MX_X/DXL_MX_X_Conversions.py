from math import *

class DXL_P2_CONV:
  def deg2bits(slef, deg, offset): # OK
    """
    Converts **degrees** to **bits** for Dynamixels
    MX and X using Protocol 2

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

    return ceil(min(((deg/0.0879) + offset),4095))


  def rad2bits(slef, rad, offset): # OK
    """
    Converts **radians** to **bits** for Dynamixels
    MX and X using Protocol 2

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

    return ceil(min((rad*(180.0/(0.0879 * pi)) + offset),4095))


  def bits2deg(slef, bits, offset): # OK
    """
    Converts **bits** to **degrees** for Dynamixels
    MX and X using Protocol 2

    Parameters
    ----------
    int bits:
        degree value
    
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

    return (bits-offset)*0.0879
  

  def bits2rad(slef, bits, offset): # OK
    """
    Converts **bits** to **radians** for Dynamixels
    MX and X using Protocol 2

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

    return (bits-offset)*((0.0879)*(pi/180.0))
  

  def calcSpeedBits(slef, x0, xf, t): # OK
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
    b = rad_s*(1/(0.1047 * 0.229)) #( rad/s->rpm * rpm->bits)

    a = min(b,32767)
    return ceil(max(1,a))
  

  def calcGradpSeg(slef, posInicGrados, posFinGrados, seg): 
    gradPseg = ceil(abs(posFinGrados - posInicGrados)/seg)
    return gradPseg

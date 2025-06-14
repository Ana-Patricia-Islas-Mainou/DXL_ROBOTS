# Class `DXL_P2_CONV` Docs

## General Information

This document explains in depth class `DXL_P2_CONV` programmed in file `DXL_MX_X_Conversions.py`.

### Purpose

The main functionality of `DXL_P2_CONV` is to perfomr conversions between dynamixel **MX**  and dynamixel **X** with firmware 41 to 45 using protocol 2 RAM table specifications.

### Availabe Functions

- [Class `DXL_P2_CONV` Docs](#class-dxl_p2_conv-docs)
  - [General Information](#general-information)
    - [Purpose](#purpose)
    - [Availabe Functions](#availabe-functions)
  - [Functions Documentations](#functions-documentations)
      - [`int: deg2bits(float deg, int offset)`](#int-deg2bitsfloat-deg-int-offset)
      - [`int: rad2bits(float rad, int offset)`](#int-rad2bitsfloat-rad-int-offset)
      - [`float: bits2deg(int bits, int offset)`](#float-bits2degint-bits-int-offset)
      - [`float: bits2rad(int bits, int offset)`](#float-bits2radint-bits-int-offset)
      - [`int: calcSpeedBits(float x0, float xf, float t)`](#int-calcspeedbitsfloat-x0-float-xf-float-t)



## Functions Documentations

#### `int: deg2bits(float deg, int offset)`

Converts **degrees** to **bits** for Dynamixels MX and X using Protocol 2.

Arguments:
+ `float deg` : degree value to be converted to bits
+ `int offset` : motor offset in bits, also known as the desiered 0 deg value in bits. For example, for half of the motor use 2048 as offset.

Returns:
+ `int` : returns the degrees value expressed as **bits**.

#### `int: rad2bits(float rad, int offset)`

Converts **radians** to **bits** for Dynamixels MX and X using Protocol 2.

Arguments:
+ `float rad` : radians value to be converted to bits
+ `int offset` : motor offset in bits, also known as the desiered 0 deg value in bits. For example, for half of the motor use 2048 as offset.

Returns:
+ `int` : returns the radians value expressed as **bits**.

#### `float: bits2deg(int bits, int offset)`

Converts **bits** to **degrees** for Dynamixels MX and X using Protocol 2

Arguments:
+ `int bits` : bits value to be converted to degrees
+ `int offset` : motor offset in bits, also known as the desiered 0 deg value in bits. For example, for half of the motor use 2048 as offset.

Returns:
+ `float` : bits value expressed as **degrees**.

#### `float: bits2rad(int bits, int offset)`

Converts **bits** to **radians** for Dynamixels MX and X using Protocol 2

Arguments:
+ `int bits` : bits value to be converted to degrees
+ `int offset` : motor offset in bits, also known as the desiered 0 deg value in bits. For example, for half of the motor use 2048 as offset.

Returns:
+ `float` : bits value expressed as **radians**.

#### `int: calcSpeedBits(float x0, float xf, float t)`

Calculates the **moving speed** in bits for Dynamixels MX and X using Protocol 2.

Arguments:
+ `float x0` : starting position in radians
+ `float xf` : end position in radians
+ `float t` : playtime

Returns:
+ `int` : speed in rad/s expressed as **bits**.
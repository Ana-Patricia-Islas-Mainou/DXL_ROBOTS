# Class `DXL_P2_CONV` Docs

## General Information

This document explains in depth class `DXL_P2_CONV` programmed in file `DXL_MX_X_Conversions.py`.

### Purpose

The main functionality of `DXL_P2_CONV` is to perfomr conversions between dynamixel **MX**  and dynamixel **X** with firmware 41 to 45 using protocol 2 RAM table specifications.

### Availabe Functions

+ [`deg2bits`](#int-deg2bitsfloat-deg-int-offset)
+ [`rad2bits`]()
+ [`bits2deg`]()


## Functions Documentations

#### `int: deg2bits(float deg, int offset)`

Converts **degrees** to **bits** for Dynamixels MX and X using Protocol 2.

Arguments:
+ `float deg` : degree value to be converted to bits
+ `int offset` : motor offset in bits, also known as the desiered 0 deg value in bits. For example, for half of the motor use 2048 as offset.

Returns:
+ `int` : returns the degrees value expressed as **bits**.
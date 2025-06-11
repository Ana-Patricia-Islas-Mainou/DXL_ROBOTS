# Class `DXL_P2` Docs

## General Information

This document explains in depth class `DXL_P2` programmed in file `DXL_MX_X_Functions.py`.

### Purpose

The main functionality of `DXL_P2` is to perfom the basic movements of dynamixel **MX**  and dynamixel **X** with firmware 41 to 45 using protocol 2 RAM table specifications.

This class needs the modules *DXL_Protocol2_Declarations* and *DXL_MX_X_Conversions* to work properly and enherits class *DXL_P2_CONV*.

### Availabe Functions

- [Class `DXL_P2` Docs](#class-dxl_p2-docs)
  - [General Information](#general-information)
    - [Purpose](#purpose)
    - [Availabe Functions](#availabe-functions)
  - [Functions Documentations](#functions-documentations)
      - [`__init__(ID)`](#__init__id)
      - [`setTorque(torque)`](#settorquetorque)
      - [`setPosition(dxl_goal_position)`](#setpositiondxl_goal_position)
      - [`readPosition()`](#readposition)
      - [`getPosition()`](#getposition)
      - [`setSpeed(dxl_goal_speed)`](#setspeeddxl_goal_speed)



## Functions Documentations

#### `__init__(ID)`

Class constructor, recieves the Dynamixel ID and sets the torque to 0 by default

Arguments:
+ `int ID` : Dynamixel ID.

#### `setTorque(torque)`

Sets ON/OFF the Dynamixel Torque

Arguments:
+ `int torque` : Dynamixel ID.

Raises:
+ `Numbher Error` : torque argument must be 1 or 0.

#### `setPosition(dxl_goal_position)`

Writes the value on to Goal Position RAM table to move the motor

Arguments:
+ `int dxl_goal_position` : Dynamixel goal position in bits.

#### `readPosition()`

Reads the value on the Present Position RAM table

#### `getPosition()`

Reads and returns the dynamixel present position.

Returns:
+ `self.present_position` : Dynamixel present position in bits.

#### `setSpeed(dxl_goal_speed)`

Writes the value to Present Speed RAM table.

Arguments:
+ `int dxl_goal_speed` : Dynamixel goal speed in bits.
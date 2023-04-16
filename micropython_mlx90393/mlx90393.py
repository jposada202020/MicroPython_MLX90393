# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT
"""
`mlx90393`
================================================================================

MicroPython Driver for the MLX90393 magnetometer sensor


* Author(s): Jose D. Montoya

Implementation Notes
--------------------

**Software and Dependencies:**

This library depends on Micropython

"""

# pylint: disable=too-many-arguments, line-too-long

from micropython import const

try:
    import struct
except ImportError:
    import ustruct as struct

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/jposada202020/MicroPython_MLX90393.git"


class CBits:
    """
    Changes bits from a byte register
    """

    def __init__(
        self,
        num_bits: int,
        register_address: int,
        start_bit: int,
        register_width=2,
        lsb_first=True,
        cmd_read=None,
        cmd_write=None,
    ) -> None:
        self.bit_mask = ((1 << num_bits) - 1) << start_bit
        self.register = register_address
        self.star_bit = start_bit
        self.lenght = register_width + 1
        self.lsb_first = lsb_first
        self.cmd_read = cmd_read
        self.cmd_write = cmd_write

    def __get__(
        self,
        obj,
        objtype=None,
    ) -> int:
        payload = bytes([self.cmd_read, self.register << 2])
        obj._i2c.writeto(obj._address, payload)

        data = bytearray(self.lenght)
        data = obj._i2c.readfrom(obj._address, self.lenght)

        mem_value = memoryview(data[1:])

        reg = 0
        order = range(len(mem_value) - 1, -1, -1)
        if not self.lsb_first:
            order = reversed(order)
        for i in order:
            reg = (reg << 8) | mem_value[i]

        reg = (reg & self.bit_mask) >> self.star_bit

        return reg

    def __set__(self, obj, value: int) -> None:
        payload = bytes([self.cmd_read, self.register << 2])
        obj._i2c.writeto(obj._address, payload)

        data = bytearray(self.lenght)
        data = obj._i2c.readfrom(obj._address, self.lenght)

        memory_value = memoryview(data[1:])

        reg = 0
        order = range(len(memory_value) - 1, -1, -1)
        if not self.lsb_first:
            order = range(0, len(memory_value))
        for i in order:
            reg = (reg << 8) | memory_value[i]
        reg &= ~self.bit_mask

        value <<= self.star_bit
        reg |= value
        reg = reg.to_bytes(self.lenght - 1, "big")

        payload = bytearray(self.lenght + 1)
        payload[0] = self.cmd_write
        payload[3] = self.register << 2
        payload[1] = reg[0]
        payload[2] = reg[1]

        obj._i2c.writeto(obj._address, payload)

        data = obj._i2c.readfrom(obj._address, self.lenght)

        obj._status_last = data[0]


class RegisterStructCMD:
    """
    Register Struct
    """

    def __init__(
        self,
        register_address: int,
        form: str,
        cmd_read: int = None,
        cmd_write: int = None,
    ) -> None:
        self.format = form
        self.register = register_address
        self.lenght = (
            struct.calcsize(form) + 1
        )  # Read the response (+1 to account for the mandatory status byte!)
        self.cmd_read = cmd_read
        self.cmd_write = cmd_write

    def __get__(
        self,
        obj,
        objtype=None,
    ):
        payload = bytes([self.cmd_read, self.register << 2])
        obj._i2c.writeto(obj._address, payload)

        data = bytearray(self.lenght)
        data = obj._i2c.readfrom(obj._address, self.lenght)

        obj._status_last, val = struct.unpack(">BH", data)

        return val

    def __set__(self, obj, value):
        data = bytearray(self.lenght)
        payload = bytes(
            [
                self.cmd_write,
                value >> 8,
                value & 0xFF,
                self.register << 2,
            ]
        )
        obj._i2c.writeto(obj._address, payload)

        data = obj._i2c.readfrom(obj._address, self.lenght)

        obj._status_last = data[0]


_CMD_RR = const(0b01010000)
_CMD_WR = const(0b01100000)
_REG_WHOAMI = const(0x0C)

# Gain settings
GAIN_5X = const(0x00)
GAIN_4X = const(0x01)
GAIN_3X = const(0x02)
GAIN_2_5X = const(0x03)
GAIN_2X = const(0x04)
GAIN_1_67X = const(0x05)
GAIN_1_33X = const(0x06)
GAIN_1X = const(0x07)


class MLX90393:
    """Main class for the Sensor

    :param ~machine.I2C i2c: The I2C bus the MLX90393 is connected to.
    :param int address: The I2C device address. Defaults to :const:`0x0C`

    :raises RuntimeError: if the sensor is not found


    **Quickstart: Importing and using the device**

    Here is an example of using the :class:`MLX90393` class.
    First you will need to import the libraries to use the sensor

    .. code-block:: python

        from machine import Pin, I2C
        import micropython_mlx90393.mlx90393 as mlx90393

    Once this is done you can define your `machine.I2C` object and define your sensor object

    .. code-block:: python

        i2c = I2C(sda=Pin(8), scl=Pin(9))
        mlx = mlx90393.MLX90393(i2c)

    Now you have access to the :attr:`magnetic` attribute

    .. code-block:: python

        magx, magy, magz = mlx.magnetic

    """

    _res0_xy = {
        0: (0.751, 0.601, 0.451, 0.376, 0.300, 0.250, 0.200, 0.150),
        1: (0.787, 0.629, 0.472, 0.393, 0.315, 0.262, 0.21, 0.157),
    }
    _res1_xy = {
        0: (1.502, 1.202, 0.901, 0.751, 0.601, 0.501, 0.401, 0.300),
        1: (1.573, 1.258, 0.944, 0.787, 0.629, 0.524, 0.419, 0.315),
    }
    _res2_xy = {
        0: (3.004, 2.403, 1.803, 1.502, 1.202, 1.001, 0.801, 0.601),
        1: (3.146, 2.517, 1.888, 1.573, 1.258, 1.049, 0.839, 0.629),
    }
    _res3_xy = {
        0: (6.009, 4.840, 3.605, 3.004, 2.403, 2.003, 1.602, 1.202),
        1: (6.292, 5.034, 3.775, 3.146, 2.517, 2.097, 1.678, 1.258),
    }
    _res0_z = {
        0: (1.210, 0.968, 0.726, 0.605, 0.484, 0.403, 0.323, 0.242),
        1: (1.267, 1.014, 0.760, 0.634, 0.507, 0.422, 0.338, 0.253),
    }
    _res1_z = {
        0: (2.420, 1.936, 1.452, 1.210, 0.968, 0.807, 0.645, 0.484),
        1: (2.534, 2.027, 1.521, 1.267, 1.014, 0.845, 0.676, 0.507),
    }
    _res2_z = {
        0: (4.840, 3.872, 2.904, 2.420, 1.936, 1.613, 1.291, 0.968),
        1: (5.068, 4.055, 3.041, 2.534, 2.027, 1.689, 1.352, 1.014),
    }
    _res3_z = {
        0: (9.680, 7.744, 5.808, 4.840, 3.872, 3.227, 2.581, 1.936),
        1: (10.137, 8.109, 6.082, 5.068, 4.055, 3.379, 2.703, 2.027),
    }

    _resolutionsxy = {0: _res0_xy, 1: _res1_xy, 2: _res2_xy, 3: _res3_xy}
    _resolutionsz = {0: _res0_z, 1: _res1_z, 2: _res2_z, 3: _res3_z}

    _reg_0 = RegisterStructCMD(0x00, "H", _CMD_RR, _CMD_WR)
    _reg_2 = RegisterStructCMD(0x02, "H", _CMD_RR, _CMD_WR)

    _bits = CBits(3, 0x02, 3, 2, False, _CMD_RR, _CMD_WR)

    # Register 0x00
    #  Z-Series(3) | Gain(3) |  Gain(1) | Gain(0) | HallConf(3) | HallConf(2) | HallConf(1) | HallConf(0) |
    # ----------------------------------------------------------------------------------------------------
    #  CONV0(1)    | AVG1(1) | AVG0(1)  | T/nA(1) |    POL(1)   | DR/Alert(1) | Soft_Reset  |   —
    _gain = CBits(3, 0x00, 4, 2, False, _CMD_RR, _CMD_WR)
    _hall = CBits(4, 0x00, 0, 2, False, _CMD_RR, _CMD_WR)

    def __init__(self, i2c, address=0x0C):
        self._i2c = i2c
        self._address = address
        self._status_last = None

    @property
    def gain(self):
        """
        The gain setting for the device.

        +----------------------------------+----------------------+
        | Mode                             | Value                |
        +==================================+======================+
        | :py:const:`mlx90393.GAIN_1_67X`  | :py:const:`0x5`      |
        | :py:const:`mlx90393.GAIN_2X`     | :py:const:`0x4`      |
        | :py:const:`mlx90393.GAIN_5X`     | :py:const:`0x0`      |
        | :py:const:`mlx90393._GAIN_SHIFT` | :py:const:`const(4)` |
        | :py:const:`mlx90393.GAIN_1_33X`  | :py:const:`0x6`      |
        | :py:const:`mlx90393.GAIN_1X`     | :py:const:`0x7`      |
        | :py:const:`mlx90393.GAIN_2_5X`   | :py:const:`0x3`      |
        | :py:const:`mlx90393.GAIN_3X`     | :py:const:`0x2`      |
        | :py:const:`mlx90393.GAIN_4X`     | :py:const:`0x1`      |
        +----------------------------------+----------------------+

        """
        gain_values = (
            "GAIN_5X",
            "GAIN_4X",
            "GAIN_3X",
            "GAIN_2_5X",
            "GAIN_2X",
            "GAIN_1_67X",
            "GAIN_1_33X",
            "GAIN_1X",
        )

        return gain_values[self._gain]

    @gain.setter
    def gain(self, value):
        if value not in range(1, 8):
            raise ValueError("Invalid GAIN setting")
        self._gain = value

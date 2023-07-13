# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya

import time
from machine import Pin, I2C
from micropython_mlx90393 import mlx90393

i2c = I2C(sda=Pin(8), scl=Pin(9))  # Correct I2C pins for UM FeatherS2
mlx = mlx90393.MLX90393(i2c)

while True:
    magx, magy, magz = mlx.magnetic
    print(f"X: {magx} uT, Y: {magy} uT, Z: {magz} uT")
    print()
    time.sleep(1)

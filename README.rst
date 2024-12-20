⛔️ DEPRECATED
===============

This repository is no longer supported, please consider using alternatives.

.. image:: http://unmaintained.tech/badge.svg
  :target: http://unmaintained.tech
  :alt: No Maintenance Intended
MicroPython Driver for the MLX90393 Sensor


Installing with mip
====================

To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_MLX90393

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_MLX90393")


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_MLX90393/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip.install("github:jposada202020/MicroPython_MLX90393/examples.json")



Installation
==============

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/micropython-mlx90393/>`_.
To install for current user:

.. code-block:: shell

    pip3 install micropython-mlx90393

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install micropython-mlx90393

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install micropython-mlx90393

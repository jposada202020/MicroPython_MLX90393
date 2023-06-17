Introduction
============


.. image:: https://img.shields.io/badge/micropython-Ok-purple.svg
    :target: https://micropython.org
    :alt: micropython

.. image:: https://readthedocs.org/projects/micropython-mlx90393/badge/?version=latest
    :target: https://micropython-mlx90393.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/pypi/v/micropython-mlx90393.svg
    :alt: latest version on PyPI
    :target: https://pypi.python.org/pypi/micropython-mlx90393

.. image:: https://static.pepy.tech/personalized-badge/micropython-mlx90393?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Pypi%20Downloads
    :alt: Total PyPI downloads
    :target: https://pepy.tech/project/micropython-mlx90393

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

MicroPython Driver for the MLX90393 Sensor


Installing with mip
====================

To install using mpremote

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_MLX90393

To install directly using a WIFI capable board

.. code-block:: shell

    mip install github:jposada202020/MicroPython_MLX90393


Installing Library Examples
============================

If you want to install library examples:

.. code-block:: shell

    mpremote mip install github:jposada202020/MicroPython_MLX90393/examples.json

To install directly using a WIFI capable board

.. code-block:: shell

    mip install github:jposada202020/MicroPython_MLX90393/examples.json



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

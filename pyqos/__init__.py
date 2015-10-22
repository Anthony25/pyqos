#!/usr/bin/python
# Author: Anthony Ruhier

import logging

logging.basicConfig(
    format="[%(levelname)s] %(message)s (%(filename)s:%(lineno)d) "
)

from pyqos.app import PyQOS

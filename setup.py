#!/usr/bin/env python
# -*- coding: utf-8 -*-

__account__     = 'iamprabhat'
__author__      = 'Prabhat Kumar, prabhat.genome@gmail.com'
__githubURL__   = 'https://github.com/iamprabhat'
__homepage__    = 'http://prabhatkumar.org/'
__license__     = 'Apache License'

# ------------------------------------------------------------------------
#
#           Copyright © 2016, Prabhat Kumar, All rights reserved.
#
# Licensed under the Apache License, Version 2.0, (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#       	http://www.apache.org/licenses/LICENSE-2.0
#                           	or
#     https://github.com/iamprabhat/HIV-Pred/blob/master/LICENSE
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ========================================================================
# =============================== HIV-Pred® ==============================
import os
import sys
import platform
import errno

from os import sep as dirsep
from os.path import isfile, join

from distutils.core import setup
from distutils.extension import Extension
from distutils.command.install import install

# A:1 - Python Version Information.
if sys.version_info[:2] < (2, 6):
    sys.stderr.write('HIV-Pred®: Python 2.5 and older is not supported!\n')
    sys.exit()

# A:2 - JavaOS Support Information.
if os.name == 'java':
    sys.stderr.write('HIV-Pred®: JavaOS is not supported!\n')
    sys.exit()

# A:3 - NumPy Support Information.
try:
    import numpy
except ImportError:
    sys.stderr.write('HIV-Pred®: numpy is not installed, you can find it at: http://numpy.scipy.org/\n')
    sys.exit()

if [int(dgt) for dgt in numpy.__version__.split('.')[:2]] < [1, 4]:
    sys.stderr.write('HIV-Pred®: numpy v1.4 or later is required, you can find it at: http://numpy.scipy.org/\n')
    sys.exit()

# A:4 - SciPy Support Information.
try:
    import scipy
except ImportError:
    sys.stderr.write('HIV-Pred®: scipy is not installed, you can find it at: http://www.scipy.org/\n')
    sys.exit()

if [int(dgt) for dgt in scipy.__version__.split('.')[:2]] < [0, 4]:
    sys.stderr.write('HIV-Pred®: scipy v0.14 or later is required, you can find it at: http://www.scipy.org/\n')
    sys.exit()

# A:5 - scikit-learn Support Information.
try:
    import sklearn
except ImportError:
    sys.stderr.write('HIV-Pred®: scikit-learn is not installed, you can find it at: http://scikit-learn.org/\n')
    sys.exit()

if [int(dgt) for dgt in sklearn.__version__.split('.')[:2]] < [0, 15]:
    sys.stderr.write('HIV-Pred®: scikit-learn v0.15.0 or later is required, you can find it at: http://scikit-learn.org/\n')
    sys.exit()

# A:6 - matplotlib Support Information.
try:
    import matplotlib
except ImportError:
    sys.stderr.write('HIV-Pred®: matplotlib is not installed, you can find it at: http://matplotlib.org/\n')
    sys.exit()

if [int(dgt) for dgt in matplotlib.__version__.split('.')[:2]] < [1, 5]:
    sys.stderr.write('HIV-Pred®: matplotlib v1.5.0 or later is required, you can find it at: http://matplotlib.org/\n')
    sys.exit()

# A:7 - seaborn Support Information.
try:
    import seaborn
except ImportError:
    sys.stderr.write('HIV-Pred®: seaborn is not installed, you can find it at: http://stanford.edu/~mwaskom/software/seaborn/\n')
    sys.exit()

if [int(dgt) for dgt in seaborn.__version__.split('.')[:2]] < [0, 6]:
    sys.stderr.write('HIV-Pred®: seaborn v0.6.0 or later is required, you can find it at: http://stanford.edu/~mwaskom/software/seaborn/\n')
    sys.exit()

# A:8 - NetworkX Support Information.
try:
    import networkx
except ImportError:
    sys.stderr.write('HIV-Pred®: networkx is not installed, you can find it at: https://networkx.github.io/\n')
    sys.exit()

if [int(dgt) for dgt in networkx.__version__.split('.')[:2]] < [1, 10]:
    sys.stderr.write('HIV-Pred®: networkx v1.10 or later is required, you can find it at: https://networkx.github.io/\n')
    sys.exit()

# =============================== HIV-Pred® ==============================
# A:9 - HIV-Pred® Information.
__version__ 	= '1.0.0'

with open('app/__init__.py') as inp:
    for line in inp:
        if line.startswith('__version__'):
            exec(line.strip())
            break

with open('docs/README.rst') as inp:
    long_description = inp.read()

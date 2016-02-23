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

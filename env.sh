#!/bin/sh


# ============================ HIV-Pred® =============================
# Handcrafted by Prabhat Kumar, http://prabhatkumar.org/.
# Copyright © 2016, Prabhat Kumar. All rights reserved.
# ====================================================================

PYV=`python -c "import sys;t='{v[0]}.{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)";`
echo "HIV-Pred® ------------"
echo "Python version is:" $PYV
echo "HIV-Pred® ------------"
DEP=`python setup.py`
echo "Checking dependency..." $DEP

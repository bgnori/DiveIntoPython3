#!/bin/sh

DISTRIBUTE_VER=0.6.48

./pyvenv-3.3.py py3.3
curl -L -O "https://pypi.python.org/packages/source/d/distribute/distribute-${DISTRIBUTE_VER}.tar.gz"
tar xf distribute-${DISTRIBUTE_VER}.tar.gz
cd distribute-${DISTRIBUTE_VER}
../py3.3/bin/python setup.py install
cd ..
./py3.3/bin/easy_install-3.3 pip



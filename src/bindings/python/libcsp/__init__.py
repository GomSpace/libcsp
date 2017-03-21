import sys
if sys.version_info >= (3, 0):
    from .libcsp_python3 import *
else:
    from libcsp_python2 import *

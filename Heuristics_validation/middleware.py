# A python wrapper for the c++ sieveisdlib.cpp
from numpy import zeros, random
import ctypes
from math import ceil

import sys
if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3")

def c_char_ptr(x):
    return x.ctypes.data_as(ctypes.POINTER(ctypes.c_char))

def c_long_ptr(x):
    return x.ctypes.data_as(ctypes.POINTER(ctypes.c_long))

def ham(v):
    return sum(v)

class SieveISDlib(object):
    def __init__(self, H, seed=None):
        c, n = H.shape
        self.c, self.n = c, n
        self.H = H

        if seed is None:
            seed = random.randint(0,2**63)

        nmax = 256 * int(ceil(n/256.))
        self.lib = ctypes.cdll.LoadLibrary("./bin/sieveisdlib-%d.so"%nmax)
        
        self.lib._setup(c, n, c_char_ptr(H), ctypes.c_long(seed))
        
    def __del__(self):
        print()

    def sieve_step(self, w, N, i):
        stats = zeros(7, dtype="long")
        self.lib._sieve_step(w, N, i, c_long_ptr(stats))
        return {"step"      : stats[0],
                "N_input"   : stats[1],
                "tried"     : stats[2],
                "found"     : stats[3],
                "ufound"    : stats[4],
                "collision" : stats[5],
                "removed"   : stats[6],
                }

    def initialize_list(self, w, N):
        self.lib._initialize_list(w, N)

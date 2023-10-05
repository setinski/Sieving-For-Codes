# Compares and visualizes theoretical prediction and experimental data.
# To run: python comparison.py $n $w $k $i
#    default: $n = 256, $w = 6, $k = 0, $i = 10

from numpy import random
from middleware import SieveISDlib
from scipy.special import binom
from math import ceil
import os.path
from sys import argv
import misc

# Code parameters
if len(argv) < 5:
    n = 256
    w = 6
    k = 0
    exp_num = 10
else:   
    n = int(argv[1])
    w = int(argv[2])
    k = int(argv[3])
    exp_num = int(argv[4])
    
# Code parameters
print("\n Code length: n = {0},\
      Error weight: w = {1}, \
      Code dimension: k = {2}, \
      Number of experiments: {3}".format(n, w, k, exp_num))
c = n-k

# Sieving parameters
C = 4.1
N = int(ceil(C * binom(n, w)/(binom(w, w//2) * binom(n-w, w//2))) )

# Data folder
if not os.path.exists('data/'):
    os.mkdir('data/')
directory = 'data/n%d/'%(n)
if not os.path.exists(directory):
    os.mkdir(directory)

# Multiple experiments
exp_data = []
fields = ["step", "N_input", "tried", "found", "ufound", "collision", "removed"]
for j in range(exp_num):
    print("\n----------Experiment {0}------------------".format(j+1))
    
    # Initialize a new random instance
    H = random.randint(0,2, size=(c, n), dtype="bool")
    siever = SieveISDlib(H)
    siever.initialize_list(w, N)
    
    # Gather experimental data
    for i in range(c):
        exp_datum = siever.sieve_step(w, N, i)
        exp_datum["collision"] += 1e-99 # Just so that it doesn't disapear from logplot when 0.
        N_input = exp_datum["N_input"]
        exp_data.append(exp_datum)
        print(exp_datum)
        if exp_datum["ufound"]==0:
            break
    
    # Write experimental data
    misc.csv_write_data(directory, fields, exp_data, "experiment", n, w, N, j+1)
    
    exp_data.clear()
    del siever




# Compares and visualizes theoretical prediction and experimental data.
# To run: python comparison.py $n $w $k
#    default: $n = 256, $w = 6, $k = 0

from numpy import random
from middleware import SieveISDlib
from scipy.special import binom
from math import ceil
import os.path
from sys import argv
import theory_predict as tp
import misc

fields = ["step", "N_input", "tried", "found", "ufound", "collision", "removed"]
def theory(n, w, i, N):
    D = dict([])
    D[fields[0]] = i
    D[fields[1]] = N
    D[fields[2]] = tp.tried_num(N)
    D[fields[3]] = tp.found_num(n, w, N)
    D[fields[4]] = tp.unique_num(n, w, i, N)
    D[fields[5]] = tp.collision_num(n, w, i, N)
    D[fields[6]] = tp.removed_num(n, w, i, N)
    return D


# Code parameters
if len(argv) < 4:
    n = 256
    w = 6
    k = 0
else:   
    n = int(argv[1])
    w = int(argv[2])
    k = int(argv[3])
    
# Code parameters
print("\n Code length: n = {0},\
      Error weight: w = {1}, \
      Code dimension: k = {2}".format(n, w, k))
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
    
# An experiment and corresponding theoretical prediction
theory_data = []
exp_data = []
print("\n Experimental data")

# Initialize a new random instance
H = random.randint(0,2, size=(c, n), dtype="bool")
siever = SieveISDlib(H)
siever.initialize_list(w, N)

for i in range(c):
    # Gather experimental data and corresponding theoretical prediction
    exp_datum = siever.sieve_step(w, N, i)
    exp_datum["collision"] += 1e-99 # Just so that it doesn't disapear from logplot when 0.
    N_input = exp_datum["N_input"]
    exp_data.append(exp_datum)
    print(exp_datum)
    theory_data.append(theory(n, w, i+1, N_input))
    if exp_datum["ufound"]==0:
        break
    
# Write experimental data
misc.csv_write_data(directory, fields, exp_data, "experiment", n, w, N)
    
# Write theoretical prediction
misc.csv_write_data(directory, fields, theory_data, "theory", n, w, N)
    
# Plot experimental data and theoretical prediction
values = ["found", "ufound", "collision", "removed"]
misc.plot_data(directory, exp_data, theory_data, n, w, N, values)



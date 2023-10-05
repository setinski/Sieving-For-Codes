# Theoretical predictions
import math
from scipy.special import binom

def prob(n, w):
    return binom(w, w/2) * binom(n - w, w/2) / binom(n,w)

def part_sols_num(n, w, i):
    return binom(n, w) / math.pow(2, i)

def tried_num(N):
    return (N/2) * (N/2 - 1)

def found_num(n, w, N):
    return tried_num(N) * prob(n, w)

def unique_num(n, w, i, N):
    temp = 1 - 1./part_sols_num(n, w, i)
    if temp >= 1:
        return 0
    return (1. - math.pow(temp, found_num(n, w, N))) / (1. - temp)

def collision_num(n, w, i, N):
    return found_num(n, w, N) - unique_num(n, w, i, N)

def removed_num(n, w, i, N):
    return max(0, unique_num(n, w, i, N) - N)

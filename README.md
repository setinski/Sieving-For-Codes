# Sieving For Codes

In this project, we provide an asymptotic analyisis of the sieving-style algorithm for solving decoding problems (SievingISD_asymptotic_optimization.ipynb) and experimental validation of the heuristics required for instantiating sieving algorithm as a sub-routine of an ISD algorithm. The numerical results accompany the theoretical results presented in the corresponding paper.

## Project's dependencies

The heuristics validation experiments require CPU that supports Advanced Vector Extensions (AVX). Both the heuristic validation experiments as well  and Python 3.

## Build the siveisd library (for Linux distributions)
<pre translate="no" dir="ltr" is-upgraded="">make
</pre>

## Run the experiments

To obtain the results and visualization of the comparison between the theoretical prediction and the experimental data, run
<pre translate="no" dir="ltr" is-upgraded="">
python comparison.py $n $w $k $i
</pre>
where $n is the code length, $w is the weight of the error, and $k is the code dimension. If no parameters are provided, $n = 256, $w = 6, and $k = 0.

To obtain the results and visualization of the comparison between the theoretical prediction and the experimental data, run
<pre translate="no" dir="ltr" is-upgraded="">
python experiments.py $n $w $k $i
</pre>
where $n is the code length, $w is the weight of the error, $k is the code dimension, and $i is the number of experiments. If no parameters are provided, $n = 256, $w = 6, $k = 0, and $i = 10.


The results of the experiments and the comparison are recorded in ./Data/n$n directory.

### Authors
anonymous


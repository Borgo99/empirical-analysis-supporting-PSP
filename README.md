# Empirical Analysis supporting PSP

This repository contains code for simulating and comparing various statistical tests—most notably, a proposed _Practical Significance Threshold (PSP)_ method.

## Overview

1. **Main Notebook** (`statistical_simulation.ipynb`):

   - Demonstrates how to run the simulation study.
   - Compares standard hypothesis testing and other methods to the new PSP approach.
   - Visualizes results (confusion matrices, correlations) and provides a brief analysis.

2. **Supporting Python Files**:
   - `PSP.py`  
     Contains the implementation of the PSP metric.
   - `statistical_methods.py`  
     Includes functions for:
     - `P_value`: Computes p-values (e.g., using a t-test).
     - `confidence_interval`: Derives confidence intervals for two groups.
     - `least_difference_in_means`: Checks whether the observed mean difference exceeds a given threshold (`pst`).

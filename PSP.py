import numpy as np
import math
from scipy import stats

def PSP(control_sample, treatment_sample, pst, equal_var=True):
  if len(control_sample) != len(treatment_sample):
    raise ValueError("Control and treatment samples must have the same length.")
  n = len(treatment_sample)
  control_mean = np.mean(control_sample)
  treatment_mean = np.mean(treatment_sample)
  control_std = np.std(control_sample, ddof=1)
  treatment_std = np.std(treatment_sample, ddof=1)
  observed_effect_size = treatment_mean - control_mean

  if equal_var:
    # 1) Calculate pooled standard deviation:
    #    sp = sqrt(((n-1)*s1^2 + (n-1)*s2^2) / (n + n - 2))
    sp = math.sqrt(((n - 1) * control_std**2 + (n - 1) * treatment_std**2) / (2*n - 2))
    # 2) Standard error of the difference under equal-variance assumption:
    #    stde = sp * sqrt(1/n + 1/n) = sp * sqrt(2/n)
    stde = sp * math.sqrt(2.0 / n)
  else:
    # Welch's approximation (unequal variance):
    # stde = sqrt(s1^2 / n + s2^2 / n)
    stde = math.sqrt(control_std**2 / n + treatment_std**2 / n)
  
  psp = 1 - stats.norm.cdf( (abs(pst) - abs(observed_effect_size))/stde )
  return psp
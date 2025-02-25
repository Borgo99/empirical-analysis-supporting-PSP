import numpy as np
from scipy import stats

def P_value(a, b, equal_var=True):
  return stats.ttest_ind(a, b, equal_var=equal_var).pvalue

def confidence_interval(a, b, confidence_level=0.95, equal_var=True):
  ci = stats.ttest_ind(a, b, equal_var=equal_var).confidence_interval(confidence_level=confidence_level)
  return ci.low, ci.high

def least_difference_in_means(control_sample, treatment_sample, pst, n_mc_simulations=10_000, alpha_credible_intervals=0.05):
  control_mean = np.mean(control_sample)
  treatment_mean = np.mean(treatment_sample)
  control_std = np.std(control_sample, ddof=1)
  treatment_std = np.std(treatment_sample, ddof=1)

  control_posterior = np.random.normal(control_mean, control_std / np.sqrt(len(control_sample)), n_mc_simulations)
  treatment_posterior = np.random.normal(treatment_mean, treatment_std / np.sqrt(len(treatment_sample)), n_mc_simulations)
  diff_posterior = treatment_posterior - control_posterior
  # credible intervals
  lower_bound = np.percentile(diff_posterior, alpha_credible_intervals/2*100)
  upper_bound = np.percentile(diff_posterior, (1 - alpha_credible_intervals/2)*100)
  # Calculate δL (Least Difference in Means)
  delta_L = min(abs(lower_bound), abs(upper_bound)) * np.sign(np.mean(diff_posterior))

  return delta_L, abs(delta_L) > abs(pst)
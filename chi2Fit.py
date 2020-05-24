#! /usr/bin/env python3

# This is a shorter (simplified) version of Philip Bechtles original script
# (available under chi2Fit_old.py).

# Simple example script for a chi2-fit - data points with errors in y only.
# For an example to do a fit for data points with errors in x and y,
# see the script chi2FitXYErr.py

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import scipy.optimize as optimize

# declare the fit-function; a line with two parameters (slope and y-intercept)
# in our case;
def f(x, a, b):
    return a * x + b

# Here the measurement points; usually you will read those from a file:
xdata = np.array([0,1,2,3,4,5])
ydata = np.array([0,1.9,4,6.5,8.1,9.8])
sigma = np.array([0.2,0.3,0.5,0.4,0.3,0.5]) # errors

# just do the fit
# IMPORTANT: In physics, our errors are typically absolute errors and
# not relative ones. Hence, you need to use the option 'absolute_sigma=True'!:
#
# Please see the documentation of the curve_fit function for more information:
# 
fitParams, fitCovariances = optimize.curve_fit(f, xdata, ydata, sigma=sigma,
                                               absolute_sigma=True)

# give meaningful names to the results:
a = fitParams[0]
b = fitParams[1]
errors = np.sqrt(np.diag(fitCovariances))
a_std_err = errors[0]
b_std_err = errors[1]

# print result to screen:
print("result of fit:\n")
print("y = a * x + b with\n")
print("a = %f +/- %f" % (a, a_std_err))
print("b = %f +/- %f" % (b, b_std_err))

# create a plot:

# font size of labels etc,
matplotlib.rcParams['font.size'] = 18
# line width of coordinate axes
matplotlib.rcParams['axes.linewidth'] = 2.0

y_fit = a * xdata + b

plt.figure()
plt.errorbar(xdata, ydata, yerr=sigma, lw=2, fmt='.', label="data points")
plt.plot(xdata, y_fit, lw=2, label="y=%.2f * x + %.2f" % (a, b))
plt.xlabel('x')
plt.ylabel('y')
plt.title("%d data points and line-fit" % (xdata.shape[0]))
plt.legend()

# show plot on screen
plt.show()

# Comment in 'plt.show()' and comment out the following if you
# want to save the plot to a file:
#plotname = 'myplot.pdf'
#plt.savefig(plotname, bbox_inches=0, dpi=600)
#plt.close()

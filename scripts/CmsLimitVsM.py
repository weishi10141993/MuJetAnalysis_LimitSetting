import math
from math import *
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

execfile("UserInput.py") #define input
execfile("UserConfig.py") #define year and config limits

def myGaus(x, mu, sigma):
    return 1./( sigma * sqrt(2.0*pi) ) * exp( - (x - mu)*(x - mu) / 2.0/sigma/sigma )

def myGaus2(x, mu, sigma):
    return exp( - (x - mu)*(x - mu) / 2.0/sigma/sigma )

#Fitted function to toy experiment limits
def fCmsLimitVsM(m):
    ## 90% CL
    if CL == 90:
        #Fit to expected limit (constant)
        return 2.33591576728
        #Fit to observed limit (After unblinding, TBD)
        #return 2.33591576728+0.490467147856* myGaus2(m,1.20105406966, 0.0158823287785) + 1.75* myGaus2(m,1.37980913362, 0.0363780607304) + 0.468148031032* myGaus2(m,1.89383556463, 0.0619017859509) + 1.2* myGaus2(m,2.37120887758, 0.0524109033795) + 2.04831493617* myGaus2(m,2.84399373813, 0.07) + 4.482483411* myGaus2(m,3.05938898807, 0.0696193158778)

    ## 95% CL
    if CL == 95 and year == 2018:
        #Fit to expected limit (avg. const from all mass points toys)
        return 3.05791963636 #2018 3.05803472727 flat pdf
        #Fit to observed limit (After unblinding, TBD)
        #return 3.00174326806+0.758400444753* myGaus2(m,1.21537045458, 0.0402388548379) + 1.81322228899* myGaus2(m,1.4117157352, 0.05) + 0.581002295405* myGaus2(m,1.90264292745, 0.0648260169513) + 1.46155733387* myGaus2(m,2.37797756173, 0.0585759605432) + 1.84612408697* myGaus2(m,2.80000000002, 0.07) + 4.89437383246* myGaus2(m,3.04849077039, 0.09)
    if CL == 95 and year == 2020:
        #Fit to expected limit (avg. const from all mass points toys)
        return 3.2920163636 

def fCmsLimitVsM_explicit(m):
    A = 3.082
    B = 1.18
    C = 552.0
    M = 0.315
    return A + B*exp( -552*(m - M)*(m - M) )

#Run 2 resolution
def fCmsResolution(m):
    return 0.003044 + 0.007025*(x1+x2)/2.0 + 0.000053*(x1+x2)*(x1+x2)/4.0

## Confidence level
if CL == 95:
    Expected_Limits_Quantile_0p5_HybridNew = Expected_Limits_Quantile_0p5_HybridNew_95 # from Expected_Limits_Quantiles.py
    Expected_Limits_Quantile_0p025_HybridNew = Expected_Limits_Quantile_0p025_HybridNew_95
    Expected_Limits_Quantile_0p975_HybridNew = Expected_Limits_Quantile_0p975_HybridNew_95
    Expected_Limits_Quantile_0p16_HybridNew  = Expected_Limits_Quantile_0p16_HybridNew_95
    Expected_Limits_Quantile_0p84_HybridNew  = Expected_Limits_Quantile_0p84_HybridNew_95
if CL == 90:
    Expected_Limits_Quantile_0p5_HybridNew = Expected_Limits_Quantile_0p5_HybridNew_90
    Expected_Limits_Quantile_0p025_HybridNew = Expected_Limits_Quantile_0p025_HybridNew_90
    Expected_Limits_Quantile_0p975_HybridNew = Expected_Limits_Quantile_0p975_HybridNew_90
    Expected_Limits_Quantile_0p16_HybridNew  = Expected_Limits_Quantile_0p16_HybridNew_90
    Expected_Limits_Quantile_0p84_HybridNew  = Expected_Limits_Quantile_0p84_HybridNew_90

# Return the expected median @%CL% CL for a given mass point
# if the mass point is not present, it makes an interpolation.
def ExpectedLimitVsM_HybridNew(m, limit_array):
    if m >= 0.2113 and m <= 60.:
        m_im1 = 0.2113
        m_i   = 0.2113
        for i in range(len(limit_array)):
            m_i   = limit_array[i][0]
            lim_i = limit_array[i][1]
            if m == m_i:
                return lim_i
            elif m > m_im1 and m < m_i:
                a = (lim_i - lim_im1) / (m_i - m_im1)
                b = (lim_im1*m_i - lim_i*m_im1) / (m_i - m_im1)
                lim = a*m+b
                return lim
            m_im1 = m_i
            lim_im1 = lim_i
    else:
        print "Warning! Mass if outside the range."

#general function to do extrapolate for ALP model
#array is in the form [m, f(m)]
def fCmsAlpExtrapolate(m, array):
    if m >= 0.5 and m <= 30.:
        m_im1 = 0.5
        m_i   = 0.5
        for i in range(len(array)):
            m_i   = array[i][0]
            lim_i = array[i][1]
            if m == m_i:
                return lim_i
            elif m > m_im1 and m < m_i:
                a = (lim_i - lim_im1) / (m_i - m_im1)
                b = (lim_im1*m_i - lim_i*m_im1) / (m_i - m_im1)
                lim = a*m+b
                return lim
            m_im1 = m_i
            lim_im1 = lim_i
    else:
        print "Warning! Mass if outside the range."

#general function to do extrapolate for NMSSM
#array is in the form [(0.50,90): (0.109)]
def fCmsNmssmExtrapolate(ma, mh, array):
    if ma < 0.5 or ma > 3.00: raise Exception, "ma = %g" % ma
    if mh < 90. or mh > 150.: raise Exception, "mh = %g" % mh
    for alow, ahigh in [(0.5,0.75),(0.75,1.0),(1.0,2.0),(2.0,3.0)]:
        for hlow, hhigh in [(90.,100.),(100.,110.),(110.,125.),(125.,150.)]:
            if alow <= ma <= ahigh and hlow <= mh <= hhigh:
                break
        if alow <= ma <= ahigh and hlow <= mh <= hhigh:
            break
    ainc = (ma - alow)/(ahigh - alow)
    hinc = (mh - hlow)/(hhigh - hlow)

    return (1. - ainc)*(1. - hinc)*array[alow, hlow] + (ainc)*(1. - hinc)*array[ahigh, hlow] + (ainc)*(hinc)*array[ahigh, hhigh] + (1. - ainc)*(hinc)*array[alow, hhigh]

# fit the data
def myGaus2(x, mu, sigma):
    #print "type x", type(x)
    #return 1./( np.sqrt(2.0*np.pi*sigma**2) ) *
    return np.exp( - (x - mu)**2 / (2.0*sigma**2) )

## fit the limits
def func(x, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s):
    return ( a +
             b*myGaus2(x, c, d) +
             e*myGaus2(x, f, g) +
             h*myGaus2(x, i, j) +
             k*myGaus2(x, l, m) +
             n*myGaus2(x, o, p) +
             q*myGaus2(x, r, s)
             )

xdata = [float(i[0]) for i in Expected_Limits_Quantile_0p5_HybridNew]
ydata = [float(i[1]) for i in Expected_Limits_Quantile_0p5_HybridNew]
print xdata
print ydata

"""
For 95% CL limits
                       bounds=([2.95,
                                0.5, 1.1, 0,
                                1.75, 1.1, 0,
                                0.25, 1.7, 0,
                                1.2, 2.1, 0,
                                0, 2.8, 0,
                                4, 2.9, 0.09],
                               [3.1,
                                1, 1.3, 0.05,
                                2, 1.6, 0.05,
                                0.75, 2.1, 0.07,
                                2, 2.7, 0.07,
                                4, 3, 0.07,
                                5, 3.1, 0.13]
                               )

"""

ydata_error = []
for p in range(0,len(xdata)):
    ydata_error.append(0.3)

popt, pcov = curve_fit(func, np.array(xdata), np.array(ydata),
                       sigma = np.array(ydata_error),
                       bounds=([2.,
                                0, 1.1, 0.0,
                                1.75, 1.1, 0,
                                0.25, 1.7, 0,
                                1.2, 2.1, 0,
                                0, 2.8, 0,
                                0, 2.9, 0.0],
                               [2.5,
                                1, 1.3, 0.03,
                                2, 1.6, 0.04,
                                0.75, 2.1, 0.07,
                                2, 2.7, 0.07,
                                4, 3, 0.07,
                                5, 3.1, 0.15]
                               )
                       )

print "Fit parameters", popt
print "Fit covariance matrix", pcov

trialX = np.linspace(xdata[0], xdata[-1], 5000)

plt.plot(xdata, ydata, 'o', label='data', markersize=3)
plt.plot(trialX, func(np.array(trialX), *popt), 'r-', label='fit')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

print (str(popt[0]) + "+" +
       str(popt[1]) + "* myGaus(m,"+ str(popt[2]) +  ", " + str(popt[3]) + ")" + " + " +
       str(popt[4]) + "* myGaus(m,"+ str(popt[5]) +  ", " + str(popt[6]) + ")" + " + " +
       str(popt[7]) + "* myGaus(m,"+ str(popt[8]) +  ", " + str(popt[9]) + ")" + " + " +
       str(popt[10]) + "* myGaus(m,"+ str(popt[11]) +  ", " + str(popt[12]) + ")" + " + " +
       str(popt[13]) + "* myGaus(m,"+ str(popt[14]) +  ", " + str(popt[15]) + ")" + " + " +
       str(popt[16]) + "* myGaus(m,"+ str(popt[17]) +  ", " + str(popt[18]) + ")"
       )

#print "Fit parameters", popt
#print "Fit covariance matrix", pcov
#plt.show()

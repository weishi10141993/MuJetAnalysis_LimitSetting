import math
from math import *
from scipy.stats import chisquare
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

def myGaus(x, mu, sigma):
    return 1./( sigma * sqrt(2.0*pi) ) * exp( - (x - mu)*(x - mu) / 2.0/sigma/sigma )

def myGaus2(x, mu, sigma):
    return exp( - (x - mu)*(x - mu) / 2.0/sigma/sigma )

CL = 95

#Fitted function to toy experiment limits
def fCmsLimitVsM(m):
    ## 90% CL
    if CL == 90:
        #Fit to expected limit (constant)
        return 2.33591576728
        #Fit to observed limit (After unblinding, TBD)
        #return 2.33591576728+0.490467147856* myGaus2(m,1.20105406966, 0.0158823287785) + 1.75* myGaus2(m,1.37980913362, 0.0363780607304) + 0.468148031032* myGaus2(m,1.89383556463, 0.0619017859509) + 1.2* myGaus2(m,2.37120887758, 0.0524109033795) + 2.04831493617* myGaus2(m,2.84399373813, 0.07) + 4.482483411* myGaus2(m,3.05938898807, 0.0696193158778)

    ## 95% CL
    if CL == 95:
        #Fit to expected limit (constant)
        return 2.97927604167
        #Fit to observed limit (After unblinding, TBD)
        #return 3.00174326806+0.758400444753* myGaus2(m,1.21537045458, 0.0402388548379) + 1.81322228899* myGaus2(m,1.4117157352, 0.05) + 0.581002295405* myGaus2(m,1.90264292745, 0.0648260169513) + 1.46155733387* myGaus2(m,2.37797756173, 0.0585759605432) + 1.84612408697* myGaus2(m,2.80000000002, 0.07) + 4.89437383246* myGaus2(m,3.04849077039, 0.09)

def fCmsLimitVsM_explicit(m):
    A = 3.082
    B = 1.18
    C = 552.0
    M = 0.315
    return A + B*exp( -552*(m - M)*(m - M) )

#Run 2 resolution
def fCmsResolution(m):
    return 0.003044 + 0.007025*(x1+x2)/2.0 + 0.000053*(x1+x2)*(x1+x2)/4.0

Limits_HybridNew_90 = [
#TBD
]

Limits_HybridNew_95 = [
[0.2113,2.85721], #(1)
[0.24,3.14809], #(1)
[0.26,2.99569], #(1)
[0.3,3.22746], #(1)
[0.33,2.99408], #(1)
[0.36,2.90431], #(1)
[0.4,3.21478], #(1)
[0.43,2.88363], #(1)
[0.46,3.16285], #(1)
[0.5,3.05437], #(1)
[0.53,2.90257], #(1)
[0.56,2.82938], #(1)
[0.6,2.9013], #(1)
[0.7,3.01325], #(1)
[0.8,3.19882], #(1)
[0.88,2.77156], #(1)
[0.9,3.23484], #(1)
[0.91,2.98645], #(1)
[0.92,3.31896], #(1)
[0.93,3.16295], #(1)
[0.94,3.33203], #(1)
[1.0,3.12111], #(1)
[1.1,2.93455], #(1)
[1.2,3.01899], #(1)
[1.3,2.97463], #(1)
[1.4,3.01032], #(1)
[1.5,2.91867], #(1)
[1.6,2.99431], #(1)
[1.7,3.07001], #(1)
[1.8,3.00661], #(1)
[1.9,3.01197], #(1)
[2.0,3.21407], #(1)
[2.1,3.03041], #(1)
[2.2,2.94901], #(1)
[2.3,3.08585], #(1)
[2.4,3.05931], #(1)
[2.5,2.89717], #(1)
[2.6,3.18292], #(1)
[2.7,3.09743], #(1)
[3.3,2.82643], #(1)
[3.4,3.0512], #(1)
[3.7,2.95011], #(1)
[4.0,2.97017], #(1)
[5.0,2.99229], #(1)
[6.0,2.96145], #(1)
[7.0,2.94032], #(1)
[8.0,2.99795], #(1)
[8.5,3.01482], #(1)
[13.0,2.86896], #(1)
[17.0,3.04703], #(1)
[21.0,3.12345], #(1)
[25.0,3.15424], #(1)
[29.0,2.96033], #(1)
[33.0,3.04571], #(1)
[37.0,2.98864], #(1)
[41.0,3.00612], #(1)
[45.0,3.07358], #(1)
[49.0,3.16882], #(1)
[53.0,3.14965], #(1)
[57.0,3.09612], #(1)
]

## assign the limits
if CL == 90:
    Limits_HybridNew = Limits_HybridNew_90
if CL == 95:
    Limits_HybridNew = Limits_HybridNew_95

# return the limit for a given mass.
# if the mass point is not present, it makes an interpolation.
def fCmsLimitVsM_HybridNew(m):
    if m >= 0.2113 and m <= 60.:
        m_im1 = 0.2113
        m_i   = 0.2113
        for i in range(len(Limits_HybridNew)):
            m_i   = Limits_HybridNew[i][0]
            lim_i = Limits_HybridNew[i][1]
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

# 2015 Granularity
#MGammaD_array = [0.2113,0.2200,0.2300,0.2400,0.2500,0.2600,0.2700,0.2800,0.2900,0.3000,0.3100,0.3200,0.3300,0.3400,0.3500,0.3600,0.3700,0.3800,0.3900,0.4000,0.4100,0.4200,0.4300,0.4400,0.4500,0.4600,0.4700,0.4800,0.4900,0.5000,0.6000,0.7000,0.8000,0.9000,1.0000,1.1000,1.2000,1.5000,2.0000,2.6000,2.7000,2.8000,2.9000,3.0000,3.1000,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]
# 2016 Granularity
#MGammaD_array = [0.2113,0.2400,0.2600,0.3000,0.3300,0.3600,0.4000,0.4300,0.4600,0.5000,0.5300,0.5600,0.6000,0.7000,0.8000,0.8800,0.9000,0.9100,0.9200,0.9300,0.9400,1.0000,1.1000,1.2000,1.3000,1.4000,1.5000,1.6000,1.7000,1.8000,1.9000,2.0000,2.1000,2.2000,2.3000,2.4000,2.5000,2.6000,2.7000,2.8000,2.9000,3.0000,3.0200,3.0500,3.0800,3.0900,3.1000,3.1200,3.1500,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]
# 2017 Granularity
MGammaD_array = [0.2113, 0.2400, 0.2600, 0.3000, 0.3300, 0.3600, 0.4000,  0.4300, 0.4600, 0.5000,
0.5300, 0.5600, 0.6000, 0.7000, 0.8000, 0.8800, 0.9000, 0.9100, 0.9200, 0.9300, 0.9400, 1.0000,
1.1000, 1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000, 2.1000, 2.2000,
2.3000, 2.4000, 2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000,
8.0000, 8.5000,
13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000]

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

xdata = [float(i[0]) for i in Limits_HybridNew]
ydata = [float(i[1]) for i in Limits_HybridNew]
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

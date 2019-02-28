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

def fCmsLimitVsM(m):
  #M = 0.315
  #LimitMin = 3.08
  #LimitMax = 8.55
  #if False:
  #  print "M = ", M
  #  print "LimitMin = ", LimitMin
  #  print "LimitMax = ", LimitMax
  #  print "sigma = ", fCmsResolution(M)
  #  print "myGaus(M, M, fCmsResolution(M) ) = ", myGaus(M, M, fCmsResolution(M) )
  #  print "LimitMax-LimitMin/myGaus[M,M,sigma(M)]/sigma(M)sqrt(2pi) = ", (LimitMax - LimitMin)/myGaus(M, M, fCmsResolution(M) )/fCmsResolution(M)/sqrt(2.0*pi)
  #  print "1/2/sigma(M)^2 = ", 1.0/2.0/fCmsResolution(M)/fCmsResolution(M)
  #  print "Err: " + str(LimitMin + (LimitMax - LimitMin)*myGaus(m, M, fCmsResolution(M) )/myGaus(M, M, fCmsResolution(M) ))
  #return LimitMin + (LimitMax - LimitMin)*myGaus(m, M, fCmsResolution(M) )/myGaus(M, M, fCmsResolution(M) )
#****************************************
# old method 95 CL v2

  ## 95% CL
  return 3.00174326806+0.758400444753* myGaus2(m,1.21537045458, 0.0402388548379) + 1.81322228899* myGaus2(m,1.4117157352, 0.05) + 0.581002295405* myGaus2(m,1.90264292745, 0.0648260169513) + 1.46155733387* myGaus2(m,2.37797756173, 0.0585759605432) + 1.84612408697* myGaus2(m,2.80000000002, 0.07) + 4.89437383246* myGaus2(m,3.04849077039, 0.09)

## 90% CL
"""
3.205 + \
0.14*exp(-0.5*((m-0.568278)/0.0809449)**2) + \
1.80706*exp(-0.5*((m-0.832)/0.035)**2) + \
0.74807*exp(-0.5*((m-1.18349)/0.0330001)**2) + \
1.8*exp(-0.5*((m-1.41324)/0.034)**2) + \
0.638387*exp(-0.5*((m-1.9109)/0.0500741)**2) + \
1.20542*exp(-0.5*((m-2.37377)/0.04)**2) + \
1.45*exp(-0.5*((m-2.9989)/0.160763)**2) + \
5.0654*exp(-0.5*((m-3.11577)/0.128669)**2)
# old method 95 CL
#  return 3.175 + \
#0.231692*exp(-0.5*((m-0.556259)/0.0997077)**2) + \
#2.28*exp(-0.5*((m-0.916552)/0.032)**2) + \
#2.1*exp(-0.5*((m-1.16447)/0.02)**2) + \
#2.25*exp(-0.5*((m-1.41355)/0.035)**2) + \
#3.0*exp(-0.5*((m-1.90464)/0.0777818)**2) + \
#1.8*exp(-0.5*((m-2.39079)/0.0469897)**2) + \
#0.685263*exp(-0.5*((m-2.74387)/0.04)**2) + \
#4.7*exp(-0.5*((m-3.10271)/0.0942601)**2)

#90CL v2
#  return 2.4 + \
#0.196258*exp(-0.5*((m-0.585342)/0.0400199)**2) + \
#1.32241*exp(-0.5*((m-0.833146)/0.0350001)**2) + \
#0.893637*exp(-0.5*((m-1.16449)/0.033)**2) + \
#1.79953*exp(-0.5*((m-1.41323)/0.03)**2) + \
#0.59907*exp(-0.5*((m-1.90641)/0.05)**2) + \
#1.1*exp(-0.5*((m-2.40133)/0.042)**2) + \
#2.20401*exp(-0.5*((m-2.999)/0.169458)**2) + \
#3.57*exp(-0.5*((m-3.1005)/0.134076)**2)

#90CL v1
#  return (3.175 + \
#0.231692*exp(-0.5*((m-0.556259)/0.0997077)**2) + \
#2.28*exp(-0.5*((m-0.916552)/0.032)**2) + \
#2.1*exp(-0.5*((m-1.16447)/0.02)**2) + \
#2.25*exp(-0.5*((m-1.41355)/0.035)**2) + \
#3.0*exp(-0.5*((m-1.90464)/0.0777818)**2) + \
#1.8*exp(-0.5*((m-2.39079)/0.0469897)**2) + \
#0.685263*exp(-0.5*((m-2.74387)/0.05)**2) + \
#5.5*exp(-0.5*((m-3.10271)/0.085)**2) ) * 0.7419354838710
"""

def fCmsLimitVsM_explicit(m):
  A = 3.082
  B = 1.18
  C = 552.0
  M = 0.315
  return A + B*exp( -552*(m - M)*(m - M) )

def fCmsResolution ( m ):
  return (0.13 + m*0.065)/5.0

Limits_HybridNew = [
[0.2113,3.02228435], #(200)
[0.24,2.97580845771], #(201)
[0.26,2.98139915], #(200)
[0.3,2.99316525], #(200)
[0.33,2.9991437], #(200)
[0.36,3.041728], #(200)
[0.4,2.9968781407], #(199)
[0.43,2.98804386935], #(199)
[0.46,3.00461291457], #(199)
[0.5,3.02047135678], #(199)
[0.53,3.02276502513], #(199)
[0.56,3.02140919598], #(199)
[0.6,2.99831371859], #(199)
[0.7,2.98560532663], #(199)
[0.8,3.02112055276], #(199)
[0.88,3.0378080402], #(199)
[0.9,3.07864070352], #(199)
[0.91,3.01536688442], #(199)
[0.92,3.02529221106], #(199)
[0.93,3.02151829146], #(199)
[0.94,3.02266155779], #(199)
[1.0,3.00756221106], #(199)
[1.1,3.01418321608], #(199)
[1.2,3.70701683417], #(199)
[1.3,3.23422316583], #(199)
[1.4,4.76588703518], #(199)
[1.5,3.38321437186], #(199)
[1.6,3.0034221608], #(199)
[1.7,3.06447085427], #(199)
[1.8,3.16235507538], #(199)
[1.9,3.58412919598], #(199)
[2.0,3.18681522613], #(199)
[2.1,3.02601226131], #(199)
[2.2,3.01883371859], #(199)
[2.3,3.60405226131], #(199)
[2.4,4.3637321608], #(199)
[2.5,3.16800673367], #(199)
[2.6,3.06458984925], #(199)
[2.7,3.81628351759], #(199)
[2.8,4.84471854271], #(199)
[2.9,5.0980060804], #(199)
[3.0,7.01268221106], #(199)
[3.02,7.5134618593], #(199)
[3.05,7.87249542714], #(199)
[3.08,7.67464226131], #(199)
[3.09,7.66184296482], #(199)
[3.1,7.3986821608], #(199)
[3.12,6.8096860804], #(199)
[3.15,5.36357648241], #(199)
[3.2,3.35443678392], #(199)
[3.3,3.00256643216], #(199)
[3.4,3.04975090452], #(199)
[3.7,3.04272843434], #(198)
[4.0,3.07987722222], #(198)
[5.0,3.03155828283], #(198)
[6.0,3.00566683417], #(199)
[7.0,2.99713213198], #(197)
[8.0,3.00079324873], #(197)
[8.5,3.04041461929], #(197)
]

def fCmsLimitVsM_HybridNew(m): # return the limit for a given mass. If the mass point is not present, it makes an interpolation.
  if m >= 0.2113 and m <= 8.55:
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
MGammaD_array = [0.2113,0.2400,0.2600,0.3000,0.3300,0.3600,0.4000,0.4300,0.4600,0.5000,0.5300,0.5600,0.6000,0.7000,0.8000,0.8800,0.9000,0.9100,0.9200,0.9300,0.9400,1.0000,1.1000,1.2000,1.3000,1.4000,1.5000,1.6000,1.7000,1.8000,1.9000,2.0000,2.1000,2.2000,2.3000,2.4000,2.5000,2.6000,2.7000,2.8000,2.9000,3.0000,3.0200,3.0500,3.0800,3.0900,3.1000,3.1200,3.1500,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]


## fit the data                                                                                                                                       
def myGaus2(x, mu, sigma):
    #print "type x", type(x)                                                                                                                    
    #return 1./( np.sqrt(2.0*np.pi*sigma**2) ) *  
  return np.exp( - (x - mu)**2 / (2.0*sigma**2) )

## fit the limits
def func(x, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):#,q,r,s):
    return ( a + 
             b*myGaus2(x, c, d) + 
             e*myGaus2(x, f, g) +
             h*myGaus2(x, i, j) +
             k*myGaus2(x, l, m) +
             n*myGaus2(x, o, p)
             #+q*myGaus2(x, r, s) 
             )

xdata = [float(i[0]) for i in Limits_HybridNew]
ydata = [float(i[1]) for i in Limits_HybridNew]
print xdata
print ydata

#xdata = np.linspace(0.2113, 8.5, 1000)
## add extra zeros
nPoints = 1000 
xdata_mod = np.linspace(xdata[0], xdata[-1], 1000)
#ydata_mod = []

ydata_error = []
for p in range(0,len(xdata)):
  ydata_error.append(0.3)
#np.linspace(xdata[0], xdata[-1], 0.3)

#for p in range(0,1000):
#  if ydata[]
#  ydata_mod = 3

popt, pcov = curve_fit(func, np.array(xdata), np.array(ydata),
                       sigma = np.array(ydata_error),
                       bounds=([2.95, 
                                0.5, 1.1, 0,  
                                1.75, 1.1, 0, 
                                0.25, 1.7, 0, 
                                1.2, 2.1, 0,
                                #0, 2.8, 0,
                                4, 2.9, 0.09],
                               [3.1, 
                                1, 1.3, 0.05, 
                                2, 1.6, 0.05,
                                0.75, 2.1, 0.07,
                                2, 2.7, 0.07,
                                #4, 3, 0.07,
                                5, 3.1, 0.13]
                               )
                       )

print "Fit parameters", popt
#print "Fit covariance matrix", pcov

"""
3.095
1.0475*exp(-0.5*((m-1.16447)/0.0330002)**2) + \
1.9*exp(-0.5*((m-1.41329)/0.03)**2) + \
0.899002*exp(-0.5*((m-1.91236)/0.05)**2) + \
1.82784*exp(-0.5*((m-2.40341)/0.038)**2) + \
16.3032*exp(-0.5*((m-3.01232)/0.120919)**2)
"""

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
       str(popt[13]) + "* myGaus(m,"+ str(popt[14]) +  ", " + str(popt[15]) + ")"# + " + " +
       #str(popt[16]) + "* myGaus(m,"+ str(popt[17]) +  ", " + str(popt[18]) + ")"
       )
       
#print "Fit parameters", popt 
#print "Fit covariance matrix", pcov

plt.show()

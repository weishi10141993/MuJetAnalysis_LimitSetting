import math
from math import *

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
#Minimizer is Linear
#Chi2                      =     0.262144
#NDf                       =           42
#p0                        =      2.93472   +/-   0.0120479  
  return 3.03;
  #return 0.13*exp(-0.5*((m-0.4)/0.13)**2)+ 3.03;
  #return 0.35*exp(-0.5*((m-0.55)/0.06)**2)+3.023;
  #return 0.23*exp(-0.5*((m-0.45)/0.15)**2) + 0.2*exp(-0.5*((m-0.85)/0.15)**2) + 0.1*exp(-0.5*((m-1.1)/0.5)**2) + 3.05 + 1.5*exp(-0.5*((m-3.1)/0.05)**2)

def fCmsLimitVsM_explicit(m):
  A = 3.082
  B = 1.18
  C = 552.0
  M = 0.315
  return A + B*exp( -552*(m - M)*(m - M) )

def myGaus(x, mu, sigma):
  return 1/( sigma * sqrt(2.0*pi) ) * exp( - (x - mu)*(x - mu) / 2.0/sigma/sigma )

def fCmsResolution ( m ):
  return (0.13 + m*0.065)/5.0

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

MGammaD_array = [0.2113,0.2200,0.2300,0.2400,0.2500,0.2600,0.2700,0.2800,0.2900,0.3000,0.3100,0.3200,0.3300,0.3400,0.3500,0.3600,0.3700,0.3800,0.3900,0.4000,0.4100,0.4200,0.4300,0.4400,0.4500,0.4600,0.4700,0.4800,0.4900,0.5000,0.6000,0.7000,0.8000,0.9000,1.0000,1.1000,1.2000,1.5000,2.0000,2.6000,2.7000,2.8000,2.9000,3.0000,3.1000,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]

Limits_HybridNew = [
#ORI bb in dia
[0.2113,3.0578935],
[0.22,2.96528894737],
[0.23,3.000537],
[0.24,3.028587],
[0.25,3.00904],
[0.26,3.111218],
[0.27,3.0019],
[0.28,3.10662],
[0.29,3.104187],
[0.3,3.1106405],
[0.31,3.017117],
[0.32,3.092018],
[0.33,3.0863545],
[0.34,3.05116],
[0.35,3.098555],
[0.36,3.1057635],
[0.37,3.0907315],
[0.38,2.97082578947],
[0.39,3.04496],
[0.4,2.9359565],
[0.41,3.112629],
[0.42,3.054734],
[0.43,3.1192695],
[0.44,3.07264],
[0.45,3.16146],
[0.46,3.0639565],
[0.47,3.020506],
[0.48,3.1337505],
[0.49,3.111762],
[0.5,3.1881825],
[0.6,3.0221945],
[0.7,3.0383085],
[0.8,3.020795],
[0.9,3.0003745],
[1.0,2.977947],
[2.0,3.163834],
[2.6,3.12079941176],
[2.7,3.2011695],
[2.8,3.1375825],
[2.9,2.88778],
[3.0,2.8159],
[3.1,2.87293666667],
[3.2,2.80841],
[3.3,3.03231896552],
[3.4,2.85207],
[3.7,2.82574],
[4.0,2.93024],
[5.0,2.91655],
[6.0,2.933275],
[7.0,3.138445],
[8.0,3.09419285714],
[8.5,3.08900333333]
]

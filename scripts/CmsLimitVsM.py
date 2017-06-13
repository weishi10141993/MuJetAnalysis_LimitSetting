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
[0.2113,3.12073148148],
[0.22,3.10489608696],
[0.23,3.15196391304],
[0.24,3.083425],
[0.25,3.14870888889],
[0.26,3.04894115385],
[0.27,3.02663352941],
[0.28,3.13445045455],
[0.29,3.11875884615],
[0.3,3.07054925926],
[0.31,3.10107407407],
[0.32,3.03536107143],
[0.33,2.94792666667],
[0.34,3.03952857143],
[0.35,3.03251321429],
[0.36,3.07451481481],
[0.37,3.00018],
[0.38,3.12087533333],
[0.39,3.01489068966],
[0.4,2.95651724138],
[0.41,3.00403939394],
[0.42,3.07648129032],
[0.43,3.031584375],
[0.44,3.06250166667],
[0.45,3.27828666667],
[0.46,3.09320608696],
[0.47,3.09977896552],
[0.48,2.98608409091],
[0.49,3.11519125],
[0.5,3.01923285714],
[0.6,3.156062],
[0.7,3.09434],
[0.8,3.12925428571],
[0.9,3.18271333333],
[1.0,3.13022708333],
[2.0,3.2039796875],
[2.6,3.227698],
[2.7,3.1803055],
[2.8,2.98599333333],
[2.9,3.0],
[3.0,3.03],
[3.1,2.39717],
[3.2,2.366825],
[3.3,2.456204],
[3.4,2.45785666667],
[3.7,2.46562375],
[4.0,2.35912333333],
[5.0,2.56398333333],
[6.0,2.906475],
[7.0,2.89176666667],
[8.0,3.03341666667],
[8.5,2.94569],
]

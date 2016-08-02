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
#p0                        =      3.07614   +/-   0.00455267  
#p1                        =   -0.0107989   +/-   0.00177602 
# If linear ****************************************
#p0                        =      3.06086   +/-   0.0061047   

  return 3.06086

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

def fCmsLimitVsM_HybridNew(m,version="default"):
  #if m >= 0.2113 and m <= 3.5536:
  if m >= 0.2113 and m <= 8.55:
    m_im1 = 0.2113
    m_i   = 0.2113
    for i in range(len(Limits_HybridNew)):
      if version == "default":
        m_i   = Limits_HybridNew[i][0]
        lim_i = Limits_HybridNew[i][1]
      elif version == "T5000":
        m_i   = Limits_HybridNew_T5000[i][0]
        lim_i = Limits_HybridNew_T5000[i][1]
      elif version == "T50000":
        m_i   = Limits_HybridNew_T50000[i][0]
        lim_i = Limits_HybridNew_T50000[i][1]
      elif version == "T500000":
        m_i   = Limits_HybridNew_T500000[i][0]
        lim_i = Limits_HybridNew_T500000[i][1]
      if m == m_i:
        return lim_i
      elif m > m_im1 and m < m_i:
        a = (lim_i - lim_im1) / (m_i - m_im1)
        b = (lim_im1*m_i - lim_i*m_im1) / (m_i - m_im1)
        lim = a*m+b
        return lim
      m_im1 = m_i
      lim_im1 = lim_i

MGammaD_array = [0.2113,0.2200,0.2300,0.2400,0.2500,0.2600,0.2700,0.2800,0.2900,0.3000,0.3100,0.3200,0.3300,0.3400,0.3500,0.3600,0.3700,0.3800,0.3900,0.4000,0.4100,0.4200,0.4300,0.4400,0.4500,0.4600,0.4700,0.4800,0.4900,0.5000,0.6000,0.7000,0.8000,0.9000,1.0000,2.0000,3.0000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]

Limits_HybridNew = [
[0.2113,2.8957],
[0.22,2.99451],
[0.23,3.07887],
[0.24,3.00772],
[0.25,2.94794],
[0.26,3.02788],
[0.27,2.99902],
[0.28,3.01652],
[0.29,2.77133],
[0.3,2.99207],
[0.31,2.99513],
[0.32,3.01911],
[0.33,2.97271],
[0.34,3.00784],
[0.35,2.94933],
[0.36,2.97843],
[0.37,3.06218],
[0.38,2.99587],
[0.39,3.02335],
[0.4,2.81368],
[0.41,3.04672],
[0.42,2.79782],
[0.43,2.98372],
[0.44,2.94674],
[0.45,3.00094],
[0.46,2.99044],
[0.47,2.96554],
[0.48,2.95728],
[0.49,3.00862],
[0.5,3.11463],
[0.6,2.95015],
[0.7,3.06325],
[0.8,2.90741],
[0.9,2.73542],
[1.0,2.99638],
[2.0,2.88221],
[3.0,3.01486],
[4.,2.97371],
[5.0,2.90761],
[6.0,2.90424],
[7.0,2.97086],
[8.0,2.84832],
[8.5,3.01102],
]

Limits_HybridNew_T5000 = [
]

Limits_HybridNew_T50000 = [
[0.2113,3.10338],
[0.22,3.08164],
[0.23,3.08974],
[0.24,3.04119],
[0.25,3.08082],
[0.26,3.05871],
[0.27,3.03628],
[0.28,3.07429],
[0.29,3.10096],
[0.3,3.10054],
[0.31,3.07557],
[0.32,3.09102],
[0.33,3.09561],
[0.34,3.08602],
[0.35,3.06486],
[0.36,3.04565],
[0.37,3.09289],
[0.38,3.08296],
[0.39,3.01921],
[0.4,3.09593],
[0.41,3.08018],
[0.42,3.07035],
[0.43,3.04492],
[0.44,3.06077],
[0.45,3.10316],
[0.46,3.08815],
[0.47,3.08905],
[0.48,3.03897],
[0.49,3.01666],
[0.5,3.10074],
[0.6,3.08452],
[0.7,3.07777],
[0.8,3.08177],
[0.9,3.0453],
[1.0,3.02379],
[2.0,3.08421],
[3.0,3.02608],
[4.0,2.98662],
[5.0,3.017],
[6.0,2.99672],
[7.0,2.99949],
[8.0,2.98838],
[8.5,3.02406],
]

Limits_HybridNew_T500000=[
]

Limits_HybridNew_T500000_notail=[
]

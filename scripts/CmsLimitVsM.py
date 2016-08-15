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
  return 0.35*exp(-0.5*((m-0.55)/0.06)**2)+3.023;

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
[0.2113,3.02268],
[0.22,3.22301],
[0.23,2.93874],
[0.24,2.8823],
[0.25,3.2013],
[0.26,2.73627],
[0.27,2.8656],
[0.28,2.9195],
[0.29,2.92397],
[0.3,3.22813],
[0.31,3.07318],
[0.32,3.02147],
[0.33,2.92781],
[0.34,2.92781],
[0.35,3.54982],
[0.36,4.27718],
[0.37,4.64881],
[0.38,4.49964],
[0.39,4.57962],
[0.4,4.78812],
[0.41,4.50035],
[0.42,4.44641],
[0.43,4.06947],
[0.44,3.44685],
[0.45,3.26633],
[0.46,3.30417],
[0.47,3.04507],
[0.48,3.08596],
[0.49,2.97477],
[0.5,2.82073],
[0.6,2.75571],
[0.7,3.16999],
[0.8,3.174],
[0.9,2.73301],
[1.0,2.92049],
[2.0,3.12532],
[3.0,3.01344],
[4.0,3.01917],
[5.0,3.06602],
[6.0,3.028],
[7.0,3.0612],
[8.0,3.11588],
[8.5,2.96095],
]

Limits_HybridNew_T5000 = [
]

Limits_HybridNew_T50000=[
[0.2113,3.06241],
[0.22,2.9768],
[0.23,3.06825],
[0.24,3.00406],
[0.25,3.09782],
[0.26,3.03427],
[0.27,2.98905],
[0.28,2.95513],
[0.29,3.07198],
[0.3,3.0445],
[0.31,3.02285],
[0.32,2.9923],
[0.33,3.0492],
[0.34,3.06646],
[0.35,3.03786],
[0.36,2.95072],
[0.37,3.02802],
[0.38,2.98404],
[0.39,2.98371],
[0.4,2.9894],
[0.41,2.99004],
[0.42,2.991815],
[0.43,2.93276],
[0.44,2.94345],
[0.45,3.03999],
[0.46,2.94875],
[0.47,3.28077],
[0.48,3.28045],
[0.49,3.02463],
[0.5,3.00182],
[0.6,3.30511],
[0.7,2.9804],
[0.8,2.97755],
[0.9,2.98359],
[1.0,2.98017],
[2.0,3.03523],
[3.0,3.03916],
[4.0,2.99524],
[5.0,2.96694],
[6.0,2.99548],
[7.0,2.98348],
[8.0,2.98643],
[8.5,2.99919],
]

Limits_HybridNew_T500000=[
]

Limits_HybridNew_T500000_notail=[
]

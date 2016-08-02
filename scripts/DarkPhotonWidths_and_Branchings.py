from math import *

execfile("scripts/R_Hadrons.py")

alphaEM        = 1.0/137.036
m_electron_GeV = 0.00051
m_muon_GeV     = 0.10566
m_pion_GeV     = 0.13957
m_tau_GeV      = 1.77682

################################################################################
#           Decay Width(gammaD -> 2 leptons) / epsilon^2 in GeV                 
################################################################################

def Width_GammaD_to_ll_over_e2_GeV(m_GammaD, m_l):
  w1 = 1/3.0*alphaEM*m_GammaD
  w2 = 1.0 - 4.0*m_l*m_l/(m_GammaD*m_GammaD)
  w3 = 1.0 + 2.0*m_l*m_l/(m_GammaD*m_GammaD)
  w = w1*sqrt(w2)*w3
  return w

#           Decay Width(gammaD -> 2 electrons) / epsilon^2 in GeV               

def Width_GammaD_to_2el_over_e2_GeV(m_GammaD):
  return Width_GammaD_to_ll_over_e2_GeV( m_GammaD, m_electron_GeV )

#           Decay Width(gammaD -> 2 muons) / epsilon^2 in GeV                   

def Width_GammaD_to_2mu_over_e2_GeV(m_GammaD):
  return Width_GammaD_to_ll_over_e2_GeV( m_GammaD, m_muon_GeV )

#           Decay Width(gammaD -> 2 taus) / epsilon^2 in GeV                   

def Width_GammaD_to_2tau_over_e2_GeV(m_GammaD):
  return Width_GammaD_to_ll_over_e2_GeV( m_GammaD, m_tau_GeV )
  
################################################################################
#           Decay Width(gammaD -> hadrons) / epsilon^2 in GeV                   
################################################################################

def Width_GammaD_to_hadrons_over_e2_GeV(m_GammaD):
  return Width_GammaD_to_2mu_over_e2_GeV(m_GammaD) * fR_Hadrons(m_GammaD)

################################################################################
#           Decay Width(gammaD -> 2 pions) / epsilon^2 in GeV                   
################################################################################

# Cross section e+e- -> mu+mu-

def CS_2mu(sqrtS):
  return 4.0 * math.pi * alphaEM * alphaEM / 3.0 / (sqrtS * sqrtS)

# Cross section e+e- -> pi+pi-
def CS_2pi(sqrtS):
  cs1 = math.pi * alphaEM * alphaEM / 3.0 / (sqrtS * sqrtS)
  cs2 = sqrt( 1.0 - 4.0 * m_pion_GeV * m_pion_GeV / (sqrtS * sqrtS) )
  r2 = 11.27 # GeV^-2 see arxiv:hep-ph/0208177 pp 26-27
  c1 =  3.3  # GeV^-4
  c2 = 13.2  # GeV^-6
  Fpi = 1.0 + r2/6.0*(sqrtS * sqrtS) + c1*(sqrtS * sqrtS)*(sqrtS * sqrtS) + c2*(sqrtS * sqrtS)*(sqrtS * sqrtS)*(sqrtS * sqrtS)
  return cs1 * cs2*cs2*cs2 * Fpi*Fpi

def Width_GammaD_to_2pi_over_e2_GeV(m_GammaD):
  if m_GammaD < 2.0 * m_pion_GeV:
    return 0.0
  else:
    return Width_GammaD_to_2mu_over_e2_GeV(m_GammaD) * CS_2pi(m_GammaD) / CS_2mu(m_GammaD)

################################################################################
#           Total Decay Width(gammaD -> all) / epsilon^2 in GeV                 
################################################################################

def Width_GammaD_over_e2_GeV(m_GammaD):
  if m_GammaD > 2.0*m_electron_GeV and m_GammaD <= 2.0*m_muon_GeV:
    return Width_GammaD_to_2el_over_e2_GeV(m_GammaD)
  elif m_GammaD > 2.0*m_muon_GeV and m_GammaD <= 2.0*m_pion_GeV:
    return Width_GammaD_to_2el_over_e2_GeV(m_GammaD) + Width_GammaD_to_2mu_over_e2_GeV(m_GammaD)
  elif m_GammaD > 2.0*m_pion_GeV and m_GammaD <= 0.36:
    return Width_GammaD_to_2el_over_e2_GeV(m_GammaD) + Width_GammaD_to_2mu_over_e2_GeV(m_GammaD) + Width_GammaD_to_2pi_over_e2_GeV(m_GammaD)
  elif m_GammaD > 0.36 and m_GammaD <= 2.0*m_tau_GeV:
    return Width_GammaD_to_2el_over_e2_GeV(m_GammaD) + Width_GammaD_to_2mu_over_e2_GeV(m_GammaD) + Width_GammaD_to_hadrons_over_e2_GeV(m_GammaD)
  else:
    return Width_GammaD_to_2el_over_e2_GeV(m_GammaD) + Width_GammaD_to_2mu_over_e2_GeV(m_GammaD) + Width_GammaD_to_2tau_over_e2_GeV(m_GammaD) + Width_GammaD_to_hadrons_over_e2_GeV(m_GammaD)

################################################################################
#                  Branching Fraction BR(gammaD -> 2mu)                         
################################################################################

def BR_GammaD_to_2mu(m_GammaD):
  return Width_GammaD_to_2mu_over_e2_GeV(m_GammaD)/Width_GammaD_over_e2_GeV(m_GammaD)

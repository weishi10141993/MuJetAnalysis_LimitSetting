import array, os, re, math
from math import *

execfile("scripts/NMSSM_Br_a_Data.py")

def fNMSSM_Br_a(ma,tanBeta,channel):
    if channel   == "bb":     channel_i = 2
    elif channel == "tautau": channel_i = 3
    elif channel == "cc":     channel_i = 4
    elif channel == "ss":     channel_i = 5
    elif channel == "mumu":   channel_i = 6
    elif channel == "gluglu": channel_i = 7
    elif channel == "gamgam": channel_i = 8
    else: raise Exception

    if   tanBeta == 1.:  BR_a_TEST = BR_a_tan_beta_1
    elif tanBeta == 1.5: BR_a_TEST = BR_a_tan_beta_1_5
    elif tanBeta == 2.:  BR_a_TEST = BR_a_tan_beta_2
    elif tanBeta == 3.:  BR_a_TEST = BR_a_tan_beta_3
    elif tanBeta == 20.: BR_a_TEST = BR_a_tan_beta_20
    elif tanBeta == 50.: BR_a_TEST = BR_a_tan_beta_50
    else: raise Exception

    ma_min = BR_a_TEST[0][0]
    ma_max = BR_a_TEST[len(BR_a_TEST)-1][0]
    if ma < ma_min or ma > ma_max: raise Exception

    # get the lower bin number
    ma_i = int(floor((ma - ma_min)/(ma_max - ma_min) * (len(BR_a_TEST) -1) ))
#    print ma_i
    low, high = BR_a_TEST[ma_i], BR_a_TEST[ma_i + 1]
    ka = (ma - low[0])/(high[0] - low[0])
    BR_a = ka * (high[channel_i] - low[channel_i]) + low[channel_i]
    return BR_a

#print fNMSSM_Br_a(2.4,1,"mumu")
#print fNMSSM_Br_a(2.43,1,"mumu")
#print fNMSSM_Br_a(2.5,1,"mumu")

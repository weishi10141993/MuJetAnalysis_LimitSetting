import ROOT, array, os, re, math, random
from math import *
import numpy as np

execfile("UserInput.py") # define model independent constants for 2017-2018
execfile("CmsAlpAcceptance.py") #ALP input
execfile("CmsNmssmAcceptance.py") #NMSSM input

if year == 2017:

    # following will be used in CmsLimitVsM.py
    Expected_Limits_Quantile_0p5_HybridNew_95 = Expected_Limits_Quantile_0p5_HybridNew_95_2017
    Expected_Limits_Quantile_0p025_HybridNew_95 = Expected_Limits_Quantile_0p025_HybridNew_95_2017
    Expected_Limits_Quantile_0p975_HybridNew_95 = Expected_Limits_Quantile_0p975_HybridNew_95_2017
    Expected_Limits_Quantile_0p16_HybridNew_95  = Expected_Limits_Quantile_0p16_HybridNew_95_2017
    Expected_Limits_Quantile_0p84_HybridNew_95  = Expected_Limits_Quantile_0p84_HybridNew_95_2017

    # following will be used in plots.py
    lumi_fbinv = lumi_fbinv_2017
    SF = SF_2017
    eFullMc_over_aGen = eFullMc_over_aGen_2017
    CmsAlpAcceptance  = CmsAlpAcceptance_2017
    CmsNmssmAcceptance = CmsNmssmAcceptance_2017

if year == 2018:

    Expected_Limits_Quantile_0p5_HybridNew_95 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
    Expected_Limits_Quantile_0p025_HybridNew_95 = Expected_Limits_Quantile_0p025_HybridNew_95_2018
    Expected_Limits_Quantile_0p975_HybridNew_95 = Expected_Limits_Quantile_0p975_HybridNew_95_2018
    Expected_Limits_Quantile_0p16_HybridNew_95  = Expected_Limits_Quantile_0p16_HybridNew_95_2018
    Expected_Limits_Quantile_0p84_HybridNew_95  = Expected_Limits_Quantile_0p84_HybridNew_95_2018

    lumi_fbinv = lumi_fbinv_2018
    SF = SF_2018
    eFullMc_over_aGen = eFullMc_over_aGen_2018
    CmsAlpAcceptance  = CmsAlpAcceptance_2018
    CmsNmssmAcceptance = CmsNmssmAcceptance_2018

header = "#bf{CMS} #it{Preliminary}    " + str(lumi_fbinv) + "fb^{-1} (" + str(year) + " 13 TeV)";

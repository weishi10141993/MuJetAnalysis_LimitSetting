import ROOT, array, os, re, math, random
from math import *
import numpy as np

execfile("../scripts/UserInput.py") # define model independent constants for 2017-2018
execfile("../scripts/CmsAlpAcceptance.py") #ALP input
execfile("../scripts/CmsNmssmAcceptance.py") #NMSSM input

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

    MaxGraphMass = m_SR3_max+20
    masses = masses2018

if year == 2018:
    Observed_Limits_HybridNew_95 = Observed_Limits_HybridNew_95_2018
    Expected_Limits_Quantile_0p5_HybridNew_95 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
    Expected_Limits_Quantile_0p025_HybridNew_95 = Expected_Limits_Quantile_0p025_HybridNew_95_2018
    Expected_Limits_Quantile_0p975_HybridNew_95 = Expected_Limits_Quantile_0p975_HybridNew_95_2018
    Expected_Limits_Quantile_0p16_HybridNew_95  = Expected_Limits_Quantile_0p16_HybridNew_95_2018
    Expected_Limits_Quantile_0p84_HybridNew_95  = Expected_Limits_Quantile_0p84_HybridNew_95_2018

    lumi_fbinv = lumi_fbinv_2018
    SF = SF_2018
    eFullMc_over_aGen = eFullMc_over_aGen_2018
    CmsAlpAcceptance  = CmsAlpAcceptance_2018 #To be updated with 2018 MC
    CmsNmssmAcceptance = CmsNmssmAcceptance_2018 #To be updated with 2018 MC

    MaxGraphMass = m_SR3_max+20
    masses = masses2018

#run combine 2016+2018
if year == 2020:
    Expected_Limits_Quantile_0p5_HybridNew_95 = Expected_Limits_Quantile_0p5_HybridNew_95_2020
    for i in range(len(Expected_Limits_Quantile_0p5_HybridNew_95_2020)):
        Expected_Limits_Quantile_0p5_HybridNew_95[i][0] = Expected_Limits_Quantile_0p5_HybridNew_95_2020[i][0]
        #two categories (2016, 2018), so two times the limit returned per category
        Expected_Limits_Quantile_0p5_HybridNew_95[i][1] = 2*Expected_Limits_Quantile_0p5_HybridNew_95_2020[i][1]

    Expected_Limits_Quantile_0p025_HybridNew_95 = Expected_Limits_Quantile_0p5_HybridNew_95
    Expected_Limits_Quantile_0p975_HybridNew_95 = Expected_Limits_Quantile_0p5_HybridNew_95
    Expected_Limits_Quantile_0p16_HybridNew_95  = Expected_Limits_Quantile_0p5_HybridNew_95
    Expected_Limits_Quantile_0p84_HybridNew_95  = Expected_Limits_Quantile_0p5_HybridNew_95

    lumi_fbinv = lumi_fbinv_2020
    #assume 2018 numbers
    SF = SF_2018
    eFullMc_over_aGen = eFullMc_over_aGen_2018
    CmsAlpAcceptance  = CmsAlpAcceptance_2018
    CmsNmssmAcceptance = CmsNmssmAcceptance_2018

    #specify max mass when drawing limits plot, stop at 10GeV for combine 2016+2018
    MaxGraphMass = m_SR2_max+2.0
    masses = masses2020

header = "#bf{CMS} #it{Preliminary}            " + str(lumi_fbinv) + " fb^{-1} (13 TeV)";

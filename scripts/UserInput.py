#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!  USER Configure Above        !
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

year = 2018 #Configure which year limits to run, options: 2018, run combine: 2020

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!  USER Configure Above        !
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#**************************************
#* Common Constants
#**************************************
#same mass points as Constants.h, will be used in PrintOutLimits.py and plots.py
masses2018 = [0.2113, 0.2400, 0.2700, 0.3000, 0.3300, 0.3600, 0.4000, 0.4300, 0.4600, 0.5000, 0.5300, 0.5600,
   0.6000, 0.7000, 0.8000, 0.9000, 1.0000, 1.1000, 1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000,
   2.1000, 2.2000, 2.3000, 2.4000, 2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 8.5000,
   13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000, 58.0000]
#For combine 2016+2018, below 10GeV
masses2020 = [0.2113, 0.2400, 0.2700, 0.3000, 0.3300, 0.3600, 0.4000, 0.4300, 0.4600, 0.5000, 0.5300, 0.5600,
   0.6000, 0.7000, 0.8000, 0.9000, 1.0000, 1.1000, 1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000,
   2.1000, 2.2000, 2.3000, 2.4000, 2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 8.5000]

#**************************************
#* Constants need for PrintOutLimits.py
#**************************************
CLsymbol = '95%' # confidence level
quantile = "0.500" # %.3f precision of expected quantiles, options: 0.500 (the following options if specified in Constants.h: 0.840, 0.160, 0.975, 0.025)
pwd = '/home/ws13/Run2Limit/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/macros/sh/'
basetxt = "/output/output_"

#endtxt = "_T50000_";
endtxt = "_T30000_";
#endtxt = "_T10000_";
#endtxt = "_";

debug  = False
debug1 = False

#************************************************
#* Constants need for CmsLimitVsM.py and Plots.py
#************************************************
CL = 95 ## upper limit

## 2017: NOT ANALYZED
lumi_fbinv_2017 = 36.73 # Total lumi [fb^-1]
SF_2017 = 1.0 # scale factor from MC to data: eFullData / eFullMc
eFullMc_over_aGen_2017 = 0.418 # average constant from all signal MC samples

## 2018
lumi_fbinv_2018 = 59.7 # Total lumi [fb^-1]
SF_2018 = 0.996 # To be updated: scale factor from MC to data: eFullData / eFullMc
eFullMc_over_aGen_2018 = 0.418 # To be updated: average constant from all signal MC samples

## 2020 Combines 2016+2018 : To be updated
lumi_fbinv_2020 = 95.6 # Total lumi [fb^-1] 35.9+59.7

## mass range for SR1/2/3
m_SR1_min  = 0.2113;
m_SR1_max  = 2.72;
m_SR2_min  = 3.24;
m_SR2_max  = 8.5;
m_SR3_min  = 11.;
m_SR3_max  = 58.;

# NMSSM limit plot ma and mh mass points: limit_CSxBR2_fb_vs_ma, limit_CSxBR2_fb_vs_mh
# following choices of 2016 unblinded result, to be updated after 2017/2018 unblinding
array_ma = [0.5, 0.75, 1.0, 1.15, 1.2, 1.3, 1.4, 1.5, 1.75, 1.8, 1.9, 2.1, 2.25, 2.4, 2.5, 2.6, 2.75, 2.85, 3.0]
array_mh = [90., 100., 110., 125., 150.]

# ALP limit plot ma mass points: limit_ALP_Higgs_vs_ma
ggHXsecpb = 48.51 #pb: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt13TeV and CERN Report 4
HiggsSMWidthMeV = 4.1 #MeV
HiggsVEV = 246 #GeV
HiggsMass = 125.10 #GeV PDG2020
Br_ALP_Lepton_1 = 1.0
Br_ALP_Lepton_0p1 = 0.1

# ALP limit plot ma mass points: limit_ALP_Lepton_vs_ma
MuMassGeV = 0.105 #GeV
CahEff_over_LambdaSquare_TeV_1    = 1. #TeV^{-2} ~ 10^{-6} GeV^{-2}
CahEff_over_LambdaSquare_TeV_0p1  = 0.1
CahEff_over_LambdaSquare_TeV_0p01 = 0.01

## Y axis maximum on N_evt
NMax = 10.0

mGammaD_GeV = [0.25, 0.40, 0.55, 0.70, 0.85, 1.00]
mGammaD_GeV_bot = 0.00 # low boundary where histograms start in m
mGammaD_GeV_min = 0.25
mGammaD_GeV_max = 2.00
mGammaD_GeV_top = 10.0 # high boundary where histograms stops in m

ctau_mm = [0.0, 0.2, 0.5, 2.0, 5.0]
ctau_mm_bot = -0.5
ctau_mm_min =  0.0
ctau_mm_max =  5.0
ctau_mm_top =  5.5
c_hbar_mm_GeV = 1.974*pow(10.0, -13) # c = 3*10^11 mm/s; hbar = 6.58*10^-25 GeV*sec

epsilon2_min  = 0.000000000001
epsilon2_max  = 0.0001
epsilon2_bins = 1000
logEpsilon2_min = -12.1
logEpsilon2_max = -7.9

# Not constant! weaker at high mass
Expected_Limits_Quantile_0p5_HybridNew_95_2018 = [
[0.2113,3.00866], #(1)
[0.24,3.03778], #(1)
[0.27,3.01782], #(1)
[0.3,3.03711], #(1)
[0.33,3.02444], #(1)
[0.36,3.04948], #(1)
[0.4,3.02743], #(1)
[0.43,3.00998], #(1)
[0.46,3.05422], #(1)
[0.5,3.04339], #(1)
[0.53,3.02845], #(1)
[0.56,3.02788], #(1)
[0.6,2.99446], #(1)
[0.7,3.0312], #(1)
[0.8,3.01875], #(1)
[0.9,3.03768], #(1)
[1.0,3.04022], #(1)
[1.1,3.02918], #(1)
[1.2,3.02844], #(1)
[1.3,3.02744], #(1)
[1.4,3.0092], #(1)
[1.5,3.04525], #(1)
[1.6,3.05674], #(1)
[1.7,2.99412], #(1)
[1.8,3.01907], #(1)
[1.9,3.04937], #(1)
[2.0,2.98751], #(1)
[2.1,3.03847], #(1)
[2.2,3.05151], #(1)
[2.3,3.01446], #(1)
[2.4,3.01396], #(1)
[2.5,3.02216], #(1)
[2.6,3.05673], #(1)
[2.7,3.05294], #(1)
[3.3,3.06988], #(1)
[3.4,3.06078], #(1)
[3.7,3.04286], #(1)
[4.0,3.01752], #(1)
[5.0,3.06069], #(1)
[6.0,3.05138], #(1)
[7.0,3.04159], #(1)
[8.0,3.04877], #(1)
[8.5,3.1025], #(1)
[13.0,3.0405], #(1)
[17.0,3.02412], #(1)
[21.0,3.14455], #(1)
[25.0,3.0343], #(1)
[29.0,3.23765], #(1)
[33.0,3.14748], #(1)
[37.0,3.25783], #(1)
[41.0,3.36524], #(1)
[45.0,3.52974], #(1)
[49.0,3.45728], #(1)
[53.0,3.63117], #(1)
[57.0,3.61274], #(1)
[58.0,3.44206], #(1)
]

# Currently use same values as 0.5 quant above, +/-1/2 sigma bands doesn't make sense for zero bkg analysis
# keep the functionality for brazilian plot
Expected_Limits_Quantile_0p84_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p16_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p975_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p025_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018

# Combined 2016+2018 limit
Expected_Limits_Quantile_0p5_HybridNew_95_2020 = [
[0.2113,1.56943], #(1)
[0.24,1.54552], #(1)
[0.27,1.55955], #(1)
[0.3,1.51414], #(1)
[0.33,1.58571], #(1)
[0.36,1.55366], #(1)
[0.4,1.55342], #(1)
[0.43,1.57698], #(1)
[0.46,1.55655], #(1)
[0.5,1.58194], #(1)
[0.53,1.56184], #(1)
[0.56,1.57446], #(1)
[0.6,1.55062], #(1)
[0.7,1.56752], #(1)
[0.8,1.5637], #(1)
[0.9,1.58054], #(1)
[1.0,1.60403], #(1)
[1.1,1.57105], #(1)
[1.2,1.55773], #(1)
[1.3,1.56405], #(1)
[1.4,1.57998], #(1)
[1.5,1.52831], #(1)
[1.6,1.55779], #(1)
[1.7,1.53917], #(1)
[1.8,1.55221], #(1)
[1.9,1.55733], #(1)
[2.0,1.56177], #(1)
[2.1,1.57462], #(1)
[2.2,1.5599], #(1)
[2.3,1.59326], #(1)
[2.4,1.5845], #(1)
[2.5,1.56143], #(1)
[2.6,1.55588], #(1)
[2.7,1.58689], #(1)
[3.3,1.58986], #(1)
[3.4,1.56438], #(1)
[3.7,1.56365], #(1)
[4.0,1.52723], #(1)
[5.0,1.56298], #(1)
[6.0,1.55326], #(1)
[7.0,1.53958], #(1)
[8.0,1.54561], #(1)
[8.5,1.55055], #(1)
]
Expected_Limits_Quantile_0p84_HybridNew_95_2020 = Expected_Limits_Quantile_0p5_HybridNew_95_2020
Expected_Limits_Quantile_0p16_HybridNew_95_2020 = Expected_Limits_Quantile_0p5_HybridNew_95_2020
Expected_Limits_Quantile_0p975_HybridNew_95_2020 = Expected_Limits_Quantile_0p5_HybridNew_95_2020
Expected_Limits_Quantile_0p025_HybridNew_95_2020 = Expected_Limits_Quantile_0p5_HybridNew_95_2020

# 2017 limits to be filled, 2017 data not analyzed
Expected_Limits_Quantile_0p5_HybridNew_95_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p84_HybridNew_95_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p16_HybridNew_95_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p975_HybridNew_95_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p025_HybridNew_95_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018

# To be filled
Expected_Limits_Quantile_0p5_HybridNew_90_2018   = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p84_HybridNew_90_2018  = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p16_HybridNew_90_2018  = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p975_HybridNew_90_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p025_HybridNew_90_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018

Expected_Limits_Quantile_0p5_HybridNew_90_2020   = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p84_HybridNew_90_2020  = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p16_HybridNew_90_2020  = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p975_HybridNew_90_2020 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p025_HybridNew_90_2020 = Expected_Limits_Quantile_0p5_HybridNew_95_2018

Expected_Limits_Quantile_0p5_HybridNew_90_2017   = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p84_HybridNew_90_2017  = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p16_HybridNew_90_2017  = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p975_HybridNew_90_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p025_HybridNew_90_2017 = Expected_Limits_Quantile_0p5_HybridNew_95_2018

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
   13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000]
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
lumi_fbinv_2018 = 59.97 # Total lumi [fb^-1]
SF_2018 = 0.996 # To be updated: scale factor from MC to data: eFullData / eFullMc
eFullMc_over_aGen_2018 = 0.418 # To be updated: average constant from all signal MC samples

## 2020 Combines 2016+2018 : To be updated
lumi_fbinv_2020 = 95.87 # Total lumi [fb^-1] 35.9+59.97

## mass range for SR1/2/3
m_SR1_min  = 0.2113;
m_SR1_max  = 2.72;
m_SR2_min  = 3.24;
m_SR2_max  = 9.;
m_SR3_min  = 11.;
m_SR3_max  = 59.;

# NMSSM limit plot ma and mh mass points: limit_CSxBR2_fb_vs_ma, limit_CSxBR2_fb_vs_mh
# following choices of 2016 unblinded result, to be updated after 2017/2018 unblinding
array_ma = [0.5, 0.75, 1.0, 1.15, 1.2, 1.3, 1.4, 1.5, 1.75, 1.8, 1.9, 2.1, 2.25, 2.4, 2.5, 2.6, 2.75, 2.85, 3.0]
array_mh = [90., 100., 110., 125., 150.]

# ALP limit plot ma mass points: limit_ALP_Higgs_vs_ma
ggHXsecpb = 48.52 #pb
HiggsSMWidthMeV = 4.1 #MeV
HiggsVEV = 246 #GeV
HiggsMass = 125.10 #GeV PDG2018
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

# Poly-4 fit at high mass
Expected_Limits_Quantile_0p5_HybridNew_95_2018 = [
[0.2113,3.14217], #(1)
[0.24,3.15082], #(1)
[0.27,3.08371], #(1)
[0.3,3.10207], #(1)
[0.33,3.14115], #(1)
[0.36,3.20133], #(1)
[0.4,3.1449], #(1)
[0.43,2.98574], #(1)
[0.46,3.21659], #(1)
[0.5,3.14683], #(1)
[0.53,3.15253], #(1)
[0.56,3.15964], #(1)
[0.6,3.24519], #(1)
[0.7,3.15944], #(1)
[0.8,3.11565], #(1)
[0.9,3.13975], #(1)
[1.0,3.12716], #(1)
[1.1,3.18017], #(1)
[1.2,3.21168], #(1)
[1.3,3.19384], #(1)
[1.4,3.1268], #(1)
[1.5,3.14898], #(1)
[1.6,3.11851], #(1)
[1.7,3.17504], #(1)
[1.8,3.15492], #(1)
[1.9,3.14711], #(1)
[2.0,3.20389], #(1)
[2.1,3.1256], #(1)
[2.2,3.13987], #(1)
[2.3,3.17173], #(1)
[2.4,3.20054], #(1)
[2.5,3.1417], #(1)
[2.6,3.17545], #(1)
[2.7,3.16057], #(1)
[3.3,3.11726], #(1)
[3.4,3.10487], #(1)
[3.7,3.10124], #(1)
[4.0,3.09712], #(1)
[5.0,3.24682], #(1)
[6.0,3.09222], #(1)
[7.0,3.05007], #(1)
[8.0,3.08314], #(1)
[8.5,3.13778], #(1)
[13.0,2.99366], #(1)
[17.0,2.99366], #(1)
[21.0,3.02251], #(1)
[25.0,3.01353], #(1)
[29.0,3.00455], #(1)
[33.0,3.01390], #(1)
[37.0,3.02325], #(1)
[41.0,3.02325], #(1)
[45.0,3.01390], #(1)
[49.0,3.05131], #(1)
[53.0,2.98798], #(1)
[57.0,3.03517], #(1)
]

# Currently use same values as 0.5 quant above, +/-1/2 sigma bands doesn't make sense for zero bkg analysis
# keep the functionality for brazilian plot
Expected_Limits_Quantile_0p84_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p16_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p975_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018
Expected_Limits_Quantile_0p025_HybridNew_95_2018 = Expected_Limits_Quantile_0p5_HybridNew_95_2018

# To be filled
Expected_Limits_Quantile_0p5_HybridNew_95_2020 = [
[0.2113,1.56943], #(1)
[0.24,1.60177], #(1)
[0.27,1.62806], #(1)
[0.3,1.62548], #(1)
[0.33,1.59103], #(1)
[0.36,1.61247], #(1)
[0.4,1.6045], #(1)
[0.43,1.59492], #(1)
[0.46,1.63647], #(1)
[0.5,1.64062], #(1)
[0.53,1.64108], #(1)
[0.56,1.62777], #(1)
[0.6,1.62813], #(1)
[0.7,1.62359], #(1)
[0.8,1.6471], #(1)
[0.9,1.62737], #(1)
[1.0,1.64005], #(1)
[1.1,1.62155], #(1)
[1.2,1.61414], #(1)
[1.3,1.6133], #(1)
[1.4,1.61381], #(1)
[1.5,1.63847], #(1)
[1.6,1.62055], #(1)
[1.7,1.65908], #(1)
[1.8,1.64181], #(1)
[1.9,1.63964], #(1)
[2.0,1.62072], #(1)
[2.1,1.59464], #(1)
[2.2,1.63322], #(1)
[2.3,1.62072], #(1)
[2.4,1.64375], #(1)
[2.5,1.60161], #(1)
[2.6,1.5678], #(1)
[2.7,1.65084], #(1)
[3.3,1.61912], #(1)
[3.4,1.6327], #(1)
[3.7,1.62141], #(1)
[4.0,1.61057], #(1)
[5.0,1.62085], #(1)
[6.0,1.61258], #(1)
[7.0,1.60016], #(1)
[8.0,1.637], #(1)
[8.5,1.6011], #(1)
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

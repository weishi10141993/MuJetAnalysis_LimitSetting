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
masses2018 = [
0.2113,  0.2400,  0.2700,  0.3000,  0.3300,  0.3600,  0.4000,  0.4500,  0.5000,  0.6000,  0.7000,  0.8000,  0.9000,  1.0000,  1.0500,  1.0600,  1.0700,
1.0800,  1.0900,  1.1000,  1.2000,  1.2500,  1.2600,  1.2700,  1.2800,  1.2900,  1.3000,  1.3100,  1.3200,  1.3300,  1.3400,  1.3500,  1.4000,  1.5000,
1.6000,  1.7000,  1.8000,  1.9000,  1.9200,  1.9300,  1.9400,  1.9500,  1.9600,  1.9700,  1.9800,  1.9900,  2.0000,  2.0100,  2.0200,  2.0300,  2.0500,
2.1000,  2.2000,  2.3000,  2.4000,  2.4200,  2.4300,  2.4400,  2.4500,  2.4600,  2.4700,  2.4800,  2.5000,  2.6000,  2.7200,  3.2400,  3.4000,  3.7000,
4.0000,  4.5000,  4.6000,  4.7000,  4.8000,  4.9000,  5.0000,  5.1000,  5.2000,  5.3000,  5.4000,  5.5000,  5.6000,  5.7000,  5.8000,  5.9000,  6.0000,
6.5000,  7.0000,  7.5000,  7.8000,  7.9000,  8.0000,  8.1000,  8.2000,  8.3000,  8.4000,  8.5000,  8.6000,  8.7000,  8.8000,  8.9000,  8.9900,  11.0000,
13.0000, 14.5000, 15.0000, 15.5000, 16.0000, 16.5000, 17.0000, 19.0000, 19.5000, 20.0000, 20.5000, 21.0000, 21.5000, 22.0000, 22.5000, 23.0000, 25.0000,
27.0000, 29.0000, 31.0000, 33.0000, 33.5000, 34.0000, 34.5000, 35.0000, 35.5000, 36.0000, 36.5000, 37.0000, 37.5000, 38.0000, 38.5000, 39.0000, 39.5000,
40.0000, 40.5000, 41.0000, 41.5000, 42.0000, 43.0000, 45.0000, 46.5000, 47.0000, 47.5000, 48.0000, 48.5000, 49.0000, 49.5000, 50.0000, 50.5000, 51.0000,
51.5000, 52.0000, 52.5000, 53.0000, 53.5000, 54.0000, 54.5000, 55.0000, 55.5000, 56.0000, 56.5000, 57.0000, 57.5000, 58.0000, 58.5000, 59.0000, 59.5000,
59.9000
]
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
m_SR2_max  = 8.99;
m_SR3_min  = 11.;
m_SR3_max  = 59.9;

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

# unbinded model independent limit
Expected_Limits_Quantile_0p5_HybridNew_95_2018 = [
[0.2113,2.82757], #(1)
[0.24,2.84641], #(1)
[0.27,2.82671], #(1)
[0.3,2.81774], #(1)
[0.33,2.80628], #(1)
[0.36,2.83889], #(1)
[0.4,2.84015], #(1)
[0.45,2.82455], #(1)
[0.5,2.82594], #(1)
[0.6,2.84025], #(1)
[0.7,2.81815], #(1)
[0.8,2.82197], #(1)
[0.9,2.8295], #(1)
[1.0,2.8276], #(1)
[1.05,3.09698], #(1)
[1.06,3.99837], #(1)
[1.07,4.02498], #(1)
[1.08,4.01029], #(1)
[1.09,4.01444], #(1)
[1.1,3.9669], #(1)
[1.2,2.8866], #(1)
[1.25,2.83632], #(1)
[1.26,2.83914], #(1)
[1.27,2.83416], #(1)
[1.28,3.09387], #(1)
[1.29,3.89895], #(1)
[1.3,3.97458], #(1)
[1.31,3.98379], #(1)
[1.32,4.01731], #(1)
[1.33,4.00868], #(1)
[1.34,3.90804], #(1)
[1.35,3.36647], #(1)
[1.4,2.89347], #(1)
[1.5,2.82661], #(1)
[1.6,2.84297], #(1)
[1.7,2.83048], #(1)
[1.8,2.80717], #(1)
[1.9,2.81693], #(1)
[1.92,2.83461], #(1)
[1.93,2.92337], #(1)
[1.94,3.28975], #(1)
[1.95,3.95362], #(1)
[1.96,3.99672], #(1)
[1.97,4.01256], #(1)
[1.98,3.99178], #(1)
[1.99,4.00212], #(1)
[2.0,3.96862], #(1)
[2.01,3.9243], #(1)
[2.02,3.74334], #(1)
[2.03,3.26027], #(1)
[2.05,3.10621], #(1)
[2.1,2.93498], #(1)
[2.2,2.85322], #(1)
[2.3,2.85465], #(1)
[2.4,3.07135], #(1)
[2.42,3.98044], #(1)
[2.43,4.00391], #(1)
[2.44,4.01611], #(1)
[2.45,4.02295], #(1)
[2.46,4.01625], #(1)
[2.47,4.03925], #(1)
[2.48,4.01997], #(1)
[2.5,3.79197], #(1)
[2.6,2.94396], #(1)
[2.72,2.88613], #(1)
[3.24,2.82583], #(1)
[3.4,2.83004], #(1)
[3.7,2.83119], #(1)
[4.0,2.81806], #(1)
[4.5,2.82444], #(1)
[4.6,2.82076], #(1)
[4.7,2.82855], #(1)
[4.8,2.82115], #(1)
[4.9,3.09995], #(1)
[5.0,3.96863], #(1)
[5.1,3.51226], #(1)
[5.2,3.05267], #(1)
[5.3,2.92844], #(1)
[5.4,2.86522], #(1)
[5.5,2.85575], #(1)
[5.6,3.23834], #(1)
[5.7,3.9941], #(1)
[5.8,3.45401], #(1)
[5.9,3.06325], #(1)
[6.0,2.91851], #(1)
[6.5,2.84319], #(1)
[7.0,2.83498], #(1)
[7.5,2.83542], #(1)
[7.8,2.84703], #(1)
[7.9,2.82294], #(1)
[8.0,2.87948], #(1)
[8.1,3.87531], #(1)
[8.2,3.94955], #(1)
[8.3,5.59076], #(1)
[8.4,6.53225], #(1)
[8.5,6.03501], #(1)
[8.6,5.162], #(1)
[8.7,3.33399], #(1)
[8.8,4.56463], #(1)
[8.9,4.48011], #(1)
[8.99,4.64197], #(1)
[11.0,2.80084], #(1)
[13.0,2.80319], #(1)
[14.5,2.81995], #(1)
[15.0,2.82549], #(1)
[15.5,3.06212], #(1)
[16.0,4.0002], #(1)
[16.5,3.96162], #(1)
[17.0,3.81928], #(1)
[19.0,3.03669], #(1)
[19.5,3.04624], #(1)
[20.0,3.04489], #(1)
[20.5,3.0696], #(1)
[21.0,4.68473], #(1)
[21.5,6.26186], #(1)
[22.0,7.59567], #(1)
[22.5,7.75555], #(1)
[23.0,7.6342], #(1)
[25.0,3.3085], #(1)
[27.0,3.01425], #(1)
[29.0,2.90595], #(1)
[31.0,2.86623], #(1)
[33.0,2.82455], #(1)
[33.5,2.86801], #(1)
[34.0,2.85826], #(1)
[34.5,4.04932], #(1)
[35.0,4.07995], #(1)
[35.5,3.4899], #(1)
[36.0,3.13102], #(1)
[36.5,2.99052], #(1)
[37.0,3.03473], #(1)
[37.5,3.82857], #(1)
[38.0,6.87937], #(1)
[38.5,8.30893], #(1)
[39.0,7.57799], #(1)
[39.5,9.35182], #(1)
[40.0,7.97069], #(1)
[40.5,8.69017], #(1)
[41.0,8.38371], #(1)
[41.5,7.82786], #(1)
[42.0,6.17165], #(1)
[43.0,3.13812], #(1)
[45.0,2.89264], #(1)
[46.5,2.90585], #(1)
[47.0,2.86752], #(1)
[47.5,3.20458], #(1)
[48.0,4.90675], #(1)
[48.5,5.4928], #(1)
[49.0,5.31158], #(1)
[49.5,4.21018], #(1)
[50.0,3.33693], #(1)
[50.5,4.01994], #(1)
[51.0,4.09502], #(1)
[51.5,3.94243], #(1)
[52.0,3.47174], #(1)
[52.5,3.14645], #(1)
[53.0,2.97995], #(1)
[53.5,3.17792], #(1)
[54.0,4.11253], #(1)
[54.5,4.17843], #(1)
[55.0,3.97197], #(1)
[55.5,3.44867], #(1)
[56.0,3.33519], #(1)
[56.5,3.61795], #(1)
[57.0,3.71542], #(1)
[57.5,3.55474], #(1)
[58.0,4.4117], #(1)
[58.5,4.37529], #(1)
[59.0,4.15575], #(1)
[59.5,3.9769], #(1)
[59.9,3.87971], #(1)
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

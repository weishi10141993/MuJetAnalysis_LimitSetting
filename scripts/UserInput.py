#**************************************
#* Common Constants
#**************************************
#same mass points as Constants.h, will be used in PrintOutLimits.py and plots.py
masses = [0.2113, 0.2400, 0.2700, 0.3000, 0.3300, 0.3600, 0.4000, 0.4300, 0.4600, 0.5000, 0.5300, 0.5600,
   0.6000, 0.7000, 0.8000, 0.9000, 1.0000, 1.1000, 1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000,
   2.1000, 2.2000, 2.3000, 2.4000, 2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 8.5000,
   13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000]

#**************************************
#* Constants need for PrintOutLimits.py
#**************************************
CLsymbol = '95%' # confidence level
quantile = "0.500" # %.3f precision of expected quantiles, options: 0.500 (the following options if specified in Constants.h: 0.840, 0.160, 0.975, 0.025)
pwd = '/home/ws13/Run2LimitSetting/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/macros/'
basetxt = "sh/OutPut_"

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

## 2017: To be updated
lumi_fbinv_2017 = 36.734 # Total lumi [fb^-1]
SF_2017 = 0.969 # scale factor from MC to data: eFullData / eFullMc
eFullMc_over_aGen_2017 = 0.55 # average constant from all signal MC samples

## 2018: To be updated
lumi_fbinv_2018 = 59.97 # Total lumi [fb^-1]
SF_2018 = 0.969 # scale factor from MC to data: eFullData / eFullMc
eFullMc_over_aGen_2018 = 0.55 # average constant from all signal MC samples, to be updated

## mass range for SR1/2/3
m_SR1_min  = 0.2113;
m_SR1_max  = 2.72;
m_SR2_min  = 3.24;
m_SR2_max  = 9.;
m_SR3_min  = 11.;
m_SR3_max  = 59.;

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

# Expected median
Expected_Limits_Quantile_0p5_HybridNew_95_2017 = [ #To be updated
[0.2113,3.05264], #(1)
[0.24,3.03073], #(1)
[0.27,3.08591], #(1)
[0.3,3.03401], #(1)
[0.33,3.02064], #(1)
[0.36,3.06425], #(1)
[0.4,3.04144], #(1)
[0.43,3.04838], #(1)
[0.46,3.05708], #(1)
[0.5,3.01607], #(1)
[0.53,3.02095], #(1)
[0.56,3.05479], #(1)
[0.6,3.07778], #(1)
[0.7,3.03656], #(1)
[0.8,3.03211], #(1)
[0.9,3.03201], #(1)
[1.0,3.06297], #(1)
[1.1,3.01307], #(1)
[1.2,3.05722], #(1)
[1.3,3.04568], #(1)
[1.4,3.03635], #(1)
[1.5,3.06325], #(1)
[1.6,3.02774], #(1)
[1.7,3.03773], #(1)
[1.8,3.02898], #(1)
[1.9,3.03819], #(1)
[2.0,3.03784], #(1)
[2.1,3.04662], #(1)
[2.2,3.01878], #(1)
[2.3,3.06337], #(1)
[2.4,3.05004], #(1)
[2.5,3.0629], #(1)
[2.6,3.02728], #(1)
[2.7,3.0434], #(1)
[3.3,3.0428], #(1)
[3.4,3.02523], #(1)
[3.7,3.02422], #(1)
[4.0,3.01951], #(1)
[5.0,3.01573], #(1)
[6.0,3.01467], #(1)
[7.0,3.02755], #(1)
[8.0,3.03069], #(1)
[8.5,3.02737], #(1)
[13.0,3.05389], #(1)
[17.0,3.03366], #(1)
[21.0,2.97383], #(1)
[25.0,3.02047], #(1)
[29.0,3.04232], #(1)
[33.0,3.00044], #(1)
[37.0,2.98249], #(1)
[41.0,2.96413], #(1)
[45.0,3.02271], #(1)
[49.0,3.01691], #(1)
[53.0,3.07171], #(1)
[57.0,3.05286], #(1)
]

Expected_Limits_Quantile_0p84_HybridNew_95_2017 = [ #To be updated
[0.2113,3.0061], #(1)
[0.24,3.04104], #(1)
[0.27,3.03834], #(1)
[0.3,3.0168], #(1)
[0.33,3.03052], #(1)
[0.36,3.01497], #(1)
[0.4,2.9981], #(1)
[0.43,3.04139], #(1)
[0.46,3.01995], #(1)
[0.5,3.05362], #(1)
[0.53,3.00179], #(1)
[0.56,3.06381], #(1)
[0.6,3.02507], #(1)
[0.7,3.02512], #(1)
[0.8,3.04959], #(1)
[0.9,3.02734], #(1)
[1.0,3.06002], #(1)
[1.1,3.07339], #(1)
[1.2,3.03859], #(1)
[1.3,3.03855], #(1)
[1.4,3.04995], #(1)
[1.5,3.02666], #(1)
[1.6,3.02773], #(1)
[1.7,3.02247], #(1)
[1.8,3.02882], #(1)
[1.9,3.04414], #(1)
[2.0,3.0439], #(1)
[2.1,3.02804], #(1)
[2.2,3.0387], #(1)
[2.3,3.0508], #(1)
[2.4,3.0274], #(1)
[2.5,3.02197], #(1)
[2.6,3.02255], #(1)
[2.7,3.02371], #(1)
[3.3,3.02547], #(1)
[3.4,3.02048], #(1)
[3.7,3.0297], #(1)
[4.0,3.02144], #(1)
[5.0,3.03212], #(1)
[6.0,3.02461], #(1)
[7.0,3.02782], #(1)
[8.0,3.01864], #(1)
[8.5,3.02912], #(1)
[13.0,2.97536], #(1)
[17.0,3.00801], #(1)
[21.0,2.99069], #(1)
[25.0,3.05725], #(1)
[29.0,3.00178], #(1)
[33.0,3.05614], #(1)
[37.0,3.04189], #(1)
[41.0,3.05876], #(1)
[45.0,3.02353], #(1)
[49.0,3.05511], #(1)
[53.0,3.0438], #(1)
[57.0,3.08593], #(1)
]

Expected_Limits_Quantile_0p16_HybridNew_95_2017 = [ #To be updated
[0.2113,3.01507], #(1)
[0.24,3.06143], #(1)
[0.27,3.02103], #(1)
[0.3,3.05177], #(1)
[0.33,3.01527], #(1)
[0.36,3.04475], #(1)
[0.4,3.01665], #(1)
[0.43,3.01166], #(1)
[0.46,3.03289], #(1)
[0.5,3.04427], #(1)
[0.53,3.07216], #(1)
[0.56,3.06235], #(1)
[0.6,3.05033], #(1)
[0.7,3.05174], #(1)
[0.8,3.0276], #(1)
[0.9,3.06501], #(1)
[1.0,3.02024], #(1)
[1.1,3.03617], #(1)
[1.2,3.00834], #(1)
[1.3,3.01745], #(1)
[1.4,3.03944], #(1)
[1.5,3.03595], #(1)
[1.6,3.03752], #(1)
[1.7,3.0449], #(1)
[1.8,3.02921], #(1)
[1.9,3.04654], #(1)
[2.0,3.0376], #(1)
[2.1,3.01145], #(1)
[2.2,3.04738], #(1)
[2.3,3.03802], #(1)
[2.4,3.03631], #(1)
[2.5,3.02564], #(1)
[2.6,3.04175], #(1)
[2.7,3.03844], #(1)
[3.3,3.02092], #(1)
[3.4,3.01829], #(1)
[3.7,3.01581], #(1)
[4.0,3.04364], #(1)
[5.0,3.01454], #(1)
[6.0,3.02582], #(1)
[7.0,3.03119], #(1)
[8.0,3.02644], #(1)
[8.5,3.0256], #(1)
[13.0,3.01108], #(1)
[17.0,3.01722], #(1)
[21.0,2.98091], #(1)
[25.0,3.01262], #(1)
[29.0,2.98702], #(1)
[33.0,2.96883], #(1)
[37.0,2.98391], #(1)
[41.0,2.99869], #(1)
[45.0,3.01624], #(1)
[49.0,3.00614], #(1)
[53.0,2.954], #(1)
[57.0,2.97423], #(1)
]

Expected_Limits_Quantile_0p975_HybridNew_95_2017 = [ #To be updated
[0.2113,3.03221], #(1)
[0.24,3.07025], #(1)
[0.27,3.10228], #(1)
[0.3,3.00895], #(1)
[0.33,3.0192], #(1)
[0.36,3.02096], #(1)
[0.4,3.03315], #(1)
[0.43,3.02086], #(1)
[0.46,3.04629], #(1)
[0.5,3.02051], #(1)
[0.53,2.98454], #(1)
[0.56,3.04741], #(1)
[0.6,3.05551], #(1)
[0.7,3.05245], #(1)
[0.8,3.03201], #(1)
[0.9,3.07323], #(1)
[1.0,3.03187], #(1)
[1.1,3.03144], #(1)
[1.2,3.05916], #(1)
[1.3,3.01091], #(1)
[1.4,3.01831], #(1)
[1.5,3.0447], #(1)
[1.6,3.05249], #(1)
[1.7,3.03749], #(1)
[1.8,3.03898], #(1)
[1.9,3.01574], #(1)
[2.0,3.03323], #(1)
[2.1,3.03314], #(1)
[2.2,3.03305], #(1)
[2.3,3.02731], #(1)
[2.4,3.03756], #(1)
[2.5,3.03277], #(1)
[2.6,3.03345], #(1)
[2.7,3.0378], #(1)
[3.3,3.03617], #(1)
[3.4,3.02805], #(1)
[3.7,3.04215], #(1)
[4.0,3.02551], #(1)
[5.0,3.01623], #(1)
[6.0,3.03072], #(1)
[7.0,3.01823], #(1)
[8.0,3.024], #(1)
[8.5,3.02913], #(1)
[13.0,2.99515], #(1)
[17.0,2.99574], #(1)
[21.0,2.96413], #(1)
[25.0,3.0896], #(1)
[29.0,3.01938], #(1)
[33.0,3.06369], #(1)
[37.0,3.11345], #(1)
[41.0,3.13906], #(1)
[45.0,3.19168], #(1)
[49.0,3.23742], #(1)
[53.0,3.31559], #(1)
[57.0,3.3985], #(1)
]

Expected_Limits_Quantile_0p025_HybridNew_95_2017 = [ #To be updated
[0.2113,3.03648], #(1)
[0.24,3.03289], #(1)
[0.27,3.03873], #(1)
[0.3,3.0699], #(1)
[0.33,3.01205], #(1)
[0.36,3.03483], #(1)
[0.4,3.05855], #(1)
[0.43,3.02778], #(1)
[0.46,3.0006], #(1)
[0.5,3.06005], #(1)
[0.53,3.04693], #(1)
[0.56,3.03744], #(1)
[0.6,3.00706], #(1)
[0.7,3.02207], #(1)
[0.8,3.0413], #(1)
[0.9,3.04287], #(1)
[1.0,3.05505], #(1)
[1.1,3.034], #(1)
[1.2,3.04364], #(1)
[1.3,3.05329], #(1)
[1.4,3.06607], #(1)
[1.5,3.02822], #(1)
[1.6,3.03378], #(1)
[1.7,3.06619], #(1)
[1.8,3.02118], #(1)
[1.9,3.03639], #(1)
[2.0,3.05161], #(1)
[2.1,3.02876], #(1)
[2.2,3.03433], #(1)
[2.3,3.03494], #(1)
[2.4,3.04213], #(1)
[2.5,3.01411], #(1)
[2.6,3.03607], #(1)
[2.7,3.01675], #(1)
[3.3,3.02932], #(1)
[3.4,3.02039], #(1)
[3.7,3.02864], #(1)
[4.0,3.0348], #(1)
[5.0,3.02061], #(1)
[6.0,3.02998], #(1)
[7.0,3.03177], #(1)
[8.0,3.0285], #(1)
[8.5,3.02802], #(1)
[13.0,2.9975], #(1)
[17.0,3.00814], #(1)
[21.0,2.99405], #(1)
[25.0,2.989], #(1)
[29.0,2.97059], #(1)
[33.0,2.97237], #(1)
[37.0,3.01744], #(1)
[41.0,3.03979], #(1)
[45.0,2.98711], #(1)
[49.0,2.98709], #(1)
[53.0,2.97769], #(1)
[57.0,2.92826], #(1)
]

# To be filled
Expected_Limits_Quantile_0p5_HybridNew_90_2017   = []
Expected_Limits_Quantile_0p84_HybridNew_90_2017  = []
Expected_Limits_Quantile_0p16_HybridNew_90_2017  = []
Expected_Limits_Quantile_0p975_HybridNew_90_2017 = []
Expected_Limits_Quantile_0p025_HybridNew_90_2017 = []

# To be updated
Expected_Limits_Quantile_0p5_HybridNew_95_2018 = [
[0.2113,3.10088], #(1)
[0.24,3.07871], #(1)
[0.27,3.10585], #(1)
[0.3,3.12185], #(1)
[0.33,3.13548], #(1)
[0.36,3.02197], #(1)
[0.4,3.10268], #(1)
[0.43,3.0901], #(1)
[0.46,3.09478], #(1)
[0.5,3.07873], #(1)
[0.53,3.08018], #(1)
[0.56,3.11205], #(1)
[0.6,3.08986], #(1)
[0.7,3.10981], #(1)
[0.8,3.0776], #(1)
[0.9,3.08241], #(1)
[1.0,3.07885], #(1)
[1.1,3.0575], #(1)
[1.2,3.05492], #(1)
[1.3,3.11622], #(1)
[1.4,3.11289], #(1)
[1.5,3.1246], #(1)
[1.6,3.05345], #(1)
[1.7,3.07845], #(1)
[1.8,3.04368], #(1)
[1.9,3.10003], #(1)
[2.0,3.08093], #(1)
[2.1,3.10484], #(1)
[2.2,3.0158], #(1)
[2.3,3.05658], #(1)
[2.4,3.03549], #(1)
[2.5,3.00932], #(1)
[2.6,3.06975], #(1)
[2.7,3.05843], #(1)
[3.3,3.00251], #(1)
[3.4,3.02714], #(1)
[3.7,3.02475], #(1)
[4.0,3.02735], #(1)
[5.0,3.02509], #(1)
[6.0,3.02994], #(1)
[7.0,3.02855], #(1)
[8.0,3.0241], #(1)
[8.5,3.03846], #(1)
[13.0,3.03837], #(1)
[17.0,3.04654], #(1)
[21.0,3.01392], #(1)
[25.0,3.03505], #(1)
[29.0,3.00347], #(1)
[33.0,3.00409], #(1)
[37.0,2.989], #(1)
[41.0,2.99908], #(1)
[45.0,2.99864], #(1)
[49.0,3.0299], #(1)
[53.0,3.03103], #(1)
[57.0,3.04026], #(1)
]

Expected_Limits_Quantile_0p84_HybridNew_95_2018 = [
[0.2113,3.06134], #(1)
[0.24,3.07982], #(1)
[0.27,3.05577], #(1)
[0.3,3.12074], #(1)
[0.33,3.09207], #(1)
[0.36,3.03953], #(1)
[0.4,3.0551], #(1)
[0.43,3.12106], #(1)
[0.46,3.10528], #(1)
[0.5,3.04677], #(1)
[0.53,3.1114], #(1)
[0.56,3.08376], #(1)
[0.6,3.04519], #(1)
[0.7,3.05208], #(1)
[0.8,3.08102], #(1)
[0.9,3.05193], #(1)
[1.0,3.14494], #(1)
[1.1,3.03074], #(1)
[1.2,3.06359], #(1)
[1.3,3.08454], #(1)
[1.4,3.07295], #(1)
[1.5,3.05953], #(1)
[1.6,3.04908], #(1)
[1.7,3.07577], #(1)
[1.8,3.03586], #(1)
[1.9,3.15627], #(1)
[2.0,3.14958], #(1)
[2.1,3.08866], #(1)
[2.2,3.12654], #(1)
[2.3,3.04025], #(1)
[2.4,3.0816], #(1)
[2.5,3.06063], #(1)
[2.6,3.07524], #(1)
[2.7,3.0911], #(1)
[3.3,3.01673], #(1)
[3.4,3.02168], #(1)
[3.7,3.04935], #(1)
[4.0,3.01983], #(1)
[5.0,3.04944], #(1)
[6.0,3.01821], #(1)
[7.0,3.02743], #(1)
[8.0,3.03891], #(1)
[8.5,3.03329], #(1)
[13.0,3.0344], #(1)
[17.0,2.95819], #(1)
[21.0,3.00727], #(1)
[25.0,3.02509], #(1)
[29.0,3.05318], #(1)
[33.0,2.98688], #(1)
[37.0,3.03844], #(1)
[41.0,3.04724], #(1)
[45.0,3.0905], #(1)
[49.0,3.03356], #(1)
[53.0,3.04447], #(1)
[57.0,3.11259], #(1)
]

Expected_Limits_Quantile_0p16_HybridNew_95_2018 = [
[0.2113,3.0696], #(1)
[0.24,3.08332], #(1)
[0.27,3.07979], #(1)
[0.3,3.07921], #(1)
[0.33,3.05155], #(1)
[0.36,3.11251], #(1)
[0.4,3.0355], #(1)
[0.43,3.06775], #(1)
[0.46,3.05184], #(1)
[0.5,3.04802], #(1)
[0.53,3.11722], #(1)
[0.56,3.03742], #(1)
[0.6,3.10663], #(1)
[0.7,3.02582], #(1)
[0.8,3.00735], #(1)
[0.9,3.12332], #(1)
[1.0,3.12715], #(1)
[1.1,3.06792], #(1)
[1.2,3.09387], #(1)
[1.3,3.07556], #(1)
[1.4,3.14842], #(1)
[1.5,3.07608], #(1)
[1.6,3.08719], #(1)
[1.7,3.07538], #(1)
[1.8,3.06942], #(1)
[1.9,3.06377], #(1)
[2.0,3.08383], #(1)
[2.1,3.12347], #(1)
[2.2,3.08016], #(1)
[2.3,3.07213], #(1)
[2.4,3.0907], #(1)
[2.5,3.10393], #(1)
[2.6,3.0545], #(1)
[2.7,3.06419], #(1)
[3.3,3.02048], #(1)
[3.4,3.03525], #(1)
[3.7,3.03807], #(1)
[4.0,3.0353], #(1)
[5.0,3.03994], #(1)
[6.0,3.0243], #(1)
[7.0,3.02558], #(1)
[8.0,3.01635], #(1)
[8.5,3.03326], #(1)
[13.0,2.97086], #(1)
[17.0,2.97505], #(1)
[21.0,2.98953], #(1)
[25.0,3.01777], #(1)
[29.0,3.02061], #(1)
[33.0,2.93225], #(1)
[37.0,2.91234], #(1)
[41.0,3.00022], #(1)
[45.0,2.9674], #(1)
[49.0,2.98067], #(1)
[53.0,2.98413], #(1)
[57.0,3.05587], #(1)
]

Expected_Limits_Quantile_0p975_HybridNew_95_2018 = [
[0.2113,3.09811], #(1)
[0.24,3.09552], #(1)
[0.27,3.02503], #(1)
[0.3,3.07052], #(1)
[0.33,3.07363], #(1)
[0.36,3.12325], #(1)
[0.4,3.07493], #(1)
[0.43,3.09324], #(1)
[0.46,3.06708], #(1)
[0.5,3.0683], #(1)
[0.53,3.09289], #(1)
[0.56,3.05652], #(1)
[0.6,3.07665], #(1)
[0.7,3.1146], #(1)
[0.8,3.08149], #(1)
[0.9,3.09225], #(1)
[1.0,3.13672], #(1)
[1.1,3.20274], #(1)
[1.2,3.12031], #(1)
[1.3,3.08504], #(1)
[1.4,3.05149], #(1)
[1.5,3.12483], #(1)
[1.6,3.12023], #(1)
[1.7,3.06357], #(1)
[1.8,3.07886], #(1)
[1.9,3.10374], #(1)
[2.0,3.37136], #(1)
[2.1,3.07321], #(1)
[2.2,3.12612], #(1)
[2.3,3.2831], #(1)
[2.4,3.05779], #(1)
[2.5,3.06965], #(1)
[2.6,3.33215], #(1)
[2.7,3.06492], #(1)
[3.3,3.00909], #(1)
[3.4,3.03652], #(1)
[3.7,3.06855], #(1)
[4.0,3.03595], #(1)
[5.0,3.02555], #(1)
[6.0,3.03406], #(1)
[7.0,3.02783], #(1)
[8.0,3.02376], #(1)
[8.5,3.03167], #(1)
[13.0,3.12472], #(1)
[17.0,2.98844], #(1)
[21.0,2.96823], #(1)
[25.0,2.98266], #(1)
[29.0,3.10446], #(1)
[33.0,3.11285], #(1)
[37.0,3.16887], #(1)
[41.0,3.22536], #(1)
[45.0,3.30929], #(1)
[49.0,3.35273], #(1)
[53.0,3.52465], #(1)
[57.0,3.71871], #(1)
]

Expected_Limits_Quantile_0p025_HybridNew_95_2018 = [
[0.2113,3.04245], #(1)
[0.24,3.07025], #(1)
[0.27,3.12231], #(1)
[0.3,3.01694], #(1)
[0.33,3.10136], #(1)
[0.36,3.05176], #(1)
[0.4,3.07229], #(1)
[0.43,3.06251], #(1)
[0.46,3.08611], #(1)
[0.5,3.07959], #(1)
[0.53,3.07326], #(1)
[0.56,3.05928], #(1)
[0.6,3.10416], #(1)
[0.7,3.01114], #(1)
[0.8,3.05392], #(1)
[0.9,3.07402], #(1)
[1.0,3.07453], #(1)
[1.1,3.01188], #(1)
[1.2,3.10052], #(1)
[1.3,3.10334], #(1)
[1.4,3.09153], #(1)
[1.5,3.04016], #(1)
[1.6,3.08159], #(1)
[1.7,3.06295], #(1)
[1.8,3.08561], #(1)
[1.9,3.06111], #(1)
[2.0,3.08344], #(1)
[2.1,3.04253], #(1)
[2.2,3.07609], #(1)
[2.3,3.0591], #(1)
[2.4,3.08637], #(1)
[2.5,3.03107], #(1)
[2.6,3.05576], #(1)
[2.7,3.06792], #(1)
[3.3,3.00197], #(1)
[3.4,3.03384], #(1)
[3.7,3.03469], #(1)
[4.0,3.02294], #(1)
[5.0,3.02656], #(1)
[6.0,3.02628], #(1)
[7.0,3.01105], #(1)
[8.0,3.02671], #(1)
[8.5,3.0126], #(1)
[13.0,3.00461], #(1)
[17.0,3.00142], #(1)
[21.0,2.98141], #(1)
[25.0,2.99069], #(1)
[29.0,3.01051], #(1)
[33.0,3.01774], #(1)
[37.0,2.99659], #(1)
[41.0,2.95532], #(1)
[45.0,2.97849], #(1)
[49.0,2.97304], #(1)
[53.0,2.98552], #(1)
[57.0,2.97781], #(1)
]

# To be filled
Expected_Limits_Quantile_0p5_HybridNew_90_2018   = []
Expected_Limits_Quantile_0p84_HybridNew_90_2018  = []
Expected_Limits_Quantile_0p16_HybridNew_90_2018  = []
Expected_Limits_Quantile_0p975_HybridNew_90_2018 = []
Expected_Limits_Quantile_0p025_HybridNew_90_2018 = []

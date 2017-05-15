## Installing the framework
0. cmsrel CMSSW_7_6_3_patch2 #(Release needed for the Hggs combine tool)
   cd CMSSW_7_6_3_patch2/src/
   cmsenv
   git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
   git clone https://github.com/lpernie/limits_2a4mu.git
   scram b -j 6;
   cd limits_2a4mu;

# Running the model independent limits

1. Copy here "ws_FINAL.root" from bbBar estimation 
   -> RooStat file which has background model inside it.

2. root -b -q .x CreateDatacards.C+
   -> The first time you need to use option "true", so you will create "CreateROOTfiles.sh", a file that uses makeWorkSpace_H2A4Mu.C to make the RooStat files with S and B needed by CMS official limit calculator.
   -> NB: makeWorkSpace_H2A4Mu.C has hardcoded inside the TH2 range and binning, plus the Signal events. So for unblinding, add here the events you see.

3. (1st time only) cd macros; source CreateROOTfiles.sh; cd .. 
   -> Make RooStat files that should be supplied to CMS official limit calculator.

3. source macros/RunOnDataCard_std.sh (or macros/RunOnDataCard_T50000)
   -> Send jobs to run on all datacards and save outputs in outPut.txt. RunOnDataCard_T50000 runs more toys and it is better, but take more time. Choose the one you want.

4. cd macros; python PrintOutLimits.py; cd ..
   -> Print a out few lines to copy inside scripts/CmsLimitVsM.py, that will be used by Plots.py.

5. vim scripts/CmsLimitVsM.py + copy the lines you just produced after "Limits_HybridNew = ["
   -> If you change method from HybridNew, you can copy the line into another list and specify the correct method in CmsLimitVsM.py.

6. python Plots_RunMe.py 
   -> To make final limit plots. Here you can specify which function of Plots.py do you want to use.

# Some notes
Plots.py takes the cutflow from NMSSM mass points.

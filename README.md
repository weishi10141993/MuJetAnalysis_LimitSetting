## Installing the framework
0. SCRAM_ARCH=slc6_amd64_gcc491; export SCRAM_ARCH;   
1. cmsrel CMSSW_7_4_7 #(Release needed for the Hggs combine tool)   
2. cd CMSSW_7_4_7/src/   
3. cmsenv    
4. git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit    
5. git clone https://github.com/lpernie/limits_2a4mu.git    
6. scram b -j 6   
7. cd limits_2a4mu    

# Running the model independent limits
1. Copy here "ws_FINAL.root" from bbBar estimation    
   -> RooStat file which has background model inside it.   

2. root -b -q .x CreateDatacards.C+   
   -> The first time you need to use option "true", so you will create "CreateROOTfiles.sh", a file that uses makeWorkSpace_H2A4Mu.C to make the RooStat files with S and B needed by CMS official limit calculator.   
   -> NB: makeWorkSpace_H2A4Mu.C has hardcoded inside the TH2 range and binning, plus the Signal events. So for unblinding, add here the events you see.   

3. (1st time only) cd macros; source CreateROOTfiles.sh; cd ..;    
   -> Make RooStat files that should be supplied to CMS official limit calculator.    

3. source macros/RunOnDataCard_std.sh (or macros/RunOnDataCard_T50000)    
   -> Send jobs to run on all datacards and save outputs in outPut.txt. RunOnDataCard_T50000 runs more toys and it is better, but take more time. Choose the one you want.    

4. cd macros; python PrintOutLimits.py; cd ..;   
   -> This macro will print the lines you have to copy inside scripts/CmsLimitVsM.py (that will be used by Plots.py). 
   -> You have to copy the lined from "That contain N limits: \n XXX" until teh line before "Now remove the worse items". Remove also the first number each line, that represent the number of the jobs used to produce such limit   

5. In case you run combine several times (or more poeple followed the steps until here), you may want to average all the results, and place in scripts/CmsLimitVsM.py the final one
   -> Imagine 2 people followed this instruction, and you have two output from "PrintOutLimits.py". You copy the lines after "That contain N limits: \n XXX" until the line before "Now remove the worse items" in tow txt files.
   -> Then you run: python MergeLimit.py (where inside you specified the txt files locations and names)
   -> It will print out the lines to place in "scripts/CmsLimitVsM.py"

6. vim scripts/CmsLimitVsM.py + copy the lines you just produced after "Limits_HybridNew = ["    
   -> If you change method from HybridNew, you can copy the line into another list and specify the correct method in CmsLimitVsM.py.    

7. python Plots_RunMe.py    
   -> To make final limit plots. Here you can specify which function of Plots.py do you want to use.    

# Some notes   
1. NMSSM plots are done assuming an efficiency for the H decay taken from 2012 analysis

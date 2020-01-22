# Notes:
Command: combine -m 125 -M HybridNew --rule CLs --testStat LHC datacard_H2A4Mu_mA_0.2200_GeV.txt -t 100000 -s -1 (--fork 10)

Method HybridNew: Searching for a signal where a small number of events are expected (<10). Because asymptotic profile likelihood test-statistic distribution is no longer a good approximation, but can be very CPU / time intensive

## Install the Higgs combine framework
One should always refer to the official [Higgs combine page](http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/) for most updated instructions.
```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13
cd CMSSW_10_2_13/src
cmsenv
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
cd HiggsAnalysis/CombinedLimit
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit
git fetch origin
git checkout v8.0.1
scramv1 b clean; scramv1 b # always make a clean build

# clone repo for the analysis
git clone -b test git@github.com:weishi10141993/MuJetAnalysis_LimitSetting
cd MuJetAnalysis_LimitSetting     
```

# Run the model independent limits
1. Copy updated "ws_FINAL.root" from bbBar estimation. It contains background p.d.f.s.   

2. In this step, the datacards for each mass points are created.
   Edit CreateDatacards.C in order to set " isLxplus=true"/"false" depending if you are on lxplus or brazos and "string pwd=" to your current directory. Then do:
   ```
   root -l -b -q  CreateDatacards.C+  
   ```
   -> The first time you need to use option "bool makeRoot=true", so you will create "CreateROOTfiles.sh", a file that uses makeWorkSpace_H2A4Mu.C to make the RooStat files with S and B needed by CMS official limit calculator.   
   -> NB: makeWorkSpace_H2A4Mu.C has hardcoded inside the TH2 range and binning, plus the Signal events. So for unblinding, add here the events you see.   

3. (1st time only) Make RooStat files that should be supplied to CMS official limit calculator. The relevant signal and background shapes (extracted from ws_FINAL.root) are imported and saved in a workspace in a root file.
   ```
   cd macros; source CreateROOTfiles.sh; cd ..;
   ```  

4. Send jobs to run on all datacards and save outputs in outPut.txt. The options with the default toys (500) is
   ```
   source macros/RunOnDataCard_std.sh
   ```
   Refer to [TAMU SLURM page](http://brazos.tamu.edu/docs/slurm.html) for info about the batch submission system.

   If you want more toys, please use one of the following below
   ```
   source macros/RunOnDataCard_T10000.sh #10000 toys per job
   source macros/RunOnDataCard_T30000.sh #30000 toys per job
   source macros/RunOnDataCard_T50000.sh #50000 toys per job
   ```
   -> RunOnDataCard_T50000 runs more toys and it is better, but take more time. Choose the one you want.    

5. ```
   cd macros; python PrintOutLimits.py; cd ..;  
   ```
   -> This macro will print the lines you have to copy inside scripts/CmsLimitVsM.py (that will be used by Plots.py).
   -> You have to copy the lined from "That contain N limits: \n XXX" until teh line before "Now remove the worse items". Remove also the first number each line, that represent the number of the jobs used to produce such limit   

6. [Not Tested] In case you run combine several times (or more people followed the steps until here), you may want to average all the results, and place in scripts/CmsLimitVsM.py the final one
   -> Imagine 2 people followed this instruction, and you have two output from "PrintOutLimits.py". You copy the lines after "That contain N limits: \n XXX" until the line before "Now remove the worse items" in tow txt files.
   -> Then you run: python MergeLimit.py (where inside you specified the txt files locations and names)
   -> It will print out the lines to place in "scripts/CmsLimitVsM.py"

7. Edit "scripts/CmsLimitVsM.py" and copy the lines you just produced after "Limits_HybridNew = ["    
   -> If you change method from HybridNew, you can copy the line into another list and specify the correct method in CmsLimitVsM.py.    

8. Make final limit plots. You can specify which functions from Plots.py to use.  
   ```
   python Plots_RunMe.py  
   ```  

# Notes   
1. NMSSM plots are done assuming an efficiency for the H decay taken from 2012 analysis

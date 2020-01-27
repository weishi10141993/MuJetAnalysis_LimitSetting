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
   ```
   cp ~/RunII2017/CMSSW_9_4_7/src/MuJetAnalysis_bbBarEstimation/ws_FINAL.root .
   ```

2. In this step, the datacards for each mass points are created. Also the submission files to run combine toy experiments are created.
   Edit CreateDatacards.C in order to set " isLxplus=true"/"false" depending if you are on lxplus or brazos and "string pwd=" to your current directory. Then do:
   ```
   root -l -b -q  CreateDatacards.C+  
   ```
   -> The first time you need to use option "bool makeRoot=true", so you will create "CreateROOTfiles.sh", a file that uses makeWorkSpace_H2A4Mu.C to make the RooStat files with S and B needed by CMS official limit calculator.   
   -> NB: makeWorkSpace_H2A4Mu.C has hardcoded inside the TH2 range and binning, plus the signal events. So for unblinding, add here the events you see.

   A typical combine command to obtain expected 95% CL limit for 0.5 quantile (median) looks like this:
   ```
   combine -n .H2A4Mu_mA_0.2113_GeV_0 -m 125 -M HybridNew --saveHybridResult --expectedFromGrid 0.500 --rule CLs --testStat LHC --cl 0.95  -s -1 -T 30000 Datacards/datacard_H2A4Mu_mA_0.2113_GeV.txt -v 1
   ```
   "--cl" is a common statistic option to many combine methods. It specifies the confidence level you want, default as 0.95 in combine. The "rule" option specifies the rule to use, default us CLs.
   "expectedFromGrid" tells combine to use the grid to compute the expected limit for this quantile. To produce observed limit, remove the "--expectedFromGrid" option.

   For more combine options:
   ```
   combine --help
   ```
   In the case the AsymptoticLimits method is used, there is no need to add "--expectedFromGrid". It will produce both observed and expected limits at different quantiles.

3. (1st time only) Make RooStat files that should be supplied to CMS official limit calculator. The relevant signal and background shapes (extracted from ws_FINAL.root) are imported and saved in a workspace in a root file.
   ```
   cd macros; source CreateROOTfiles.sh; cd ..;
   ```  

4. Send jobs to run on all datacards and save outputs in outPut.txt. The default toys in combine is 500. Typically, we'll need 30000 toys/job:
   ```
   source macros/RunOnDataCard_T30000.sh #30000 toys/job (recommended)
   #source macros/RunOnDataCard_std.sh #500 toys/job
   #source macros/RunOnDataCard_T10000.sh #10000 toys/job
   #source macros/RunOnDataCard_T50000.sh #50000 toys/job
   ```
   The more toys, the better, but it takes more time. Refer to [TAMU SLURM page](http://brazos.tamu.edu/docs/slurm.html) for info about the batch submission system.

   After jobs are done, toy stats distributions along with the limit value, error and expected quantiles will be stored in root files like this:
   ```
   higgsCombine.H2A4Mu_mA_0.2113_GeV_0.HybridNew.mH125.1239963725.quant0.500.root
   ```

   Run the following to plot the test statistic distributions:
   ```
   python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/plotTestStatCLs.py --input higgsCombine.H2A4Mu_mA_0.2113_GeV_0.HybridNew.mH125.1239963725.quant0.500.root --poi r --val all --mass 125
   ```
   This produces a new ROOT file "cls_qmu_distributions.root" containing the plots.

5. This macro will print the lines you have to copy inside scripts/CmsLimitVsM.py (that will be used by Plots.py).
   Edit the quantile parameter file to get limits for that quantile each time.
   ```
   cd macros; python PrintOutLimits.py; cd ..;  
   ```
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

2. Method HybridNew: Searching for a signal where a small number of events are expected (<10). Because asymptotic profile likelihood test-statistic distribution is no longer a good approximation, but can be very CPU / time intensive

3. Command: combine -m 125 -M HybridNew --rule CLs --testStat LHC datacard_H2A4Mu_mA_0.2200_GeV.txt -t 100000 -s -1 (--fork 10)

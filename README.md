## Install the Higgs combine framework
One should always refer to the official [Higgs combine page](http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/) for most updated instructions.
```
#If use TAMU Terra cluster, need to do the following after log-in (as of Mar 23):
# source /scratch/group/mitchcomp/bin/cms-setup
# source /cvmfs/cms.cern.ch/cmsset_default.sh

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

# Run the model independent limits for each year
1. Make sure background shape root file from each year is updated from low mass background estimation.    

2. Create the data card and submission files to run combine toy experiments for each mass point. Edit Config.h in order to set which year (default is 2018, can choose 2016/2017/2018) to run. Also edit Constants.h to update signal and background rates for the year. Then do:

   ```
   root -l -b -q  CreateDatacards.C+
   ```

   Note:The first time you need to use option "bool makeRoot=true", so you will create "CreateROOTfiles.sh", a file that uses makeWorkSpace_H2A4Mu.C to make the RooStat files with S and B needed by CMS official limit calculator. makeWorkSpace_H2A4Mu.C has hardcoded inside the TH2 range, binning and the signal events. So for unblinding, add here events you see.

3. (1st time only) Create and save signal and background shapes to a workspace in a root file for each mass point.

   ```
   cd macros; source CreateROOTfiles.sh; cd ..;
   ```

4. Send jobs to run combine for each mass point.

   ```
   source macros/RunOnDataCard_T30000.sh #600000 toys/job (recommended)
   ```

   The more toys, the better, but it takes more time. Refer to [TAMU Terra page](https://hprc.tamu.edu/wiki/Terra:Batch_Processing_SLURM) for info about the slurm batch system.

   After jobs are done, toy stats distributions along with the limit value, error and expected quantiles will be stored in root files like this:
   ```
   higgsCombine.H2A4Mu_mA_*_GeV_0.HybridNew.mH125.*.quant0.500.root
   ```

   Run the following to plot the test statistic distributions:
   ```
   python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/plotTestStatCLs.py --input higgsCombine.H2A4Mu_mA_*.root --poi r --val all --mass 125
   ```
   This produces a new ROOT file "cls_qmu_distributions.root" containing the plots.

5. Print the limit of each mass point that you need to copy inside scripts/UserInput.py (later will be used by CmsLimitVsM.py and Plots.py). Edit other parameters in UserInput.py at the 'PrintOutLimits.py' block if necessary. Then do:


   ```
   cd macros; python PrintOutLimits.py; cd ..;  
   ```

   Note: You have to copy the line from "That contain N limits: \n XXX" until the line before "Now remove the worse items". Remove also the first number each line, that represent the number of the jobs used to produce such limit.   

6. [Not Tested] In case you run combine several times (or more people followed the steps until here), you may want to average all the results, and place in scripts/CmsLimitVsM.py the final one
   -> Imagine 2 people followed this instruction, and you have two output from "PrintOutLimits.py". You copy the lines after "That contain N limits: \n XXX" until the line before "Now remove the worse items" in tow txt files.
   -> Then you run: python MergeLimit.py (where inside you specified the txt files locations and names)
   -> It will print out the lines to place in "scripts/CmsLimitVsM.py"

7. Edit "scripts/UserInput.py" and copy the lines you just produced for the quantile (default: only 0.5 quantile) for that year.
   Note: If you change method from HybridNew, you can copy the line into another list and specify the correct method in CmsLimitVsM.py.    

8. After all limits from all quantiles are filled in UserInput.py, now we make final limit plots. Edit year (default as 2018) in scripts/UserInput.py. You can specify which plots to draw from Plots.py. The default output dir is scripts/plots95.

   ```
   cd scripts; python Plots_RunMe.py  
   ```  

   ALP limits: After running, the files "ALPLimits/CMSRun2ALP*.txt" are updated. Replace the same files in "ALPLimits/Electron_Coupling/" with the updated files and run ALP_CMSRun2.nb in Mathematica to get updated limit plot for ALP couplings to leptons. The ALP couplings to the higgs limit plot is in scripts/plots95.

   NMSSM Limits: The NMSSM limit as a function of CP-even/odd higgs is in scripts/plots95.

# Combine data cards of multiple years
1. The mass points below 9GeV will be combined for 2016-2018. The mass points above 9GeV will be combined for 2017-2018. Should be dense enough as observed events of each year can have quite different distributions.

2. Edit the CombineDataCards option in CreateDatacards.C to true and run the following to combine datacards:

   ```
   root -l -b -q  CreateDatacards.C+ # this creates shell scripts below
   cd macros;
   source CombineLowMassThreeYears.sh;
   source CombineAllMassTwoYears.sh;
   cd ..;
   ```
   Combined cards should appear in Datacards/Run2Combined folder.

3. Send jobs to run combine for each mass point with combine data cards:

   ```
   source macros/RunOnDataCardCombineThreeYear_T30000.sh
   source macros/RunOnDataCardCombineTwoYear_T30000.sh
   ```


# Notes   
1. NMSSM plots are done assuming an efficiency for the H decay taken from 2012 analysis

2. Method HybridNew: Searching for a signal where a small number of events are expected (<10). Because asymptotic profile likelihood test-statistic distribution is no longer a good approximation, but can be very CPU / time intensive

3. A typical combine command to obtain expected 95% CL limit for 0.5 quantile (median) looks like this:
```
combine -n .H2A4Mu_mA_0.2113_GeV_0 -m 125 -M HybridNew --saveHybridResult --expectedFromGrid 0.500 --rule CLs --testStat LHC --cl 0.95  -s -1 -T 30000 Datacards/datacard_H2A4Mu_mA_0.2113_GeV.txt -v 1
```

"--cl" is a common statistic option to many combine methods. It specifies the confidence level you want, default as 0.95 in combine. The "rule" option specifies the rule to use, default is CLs.
"expectedFromGrid" tells combine to use the grid to compute the expected limit for this quantile. To produce observed limit, remove the "--expectedFromGrid" option.
In case you have some knowledge of where the limit should be, then setting an appropriate --rMax can speed up the search.

Finding the expected -2 s.t.d. deviation band can take significantly longer: CLs = CLs+b / CLb where CLb = 0.025 by construction, Need ~ 20 times as many toys to get same CLs accuracy as for median. You can use the --fork N option to run up to N toys in parallel.

For more combine options:
```
combine --help
```

## Install the Higgs Combine Framework
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

##  Model Independent Limits for Each Year
1. Make sure background shape root file (ws_*FINAL.root) from that year (default 2018) is updated from low mass background estimation. Make sure high mass background shape is up-to-date.  

2. Create the data card and submission files to run combine toy experiments for each mass point. Edit Config.h to set the year (default is 2018, the 2020 option will combine data cards for 2016+2018). Also edit Constants.h to update signal and background rates for the year. Then do:

   ```
   root -l -b -q  CreateDatacards.C+
   ```

   Note:The first time you need to use option "bool makeRoot=true", so you will create "CreateROOTfiles.sh", a file that uses makeWorkSpace_H2A4Mu.C to make the RooStat files with signal and background needed by limit calculator. makeWorkSpace_H2A4Mu.C has hardcoded inside the TH2 range, binning and the signal events. So for unblinding, add here events you see.

   After running this step, you should be able to see the data cards appear in the folder "Datacards/<year>". Also two shell scripts in step 3 and 4 should be there.

3. (1st time only) Create and save signal and background shapes to a workspace in a root file for each mass point.

   ```
   cd macros; source CreateROOTfiles.sh; cd ..;
   ```

   After this step you should be able to find the root files for each mass point in "workSpaces/<year>" folder.

4. Send jobs to run combine for each mass point. Before submit, test run one point using the combine command. Stay outside the macros directory to source the file below as the relative directory matters here.

   ```
   source macros/RunOnDataCard_T30000.sh #30k toys/job (recommended)
   ```

   The more toys, the better, but it takes more time. Refer to [TAMU Terra page](https://hprc.tamu.edu/wiki/Terra:Batch_Processing_SLURM) for info about the slurm batch system.

   After the jobs are done, you should be able to see the text file containing the limit for each mass point in "macros/sh/<year>/output/".

   [Optional]
   After jobs are done, toy stats distributions along with the limit value, error and expected quantiles will be stored in root files like this:
   ```
   higgsCombine.H2A4Mu_mA_*_GeV_0.HybridNew.mH125.*.quant0.500.root
   ```

   Run the following to plot the test statistic distributions:
   ```
   python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/plotTestStatCLs.py --input higgsCombine.H2A4Mu_mA_*.root --poi r --val all --mass 125
   ```
   This produces a new ROOT file "cls_qmu_distributions.root" containing the plots.

5. This step prints the limit of each mass point in the text files of previous step. You will need to copy the printed limits inside scripts/UserInput.py (later to be used by CmsLimitVsM.py and Plots.py). Edit other parameters in UserInput.py at the 'PrintOutLimits.py' block if necessary. Then do:

   ```
   cd macros; python PrintOutLimits.py; cd ..;
   ```

   Note: You have to copy the line from "That contain N limits: \n XXX" until the line before "Now remove the worse items". Remove also the first number each line, that represent the number of the jobs used to produce such limit.   

6. [Note: this step is not tested, use with caution!!!] In case you run combine several times (or more people followed the steps until here), you may want to average all the results, and place in scripts/CmsLimitVsM.py the final one
   -> Imagine 2 people followed this instruction, and you have two output from "PrintOutLimits.py". You copy the lines after "That contain N limits: \n XXX" until the line before "Now remove the worse items" in tow txt files.
   -> Then you run: python MergeLimit.py (where inside you specified the txt files locations and names)
   -> It will print out the lines to place in "scripts/CmsLimitVsM.py"

7. Edit "scripts/UserInput.py" and copy the lines you just produced for the quantile (default: only 0.5 quantile) for that year.
   Note: If you change method from HybridNew, you can copy the line into another list and specify the correct method in CmsLimitVsM.py.    

8. After all limits from all quantiles are filled in UserInput.py, now we make final limit plots. Edit year (default as 2018) in scripts/UserInput.py. You can specify which plots to draw from Plots.py. The default output dir is 'scripts/plots95'.

   ```
   cd scripts; python Plots_RunMe.py
   ```  

9. Limits for benchmark Models:

   (A) ALP limits:

   The ALP couplings to the higgs and leptons limit plot is in scripts/plots95.

   To get updated limit plot for ALP couplings to leptons in the theory paper: after running the command in previous step, files "ALPLimits/CMSRun2ALP*.txt" will be updated. Replace the same files in "ALPLimits/Electron_Coupling/" with the updated text files and evaluate 'ALP_CMSRun2.nb' in Mathematica (tested in 12.1.1 student version) to get updated limit plot for ALP couplings to leptons.

   Note: Download the ALPLimits folder to local Downloads folder, make sure the directory setting in 'ALP_CMSRun2.nb' match your local directory, default at these input lines:

   In[114]: ~/Downloads/ALPLimits/MathematicaConfig/mmapkg

   In[171]: ~/Downloads/ALPLimits/MathematicaConfig/RunDec.m

   In[180]: ~/Downloads/ALPLimits/Electron_Coupling

   (B) NMSSM Limits: The NMSSM limits as a function of CP-even/odd higgs mass are in scripts/plots95.

   (C) Dark SUSY Limits: Ask Alfredo for help.

## Combine Data Cards (2016+2018) Below 9 GeV
1. Make sure the workSpace of 2016 and 2018 contain the updated shape files. Make sure 2016 and 2018 data cards are available at each mass point.

   Notes: The mass points above 9GeV will be for 2018 only. Should be dense enough as observed events of each year can have quite different distributions.

2. Edit the year in 'Config.h' to 2020 (default is 2018), and run the following to combine data cards:

   ```
   root -l -b -q  CreateDatacards.C+ # this creates the 'CombineLowMass.sh' file below
   cd Datacards/2020;
   source CombineLowMass.sh;
   cd ../..;
   ```
   After this step, combined data cards should appear in Datacards/2020 folder. Also the shell script used in step 3 is created.

3. Send jobs to run combine for each mass point with combined data cards:

   ```
   source macros/RunOnDataCardCombineLowMass_T30000.sh
   ```

4. Change year to 2020 (default is 2018) in 'scripts/UserInput.py'. Edit other parameters in UserInput.py at the 'PrintOutLimits.py' block if necessary. Then do:

   ```
   cd macros; python PrintOutLimits.py; cd ..;
   ```
   Once done, open "scripts/UserInput.py" and copy the lines you just produced for the quantile (default: only 0.5 quantile) for year 2020 (i.e., combined 2016+2018).

6. Make sure the year is 2020 (default is 2018) in 'scripts/UserInput.py'. After above limits are filled in UserInput.py, you can specify which plots to draw from Plots.py. The default output dir is 'scripts/plots95'.

   ```
   cd scripts; python Plots_RunMe.py
   ```  


## Notes   
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

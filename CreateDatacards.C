#include <stdio.h>
#include <TH1F.h>
#include <TFile.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TH2F.h>
#include <TH1D.h>
#include <THStack.h>
#include <TRandom3.h>
#include <TFormula.h>
#include <TPad.h>
#include <TLegend.h>
#include <TStyle.h>
#include <TROOT.h>
#include <TMarker.h>
#include <TChain.h>
#include <memory>
#include <string>
#include <map>
#include <vector>
#include "TTree.h"
#include "TLatex.h"
#include "TMath.h"
#include "TBranch.h"
#include "TFile.h"
#include "TStyle.h"
#include "TString.h"
#include "TEventList.h"
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>

#define N_Signals 60 //48 low mass + 12 high mass

void CreateDatacards( bool makeRoot=true ){
  //*******************************
  // User change parameters below
  //*******************************
  //On which machine are you running jobs? Brazos: false; Lxplus: true
  bool isLxplus = false;

  //Expected Limit quantiles
  float expected_quantiles[5] = {0.500, 0.840, 0.160, 0.975, 0.025};

  //TString Myrule = "--rule CLs --LHCmode LHC-limits --toysFrequentist"; //OLD command "--rule CLs --testStat LHC"
  TString Myrule = "--rule CLs --testStat LHC";
  Myrule = Myrule + " --cl 0.95";
  string pwd = "/home/ws13/Run2LimitSetting/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/";

  //After unblinding data, need to change the mass granularity accordingly
  float masses[N_Signals] = {0.2113, 0.2400, 0.2600, 0.3000, 0.3300, 0.3600, 0.4000, 0.4300, 0.4600, 0.5000,
     0.5300, 0.5600, 0.6000, 0.7000, 0.8000, 0.8800, 0.9000, 0.9100, 0.9200, 0.9300, 0.9400, 1.0000, 1.1000,
     1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000, 2.1000, 2.2000, 2.3000, 2.4000,
     2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 8.5000,
     13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000};

  bool DiffSeed=true;
  int Ninit=0, Nend=1;//Each mass point will be submitted (Nend-Ninit) times

  int Seeds[N_Signals]={0};
  for( int i=0; i<N_Signals; i++){ Seeds[i]=-1; }

  //N events
  int obs = -1;
  //==============
  //2017 expected
  //==============
  //SR1: Below J/psi
  float signal1_rate = 1, BBbar_below_Jpsi_2D_rate = 1.50; //Sig and Bkg rate
  float BBbar_norm = 1.123, BBbar_syst = 1.2; //Background Uncertainties, also apply to SR2
  //SR2: Above J/psi, below 9 GeV
  float signal2_rate = 1, BBbar_above_Jpsi_2D_rate = 0.06;
  //SR3: Above 9 GeV
  float signal3_rate = 1, HighMassBKG_rate = 7.24;

  //Signal Uncertainties
  float lumi_13TeV = 1.025, mu_hlt = 1.015, mu_id = 1.024, mu_iso = 1.02, mu_pu = 1.0017;
  float ovlp_trk = 1.024, ovlp_mu = 1.026, dimu_M = 1.015, nnlo_pt = 1.02, pdf_as = 1.08, HxecBr = 1.038;

  /*
  //==============
  //2016 expected
  //==============
  float signal_rate = 1, BBbar_2D_rate = 7.2584, DJpsiS_2D_rate = 0.31806, DJpsiD_2D_rate = 0.019;
  //Signal Uncertainties
  float lumi_13TeV = 1.025, mu_hlt = 1.06, mu_id = 1.024, mu_iso = 1.02, mu_pu = 1.0017;
  float ovlp_trk = 1.024, ovlp_mu = 1.026, dimu_M = 1.015, nnlo_pt = 1.02, pdf_as = 1.08, HxecBr = 1.038;
  //Background Uncertainties
  float BBbar_norm=43, BBbar_norm2=0.1688, BBbar_norm3=1.123, BBbar_syst=1.2;
  float DJpsiD_norm=5, DJpsiD_norm2=0.0038, DJpsiS_norm=27, DJpsiS_norm2=0.01178, DJpsi_extr=1.15;
  */

  //*******************************
  // User change parameters above
  //*******************************

  //Creat Folders
  TString makeFold="mkdir -p macros/sh";
  system( makeFold.Data() );
  makeFold="mkdir -p workSpaces";
  system( makeFold.Data() );
  makeFold="mkdir -p Datacards";
  system( makeFold.Data() );
  makeFold="mkdir -p plots/PDF";
  system( makeFold.Data() );
  makeFold="mkdir -p plots/PNG";
  system( makeFold.Data() );
  makeFold="mkdir -p plots/C";
  system( makeFold.Data() );

  //Create ROOT file
  if(makeRoot){
    FILE *file_sh=fopen("macros/CreateROOTfiles.sh", "w");
    for(int i=0; i<N_Signals; i++){
      fprintf(file_sh, "root -l -b -q 'makeWorkSpace_H2A4Mu.C(%.4f)'\n", masses[i]);
    }
    fclose(file_sh);
  }

  //Create submission files
  string endCom="sh";
  if(!isLxplus) endCom="slrm";

  FILE *file_sh_std = fopen("macros/RunOnDataCard_std.sh", "w");
  for(int h=0;h<5;h++){//loop over quantile
    for(int Nit=Ninit; Nit<Nend; Nit++ ){//loop over number of jobs
      string pedex = std::to_string(Nit);
      for(int i=0; i<N_Signals; i++){//loop over mass points
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_std, "%s \n", command);
      }
    }
  }
  fclose(file_sh_std);

  FILE *file_sh_10k = fopen("macros/RunOnDataCard_T10000.sh", "w");
  for(int h=0;h<5;h++){
    for(int Nit=Ninit; Nit<Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      for(int i=0; i<N_Signals; i++){
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_T10000_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else         sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_T10000_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_10k, "%s \n", command);
      }
    }
  }
  fclose(file_sh_10k);

  FILE *file_sh_50k = fopen("macros/RunOnDataCard_T50000.sh", "w");
  for(int h=0;h<5;h++){
    for(int Nit=Ninit; Nit<Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      for(int i=0; i<N_Signals; i++){
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_T50000_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else         sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_T50000_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_50k, "%s \n", command);
      }
    }
  }
  fclose(file_sh_50k);

  FILE *file_sh_30k = fopen("macros/RunOnDataCard_T30000.sh", "w");
  for(int h=0;h<5;h++){
    for(int Nit=Ninit; Nit<Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      for(int i=0; i<N_Signals; i++){
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_T30000_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else         sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_T30000_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_30k, "%s \n", command);
      }
    }
  }
  fclose(file_sh_30k);

  // Produce submission file
  // Loop over quantiles
  for(int h=0;h<5;h++){
    // Loop over jobs
    for(int Nit=Ninit; Nit<Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      // Loop over mass points
      for(int i=0; i<N_Signals; i++){
        char name[100];
        char name_T10000[100];
        char name_T50000[100];
        char name_T30000[100];
        sprintf(name, "macros/sh/send_%.3f_%.4f_%s.%s", expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        sprintf(name_T10000, "macros/sh/send_%.3f_%.4f_T10000_%s.%s", expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        sprintf(name_T50000, "macros/sh/send_%.3f_%.4f_T50000_%s.%s", expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        sprintf(name_T30000, "macros/sh/send_%.3f_%.4f_T30000_%s.%s", expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());

        FILE *file_combine_std=fopen(name, "w");
        fprintf(file_combine_std, "#!/bin/bash\n");
        if(!isLxplus){
          fprintf(file_combine_std, "#SBATCH -J runsplit\n");
          fprintf(file_combine_std, "#SBATCH -p stakeholder-4g\n");
          fprintf(file_combine_std, "#SBATCH -n1\n");
          fprintf(file_combine_std, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_std, "#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_std, "#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
          fprintf(file_combine_std, "#SBATCH --ntasks-per-core=1\n");
        }
        fprintf(file_combine_std, "cd %s \n", pwd.c_str());
        fprintf(file_combine_std, "eval `scramv1 runtime -sh`\n");
        if(DiffSeed) fprintf(file_combine_std, "combine -n .H2A4Mu_mA_%.4f_GeV_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        else         fprintf(file_combine_std, "combine -n .H2A4Mu_mA_%.4f_GeV_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        fclose(file_combine_std);

        FILE *file_combine_10k=fopen(name_T10000, "w");
        fprintf(file_combine_10k, "#!/bin/bash\n");
        if(!isLxplus){
          fprintf(file_combine_10k, "#SBATCH -J runsplit\n");
          fprintf(file_combine_10k, "#SBATCH -p stakeholder-4g\n");
          fprintf(file_combine_10k, "#SBATCH -n1\n");
          fprintf(file_combine_10k, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_10k, "#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_10k, "#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
          fprintf(file_combine_10k, "#SBATCH --ntasks-per-core=1\n");
        }
        fprintf(file_combine_10k, "cd %s \n", pwd.c_str());
        fprintf(file_combine_10k, "eval `scramv1 runtime -sh`\n");
        if(DiffSeed) fprintf(file_combine_10k, "combine -n .H2A4Mu_mA_%.4f_GeV_T10000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d -T 10000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T10000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        else         fprintf(file_combine_10k, "combine -n .H2A4Mu_mA_%.4f_GeV_T10000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -T 10000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T10000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        fclose(file_combine_10k);

        FILE *file_combine_50k = fopen(name_T50000, "w");
        fprintf(file_combine_50k, "#!/bin/bash\n");
        if(!isLxplus){
          fprintf(file_combine_50k, "#SBATCH -J runsplit\n");
          fprintf(file_combine_50k, "#SBATCH -p stakeholder-4g\n");
          fprintf(file_combine_50k, "#SBATCH -n1\n");
          fprintf(file_combine_50k, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_50k, "#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_50k, "#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
          fprintf(file_combine_50k, "#SBATCH --ntasks-per-core=1\n");
        }
        fprintf(file_combine_50k, "cd %s \n",pwd.c_str());
        fprintf(file_combine_50k, "eval `scramv1 runtime -sh`\n");
        if(DiffSeed) fprintf(file_combine_50k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T50000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d -T 50000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T50000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        else         fprintf(file_combine_50k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T50000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -T 50000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T50000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        fclose(file_combine_50k);

        FILE *file_combine_30k = fopen(name_T30000, "w");
        fprintf(file_combine_30k, "#!/bin/bash\n");
        if(!isLxplus){
          fprintf(file_combine_30k, "#SBATCH -J runsplit\n");
          fprintf(file_combine_30k, "#SBATCH -p stakeholder-4g\n");
          fprintf(file_combine_30k, "#SBATCH -n1\n");
          fprintf(file_combine_30k, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_30k, "#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_30k, "#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
          fprintf(file_combine_30k, "#SBATCH --ntasks-per-core=1\n");
        }
        fprintf(file_combine_30k, "cd %s \n",pwd.c_str());
        fprintf(file_combine_30k, "eval `scramv1 runtime -sh`\n");
        if(DiffSeed) fprintf(file_combine_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d -T 30000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        else         fprintf(file_combine_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -T 30000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        fclose(file_combine_30k);
      }//End N_Signals
    }//End Ninit
  }//End h quantile

  //Create datacards for each mass point
  for(int i=0; i<N_Signals; i++){
    stringstream massesS;
    massesS << fixed << setprecision(4) << masses[i];
    TString Thisname_txt = "datacard_H2A4Mu_mA_" + massesS.str() + "_GeV.txt";
    FILE *file_txt=fopen( ("Datacards/" + Thisname_txt).Data(),"w");
    fprintf(file_txt, "# HybridNew CLs: \n");
    fprintf(file_txt, "#    combine      -n .H2A4Mu_mA_%.4f_GeV            -m 125 -M HybridNew --rule CLs --LHCmode LHC-limits     datacard_H2A4Mu_mA_%.4f_GeV.txt \n", masses[i], masses[i]);
    fprintf(file_txt, "# Maximum likelihood fits and diagnostics \n");
    fprintf(file_txt, "#    combine      -n .H2A4Mu_mA_%.4f_GeV_expSignal0 -m 125 -M MaxLikelihoodFit --expectSignal=0 -t -1 datacard_H2A4Mu_mA_%.4f_GeV.txt \n", masses[i], masses[i]);
    fprintf(file_txt, "#    combine      -n .H2A4Mu_mA_%.4f_GeV_expSignal1 -m 125 -M MaxLikelihoodFit --expectSignal=1 -t -1 datacard_H2A4Mu_mA_%.4f_GeV.txt \n", masses[i], masses[i]);
    if(masses[i] < 3.09){//Below J/psi
      fprintf(file_txt, "imax 1  number of channels \n");
      fprintf(file_txt, "jmax 1  number of backgrounds \n");
      fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", masses[i]);
      fprintf(file_txt, "shapes data_obs A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR1 \n",masses[i]);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin               A \n");
      fprintf(file_txt, "observation      %d \n", obs);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin                           A          A \n");
      fprintf(file_txt, "process                       0          1 \n");
      fprintf(file_txt, "process                       signal1    BBbar_below_Jpsi_2D \n");
      fprintf(file_txt, "rate                          %.3f       %.3f \n", signal1_rate, BBbar_below_Jpsi_2D_rate);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "lumi_13TeV              lnN   %.3f       -        Lumi (signal only; BBbar background are data-driven) \n", lumi_13TeV);
      fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       -        Muon trigger \n", mu_hlt);
      fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       -        Muon identification \n", mu_id);
      fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       -        Muon isolation \n", mu_iso);
      fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       -        Reconstruction of close muons in the muon system \n", mu_pu);
      fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       -        Theoretical uncertainties in acceptance (not included in model independent limit) \n", pdf_as);
      fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       -        Theoretical uncertainties in production (not included in model independent limit) \n", HxecBr);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       -        Reconstruction of close muons in the tracker \n", ovlp_trk);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       -        Reconstruction of close muons in the muon system \n", ovlp_mu);
      fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       -        Dimuons mass consistency m1~m2 \n", dimu_M);
      fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       -        Reconstruction of close muons in the muon system \n", nnlo_pt);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_norm   lnN     -        %.3f     BBbar estimate\n", BBbar_norm);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_syst   lnN     -        %.3f     Syst on BBar normalization from the difference of the estimation done inverting ISO cut \n", BBbar_syst);
    }
    else if (masses[i] > 3.09 && masses[i] < 9){//Above J/psi
      fprintf(file_txt, "imax 1  number of channels \n");
      fprintf(file_txt, "jmax 1  number of backgrounds \n");
      fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", masses[i]);
      fprintf(file_txt, "shapes data_obs A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR2 \n",masses[i]);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin               A \n");
      fprintf(file_txt, "observation      %d \n", obs);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin                           A          A \n");
      fprintf(file_txt, "process                       0          1 \n");
      fprintf(file_txt, "process                       signal2    BBbar_above_Jpsi_2D \n");
      fprintf(file_txt, "rate                          %.3f       %.3f \n", signal2_rate, BBbar_above_Jpsi_2D_rate);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "lumi_13TeV              lnN   %.3f       -        Lumi (signal only; BBbar background are data-driven) \n", lumi_13TeV);
      fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       -        Muon trigger \n", mu_hlt);
      fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       -        Muon identification \n", mu_id);
      fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       -        Muon isolation \n", mu_iso);
      fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       -        Reconstruction of close muons in the muon system \n", mu_pu);
      fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       -        Theoretical uncertainties in acceptance (not included in model independent limit) \n", pdf_as);
      fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       -        Theoretical uncertainties in production (not included in model independent limit) \n", HxecBr);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       -        Reconstruction of close muons in the tracker \n", ovlp_trk);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       -        Reconstruction of close muons in the muon system \n", ovlp_mu);
      fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       -        Dimuons mass consistency m1~m2 \n", dimu_M);
      fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       -        Reconstruction of close muons in the muon system \n", nnlo_pt);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_norm   lnN     -        %.3f     BBbar estimate\n", BBbar_norm);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_syst   lnN     -        %.3f     Syst on BBar normalization from the difference of the estimation done inverting ISO cut \n", BBbar_syst);
    }
    else if (masses[i] > 9){//High mass backgrounds
      fprintf(file_txt, "imax 1  number of channels \n");
      fprintf(file_txt, "jmax 1  number of backgrounds \n");
      fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", masses[i]);
      fprintf(file_txt, "shapes data_obs A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR3 \n",masses[i]);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin               A \n");
      fprintf(file_txt, "observation      %d \n", obs);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin                           A          A \n");
      fprintf(file_txt, "process                       0          1 \n");
      fprintf(file_txt, "process                       signal3    HighMassBKG \n");
      fprintf(file_txt, "rate                          %.3f       %.3f \n", signal3_rate, HighMassBKG_rate);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "lumi_13TeV              lnN   %.3f       %.3f        Lumi (signal only; BBbar background are data-driven) \n", lumi_13TeV, lumi_13TeV);
      fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       %.3f        Muon trigger \n", mu_hlt, mu_hlt);
      fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       %.3f        Muon identification \n", mu_id, mu_id);
      fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       %.3f        Muon isolation \n", mu_iso, mu_iso);
      fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       %.3f        Reconstruction of close muons in the muon system \n", mu_pu, mu_pu);
      fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       -           Theoretical uncertainties in acceptance (not included in model independent limit) \n", pdf_as);
      fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       -           Theoretical uncertainties in production (not included in model independent limit) \n", HxecBr);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       %.3f        Reconstruction of close muons in the tracker \n", ovlp_trk, ovlp_trk);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       %.3f        Reconstruction of close muons in the muon system \n", ovlp_mu, ovlp_mu);
      fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       %.3f        Dimuons mass consistency m1~m2 \n", dimu_M, dimu_M);
      fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       %.3f        Reconstruction of close muons in the muon system \n", nnlo_pt, nnlo_pt);
    }
    //Add high mass bkgs
    fclose(file_txt);
  }
}

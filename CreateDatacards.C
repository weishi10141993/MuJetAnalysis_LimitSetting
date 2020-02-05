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

#include "Constants.h" //Define constants used in this macro
#include "Config.h" //Config inputs for the macro

void CreateDatacards( bool makeRoot=true ){

  //Configure inputs for year
  Limit_cfg::ConfigureInput(year);

  int Seeds[N_Signals]={0};
  for( int i = 0; i < N_Signals; i++){ Seeds[i]=-1; }

  //Creat Folders
  TString makeFold="mkdir -p macros/sh";
  system( makeFold.Data() );
  makeFold="mkdir -p macros/batch";//batch err and output
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
  for(int h = 0; h < N_Quantiles; h++){//loop over quantile
    for(int Nit = Ninit; Nit < Nend; Nit++ ){//loop over number of jobs
      string pedex = std::to_string(Nit);
      for(int i = 0; i < N_Signals; i++){//loop over mass points
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_std, "%s \n", command);
      }
    }
  }
  fclose(file_sh_std);

  FILE *file_sh_10k = fopen("macros/RunOnDataCard_T10000.sh", "w");
  for(int h = 0; h < N_Quantiles; h++){
    for(int Nit = Ninit; Nit < Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      for(int i = 0; i < N_Signals; i++){
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_T10000_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else         sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_T10000_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_10k, "%s \n", command);
      }
    }
  }
  fclose(file_sh_10k);

  FILE *file_sh_50k = fopen("macros/RunOnDataCard_T50000.sh", "w");
  for(int h = 0; h < N_Quantiles; h++){
    for(int Nit = Ninit; Nit < Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      for(int i = 0; i < N_Signals; i++){
        char command[100];
        if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send_%.3f_%.4f_T50000_%s.%s", masses[i], pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        else         sprintf(command, "sbatch %s/macros/sh/send_%.3f_%.4f_T50000_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
        fprintf(file_sh_50k, "%s \n", command);
      }
    }
  }
  fclose(file_sh_50k);

  FILE *file_sh_30k = fopen("macros/RunOnDataCard_T30000.sh", "w");
  for(int h = 0; h < N_Quantiles; h++){
    for(int Nit = Ninit; Nit < Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      for(int i = 0; i < N_Signals; i++){
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
  for(int h = 0; h < N_Quantiles; h++){
    // Loop over jobs
    for(int Nit = Ninit; Nit < Nend; Nit++ ){
      string pedex = std::to_string(Nit);
      // Loop over mass points
      for(int i = 0; i < N_Signals; i++){
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
          fprintf(file_combine_std, "#SBATCH -J runsplit\n"); //FYI, http://brazos.tamu.edu/docs/slurm.html
          fprintf(file_combine_std, "#SBATCH -p stakeholder-4g\n");
          fprintf(file_combine_std, "#SBATCH --time=120:00:00\n");// time limit of Brazos
          fprintf(file_combine_std, "#SBATCH --mem-per-cpu=4000\n"); // 4GB memory limit per core
          fprintf(file_combine_std, "#SBATCH --ntasks-per-node=16\n"); // This specifies how many cores you want
          fprintf(file_combine_std, "#SBATCH -N 1\n");// # of hosts you want to run on. "-N 1" ensures to get all cores on the same physical host, so they share memory.
          fprintf(file_combine_std, "#SBATCH -o macros/batch/batchjobs_runsplit-%%A-%%a.out\n");// batch err and output directed to folder batch
          fprintf(file_combine_std, "#SBATCH -e macros/batch/batchjobs_runsplit-%%A-%%a.err\n");
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
          fprintf(file_combine_10k, "#SBATCH --time=120:00:00\n");
          fprintf(file_combine_10k, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_10k, "#SBATCH --ntasks-per-node=16\n");
          fprintf(file_combine_10k, "#SBATCH -N 1\n");
          fprintf(file_combine_10k, "#SBATCH -o macros/batch/batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_10k, "#SBATCH -e macros/batch/batchjobs_runsplit-%%A-%%a.err\n");
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
          fprintf(file_combine_50k, "#SBATCH --time=120:00:00\n");
          fprintf(file_combine_50k, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_50k, "#SBATCH --ntasks-per-node=16\n");
          fprintf(file_combine_50k, "#SBATCH -N 1\n");
          fprintf(file_combine_50k, "#SBATCH -o macros/batch/batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_50k, "#SBATCH -e macros/batch/batchjobs_runsplit-%%A-%%a.err\n");
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
          fprintf(file_combine_30k, "#SBATCH --time=120:00:00\n");
          fprintf(file_combine_30k, "#SBATCH --mem-per-cpu=4000\n");
          fprintf(file_combine_30k, "#SBATCH --ntasks-per-node=16\n");
          fprintf(file_combine_30k, "#SBATCH -N 1\n");
          fprintf(file_combine_30k, "#SBATCH -o macros/batch/batchjobs_runsplit-%%A-%%a.out\n");
          fprintf(file_combine_30k, "#SBATCH -e macros/batch/batchjobs_runsplit-%%A-%%a.err\n");
        }
        fprintf(file_combine_30k, "cd %s \n",pwd.c_str());
        fprintf(file_combine_30k, "eval `scramv1 runtime -sh`\n");
        if(DiffSeed) fprintf(file_combine_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d -T 300000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
        else         fprintf(file_combine_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -T 300000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
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
    //***************
    //* Below J/psi *
    //***************
    if(masses[i] < 3.09){
      fprintf(file_txt, "imax 1  number of channels \n");
      fprintf(file_txt, "jmax 1  number of backgrounds \n");
      fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", masses[i]);
      fprintf(file_txt, "shapes data_obs A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR1 \n",masses[i]);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin               A \n");
      fprintf(file_txt, "observation      %d \n", obs_SR1);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin                           A          A \n");
      fprintf(file_txt, "process                       0          1 \n");
      fprintf(file_txt, "process                       signal1    BBbar_below_Jpsi_2D \n");
      fprintf(file_txt, "rate                          %.3f       %.3f \n", signal1_rate, BBbar_below_Jpsi_2D_rate);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "lumi_13TeV              lnN   %.3f       - \n", lumi_13TeV);
      fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       - \n", mu_hlt);
      fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       - \n", mu_id);
      fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       - \n", mu_iso);
      fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       - \n", mu_pu);
      fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       - \n", pdf_as);
      fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       - \n", HxecBr);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       - \n", ovlp_trk);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       - \n", ovlp_mu);
      fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       - \n", dimu_M);
      fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       - \n", nnlo_pt);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_norm   lnN     -        %.3f \n", BBbar_norm);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_syst   lnN     -        %.3f \n", BBbar_syst);
    }
    //***************
    //* Above J/psi *
    //***************
    else if (masses[i] > 3.09 && masses[i] < 9){
      fprintf(file_txt, "imax 1  number of channels \n");
      fprintf(file_txt, "jmax 1  number of backgrounds \n");
      fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", masses[i]);
      fprintf(file_txt, "shapes data_obs A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR2 \n",masses[i]);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin               A \n");
      fprintf(file_txt, "observation      %d \n", obs_SR2);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin                           A          A \n");
      fprintf(file_txt, "process                       0          1 \n");
      fprintf(file_txt, "process                       signal2    BBbar_above_Jpsi_2D \n");
      fprintf(file_txt, "rate                          %.3f       %.3f \n", signal2_rate, BBbar_above_Jpsi_2D_rate);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "lumi_13TeV              lnN   %.3f       - \n", lumi_13TeV);
      fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       - \n", mu_hlt);
      fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       - \n", mu_id);
      fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       - \n", mu_iso);
      fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       - \n", mu_pu);
      fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       - \n", pdf_as);
      fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       - \n", HxecBr);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       - \n", ovlp_trk);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       - \n", ovlp_mu);
      fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       - \n", dimu_M);
      fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       - \n", nnlo_pt);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_norm   lnN     -        %.3f \n", BBbar_norm);
      fprintf(file_txt, "CMS_H2A4Mu_BBbar_syst   lnN     -        %.3f \n", BBbar_syst);
    }
    //*************************
    //* High mass backgrounds *
    //*************************
    else if (masses[i] > 9){
      fprintf(file_txt, "imax 1  number of channels \n");
      fprintf(file_txt, "jmax 1  number of backgrounds \n");
      fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", masses[i]);
      fprintf(file_txt, "shapes data_obs A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR3 \n",masses[i]);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin               A \n");
      fprintf(file_txt, "observation      %d \n", obs_SR3);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "bin                           A          A \n");
      fprintf(file_txt, "process                       0          1 \n");
      fprintf(file_txt, "process                       signal3    HighMassBKG \n");
      fprintf(file_txt, "rate                          %.3f       %.3f \n", signal3_rate, HighMassBKG_rate);
      fprintf(file_txt, "----------------------------------------------------------------------------- \n");
      fprintf(file_txt, "lumi_13TeV              lnN   %.3f       %.3f \n", lumi_13TeV, lumi_13TeV);
      fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       %.3f \n", mu_hlt, mu_hlt);
      fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       %.3f \n", mu_id, mu_id);
      fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       %.3f \n", mu_iso, mu_iso);
      fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       %.3f \n", mu_pu, mu_pu);
      fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       -    \n", pdf_as);
      fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       -    \n", HxecBr);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       %.3f \n", ovlp_trk, ovlp_trk);
      fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       %.3f \n", ovlp_mu, ovlp_mu);
      fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       %.3f \n", dimu_M, dimu_M);
      fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       %.3f \n", nnlo_pt, nnlo_pt);
    }
    fclose(file_txt);
  }
}

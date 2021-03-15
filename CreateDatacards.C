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
#include "Helpers.h"//several interpolation functions

void CreateDatacards(){

  bool makeRoot(true);
  //Configure inputs for year
  Limit_cfg::ConfigureInput(year);

  int Seeds[N_Signals]={0};
  for( int i = 0; i < N_Signals; i++){ Seeds[i]=-1; }

  //Creat Folders
  TString makeFold="mkdir -p plots/PDF";
  system( makeFold.Data() );
  makeFold="mkdir -p plots/PNG";
  system( makeFold.Data() );
  makeFold="mkdir -p plots/C";
  system( makeFold.Data() );

  // Shell script to submit batch job for all mass points of each year
  string endCom = "sh";
  if( !isLxplus ) endCom = "slrm";

  if( year != 2020 ){
    // Shell script to produce ROOT file containing signal and bkg shapes for all mass pionts of each year
    if( makeRoot ){
      FILE *file_sh = fopen("macros/CreateROOTfiles.sh", "w");
      for(int i = 0; i < N_Signals; i++){
        if( (year == 2016 && masses[i] < 9) || (year == 2017 || year == 2018) ){
          fprintf(file_sh, "root -l -b -q 'makeWorkSpace_H2A4Mu.C(%.4f)'\n", masses[i]);
        }
      }
      fclose(file_sh);
    }

    FILE *file_sh_30k = fopen("macros/RunOnDataCard_T30000.sh", "w");
    for(int h = 0; h < N_Quantiles; h++){
      for(int Nit = Ninit; Nit < Nend; Nit++ ){
        string pedex = std::to_string(Nit);
        for(int i = 0; i < N_Signals; i++){
          char command[100];
          if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/%d/send_%.3f_%.4f_T30000_%s.%s", masses[i], pwd.c_str(), year, expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
          else         sprintf(command, "sbatch %s/macros/sh/%d/send_%.3f_%.4f_T30000_%s.%s", pwd.c_str(), year, expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
          if( (year == 2016 && masses[i] < 9) || (year == 2017 || year == 2018) ){
            fprintf(file_sh_30k, "%s \n", command);
          }
        }
      }
    }//end quantiles
    fclose(file_sh_30k);

    // Create submission file for each mass piont
    // Loop over quantiles
    for(int h = 0; h < N_Quantiles; h++){
      // Loop over jobs
      for(int Nit = Ninit; Nit < Nend; Nit++ ){
        string pedex = std::to_string(Nit);
        // Loop over mass points
        for(int i = 0; i < N_Signals; i++){
          char name_T30000[100];
          sprintf(name_T30000, "macros/sh/%d/send_%.3f_%.4f_T30000_%s.%s", year, expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());

          if( (year == 2016 && masses[i] < 9) || (year == 2017 || year == 2018) ){
            FILE *file_30k = fopen(name_T30000, "w");
            fprintf(file_30k, "#!/bin/bash\n");
            if(!isLxplus){
              fprintf(file_30k, "#SBATCH --job-name=ToyLimit\n");//FYI: https://hprc.tamu.edu/wiki/Terra:Batch_Processing_SLURM
              fprintf(file_30k, "#SBATCH --time=03:00:00\n");
              fprintf(file_30k, "#SBATCH --nodes=1\n");
              fprintf(file_30k, "#SBATCH --mem-per-cpu=10000\n");
              fprintf(file_30k, "#SBATCH --ntasks-per-node=1\n");
              fprintf(file_30k, "#SBATCH --output=macros/batch/ToyLimit.out.%%j\n");
              fprintf(file_30k, "#SBATCH --account=122747015988\n");
              fprintf(file_30k, "\n");
              fprintf(file_30k, "module load cctools\n");
              fprintf(file_30k, "export PARROT_CVMFS_ALIEN_CACHE=/scratch/group/mitchcomp/CVMFS_cache\n");
              fprintf(file_30k, "cmsSite=/scratch/group/mitchcomp/CMS/LOCAL_TAMU_HPRC\n");
              fprintf(file_30k, "cmsMount=--mount=/cvmfs/cms.cern.ch/SITECONF/local=$cmsSite\n");
              fprintf(file_30k, "\n");
              fprintf(file_30k, "parrot_run $cmsMount $SHELL << EOF\n");
              fprintf(file_30k, "shopt -s expand_aliases\n");
              fprintf(file_30k, "source /cvmfs/cms.cern.ch/cmsset_default.sh\n");
            }
            fprintf(file_30k, "cd %s\n", pwd.c_str());
            fprintf(file_30k, "cmsenv\n");
            if(DiffSeed) fprintf(file_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d -T 30000 --fork 50 Datacards/%d/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/%d/output/output_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], year, masses[i], year, expected_quantiles[h], masses[i], pedex.c_str());
            else         fprintf(file_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -T 30000 --fork 50 Datacards/%d/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/%d/output/output_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], year, masses[i], year, expected_quantiles[h], masses[i], pedex.c_str());
            if(!isLxplus) fprintf(file_30k, "EOF\n");
            fclose(file_30k);
          }
        }//End N_Signals
      }//End Ninit
    }//End h quantile

    //Create datacards for each mass point
    for(int i=0; i<N_Signals; i++){
      char Thisname_txt[100];
      sprintf(Thisname_txt, "Datacards/%d/datacard_H2A4Mu_mA_%.4f_GeV.txt", year, masses[i]);

      if( (year == 2016 && masses[i] < 9) || (year == 2017 || year == 2018) ){
        FILE *file_txt = fopen(Thisname_txt, "w");

        //***************
        //* Below J/psi *
        //***************
        if(masses[i] < 3.09){
          fprintf(file_txt, "imax 1  number of channels \n");
          fprintf(file_txt, "jmax 1  number of backgrounds \n");
          fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
          fprintf(file_txt, "----------------------------------------------------------------------------- \n");
          fprintf(file_txt, "shapes * * ../../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", year, masses[i]);
          fprintf(file_txt, "shapes data_obs A  ../../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR1 \n", year, masses[i]);
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
          fprintf(file_txt, "CMS_eff_mu_pu_eff       lnN   %.3f       - \n", mu_pu_eff);
          fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       - \n", mu_pu);
          fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       - \n", pdf_as);
          fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       - \n", HxecBr);
          fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       - \n", ovlp_trk);
          fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       - \n", ovlp_mu);
          fprintf(file_txt, "CMS_H2A4Mu_eff_llp_mu   lnN   %.3f       - \n", llp_mu);
          fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       - \n", dimu_M);
          fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       - \n", nnlo_pt);
          fprintf(file_txt, "CMS_H2A4Mu_BBbar_norm   lnN     -        %.3f \n", BBbar_norm_SR1);
          fprintf(file_txt, "CMS_H2A4Mu_BBbar_syst   lnN     -        %.3f \n", BBbar_syst_SR1);
          fprintf(file_txt, "signal1_sigma          param  %.3f       %.4f \n", Helpers_cfg::My_Sigma(masses[i],masses[i]), Helpers_cfg::My_Sigma_Unc(masses[i],masses[i]));// need %.4f to avoid zero un
          fprintf(file_txt, "signal1_alpha          param  %.3f       %.3f \n", Helpers_cfg::My_Alpha(masses[i],masses[i]), Helpers_cfg::My_Alpha_Unc(masses[i],masses[i]));
          fprintf(file_txt, "signal1_n              param  %.3f       %.3f \n", Helpers_cfg::My_n(masses[i],masses[i]), Helpers_cfg::My_n_Unc(masses[i],masses[i]));
        }
        //***************
        //* Above J/psi *
        //***************
        else if (masses[i] > 3.09 && masses[i] < 9){
          fprintf(file_txt, "imax 1  number of channels \n");
          fprintf(file_txt, "jmax 1  number of backgrounds \n");
          fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
          fprintf(file_txt, "----------------------------------------------------------------------------- \n");
          fprintf(file_txt, "shapes * * ../../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", year, masses[i]);
          fprintf(file_txt, "shapes data_obs A  ../../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR2 \n", year, masses[i]);
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
          fprintf(file_txt, "CMS_eff_mu_pu_eff       lnN   %.3f       - \n", mu_pu_eff);
          fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       - \n", mu_pu);
          fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       - \n", pdf_as);
          fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       - \n", HxecBr);
          fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f       - \n", ovlp_trk);
          fprintf(file_txt, "CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f       - \n", ovlp_mu);
          fprintf(file_txt, "CMS_H2A4Mu_eff_llp_mu   lnN   %.3f       - \n", llp_mu);
          fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       - \n", dimu_M);
          fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       - \n", nnlo_pt);
          fprintf(file_txt, "CMS_H2A4Mu_BBbar_norm   lnN     -        %.3f \n", BBbar_norm_SR2);
          fprintf(file_txt, "CMS_H2A4Mu_BBbar_syst   lnN     -        %.3f \n", BBbar_syst_SR2);
          fprintf(file_txt, "signal2_sigma          param  %.3f       %.4f \n", Helpers_cfg::My_Sigma(masses[i],masses[i]), Helpers_cfg::My_Sigma_Unc(masses[i],masses[i]));
          fprintf(file_txt, "signal2_alpha          param  %.3f       %.3f \n", Helpers_cfg::My_Alpha(masses[i],masses[i]), Helpers_cfg::My_Alpha_Unc(masses[i],masses[i]));
          fprintf(file_txt, "signal2_n              param  %.3f       %.3f \n", Helpers_cfg::My_n(masses[i],masses[i]), Helpers_cfg::My_n_Unc(masses[i],masses[i]));
        }
        //*************************
        //* High mass backgrounds *
        //*************************
        else if ( masses[i] > 9 ){
          fprintf(file_txt, "imax 1  number of channels \n");
          fprintf(file_txt, "jmax 1  number of backgrounds \n");
          fprintf(file_txt, "kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
          fprintf(file_txt, "----------------------------------------------------------------------------- \n");
          fprintf(file_txt, "shapes * * ../../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n", year, masses[i]);
          fprintf(file_txt, "shapes data_obs A  ../../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:data_obs_SR3 \n", year, masses[i]);
          fprintf(file_txt, "----------------------------------------------------------------------------- \n");
          fprintf(file_txt, "bin               A \n");
          fprintf(file_txt, "observation      %d \n", obs_SR3);
          fprintf(file_txt, "----------------------------------------------------------------------------- \n");
          fprintf(file_txt, "bin                           A          A \n");
          fprintf(file_txt, "process                       0          1 \n");
          fprintf(file_txt, "process                       signal3    HighMassBKG \n");
          fprintf(file_txt, "rate                          %.3f       %.3f \n", signal3_rate, HighMassBKG_rate);
          fprintf(file_txt, "----------------------------------------------------------------------------- \n");
          fprintf(file_txt, "lumi_13TeV              lnN   %.3f       %.3f \n", lumi_13TeV, lumi_13TeV);//MC driven
          fprintf(file_txt, "CMS_eff_mu_hlt          lnN   %.3f       %.3f \n", mu_hlt, mu_hlt);
          fprintf(file_txt, "CMS_eff_mu_id           lnN   %.3f       %.3f \n", mu_id, mu_id);
          fprintf(file_txt, "CMS_eff_mu_iso          lnN   %.3f       %.3f \n", mu_iso, mu_iso);
          fprintf(file_txt, "CMS_eff_mu_pu_eff       lnN   %.3f       -    \n", mu_pu_eff);
          fprintf(file_txt, "CMS_eff_mu_pileup       lnN   %.3f       -    \n", mu_pu);
          fprintf(file_txt, "QCDscale_ggH            lnN   %.3f       -    \n", pdf_as);
          fprintf(file_txt, "Xsec_BR_decay           lnN   %.3f       -    \n", HxecBr);
          fprintf(file_txt, "CMS_H2A4Mu_eff_llp_mu   lnN   %.3f       -    \n", llp_mu);
          fprintf(file_txt, "CMS_H2A4Mu_effdimu_mass lnN   %.3f       -    \n", dimu_M);
          fprintf(file_txt, "CMS_H2A4Mu_nnlo_pt      lnN   %.3f       -    \n", nnlo_pt);
          fprintf(file_txt, "CMS_H2A4Mu_BKG_norm     lnN     -        %.3f \n", BKG_norm_SR3);
          fprintf(file_txt, "CMS_H2A4Mu_BKG_syst     lnN     -        %.3f \n", BKG_syst_SR3);
          fprintf(file_txt, "CMS_H2A4Mu_BKG_shape    lnN     -        %.3f \n", BKG_shape_SR3);
          fprintf(file_txt, "signal3_sigma          param  %.3f       %.4f \n", Helpers_cfg::My_Sigma(masses[i],masses[i]), Helpers_cfg::My_Sigma_Unc(masses[i],masses[i]));
          fprintf(file_txt, "signal3_alpha          param  %.3f       %.3f \n", Helpers_cfg::My_Alpha(masses[i],masses[i]), Helpers_cfg::My_Alpha_Unc(masses[i],masses[i]));
          fprintf(file_txt, "signal3_n              param  %.3f       %.3f \n", Helpers_cfg::My_n(masses[i],masses[i]), Helpers_cfg::My_n_Unc(masses[i],masses[i]));
        }
        fclose(file_txt);
      }
    }//end Nsignals
  }// if not combine, produce for each year

  //==============================================
  //= Combine data cards below 9GeV for 2016+2018
  //==============================================
  if( year == 2020 ){

    FILE *file_sh_combine_low_mass = fopen("Datacards/2020/CombineLowMass.sh", "w");//Below 9GeV for 2016+2018
    for(int i = 0; i < N_Signals; i++){
      if( masses[i] < 9 ){
        fprintf(file_sh_combine_low_mass, "cp ../2016/datacard_H2A4Mu_mA_%.4f_GeV.txt datacard_2016_H2A4Mu_mA_%.4f_GeV.txt\n", masses[i], masses[i]);
        fprintf(file_sh_combine_low_mass, "cp ../2018/datacard_H2A4Mu_mA_%.4f_GeV.txt datacard_2018_H2A4Mu_mA_%.4f_GeV.txt\n", masses[i], masses[i]);
        fprintf(file_sh_combine_low_mass, "combineCards.py datacard_2016_H2A4Mu_mA_%.4f_GeV.txt datacard_2018_H2A4Mu_mA_%.4f_GeV.txt > datacard_H2A4Mu_mA_%.4f_GeV.txt\n", masses[i],  masses[i],  masses[i]);
        fprintf(file_sh_combine_low_mass, "rm datacard_2016_H2A4Mu_mA_%.4f_GeV.txt\n", masses[i]);
        fprintf(file_sh_combine_low_mass, "rm datacard_2018_H2A4Mu_mA_%.4f_GeV.txt\n", masses[i]);
      }
    }
    fclose(file_sh_combine_low_mass);


    // Shell script to submit batch job for all mass points of combined data card
    FILE *sh_submit_low_mass_30k = fopen("macros/RunOnDataCardCombineLowMass_T30000.sh", "w");
    for(int h = 0; h < N_Quantiles; h++){
      for(int Nit = Ninit; Nit < Nend; Nit++ ){
        string pedex = std::to_string(Nit);
        for(int i = 0; i < N_Signals; i++){
          char commandcomb[100];
          //assume on TAMU Terra
          sprintf(commandcomb, "sbatch %s/macros/sh/2020/send_%.3f_%.4f_T30000_%s.%s", pwd.c_str(), expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
          if( masses[i] < 9 ){ fprintf(sh_submit_low_mass_30k, "%s \n", commandcomb); }
        }
      }
    }
    fclose(sh_submit_low_mass_30k);

    // Create batch file for each mass piont with combined data card
    for(int h = 0; h < N_Quantiles; h++){
      // Loop over jobs
      for(int Nit = Ninit; Nit < Nend; Nit++ ){
        string pedex = std::to_string(Nit);
        // Loop over mass points
        for(int i = 0; i < N_Signals; i++){
          //Below 9GeV for 2016+2018
          if( masses[i] < 9 ){
            char name_combine_T30000[100];
            sprintf(name_combine_T30000, "macros/sh/2020/send_%.3f_%.4f_T30000_%s.%s", expected_quantiles[h], masses[i], pedex.c_str(), endCom.c_str());
            FILE *file_combine_30k = fopen(name_combine_T30000, "w");
            fprintf(file_combine_30k, "#!/bin/bash\n");
            fprintf(file_combine_30k, "#SBATCH --job-name=ToyLimit\n");//FYI: https://hprc.tamu.edu/wiki/Terra:Batch_Processing_SLURM
            fprintf(file_combine_30k, "#SBATCH --time=03:00:00\n");
            fprintf(file_combine_30k, "#SBATCH --nodes=1\n");
            fprintf(file_combine_30k, "#SBATCH --mem-per-cpu=15000\n");
            fprintf(file_combine_30k, "#SBATCH --ntasks-per-node=1\n");
            fprintf(file_combine_30k, "#SBATCH --output=macros/batch/ToyLimit.out.%%j\n");
            fprintf(file_combine_30k, "#SBATCH --account=122747015988\n");
            fprintf(file_combine_30k, "\n");
            fprintf(file_combine_30k, "module load cctools\n");
            fprintf(file_combine_30k, "export PARROT_CVMFS_ALIEN_CACHE=/scratch/group/mitchcomp/CVMFS_cache\n");
            fprintf(file_combine_30k, "cmsSite=/scratch/group/mitchcomp/CMS/LOCAL_TAMU_HPRC\n");
            fprintf(file_combine_30k, "cmsMount=--mount=/cvmfs/cms.cern.ch/SITECONF/local=$cmsSite\n");
            fprintf(file_combine_30k, "\n");
            fprintf(file_combine_30k, "parrot_run $cmsMount $SHELL << EOF\n");
            fprintf(file_combine_30k, "shopt -s expand_aliases\n");
            fprintf(file_combine_30k, "source /cvmfs/cms.cern.ch/cmsset_default.sh\n");
            fprintf(file_combine_30k, "cd %s\n", pwd.c_str());
            fprintf(file_combine_30k, "cmsenv\n");
            if(DiffSeed) fprintf(file_combine_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -s %d -T 30000 --fork 50 Datacards/2020/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/2020/output/output_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], Seeds[i], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
            else         fprintf(file_combine_30k, "combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew --saveHybridResult --expectedFromGrid %.3f " + Myrule + " -T 30000 --fork 50 Datacards/2020/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/2020/output/output_%.3f_%.4f_T30000_%s.txt \n", masses[i], pedex.c_str(), expected_quantiles[h], masses[i], expected_quantiles[h], masses[i], pedex.c_str());
            fprintf(file_combine_30k, "EOF\n");
            fclose(file_combine_30k);
          }
        }//End N_Signals
      }//End Ninit
    }//End h quantile

  }//end
  //=========================
  //= End Combine data cards
  //=========================
}

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

#define N_Signals 59

void CreateDatacards( bool makeRoot=true ){
  //Parameters
  bool isLxplus=false;
  //TString Myrule = "--rule CLs --LHCmode LHC-limits --toysFrequentist"; //OLD command "--rule CLs --testStat LHC"
  TString Myrule = "--rule CLs --testStat LHC";
  Myrule = Myrule + " --cl 0.95";
  string pwd = "/home/ws13/Run2LimitSetting/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/";
  bool DiffSeed=true;

  // need to do this 10 times because can only run -T 1000 at a time!!!!
  int nBatch = 12;
  int Ninit=0+nBatch*30, Nend=30+nBatch*30;
  //Each mass is submitted (Nend-Ninit) times. If you need to accumulate statistic you can resubmit from 41 to X.
  //After looking at data we need to change the mass granularity
  float masses[N_Signals] = {0.2113,0.2400,0.2600,0.3000,0.3300,0.3600,0.4000,0.4300,0.4600,0.5000,0.5300,0.5600,0.6000,0.7000,0.8000,0.8800,0.9000,0.9100,0.9200,0.9300,0.9400,1.0000,1.1000,1.2000,1.3000,1.4000,1.5000,1.6000,1.7000,1.8000,1.9000,2.0000,2.1000,2.2000,2.3000,2.4000,2.5000,2.6000,2.7000,2.8000,2.9000,3.0000,3.0200,3.0500,3.0800,3.0900,3.1000,3.1200,3.1500,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000};

  int Seeds[N_Signals]={0};

  for( int i=0; i<N_Signals; i++){ Seeds[i]=-1; }

  //N events
  int obs = -1;
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

  //==============
  //2017 expected
  //==============
  float signal_rate = 1, BBbar_2D_rate = 5.65294, DJpsiS_2D_rate = 0.31806, DJpsiD_2D_rate = 0.019;
  //Signal Uncertainties
  float lumi_13TeV = 1.025, mu_hlt = 1.06, mu_id = 1.024, mu_iso = 1.02, mu_pu = 1.0017;
  float ovlp_trk = 1.024, ovlp_mu = 1.026, dimu_M = 1.015, nnlo_pt = 1.02, pdf_as = 1.08, HxecBr = 1.038;
  //Background Uncertainties
  float BBbar_norm=43, BBbar_norm2=0.1688, BBbar_norm3=1.123, BBbar_syst=1.2;
  float DJpsiD_norm=5, DJpsiD_norm2=0.0038, DJpsiS_norm=27, DJpsiS_norm2=0.01178, DJpsi_extr=1.15;

  /*
  //==============
  //2018 expected
  //==============
  float signal_rate = 1, BBbar_2D_rate = TBD,  DJpsiS_2D_rate = TBD, DJpsiD_2D_rate = TBD;
  //Signal Uncertainties
  float lumi_13TeV = 1.025, mu_hlt = 1.06, mu_id = 1.024, mu_iso = 1.02, mu_pu = 1.0017;
  float ovlp_trk = 1.024, ovlp_mu = 1.026, dimu_M = 1.015, nnlo_pt = 1.02, pdf_as = 1.08, HxecBr = 1.038;
  //Background Uncertainties
  float BBbar_norm=43, BBbar_norm2=0.1688, BBbar_norm3=1.123, BBbar_syst=1.2;
  float DJpsiD_norm=5, DJpsiD_norm2=0.0038, DJpsiS_norm=27, DJpsiS_norm2=0.01178, DJpsi_extr=1.15;
  */

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
  FILE *file_sh1=fopen("macros/RunOnDataCard_std.sh","w");
  for(int Nit=Ninit; Nit<Nend; Nit++ ){
    string pedex = std::to_string(Nit);
    for(int i=0; i<N_Signals; i++){
	char command[100];
	if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send%.4f_%s.%s", masses[i], pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	else sprintf(command, "sbatch %s/macros/sh/send%.4f_%s.%s", pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	fprintf(file_sh1,"%s \n",command);
    }
  }
  fclose(file_sh1);
  FILE *file_sh1b=fopen("macros/RunOnDataCard_T10000.sh","w");
  for(int Nit=Ninit; Nit<Nend; Nit++ ){
    string pedex = std::to_string(Nit);
    for(int i=0; i<N_Signals; i++){
	char command[100];
	if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send%.4f_T10000_%s.%s", masses[i], pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	else         sprintf(command, "sbatch %s/macros/sh/send%.4f_T10000_%s.%s", pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	fprintf(file_sh1b,"%s \n",command);
    }
  }
  fclose(file_sh1b);
  FILE *file_sh2=fopen("macros/RunOnDataCard_T50000.sh","w");
  for(int Nit=Ninit; Nit<Nend; Nit++ ){
    string pedex = std::to_string(Nit);
    for(int i=0; i<N_Signals; i++){
	char command[100];
	if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send%.4f_T50000_%s.%s", masses[i], pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	else         sprintf(command, "sbatch %s/macros/sh/send%.4f_T50000_%s.%s", pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	fprintf(file_sh2,"%s \n",command);
    }
  }
  fclose(file_sh2);
  FILE *file_sh3=fopen("macros/RunOnDataCard_T30000.sh","w");
  for(int Nit=Ninit; Nit<Nend; Nit++ ){
    string pedex = std::to_string(Nit);
    for(int i=0; i<N_Signals; i++){
	char command[100];
	if(isLxplus) sprintf(command, "bsub -q 1nd -u youremail -J \"comb%.4f\" bash %s/macros/sh/send%.4f_T30000_%s.%s", masses[i], pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	else         sprintf(command, "sbatch %s/macros/sh/send%.4f_T30000_%s.%s", pwd.c_str(), masses[i], pedex.c_str(), endCom.c_str());
	fprintf(file_sh3,"%s \n",command);
    }
  }
  fclose(file_sh3);

  for(int Nit=Ninit; Nit<Nend; Nit++ ){
    string pedex = std::to_string(Nit);
    for(int i=0; i<N_Signals; i++){
	//File.sh to run on all datacard
	char name[100];
	char name_T10000[100];
	char name_T50000[100];
	char name_T30000[100];
	sprintf(name, "macros/sh/send%.4f_%s.%s",masses[i],pedex.c_str(),endCom.c_str());
	sprintf(name_T10000, "macros/sh/send%.4f_T10000_%s.%s",masses[i],pedex.c_str(),endCom.c_str());
	sprintf(name_T50000, "macros/sh/send%.4f_T50000_%s.%s",masses[i],pedex.c_str(),endCom.c_str());
	sprintf(name_T30000, "macros/sh/send%.4f_T30000_%s.%s",masses[i],pedex.c_str(),endCom.c_str());
	FILE *file_sh4=fopen(name,"w");
	fprintf(file_sh4,"#!/bin/bash\n");
	if(!isLxplus){
	  fprintf(file_sh4,"#SBATCH -J runsplit\n");
	  fprintf(file_sh4,"#SBATCH -p stakeholder-4g\n");
	  fprintf(file_sh4,"#SBATCH -n1\n");
	  fprintf(file_sh4,"#SBATCH --mem-per-cpu=4000\n");
	  fprintf(file_sh4,"#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
	  fprintf(file_sh4,"#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
	  fprintf(file_sh4,"#SBATCH --ntasks-per-core=1\n");
	}
	fprintf(file_sh4,"cd %s \n",pwd.c_str());
	fprintf(file_sh4,"eval `scramv1 runtime -sh`\n");
	if(DiffSeed) fprintf(file_sh4,"combine -n .H2A4Mu_mA_%.4f_GeV_%s -m 125 -M HybridNew " + Myrule + " -s %d Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_%s.txt \n",masses[i],pedex.c_str(),Seeds[i],masses[i],masses[i],pedex.c_str());
	else         fprintf(file_sh4,"combine -n .H2A4Mu_mA_%.4f_GeV_%s -m 125 -M HybridNew " + Myrule + " Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_%s.txt \n",masses[i],pedex.c_str(),masses[i],masses[i],pedex.c_str());
	fclose(file_sh4);
	FILE *file_sh4b=fopen(name_T10000,"w");
	fprintf(file_sh4b,"#!/bin/bash\n");
	if(!isLxplus){
	  fprintf(file_sh4b,"#SBATCH -J runsplit\n");
	  fprintf(file_sh4b,"#SBATCH -p stakeholder-4g\n");
	  fprintf(file_sh4b,"#SBATCH -n1\n");
	  fprintf(file_sh4b,"#SBATCH --mem-per-cpu=4000\n");
	  fprintf(file_sh4b,"#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
	  fprintf(file_sh4b,"#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
	  fprintf(file_sh4b,"#SBATCH --ntasks-per-core=1\n");
	}
	fprintf(file_sh4b,"cd %s \n",pwd.c_str());
	fprintf(file_sh4b,"eval `scramv1 runtime -sh`\n");
	if(DiffSeed) fprintf(file_sh4b,"combine -n .H2A4Mu_mA_%.4f_GeV_T10000_%s -m 125 -M HybridNew " + Myrule + " -s %d -T 1000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_T10000_%s.txt \n",masses[i],pedex.c_str(),Seeds[i],masses[i],masses[i],pedex.c_str());
	else         fprintf(file_sh4b,"combine -n .H2A4Mu_mA_%.4f_GeV_T10000_%s -m 125 -M HybridNew " + Myrule + " -T 1000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_T10000_%s.txt \n",masses[i],pedex.c_str(),masses[i],masses[i],pedex.c_str());
	fclose(file_sh4b);
	FILE *file_sh5=fopen(name_T50000,"w");
	fprintf(file_sh5,"#!/bin/bash\n");
	if(!isLxplus){
	  fprintf(file_sh5,"#SBATCH -J runsplit\n");
	  fprintf(file_sh5,"#SBATCH -p stakeholder-4g\n");
	  fprintf(file_sh5,"#SBATCH -n1\n");
	  fprintf(file_sh5,"#SBATCH --mem-per-cpu=4000\n");
	  fprintf(file_sh5,"#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
	  fprintf(file_sh5,"#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
	  fprintf(file_sh5,"#SBATCH --ntasks-per-core=1\n");
	}
	fprintf(file_sh5,"cd %s \n",pwd.c_str());
	fprintf(file_sh5,"eval `scramv1 runtime -sh`\n");
	if(DiffSeed) fprintf(file_sh5,"combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T50000_%s -m 125 -M HybridNew " + Myrule + " -s %d -T 50000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_T50000_%s.txt \n",masses[i],pedex.c_str(),Seeds[i],masses[i],masses[i],pedex.c_str());
	else         fprintf(file_sh5,"combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T50000_%s -m 125 -M HybridNew " + Myrule + " -T 50000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_T50000_%s.txt \n",masses[i],pedex.c_str(),masses[i],masses[i],pedex.c_str());
	fclose(file_sh5);
	FILE *file_sh6=fopen(name_T30000,"w");
	fprintf(file_sh6,"#!/bin/bash\n");
	if(!isLxplus){
	  fprintf(file_sh6,"#SBATCH -J runsplit\n");
	  fprintf(file_sh6,"#SBATCH -p stakeholder-4g\n");
	  fprintf(file_sh6,"#SBATCH -n1\n");
	  fprintf(file_sh6,"#SBATCH --mem-per-cpu=4000\n");
	  fprintf(file_sh6,"#SBATCH -o batchjobs_runsplit-%%A-%%a.out\n");
	  fprintf(file_sh6,"#SBATCH -e batchjobs_runsplit-%%A-%%a.err\n");
	  fprintf(file_sh6,"#SBATCH --ntasks-per-core=1\n");
	}
	fprintf(file_sh6,"cd %s \n",pwd.c_str());
	fprintf(file_sh6,"eval `scramv1 runtime -sh`\n");
	if(DiffSeed) fprintf(file_sh6,"combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew " + Myrule + " -s %d -T 30000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_T30000_%s.txt \n",masses[i],pedex.c_str(),Seeds[i],masses[i],masses[i],pedex.c_str());
	else         fprintf(file_sh6,"combine -n .H2A4Mu_mA_%.4f_GeV_LHC_T30000_%s -m 125 -M HybridNew " + Myrule + " -T 30000 --fork 50 Datacards/datacard_H2A4Mu_mA_%.4f_GeV.txt > macros/sh/OutPut_%.4f_T30000_%s.txt \n",masses[i],pedex.c_str(),masses[i],masses[i],pedex.c_str());
	fclose(file_sh6);
    }
  }

  //Create Datacards
  for(int i=0; i<N_Signals; i++){
    stringstream massesS;
    massesS << fixed << setprecision(4) << masses[i];
    TString Thisname_txt = "datacard_H2A4Mu_mA_" + massesS.str() + "_GeV.txt";
    FILE *file_txt=fopen( ("Datacards/" + Thisname_txt).Data(),"w");
    fprintf(file_txt,"# HybridNew CLs: \n");
    fprintf(file_txt,"#    combine      -n .H2A4Mu_mA_%.4f_GeV            -m 125 -M HybridNew --rule CLs --LHCmode LHC-limits     datacard_H2A4Mu_mA_%.4f_GeV.txt \n",masses[i],masses[i]);
    fprintf(file_txt,"# Maximum likelihood fits and diagnostics \n");
    fprintf(file_txt,"#    combine      -n .H2A4Mu_mA_%.4f_GeV_expSignal0 -m 125 -M MaxLikelihoodFit --expectSignal=0 -t -1 datacard_H2A4Mu_mA_%.4f_GeV.txt \n",masses[i],masses[i]);
    fprintf(file_txt,"#    combine      -n .H2A4Mu_mA_%.4f_GeV_expSignal1 -m 125 -M MaxLikelihoodFit --expectSignal=1 -t -1 datacard_H2A4Mu_mA_%.4f_GeV.txt \n",masses[i],masses[i]);
    fprintf(file_txt,"imax 1  number of channels \n");
    fprintf(file_txt,"jmax 3  number of backgrounds \n");
    fprintf(file_txt,"kmax *  number of nuisance parameters (sources of systematical uncertainties) \n");
    fprintf(file_txt,"------------------------------- \n");
    fprintf(file_txt,"shapes * * ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:$PROCESS \n",masses[i]);
    fprintf(file_txt,"shapes DJpsiS_2D A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:DJpsi_2D \n",masses[i]);
    fprintf(file_txt,"shapes DJpsiD_2D A  ../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root w_H2A4Mu:DJpsi_2D \n",masses[i]);
    fprintf(file_txt,"------------------------------- \n");
    fprintf(file_txt,"bin               A \n");
    fprintf(file_txt,"observation      %d \n",obs);
    fprintf(file_txt,"------------------------------- \n");
    fprintf(file_txt,"bin                           A          A         A         A \n");
    fprintf(file_txt,"process                       0          1         2         3 \n");
    fprintf(file_txt,"process                       signal     BBbar_2D  DJpsiS_2D DJpsiD_2D \n");
    fprintf(file_txt,"rate                          %.3f          %.3f       %.3f      %.3f \n", signal_rate,BBbar_2D_rate,DJpsiS_2D_rate,DJpsiD_2D_rate);
    fprintf(file_txt,"------------------------------- \n");
    fprintf(file_txt,"lumi_13TeV              lnN   %.3f      -         -         -           Lumi (signal only; BBbar and DJpsi backgrounds are data-driven) \n", lumi_13TeV);
    fprintf(file_txt,"CMS_eff_mu_hlt          lnN   %.3f      -         -         -           Muon trigger \n", mu_hlt);
    fprintf(file_txt,"CMS_eff_mu_id           lnN   %.3f      -         -         -           Muon identification \n", mu_id);
    fprintf(file_txt,"CMS_eff_mu_iso          lnN   %.3f      -         -         -           Muon isolation \n", mu_iso);
    fprintf(file_txt,"CMS_eff_mu_pileup       lnN   %.3f      -         -         -           Reconstruction of close muons in the muon system \n", mu_pu);
    fprintf(file_txt,"QCDscale_ggH            lnN   %.3f      -         -         -           Theoretical uncertainties in acceptance (not included in model independent limit) \n", pdf_as);
    fprintf(file_txt,"Xsec_BR_decay           lnN   %.3f      -         -         -           Theoretical uncertainties in production (not included in model independent limit) \n", HxecBr);
    fprintf(file_txt,"CMS_H2A4Mu_eff_ovlp_trk lnN   %.3f      -         -         -           Reconstruction of close muons in the tracker \n", ovlp_trk);
    fprintf(file_txt,"CMS_H2A4Mu_eff_ovlp_mu  lnN   %.3f      -         -         -           Reconstruction of close muons in the muon system \n", ovlp_mu);
    fprintf(file_txt,"CMS_H2A4Mu_effdimu_mass lnN   %.3f      -         -         -           Dimuons mass consistency m1~m2 \n", dimu_M);
    fprintf(file_txt,"CMS_H2A4Mu_nnlo_pt      lnN   %.3f      -         -         -           Reconstruction of close muons in the muon system \n", nnlo_pt);
    fprintf(file_txt,"CMS_H2A4Mu_BBbar_norm   lnN     -       %.3f      -         -           BBbar estimate\n", BBbar_norm3);
    //fprintf(file_txt,"CMS_H2A4Mu_BBbar_norm   gmN %.0f  -       %.3f      -         -           BBbar estimate of 9.2 comes from 56 data events in sidebands (here put the total number of events and scale factor in signal region). BBbar_norm*BBbar_norm2 should give number in signare region.  \n", BBbar_norm, BBbar_norm2);
    fprintf(file_txt,"CMS_H2A4Mu_BBbar_syst   lnN     -       %.3f      -         -           Syst on BBar normalization from the difference of the estimation done inverting ISO cut \n", BBbar_syst);
    fprintf(file_txt,"CMS_H2A4Mu_DJpsi_extr   lnN     -         -       %.3f     %.3f        Double J/psi MC-to-data extrapolation \n", DJpsi_extr, DJpsi_extr);
    fprintf(file_txt,"CMS_H2A4Mu_DJpsiS_norm  gmN %.0f  -         -       %.4f     -           Double J/psi single parton scattering (SPS) estimate of 0.061 comes from 3 MC events \n", DJpsiS_norm, DJpsiS_norm2);
    fprintf(file_txt,"CMS_H2A4Mu_DJpsiD_norm  gmN %.0f   -         -        -        %.6f     Double J/psi double parton scattering (DPS) estimate of 0.003 comes from 8 MC events \n", DJpsiD_norm, DJpsiD_norm2);
    fclose(file_txt);
  }
}

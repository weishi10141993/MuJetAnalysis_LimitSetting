//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  USER Configure Below        !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

const int year = 2018;//Configure which year ntuples to run, options: 2017, 2018

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  USER Configure Above        !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Initialize variables for macros  !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//To be used in datacards in CreateDatacards.C
TString Myrule = ""; // Combine rule
string pwd = ""; //Absolite dir of the repo

//Signal and background rates
// SR1: Below J/psi
float signal1_rate;//signal normalization
float BBbar_below_Jpsi_2D_rate; //Bkg rate
// SR2: Above J/psi, below 9 GeV
float signal2_rate;
float BBbar_above_Jpsi_2D_rate;
// SR3: Above 9 GeV
float signal3_rate;
float HighMassBKG_rate;

// Background Uncertainties: apply to SR1 and SR2
float BBbar_norm;
float BBbar_syst;

// Systematic Uncertainties
float lumi_13TeV; //Lumi (only affect signal; BBbar background are data-driven)
float mu_hlt; //Muon trigger
float mu_id; //Muon identification
float mu_iso; //Muon isolation
float mu_pu; //pileup
float ovlp_trk; //Reconstruction of close muons in the tracker
float ovlp_mu; //Reconstruction of close muons in the muon system
float dimu_M; //Dimuons mass consistency m1~m2
float nnlo_pt; //NNLO Higgs pT re-weighting
float pdf_as; //Theoretical uncertainties in acceptance (not included in model independent limit)
float HxecBr; //Theoretical uncertainties in production (not included in model independent limit)

TString inputFile1; // input file for makeWorkSpace_H2A4Mu.C

int obs_SR1, obs_SR2, obs_SR3; //observed events (-1 for expected limits)

namespace Limit_cfg {

  inline void ConfigureInput( const int year ) {

    std::cout << "\nConfiguring inputs for year " << year << std::endl;

    if(year == 2017){
      signal1_rate = signal1_rate_2017; BBbar_below_Jpsi_2D_rate = BBbar_below_Jpsi_2D_rate_2017;
      signal2_rate = signal2_rate_2017; BBbar_above_Jpsi_2D_rate = BBbar_above_Jpsi_2D_rate_2017;
      signal3_rate = signal3_rate_2017; HighMassBKG_rate         = HighMassBKG_rate_2017;
      BBbar_norm   = BBbar_norm_2017;   BBbar_syst = BBbar_syst_2017;
      lumi_13TeV   = lumi_13TeV_2017;   mu_hlt     = mu_hlt_2017;  mu_id  = mu_id_2017;  mu_iso  = mu_iso_2017;  mu_pu  = mu_pu_2017;
      ovlp_trk     = ovlp_trk_2017;     ovlp_mu    = ovlp_mu_2017; dimu_M = dimu_M_2017; nnlo_pt = nnlo_pt_2017; pdf_as = pdf_as_2017; HxecBr = HxecBr_2017;

      inputFile1 = "../ws_2017_FINAL.root";
      obs_SR1    = obs_SR1_2017;
      obs_SR2    = obs_SR2_2017;
      obs_SR3    = obs_SR3_2017;

    }//end 2017
    else if(year == 2018){
      signal1_rate = signal1_rate_2018; BBbar_below_Jpsi_2D_rate = BBbar_below_Jpsi_2D_rate_2018;
      signal2_rate = signal2_rate_2018; BBbar_above_Jpsi_2D_rate = BBbar_above_Jpsi_2D_rate_2018;
      signal3_rate = signal3_rate_2018; HighMassBKG_rate         = HighMassBKG_rate_2018;
      BBbar_norm = BBbar_norm_2018; BBbar_syst = BBbar_syst_2018;
      lumi_13TeV = lumi_13TeV_2018; mu_hlt     = mu_hlt_2018;  mu_id  = mu_id_2018;  mu_iso  = mu_iso_2018;  mu_pu  = mu_pu_2018;
      ovlp_trk   = ovlp_trk_2018;   ovlp_mu    = ovlp_mu_2018; dimu_M = dimu_M_2018; nnlo_pt = nnlo_pt_2018; pdf_as = pdf_as_2018; HxecBr = HxecBr_2018;

      inputFile1 = "../ws_2018_FINAL.root";
      obs_SR1    = obs_SR1_2018;
      obs_SR2    = obs_SR2_2018;
      obs_SR3    = obs_SR3_2018;

    }//end 2018
    else{
      std::cout << "*** User input year is unknown! Please check. ***" << std::endl;
    }

    //Common Combine rule for 2017 and 2018
    Myrule = Myrule + "--rule CLs --testStat LHC --cl 0.95 --rAbsAcc 0.01 --rRelAcc 0.001";//Require accuracy on r because of ~zero bkg analysis, otherwise r fluctuates
    pwd = pwd + "/home/ws13/Run2LimitSetting/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/";

  } // End function

} // End namespace

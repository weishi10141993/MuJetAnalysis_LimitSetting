//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  USER Configure Below        !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

const int year = 2018;//Configure which year ntuples to run, options: 2018, 2020(combine 2016+2018)

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

// Background Uncertainties at SR1,2,3
float BBbar_norm;
float BBbar_norm_SR1;
float BBbar_norm_SR2;
float BKG_norm_SR3;

float BBbar_syst;
float BBbar_syst_SR1;
float BBbar_syst_SR2;
float BKG_syst_SR3;
float BKG_shape_SR3;

//signal shape unc
float signal1_sigma_unc;
float signal1_alpha_unc;
float signal1_n_unc;
float signal2_sigma_unc;
float signal2_alpha_unc;
float signal2_n_unc;
float signal3_sigma_unc;
float signal3_alpha_unc;
float signal3_n_unc;

// Systematic Uncertainties
float lumi_13TeV; //Lumi (only affect signal; BBbar background are data-driven)
float mu_hlt; //Muon trigger
float mu_id; //Muon identification
float mu_iso; //Muon isolation
float mu_pu_eff; //high pileup effect
float mu_pu; //pileup distribution
float ovlp_trk; //Reconstruction of close muons in the tracker
float ovlp_mu; //Reconstruction of close muons in the muon system
float llp_mu; //Reconstruction of close muons in the muon system
float dimu_M; //Dimuons mass consistency m1~m2
float nnlo_pt; //NNLO Higgs pT re-weighting
float pdf_as; //Theoretical uncertainties in acceptance (not included in model independent limit)
float HxecBr; //Theoretical uncertainties in production (not included in model independent limit)

TString inputFile1; // input file for makeWorkSpace_H2A4Mu.C

int obs_SR1, obs_SR2, obs_SR3; //observed events (-1 for expected limits)

namespace Limit_cfg {

  //Background pdf for high mass: Interpolation between consective bins
  /*double MCBinCenterMass[14] = {12.75, 16.25, 19.75, 23.25, 26.75, 30.25, 33.75, 37.25, 40.75, 44.25, 47.75, 51.25, 54.75, 58.25};

  double MCBinContentm1[14] = {0.0260007, 0.070103, 0.457687, 0.161783, 0.157428, 0.62272, 0.599198, 0.887516, 1.56432, 2.07059, 0.707749, 1.12067, 2.29358, 0.954618};
  double MCBinErrm1[14] = {0.00764504, 0.0148186, 0.357686, 0.0232653, 0.0228677, 0.160303, 0.117906, 0.195744, 0.530653, 0.765715, 0.117726, 0.224549, 0.773769, 0.375918};

  double MCBinContentm2[14] = {0.0263188, 0.0750433, 0.462819, 0.149645, 0.17395, 0.482848, 0.851617, 0.792001, 1.40641, 2.22213, 0.8121, 1.09374, 1.93753, 1.20782};
  double MCBinErrm2[14] = {0.00767975, 0.0153949, 0.357711, 0.0224435, 0.0240383, 0.116155, 0.195536, 0.162129, 0.518903, 0.773695, 0.16106, 0.224314, 0.563703, 0.640463};
*/
  inline void ConfigureInput( const int year ) {

    std::cout << "\nConfiguring inputs for year " << year << std::endl;

    if ( year == 2017 ) {
      signal1_rate = signal1_rate_2017; BBbar_below_Jpsi_2D_rate = BBbar_below_Jpsi_2D_rate_2017;
      signal2_rate = signal2_rate_2017; BBbar_above_Jpsi_2D_rate = BBbar_above_Jpsi_2D_rate_2017;
      signal3_rate = signal3_rate_2017; HighMassBKG_rate         = HighMassBKG_rate_2017;
      BBbar_norm   = BBbar_norm_2017;   BBbar_syst = BBbar_syst_2017;
      lumi_13TeV   = lumi_13TeV_2017;   mu_hlt     = mu_hlt_2017;  mu_id  = mu_id_2017;  mu_iso  = mu_iso_2017;  mu_pu_eff = mu_pu_eff_2017; mu_pu  = mu_pu_2017;
      ovlp_trk     = ovlp_trk_2017;     ovlp_mu    = ovlp_mu_2017; llp_mu = llp_mu_2017; dimu_M = dimu_M_2017; nnlo_pt = nnlo_pt_2017; pdf_as = pdf_as_2017; HxecBr = HxecBr_2017;

      inputFile1 = "../ws_2017_FINAL.root";
      obs_SR1    = obs_SR1_2017;
      obs_SR2    = obs_SR2_2017;
      obs_SR3    = obs_SR3_2017;
    }//end 2017
    else if ( year == 2018 ) {
      signal1_rate = signal1_rate_2018; BBbar_below_Jpsi_2D_rate = BBbar_below_Jpsi_2D_rate_2018;
      signal2_rate = signal2_rate_2018; BBbar_above_Jpsi_2D_rate = BBbar_above_Jpsi_2D_rate_2018;
      signal3_rate = signal3_rate_2018; HighMassBKG_rate         = HighMassBKG_rate_2018;
      BBbar_norm_SR1 = BBbar_norm_2018_SR1; BBbar_syst_SR1 = BBbar_syst_2018_SR1;
      BBbar_norm_SR2 = BBbar_norm_2018_SR2; BBbar_syst_SR2 = BBbar_syst_2018_SR2;
      BKG_norm_SR3   = BKG_norm_2018_SR3;   BKG_syst_SR3   = BKG_syst_2018_SR3;  BKG_shape_SR3 = BKG_shape_2018_SR3;

      signal1_sigma_unc = signal1_sigma_unc_2018; signal1_alpha_unc = signal1_alpha_unc_2018; signal1_n_unc = signal1_n_unc_2018;
      signal2_sigma_unc = signal2_sigma_unc_2018; signal2_alpha_unc = signal2_alpha_unc_2018; signal2_n_unc = signal2_n_unc_2018;
      signal3_sigma_unc = signal3_sigma_unc_2018; signal3_alpha_unc = signal3_alpha_unc_2018; signal3_n_unc = signal3_n_unc_2018;

      lumi_13TeV = lumi_13TeV_2018; mu_hlt     = mu_hlt_2018;  mu_id  = mu_id_2018;  mu_iso  = mu_iso_2018;  mu_pu_eff = mu_pu_eff_2018; mu_pu  = mu_pu_2018;
      ovlp_trk   = ovlp_trk_2018;   ovlp_mu    = ovlp_mu_2018; llp_mu = llp_mu_2018; dimu_M = dimu_M_2018; nnlo_pt = nnlo_pt_2018; pdf_as = pdf_as_2018; HxecBr = HxecBr_2018;

      inputFile1 = "../ws_2018_FINAL.root";
      obs_SR1    = obs_SR1_2018;
      obs_SR2    = obs_SR2_2018;
      obs_SR3    = obs_SR3_2018;
    }//end 2018
    else if ( year == 2016 ) {
      signal1_rate = signal1_rate_2016; BBbar_below_Jpsi_2D_rate = BBbar_below_Jpsi_2D_rate_2016;
      signal2_rate = signal2_rate_2016; BBbar_above_Jpsi_2D_rate = BBbar_above_Jpsi_2D_rate_2016;
      //BBbar_norm = BBbar_norm_2016; BBbar_syst = BBbar_syst_2016;
      BBbar_norm_SR1 = BBbar_norm_2016_SR1; BBbar_syst_SR1 = BBbar_syst_2016_SR1;
      BBbar_norm_SR2 = BBbar_norm_2016_SR2; BBbar_syst_SR2 = BBbar_syst_2016_SR2;
      lumi_13TeV = lumi_13TeV_2016; mu_hlt     = mu_hlt_2016;  mu_id  = mu_id_2016;  mu_iso  = mu_iso_2016;  mu_pu_eff = mu_pu_eff_2016; mu_pu  = mu_pu_2016;
      ovlp_trk   = ovlp_trk_2016;   ovlp_mu    = ovlp_mu_2016; llp_mu = llp_mu_2016; dimu_M = dimu_M_2016; nnlo_pt = nnlo_pt_2016; pdf_as = pdf_as_2016; HxecBr = HxecBr_2016;

      inputFile1 = "../ws_2016_FINAL.root";
      obs_SR1    = obs_SR1_2016;
      obs_SR2    = obs_SR2_2016;
    }//end 2016
    else if ( year == 2020 ) {
      std::cout << "*** Combining data cards of 2016 and 2018 below 9 GeV. ***" << std::endl;
    }
    else{
      std::cout << "*** User input year is unknown! Please check. ***" << std::endl;
    }

    //Common Combine rule for 2017 and 2018: use --LHCmode LHC-limits when unblinding as suggested by HiggsCombine people
    Myrule = Myrule + "--rule CLs --LHC-mode LHC-limits --cl 0.95 --rAbsAcc 0.01 --rRelAcc 0.001";//Require accuracy on r because of ~zero bkg analysis, otherwise r fluctuates
    pwd = pwd + "/home/ws13/Run2Limit/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/";

  } // End function

} // End namespace

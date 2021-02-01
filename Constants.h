//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Common Constants for many macros !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Constants for CreateDatacards.C    !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Default machine: TAMU Terra, CERN Lxplus not tested yet
bool isLxplus = false;
// Expected Limit quantiles: %.3f
// const int N_Quantiles = 5;
const int N_Quantiles = 1;//ATM, doesn't make much sense to quote other quantiles
// float expected_quantiles[N_Quantiles] = {0.500, 0.840, 0.160, 0.975, 0.025};
float expected_quantiles[N_Quantiles] = {0.500};
// # of mass points for expected limits (before unblinding), see below
const int N_Signals = 56;
float masses[N_Signals] = {0.2113, 0.2400, 0.2700, 0.3000, 0.3300, 0.3600, 0.4000, 0.4300, 0.4600, 0.5000, 0.5300, 0.5600,
   0.6000, 0.7000, 0.8000, 0.9000, 1.0000, 1.1000, 1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000,
   2.1000, 2.2000, 2.3000, 2.4000, 2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 8.5000,
   13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000, 58.0000};

bool DiffSeed = true; //Use differnet seed each time using combine
int Ninit = 0, Nend = 1; // Each mass point will be submitted (Nend-Ninit) times

// Following constants are used in datacards, 2018 to be finalized (2016 is finalized), 2017 data is not analyzed
// SR1: Below J/psi
float signal1_rate_2017 = 1, BBbar_below_Jpsi_2D_rate_2017 = 1.29;//NOT ANALYZED
float signal1_rate_2018 = 1, BBbar_below_Jpsi_2D_rate_2018 = 4.34;
float signal1_rate_2016 = 1, BBbar_below_Jpsi_2D_rate_2016 = 7.26;
// SR2: Above J/psi, below 9 GeV
float signal2_rate_2017 = 1, BBbar_above_Jpsi_2D_rate_2017 = 0.01;//NOT ANALYZED
float signal2_rate_2018 = 1, BBbar_above_Jpsi_2D_rate_2018 = 6.16;
float signal2_rate_2016 = 1, BBbar_above_Jpsi_2D_rate_2016 = 7.26;
// SR3: Above 9 GeV
float signal3_rate_2017 = 1, HighMassBKG_rate_2017 = 7.24;
float signal3_rate_2018 = 1, HighMassBKG_rate_2018 = 12.28;
// Background Uncertainties: apply to SR1 and SR2
// 2018 SR1: Stat. uncetainty 10.1%; SR2: Stat. unc. 12.3%; Sys. unc. SR1 4.1%, SR2 1.5%
float BBbar_norm_2018_SR1 = 1.101, BBbar_norm_2018_SR2 = 1.123, BBbar_syst_2018_SR1 = 1.041, BBbar_syst_2018_SR2 = 1.015;
float BBbar_norm_2016_SR1 = 1.123, BBbar_norm_2016_SR2 = 1.123, BBbar_syst_2016_SR1 = 1.200, BBbar_syst_2016_SR2 = 1.200;
//float BBbar_norm_2016  = 1.123,  BBbar_syst_2016 = 1.2;
// 2017 not analyzed
float BBbar_norm_2017  = 1.127,  BBbar_syst_2017 = 1.2;

// 2018 SR3: stat. unc. 16.4%, Sys. unc 2.3%
float BKG_norm_2018_SR3 = 1.164, BKG_syst_2018_SR3 = 1.023, BKG_shape_2018_SR3 = 1.100;

// Systematic Uncertainties: Need to add MC scale to data at high mass, to be updated: PU/mass window/HLT
float lumi_13TeV_2018 = 1.025, mu_hlt_2018  = 1.006, mu_id_2018  = 1.024, mu_iso_2018  = 1.002, mu_pu_2018  = 1.0005, mu_pu_eff_2018 = 1.018, ovlp_trk_2018 = 1.024, ovlp_mu_2018 = 1.026, dimu_M_2018 = 1.0024, nnlo_pt_2018 = 1.02, pdf_as_2018 = 1.08, HxecBr_2018 = 1.038;
float lumi_13TeV_2016 = 1.025, mu_hlt_2016  = 1.060, mu_id_2016  = 1.024, mu_iso_2016  = 1.002, mu_pu_2016  = 1.0017, mu_pu_eff_2016 = 1.000, ovlp_trk_2016 = 1.024, ovlp_mu_2016 = 1.026, dimu_M_2016 = 1.015, nnlo_pt_2016 = 1.02, pdf_as_2016 = 1.08, HxecBr_2016 = 1.038;
// 2017 not analyzed
float lumi_13TeV_2017 = 1.025, mu_hlt_2017  = 1.015, mu_id_2017  = 1.024, mu_iso_2017  = 1.002, mu_pu_2017  = 1.0017, mu_pu_eff_2017 = 1.018, ovlp_trk_2017 = 1.024, ovlp_mu_2017 = 1.026, dimu_M_2017 = 1.000, nnlo_pt_2017 = 1.02, pdf_as_2017 = 1.08, HxecBr_2017 = 1.038;

// Observed events after unblinding
int obs_SR1_2017 = -1, obs_SR2_2017 = -1, obs_SR3_2017 = -1;
int obs_SR1_2018 = -1, obs_SR2_2018 = -1, obs_SR3_2018 = -1;
int obs_SR1_2016 = -1, obs_SR2_2016 = -1; //no SR3 for 2016

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Constants for makeWorkSpace_H2A4Mu.C    !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//Define SR1/2/3 mass ranges
// SR1: Below Jpsi
const double       m_SR1_min  = 0.2113;
const double       m_SR1_max  = 2.72;
const unsigned int m_SR1_bins = 63;//same as bbBar background binning
// SR2: Above Jpsi and below 9GeV
const double       m_SR2_min  = 3.24;
const double       m_SR2_max  = 9.;
const unsigned int m_SR2_bins = 144;//same as bbBar background binning
// SR3: Above 9GeV high mass
const double       m_SR3_min  = 11.;
const double       m_SR3_max  = 60.;
const unsigned int m_SR3_bins = 14;
//2016
const double       m_min      = 0.2113;
const double       m_max      = 9.;
const unsigned int m_bins     = 220;

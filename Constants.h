//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Common Constants for many macros !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Constants for CreateDatacards.C    !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Default machine: TAMU Terra, CERN Lxplus not tested yet
bool isLxplus = false;
// Expected Limit quantiles: %.3f
//const int N_Quantiles = 5;
//float expected_quantiles[N_Quantiles] = {0.500, 0.840, 0.160, 0.975, 0.025};
const int N_Quantiles = 1;//ATM, doesn't make much sense to quote other quantiles
float expected_quantiles[N_Quantiles] = {0.500};

// # of mass points for expected limits (before unblinding), see below
const int N_Signals = 170;
float masses[N_Signals] = {
  0.2113,  0.2400,  0.2700,  0.3000,  0.3300,  0.3600,  0.4000,  0.4500,  0.6000,  0.7000,  0.8000,  0.9000,  1.0000,  1.0500,  1.0600,  1.0700,  1.0800,
  1.0900,  1.1000,  1.2000,  1.2500,  1.2600,  1.2700,  1.2800,  1.2900,  1.3000,  1.3100,  1.3200,  1.3300,  1.3400,  1.3500,  1.4000,  1.5000,  1.6000,
  1.7000,  1.8000,  1.9000,  1.9200,  1.9300,  1.9400,  1.9500,  1.9600,  1.9700,  1.9800,  1.9900,  2.0000,  2.0100,  2.0200,  2.0300,  2.0500,  2.1000,
  2.2000,  2.3000,  2.4000,  2.4200,  2.4300,  2.4400,  2.4500,  2.4600,  2.4700,  2.4800,  2.5000,  2.6000,  2.7200,  3.2400,  3.4000,  3.7000,  4.0000,
  4.5000,  4.6000,  4.7000,  4.8000,  4.9000,  5.0000,  5.1000,  5.2000,  5.3000,  5.4000,  5.5000,  5.6000,  5.7000,  5.8000,  5.9000,  6.0000,  6.5000,
  7.0000,  7.5000,  7.8000,  7.9000,  8.0000,  8.1000,  8.2000,  8.3000,  8.4000,  8.5000,  8.6000,  8.7000,  8.8000,  8.9000,  8.9900,  11.0000, 13.0000,
  14.5000, 15.0000, 15.5000, 16.0000, 16.5000, 17.0000, 19.0000, 19.5000, 20.0000, 20.5000, 21.0000, 21.5000, 22.0000, 22.5000, 23.0000, 25.0000, 27.0000,
  29.0000, 31.0000, 33.0000, 33.5000, 34.0000, 34.5000, 35.0000, 35.5000, 36.0000, 36.5000, 37.0000, 37.5000, 38.0000, 38.5000, 39.0000, 39.5000, 40.0000,
  40.5000, 41.0000, 41.5000, 42.0000, 43.0000, 45.0000, 46.5000, 47.0000, 47.5000, 48.0000, 48.5000, 49.0000, 49.5000, 50.0000, 50.5000, 51.0000, 51.5000,
  52.0000, 52.5000, 53.0000, 53.5000, 54.0000, 54.5000, 55.0000, 55.5000, 56.0000, 56.5000, 57.0000, 57.5000, 58.0000, 58.5000, 59.0000, 59.5000, 59.9000
 };

bool Expected = true; // Use combine for expected limits; if false, produce observed limits
bool DiffSeed = true; // Use differnet seed each time using combine
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

// 2018 SR3: stat. unc. 16.4%, Sys. unc 2.3%, shape unc 23.8%
float BKG_norm_2018_SR3 = 1.164, BKG_syst_2018_SR3 = 1.023, BKG_shape_2018_SR3 = 1.238;

// 2018 signal CB shape param unc: use same for all signals, derived from prompt dark photon CB fits
float signal1_sigma_unc_2018 = 0.029, signal1_alpha_unc_2018 = 0.094, signal1_n_unc_2018 = 0.288;
float signal2_sigma_unc_2018 = 0.029, signal2_alpha_unc_2018 = 0.094, signal2_n_unc_2018 = 0.288;
float signal3_sigma_unc_2018 = 0.029, signal3_alpha_unc_2018 = 0.094, signal3_n_unc_2018 = 0.288;

// Systematic Uncertainties: Need to add MC scale to data at high mass, to be updated: PU/mass window/HLT
float lumi_13TeV_2018 = 1.025, mu_hlt_2018  = 1.006, mu_id_2018  = 1.024, mu_iso_2018  = 1.002, mu_pu_2018  = 1.0005, mu_pu_eff_2018 = 1.018, ovlp_trk_2018 = 1.024, ovlp_mu_2018 = 1.026, llp_mu_2018 = 1.010, dimu_M_2018 = 1.0024, nnlo_pt_2018 = 1.02, pdf_as_2018 = 1.08, HxecBr_2018 = 1.038;
float lumi_13TeV_2016 = 1.025, mu_hlt_2016  = 1.060, mu_id_2016  = 1.024, mu_iso_2016  = 1.002, mu_pu_2016  = 1.0017, mu_pu_eff_2016 = 1.000, ovlp_trk_2016 = 1.024, ovlp_mu_2016 = 1.026, llp_mu_2016 = 1.000, dimu_M_2016 = 1.015, nnlo_pt_2016 = 1.02, pdf_as_2016 = 1.08, HxecBr_2016 = 1.038;
// 2017 not analyzed
float lumi_13TeV_2017 = 1.025, mu_hlt_2017  = 1.015, mu_id_2017  = 1.024, mu_iso_2017  = 1.002, mu_pu_2017  = 1.0017, mu_pu_eff_2017 = 1.018, ovlp_trk_2017 = 1.024, ovlp_mu_2017 = 1.026, llp_mu_2017 = 1.000, dimu_M_2017 = 1.000, nnlo_pt_2017 = 1.02, pdf_as_2017 = 1.08, HxecBr_2017 = 1.038;

// Observed events after unblinding
int obs_SR1_2017 = -1, obs_SR2_2017 = -1, obs_SR3_2017 = -1;
int obs_SR1_2018 =  4, obs_SR2_2018 =  6, obs_SR3_2018 = 20;
int obs_SR1_2016 = -1, obs_SR2_2016 = -1; //no SR3 for 2016

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Constants for makeWorkSpace_H2A4Mu.C    !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//Define SR1/2/3 mass ranges
// SR1: Below Jpsi
const double       m_SR1_min  = 0.2113;
const double       m_SR1_max  = 2.72;
const unsigned int m_SR1_bins = 63; // same as bbBar background binning
// SR2: Above Jpsi and below 9 GeV
const double       m_SR2_min  = 3.24;
const double       m_SR2_max  = 9.;
const unsigned int m_SR2_bins = 144; // same as bbBar background binning
// SR3: Above Upsilon high mass
const double       m_SR3_min  = 11.;
const double       m_SR3_max  = 60.;
const unsigned int m_SR3_bins = 100; // this can't be 14 bins like the background plot as it will fail GoF test when unblinding, use 100
//2016
const double       m_min      = 0.2113;
const double       m_max      = 9.;
const unsigned int m_bins     = 220;

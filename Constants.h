//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Common Constants for many macros !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
//!  Constants for CreateDatacards.C    !
//!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// Default machine: Brazos, Lxplus not tested yet
bool isLxplus = false;
// Expected Limit quantiles: %.3f
// const int N_Quantiles = 5;
// float expected_quantiles[N_Quantiles] = {0.500, 0.840, 0.160, 0.975, 0.025};
const int N_Quantiles = 1;//ATM, doesn't make much sense to quote other quantiles
float expected_quantiles[N_Quantiles] = {0.500};
// # of mass points for expected limits (before unblinding), see below
const int N_Signals = 55;
float masses[N_Signals] = {0.2113, 0.2400, 0.2700, 0.3000, 0.3300, 0.3600, 0.4000, 0.4300, 0.4600, 0.5000, 0.5300, 0.5600,
   0.6000, 0.7000, 0.8000, 0.9000, 1.0000, 1.1000, 1.2000, 1.3000, 1.4000, 1.5000, 1.6000, 1.7000, 1.8000, 1.9000, 2.0000,
   2.1000, 2.2000, 2.3000, 2.4000, 2.5000, 2.6000, 2.7000, 3.3000, 3.4000, 3.7000, 4.0000, 5.0000, 6.0000, 7.0000, 8.0000, 8.5000,
   13.0000, 17.0000, 21.0000, 25.0000, 29.0000, 33.0000, 37.0000, 41.0000, 45.0000, 49.0000, 53.0000, 57.0000};

bool DiffSeed = true; //Use differnet seed each time using combine
int Ninit = 0, Nend = 1; // Each mass point will be submitted (Nend-Ninit) times

// Following constants are used in datacards for 2017 and 2018: to be finalized
// SR1: Below J/psi
float signal1_rate_2017 = 1, BBbar_below_Jpsi_2D_rate_2017 = 1.29;
float signal1_rate_2018 = 1, BBbar_below_Jpsi_2D_rate_2018 = 2.78;
// SR2: Above J/psi, below 9 GeV
float signal2_rate_2017 = 1, BBbar_above_Jpsi_2D_rate_2017 = 0.01;//!!!Note!!!:suppose to be 0, but use 0.01 for tool to run
float signal2_rate_2018 = 1, BBbar_above_Jpsi_2D_rate_2018 = 0.29;
// SR3: Above 9 GeV
float signal3_rate_2017 = 1, HighMassBKG_rate_2017 = 7.24;
float signal3_rate_2018 = 1, HighMassBKG_rate_2018 = 10.55;
// Background Uncertainties: apply to SR1 and SR2
float BBbar_norm_2017   = 1.123,   BBbar_syst_2017 = 1.2;
float BBbar_norm_2018   = 1.123,   BBbar_syst_2018 = 1.2;
// Systematic Uncertainties
float lumi_13TeV_2017 = 1.025, mu_hlt_2017  = 1.015, mu_id_2017  = 1.024, mu_iso_2017  = 1.02, mu_pu_2017  = 1.0017;
float ovlp_trk_2017   = 1.024, ovlp_mu_2017 = 1.026, dimu_M_2017 = 1.015, nnlo_pt_2017 = 1.02, pdf_as_2017 = 1.08, HxecBr_2017 = 1.038;
float lumi_13TeV_2018 = 1.025, mu_hlt_2018  = 1.015, mu_id_2018  = 1.024, mu_iso_2018  = 1.02, mu_pu_2018  = 1.0017;
float ovlp_trk_2018   = 1.024, ovlp_mu_2018 = 1.026, dimu_M_2018 = 1.015, nnlo_pt_2018 = 1.02, pdf_as_2018 = 1.08, HxecBr_2018 = 1.038;

// Observed events after unblinding
int obs_SR1_2017 = -1, obs_SR2_2017 = -1, obs_SR3_2017 = -1;
int obs_SR1_2018 = -1, obs_SR2_2018 = -1, obs_SR3_2018 = -1;

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
const double       m_SR3_max  = 59.;
const unsigned int m_SR3_bins = 12;

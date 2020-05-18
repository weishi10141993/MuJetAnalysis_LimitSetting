#include "TFile.h"
#include "TStopwatch.h"
#include "TCanvas.h"
#include "TTree.h"
#include "TF1.h"
#include "TH1.h"
#include "TH2.h"
#include "TChain.h"
#include "TRandom3.h"
#include "TStyle.h"
#include "TPaveText.h"
#include "TLatex.h"
#include "TLegend.h"
#include "TROOT.h"
#include "TMatrixDSym.h"
#include "TMath.h"

#include <sstream>
#include <iostream>
#include <string>

#include "RooAbsPdf.h"
#include "RooProdPdf.h"
#include "RooRealVar.h"
#include "RooAbsReal.h"
#include "RooRealProxy.h"
#include "RooDataHist.h"
#include "RooDataSet.h"
#include "RooPlot.h"
#include "RooHist.h"
#include "RooWorkspace.h"
#include "RooRandom.h"
#include "RooFitResult.h"
#include "RooClassFactory.h"
#include "RooHistPdf.h"
#include "RooCustomizer.h"
#include "RooMultiVarGaussian.h"
#include "RooTFnBinding.h"
#include "RooArgusBG.h"
#include "RooBernstein.h"
#include "RooGaussian.h"
#include "RooPolynomial.h"
#include "RooChebychev.h"
#include "RooGenericPdf.h"
#include "RooAddPdf.h"
#include "RooCBShape.h"

#include "../Constants.h"
#include "../Config.h"

#ifndef __CINT__
#include "RooCFunction1Binding.h"
#endif

using namespace RooFit;

class RooUserPdf : public RooAbsPdf {

  public:
    RooUserPdf(const char *name, const char *title, RooAbsReal& _x1, RooAbsReal& _x2);
    RooUserPdf(const RooUserPdf& other, const char* name=0) ;
    virtual TObject* clone(const char* newname) const {return new RooUserPdf(*this,newname);}
    inline virtual ~RooUserPdf() { }

  protected:
    RooRealProxy x1;
    RooRealProxy x2;
    Double_t evaluate() const ;

  private:
    ClassDef(RooUserPdf,0)
};

RooUserPdf::RooUserPdf(const char *name, const char *title, RooAbsReal& _x1, RooAbsReal& _x2) :
  RooAbsPdf(name,title),
  x1("x1","Dependent1",this,_x1),
  x2("x2","Dependent2",this,_x2)
{}

RooUserPdf::RooUserPdf(const RooUserPdf& other, const char* name) :
  RooAbsPdf(other,name),
  x1("x1", this, other.x1),
  x2("x2", this, other.x2)
{}

Double_t RooUserPdf::evaluate() const
{
  Double_t res;

  if ( fabs(x1-x2) < 3*(0.003044 + 0.007025*(x1+x2)/2.0 + 0.000053*(x1+x2)*(x1+x2)/4.0) ) {
    res = 1.0;
  } else {
    res = 0.0;
  }
  return res;
}

void makeWorkSpace_H2A4Mu(double mA_GeV = 0.4, int seed=37) {

  //Configure inputfile for year
  Limit_cfg::ConfigureInput(year);

  using namespace RooFit;
  RooRandom::randomGenerator()->SetSeed(seed);
  RooWorkspace *w_H2A4Mu = new RooWorkspace("w_H2A4Mu");

  RooRealVar m1_below_Jpsi("m1_below_Jpsi", "m_{#mu#mu_{1}}", m_SR1_min, m_SR1_max, "GeV");
  RooRealVar m2_below_Jpsi("m2_below_Jpsi", "m_{#mu#mu_{2}}", m_SR1_min, m_SR1_max, "GeV");
  RooRealVar m1_above_Jpsi("m1_above_Jpsi", "m_{#mu#mu_{1}}", m_SR2_min, m_SR2_max, "GeV");
  RooRealVar m2_above_Jpsi("m2_above_Jpsi", "m_{#mu#mu_{2}}", m_SR2_min, m_SR2_max, "GeV");
  RooRealVar m1_high_mass("m1_high_mass", "m_{#mu#mu_{1}}", m_SR3_min, m_SR3_max, "GeV");
  RooRealVar m2_high_mass("m2_high_mass", "m_{#mu#mu_{2}}", m_SR3_min, m_SR3_max, "GeV");
  RooRealVar m1("m1", "m_{(#mu#mu)_{1}}", m_min, m_max, "GeV");//for 2016
  RooRealVar m2("m2", "m_{(#mu#mu)_{2}}", m_min, m_max, "GeV");
  m1_below_Jpsi.setBins(m_SR1_bins);
  m2_below_Jpsi.setBins(m_SR1_bins);
  m1_above_Jpsi.setBins(m_SR2_bins);
  m2_above_Jpsi.setBins(m_SR2_bins);
  m1_high_mass.setBins(m_SR3_bins);
  m2_high_mass.setBins(m_SR3_bins);
  m1.setBins(m_bins);
  m2.setBins(m_bins);

  if(year==2017 || year==2018){
    w_H2A4Mu->import(m1_below_Jpsi);
    w_H2A4Mu->import(m2_below_Jpsi);
    w_H2A4Mu->import(m1_above_Jpsi);
    w_H2A4Mu->import(m2_above_Jpsi);
    w_H2A4Mu->import(m1_high_mass);
    w_H2A4Mu->import(m2_high_mass);
  }
  if(year==2016){
    w_H2A4Mu->import(m1);
    w_H2A4Mu->import(m2);
  }

  //Signal Diagonal Area in 2017 and 2018
  RooGenericPdf dia1( "dia1", "generic PDF for diagonal region at SR1", "fabs(m1_below_Jpsi-m2_below_Jpsi) < 3*(0.003044 + 0.007025*(m1_below_Jpsi+m2_below_Jpsi)/2.0 + 0.000053*(m1_below_Jpsi+m2_below_Jpsi)*(m1_below_Jpsi+m2_below_Jpsi)/4.0)", RooArgSet(m1_below_Jpsi, m2_below_Jpsi) );
  RooGenericPdf dia2( "dia2", "generic PDF for diaginal region at SR2", "fabs(m1_above_Jpsi-m2_above_Jpsi) < 3*(0.003044 + 0.007025*(m1_above_Jpsi+m2_above_Jpsi)/2.0 + 0.000053*(m1_above_Jpsi+m2_above_Jpsi)*(m1_above_Jpsi+m2_above_Jpsi)/4.0)", RooArgSet(m1_above_Jpsi, m2_above_Jpsi) );
  RooGenericPdf dia3( "dia3", "generic PDF for diaginal region at SR3", "fabs(m1_high_mass-m2_high_mass) < 3*(0.003044 + 0.007025*(m1_high_mass+m2_high_mass)/2.0 + 0.000053*(m1_high_mass+m2_high_mass)*(m1_high_mass+m2_high_mass)/4.0)", RooArgSet(m1_high_mass, m2_high_mass) );
  //2016 window
  RooGenericPdf dia2016( "dia2016", "generic PDF for diaginal region in 2016", "fabs(m1-m2) < (0.13 + 0.065*(m1 + m2)/2.)", RooArgSet(m1,m2) );

  if(year==2017 || year==2018){
    w_H2A4Mu->import(dia1);
    w_H2A4Mu->import(dia2);
    w_H2A4Mu->import(dia3);
  }
  if(year==2016){
    w_H2A4Mu->import(dia2016);
  }

  //Observed data in SR1
  Double_t massC_SR1, massF_SR1;
  TTree* tree_dimudimu_signal1_2D = new TTree("tree_dimudimu_signal1_2D", "tree_dimudimu_signal1_2D");
  tree_dimudimu_signal1_2D->Branch("massC_SR1", &massC_SR1, "massC_SR1/D");
  tree_dimudimu_signal1_2D->Branch("massF_SR1", &massF_SR1, "massF_SR1/D");

  //Observed data in SR2
  Double_t massC_SR2, massF_SR2;
  TTree* tree_dimudimu_signal2_2D = new TTree("tree_dimudimu_signal2_2D", "tree_dimudimu_signal2_2D");
  tree_dimudimu_signal2_2D->Branch("massC_SR2", &massC_SR2, "massC_SR2/D");
  tree_dimudimu_signal2_2D->Branch("massF_SR2", &massF_SR2, "massF_SR2/D");

  //Observed data in SR3
  Double_t massC_SR3, massF_SR3;
  TTree* tree_dimudimu_signal3_2D = new TTree("tree_dimudimu_signal3_2D", "tree_dimudimu_signal3_2D");
  tree_dimudimu_signal3_2D->Branch("massC_SR3", &massC_SR3, "massC_SR3/D");
  tree_dimudimu_signal3_2D->Branch("massF_SR3", &massF_SR3, "massF_SR3/D");

  //Observed data in 2016
  Double_t massC, massF;
  TTree* tree_dimudimu_signal2016_2D = new TTree("tree_dimudimu_signal2016_2D","tree_dimudimu_signal2016_2D");
  tree_dimudimu_signal2016_2D->Branch("massC", &massC, "massC/D");
  tree_dimudimu_signal2016_2D->Branch("massF", &massF, "massF/D");

  //===================
  //BLINDED DATA
  //===================
  if(year==2017 || year==2018){
    massC_SR1 = 100.;
    massF_SR1 = 100.;
    massC_SR2 = 100.;
    massF_SR2 = 100.;
    massC_SR3 = 100.;
    massF_SR3 = 100.;
  }
  if(year==2016){
    massC = 100.;
    massF = 100.;
  }

  /*
  //===================
  //2016 Data Unblinded
  //===================
  // massC =0.8079733;   massF = 0.7267103; tree_dimudimu_signal2016_2D->Fill();
  massC =2.8599584;   massF = 3.0017674; tree_dimudimu_signal2016_2D->Fill();
  // massC =0.4258973;   massF = 0.5848349; tree_dimudimu_signal2016_2D->Fill();
  // massC =3.0722196;   massF = 3.2662851; tree_dimudimu_signal2016_2D->Fill();
  massC =3.0728187;   massF = 3.0538983; tree_dimudimu_signal2016_2D->Fill();
  // massC =3.0950253;   massF = 3.3617882; tree_dimudimu_signal2016_2D->Fill();
  massC =3.1521356;   massF = 2.8546791; tree_dimudimu_signal2016_2D->Fill();
  massC =2.8254406;   massF = 2.6496100; tree_dimudimu_signal2016_2D->Fill();
  massC =1.2541753;   massF = 1.1524148; tree_dimudimu_signal2016_2D->Fill();
  massC =2.3863873;   massF = 2.3582603; tree_dimudimu_signal2016_2D->Fill();
  massC =3.0641751;   massF = 3.0972354; tree_dimudimu_signal2016_2D->Fill();
  massC =1.9403913;   massF = 1.8196427; tree_dimudimu_signal2016_2D->Fill();
  massC =1.3540757;   massF = 1.4834892; tree_dimudimu_signal2016_2D->Fill();
  */

  //===================
  //2017 Data Unblinded
  //===================
  /*
  massC_SR1 = 100.;
  massF_SR1 = 100.;
  massC_SR2 = 100.;
  massF_SR2 = 100.;
  massC_SR3 = 100.;
  massF_SR3 = 100.;*/

  //===================
  //2018 Data Unblinded
  //===================
  /*
  massC_SR1 = 100.;
  massF_SR1 = 100.;
  massC_SR2 = 100.;
  massF_SR2 = 100.;
  massC_SR3 = 100.;
  massF_SR3 = 100.;*/

  cout<<"--- PRINT signal trees ---"<<endl;
  tree_dimudimu_signal1_2D->Print();
  tree_dimudimu_signal2_2D->Print();
  tree_dimudimu_signal3_2D->Print();
  tree_dimudimu_signal2016_2D->Print();
  cout<<"-------------------------------------"<<endl;
  tree_dimudimu_signal1_2D->GetBranch("massC_SR1")->SetName("m1_below_Jpsi");
  tree_dimudimu_signal1_2D->GetBranch("massF_SR1")->SetName("m2_below_Jpsi");
  tree_dimudimu_signal2_2D->GetBranch("massC_SR2")->SetName("m1_above_Jpsi");
  tree_dimudimu_signal2_2D->GetBranch("massF_SR2")->SetName("m2_above_Jpsi");
  tree_dimudimu_signal3_2D->GetBranch("massC_SR3")->SetName("m1_high_mass");
  tree_dimudimu_signal3_2D->GetBranch("massF_SR3")->SetName("m2_high_mass");
  tree_dimudimu_signal2016_2D->GetBranch("massC")->SetName("m1");
  tree_dimudimu_signal2016_2D->GetBranch("massF")->SetName("m2");

  RooDataSet* ds_dimudimu_signal1_2D = new RooDataSet("ds_dimudimu_signal1_2D", "ds_dimudimu_signal1_2D", tree_dimudimu_signal1_2D, RooArgSet(m1_below_Jpsi, m2_below_Jpsi) );
  RooDataSet* ds_dimudimu_signal2_2D = new RooDataSet("ds_dimudimu_signal2_2D", "ds_dimudimu_signal2_2D", tree_dimudimu_signal2_2D, RooArgSet(m1_above_Jpsi, m2_above_Jpsi) );
  RooDataSet* ds_dimudimu_signal3_2D = new RooDataSet("ds_dimudimu_signal3_2D", "ds_dimudimu_signal3_2D", tree_dimudimu_signal3_2D, RooArgSet(m1_high_mass, m2_high_mass) );
  RooDataSet* ds_dimudimu_signal2016SR1_2D = new RooDataSet("ds_dimudimu_signal2016SR1_2D", "ds_dimudimu_signal2016SR1_2D", tree_dimudimu_signal2016_2D, RooArgSet(m1, m2) );
  RooDataSet* ds_dimudimu_signal2016SR2_2D = new RooDataSet("ds_dimudimu_signal2016SR2_2D", "ds_dimudimu_signal2016SR2_2D", tree_dimudimu_signal2016_2D, RooArgSet(m1, m2) );
  cout<<"--- PRINT signal datasets ---"<<endl;
  ds_dimudimu_signal1_2D->Print("v");
  ds_dimudimu_signal2_2D->Print("v");
  ds_dimudimu_signal3_2D->Print("v");
  ds_dimudimu_signal2016SR1_2D->Print("v");
  ds_dimudimu_signal2016SR2_2D->Print("v");
  cout<<"-------------------------------------"<<endl;

  if(year==2017 || year==2018){
    w_H2A4Mu->import(*ds_dimudimu_signal1_2D, Rename("data_obs_SR1"));//this will be used for the wildcard in shapes in datacard
    w_H2A4Mu->import(*ds_dimudimu_signal2_2D, Rename("data_obs_SR2"));
    w_H2A4Mu->import(*ds_dimudimu_signal3_2D, Rename("data_obs_SR3"));
  }
  if(year==2016){
    w_H2A4Mu->import(*ds_dimudimu_signal2016SR1_2D, Rename("data_obs_SR1"));
    w_H2A4Mu->import(*ds_dimudimu_signal2016SR2_2D, Rename("data_obs_SR2"));
  }

  //Signal parameteres below Jpsi
  RooRealVar signal1_mA("signal1_mA", "signal1_mA", mA_GeV);
  RooRealVar signal1_sigma("signal1_sigma", "signal1_sigma", 0.003044 + 0.007025*mA_GeV + 0.000053*mA_GeV*mA_GeV );
  RooRealVar signal1_alpha("signal1_alpha", "signal1_alpha", 1.75);
  RooRealVar signal1_n("signal1_n", "signal1_n", 2.0);
  //Signal Shape
  RooCBShape signal1_m1("signal1_m1", "signal1_m1", m1_below_Jpsi, signal1_mA, signal1_sigma, signal1_alpha, signal1_n);
  RooCBShape signal1_m2("signal1_m2", "signal1_m2", m2_below_Jpsi, signal1_mA, signal1_sigma, signal1_alpha, signal1_n);

  //Signal parameteres above Jpsi
  RooRealVar signal2_mA("signal2_mA", "signal2_mA", mA_GeV);
  RooRealVar signal2_sigma("signal2_sigma", "signal2_sigma", 0.003044 + 0.007025*mA_GeV + 0.000053*mA_GeV*mA_GeV );
  RooRealVar signal2_alpha("signal2_alpha", "signal2_alpha", 1.75);
  RooRealVar signal2_n("signal2_n", "signal2_n", 2.0);
  //Signal Shape
  RooCBShape signal2_m1("signal2_m1", "signal2_m1", m1_above_Jpsi, signal2_mA, signal2_sigma, signal2_alpha, signal2_n);
  RooCBShape signal2_m2("signal2_m2", "signal2_m2", m2_above_Jpsi, signal2_mA, signal2_sigma, signal2_alpha, signal2_n);

  //Signal parameteres at high mass
  RooRealVar signal3_mA("signal3_mA", "signal3_mA", mA_GeV);
  RooRealVar signal3_sigma("signal3_sigma", "signal3_sigma", 0.003044 + 0.007025*mA_GeV + 0.000053*mA_GeV*mA_GeV );
  RooRealVar signal3_alpha("signal3_alpha", "signal3_alpha", 1.75);
  RooRealVar signal3_n("signal3_n", "signal3_n", 2.0);
  //Signal Shape
  RooCBShape signal3_m1("signal3_m1", "signal3_m1", m1_high_mass, signal3_mA, signal3_sigma, signal3_alpha, signal3_n);
  RooCBShape signal3_m2("signal3_m2", "signal3_m2", m2_high_mass, signal3_mA, signal3_sigma, signal3_alpha, signal3_n);

  //Signal parameteres
  RooRealVar signal2016_mA("signal2016_mA", "signal2016_mA", mA_GeV);
  RooRealVar signal2016_sigma("signal2016_sigma", "signal2016_sigma", (0.13 + 0.065*mA_GeV)/5.0 );
  RooRealVar signal2016_alpha("signal2016_alpha", "signal2016_alpha", 1.75);
  RooRealVar signal2016_n("signal2016_n", "signal2016_n", 2.0);
  //Signal 2D template
  RooCBShape signal2016_m1("signal2016_m1", "signal2016_m1", m1, signal2016_mA, signal2016_sigma, signal2016_alpha, signal2016_n);
  RooCBShape signal2016_m2("signal2016_m2", "signal2016_m2", m2, signal2016_mA, signal2016_sigma, signal2016_alpha, signal2016_n);

  if(year==2017 || year==2018){
    w_H2A4Mu->import(signal1_m1);
    w_H2A4Mu->import(signal1_m2);
    w_H2A4Mu->factory("PROD::signal1(signal1_m1, signal1_m2)");
    w_H2A4Mu->import(signal2_m1);
    w_H2A4Mu->import(signal2_m2);
    w_H2A4Mu->factory("PROD::signal2(signal2_m1, signal2_m2)");
    w_H2A4Mu->import(signal3_m1);
    w_H2A4Mu->import(signal3_m2);
    w_H2A4Mu->factory("PROD::signal3(signal3_m1, signal3_m2)");
  }
  if(year==2016){
    w_H2A4Mu->import(signal2016_m1);
    w_H2A4Mu->import(signal2016_m2);
    w_H2A4Mu->factory("PROD::signal1(signal2016_m1, signal2016_m2)");
    w_H2A4Mu->factory("PROD::signal2(signal2016_m1, signal2016_m2)");
  }

  TFile* file = new TFile(inputFile1); // defined in ../Config.h
  RooWorkspace *w = (RooWorkspace*) file->Get("w");
  if(year==2017 || year==2018){
    w_H2A4Mu->import( *w->pdf("template1D_m1_below_Jpsi") );
    w_H2A4Mu->import( *w->pdf("template1D_m2_below_Jpsi") );
    w_H2A4Mu->factory("PROD::BBbar_below_Jpsi_2D(template1D_m1_below_Jpsi, template1D_m2_below_Jpsi)*dia1");
    w_H2A4Mu->import( *w->pdf("template1D_m1_above_Jpsi") );
    w_H2A4Mu->import( *w->pdf("template1D_m2_above_Jpsi") );
    w_H2A4Mu->factory("PROD::BBbar_above_Jpsi_2D(template1D_m1_above_Jpsi, template1D_m2_above_Jpsi)*dia2");
  }
  if(year==2016){
    w_H2A4Mu->import( *w->pdf("template1D_m1") );
    w_H2A4Mu->import( *w->pdf("template1D_m2") );
    w_H2A4Mu->factory("PROD::BBbar_below_Jpsi_2D(template1D_m1, template1D_m2)*dia2016");
    w_H2A4Mu->factory("PROD::BBbar_above_Jpsi_2D(template1D_m1, template1D_m2)*dia2016");//keep same name as 2017 and 2018
  }

  //**************************************************
  //Here we need a bkg pdf for high mass, TBD @Jan17
  //**************************************************
  /*
  //A flat/uniform pdf
  w_H2A4Mu->factory("SUM::template1D_m1_high_mass(1.0*Uniform(m1_high_mass))");
  w_H2A4Mu->factory("SUM::template1D_m2_high_mass(1.0*Uniform(m2_high_mass))");
  w_H2A4Mu->factory("PROD::HighMassBKG(template1D_m1_high_mass, template1D_m2_high_mass)*dia3");
  */

  //A binned likelihood fitted poly-n function
  //poly-0
  //2017 m1: p0=4.65780e-01 (FCN=1.18272); m2: p0=4.72551e-01 (FCN=1.13543)
  //2018 m1: p0=8.68679e-01 (FCN=2.12934); m2: p0=8.60217e-01 (FCN=2.02808)

  //poly-4
  RooGenericPdf HighMassFit2017_m1( "HighMassFit2017_m1", "2017 m1 fit function for estimated BKG at SR3", "2.10843 - 0.367391*m1_high_mass + 0.0213367*m1_high_mass*m1_high_mass - 0.000454813*m1_high_mass*m1_high_mass*m1_high_mass + 0.00000324109*m1_high_mass*m1_high_mass*m1_high_mass*m1_high_mass", RooArgSet(m1_high_mass) );//FCN=0.241282
  RooGenericPdf HighMassFit2017_m2( "HighMassFit2017_m2", "2017 m2 fit function for estimated BKG at SR3", "2.27162 - 0.394333*m2_high_mass + 0.0228821*m2_high_mass*m2_high_mass - 0.000491115*m2_high_mass*m2_high_mass*m2_high_mass + 0.00000353842*m2_high_mass*m2_high_mass*m2_high_mass*m2_high_mass", RooArgSet(m2_high_mass) );//FCN=0.197935
  RooGenericPdf HighMassFit2018_m1( "HighMassFit2018_m1", "2018 m1 fit function for estimated BKG at SR3", "4.36662 - 0.772224*m1_high_mass + 0.0458093*m1_high_mass*m1_high_mass - 0.00101979*m1_high_mass*m1_high_mass*m1_high_mass  + 0.00000769120*m1_high_mass*m1_high_mass*m1_high_mass*m1_high_mass", RooArgSet(m1_high_mass) );//FCN=0.306416
  RooGenericPdf HighMassFit2018_m2( "HighMassFit2018_m2", "2018 m2 fit function for estimated BKG at SR3", "4.11417 - 0.730639*m2_high_mass + 0.0435120*m2_high_mass*m2_high_mass - 0.000969273*m2_high_mass*m2_high_mass*m2_high_mass + 0.00000730823*m2_high_mass*m2_high_mass*m2_high_mass*m2_high_mass", RooArgSet(m2_high_mass) );//FCN=0.260233
  if (year == 2017){
    w_H2A4Mu->import(HighMassFit2017_m1);
    w_H2A4Mu->import(HighMassFit2017_m2);
    w_H2A4Mu->factory("PROD::HighMassBKG(HighMassFit2017_m1, HighMassFit2017_m2)*dia3");
  }
  if (year == 2018){
    w_H2A4Mu->import(HighMassFit2018_m1);
    w_H2A4Mu->import(HighMassFit2018_m2);
    w_H2A4Mu->factory("PROD::HighMassBKG(HighMassFit2018_m1, HighMassFit2018_m2)*dia3");
  }

  // Set all fit variables to constants
  if(year == 2017 || year == 2018){
    w_H2A4Mu->var("MmumuC_c_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("MmumuC_p_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("adHocC_mass_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("adHocC_sigma_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC06_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC16_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC26_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC36_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC46_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC56_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC66_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_MmumuC_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_adHocC_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_bgC_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_etaC_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_phiC_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_rhoC_below_Jpsi")->setConstant(true);

    w_H2A4Mu->var("MmumuF_c_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("MmumuF_p_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("adHocF_mass_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("adHocF_sigma_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF06_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF16_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF26_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF36_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF46_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF56_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF66_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_MmumuF_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_adHocF_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_bgF_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_etaF_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_phiF_below_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_rhoF_below_Jpsi")->setConstant(true);

    w_H2A4Mu->var("bC06_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC16_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC26_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC36_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC46_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC56_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bC66_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("psiC_sigma_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_bgC_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_psiC_above_Jpsi")->setConstant(true);

    w_H2A4Mu->var("bF06_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF16_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF26_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF36_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF46_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF56_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("bF66_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("psiF_sigma_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_bgF_above_Jpsi")->setConstant(true);
    w_H2A4Mu->var("norm_psiF_above_Jpsi")->setConstant(true);
    //Below Jpsi
    w_H2A4Mu->var("signal1_mA")->setConstant(true);
    w_H2A4Mu->var("signal1_sigma")->setConstant(true);
    w_H2A4Mu->var("signal1_alpha")->setConstant(true);
    w_H2A4Mu->var("signal1_n")->setConstant(true);
    //Above Jpsi
    w_H2A4Mu->var("signal2_mA")->setConstant(true);
    w_H2A4Mu->var("signal2_sigma")->setConstant(true);
    w_H2A4Mu->var("signal2_alpha")->setConstant(true);
    w_H2A4Mu->var("signal2_n")->setConstant(true);
    //High mass
    w_H2A4Mu->var("signal3_mA")->setConstant(true);
    w_H2A4Mu->var("signal3_sigma")->setConstant(true);
    w_H2A4Mu->var("signal3_alpha")->setConstant(true);
    w_H2A4Mu->var("signal3_n")->setConstant(true);
  }
  if(year == 2016){
    w_H2A4Mu->var("JpsiC_alpha")->setConstant(true);
    w_H2A4Mu->var("JpsiC_mean")->setConstant(true);
    w_H2A4Mu->var("JpsiC_n")->setConstant(true);
    w_H2A4Mu->var("JpsiC_sigma")->setConstant(true);
    w_H2A4Mu->var("JpsiF_alpha")->setConstant(true);
    w_H2A4Mu->var("JpsiF_mean")->setConstant(true);
    w_H2A4Mu->var("JpsiF_n")->setConstant(true);
    w_H2A4Mu->var("JpsiF_sigma")->setConstant(true);
    w_H2A4Mu->var("norm_JpsiC")->setConstant(true);
    w_H2A4Mu->var("norm_JpsiF")->setConstant(true);

    w_H2A4Mu->var("MmumuC_c")->setConstant(true);
    w_H2A4Mu->var("MmumuC_p")->setConstant(true);
    w_H2A4Mu->var("MmumuF_c")->setConstant(true);
    w_H2A4Mu->var("MmumuF_p")->setConstant(true);
    w_H2A4Mu->var("norm_MmumuC")->setConstant(true);
    w_H2A4Mu->var("norm_MmumuF")->setConstant(true);

    w_H2A4Mu->var("bC06")->setConstant(true);
    w_H2A4Mu->var("bC16")->setConstant(true);
    w_H2A4Mu->var("bC26")->setConstant(true);
    w_H2A4Mu->var("bC36")->setConstant(true);
    w_H2A4Mu->var("bC46")->setConstant(true);
    w_H2A4Mu->var("bC56")->setConstant(true);
    w_H2A4Mu->var("bC66")->setConstant(true);
    w_H2A4Mu->var("bF06")->setConstant(true);
    w_H2A4Mu->var("bF16")->setConstant(true);
    w_H2A4Mu->var("bF26")->setConstant(true);
    w_H2A4Mu->var("bF36")->setConstant(true);
    w_H2A4Mu->var("bF46")->setConstant(true);
    w_H2A4Mu->var("bF56")->setConstant(true);
    w_H2A4Mu->var("bF66")->setConstant(true);
    w_H2A4Mu->var("norm_bgC")->setConstant(true);
    w_H2A4Mu->var("norm_bgF")->setConstant(true);

    w_H2A4Mu->var("norm_etaC")->setConstant(true);
    w_H2A4Mu->var("norm_etaF")->setConstant(true);
    w_H2A4Mu->var("norm_phiC")->setConstant(true);
    w_H2A4Mu->var("norm_phiF")->setConstant(true);
    w_H2A4Mu->var("norm_rhoC")->setConstant(true);
    w_H2A4Mu->var("norm_rhoF")->setConstant(true);

    w_H2A4Mu->var("psiC_sigma")->setConstant(true);
    w_H2A4Mu->var("psiF_sigma")->setConstant(true);
    w_H2A4Mu->var("norm_psiC")->setConstant(true);
    w_H2A4Mu->var("norm_psiF")->setConstant(true);

    w_H2A4Mu->var("norm_adHocC")->setConstant(true);
    w_H2A4Mu->var("norm_adHocF")->setConstant(true);
    w_H2A4Mu->var("adHocC_mass")->setConstant(true);
    w_H2A4Mu->var("adHocF_mass")->setConstant(true);
    w_H2A4Mu->var("adHocC_sigma")->setConstant(true);
    w_H2A4Mu->var("adHocF_sigma")->setConstant(true);

    w_H2A4Mu->var("signal2016_mA")->setConstant(true);
    w_H2A4Mu->var("signal2016_n")->setConstant(true);
    w_H2A4Mu->var("signal2016_sigma")->setConstant(true);
  }

  cout<<"---------------WORKING-SPACE----------------"<<endl;
  w_H2A4Mu->Print("v");
  TString ws_fileName = Form("../workSpaces/%d/ws_H2A4Mu_mA_%.4f_GeV.root", year, mA_GeV);
  cout << "save work space to file: " << ws_fileName << endl;
  w_H2A4Mu->writeToFile(ws_fileName);
}

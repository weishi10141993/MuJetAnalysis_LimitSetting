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

  if ( fabs(x1 - x2) < 5.*(0.026 + 0.013*(x1 + x2)/2.) ) {
    res = 1.0;
  } else {
    res = 0.0;
  }
  return res;
}

void makeWorkSpace_H2A4Mu(double mA_GeV = 0.4, int seed=37) {

  using namespace RooFit;
  RooRandom::randomGenerator()->SetSeed(seed); 
  RooWorkspace *w_H2A4Mu = new RooWorkspace("w_H2A4Mu");
  const double       m_min  = 0.2113;
  const double       m_max  = 9.;
  const unsigned int m_bins = 220;
  RooRealVar m1("m1","m_{#mu#mu_{1}}",m_min,m_max,"GeV/#it{c}^{2}");
  RooRealVar m2("m2","m_{#mu#mu_{2}}",m_min,m_max,"GeV/#it{c}^{2}");
  m1.setBins(m_bins);
  m2.setBins(m_bins);
  w_H2A4Mu->import(m1);
  w_H2A4Mu->import(m2);

  //Signal Diagonal Area 
  RooGenericPdf dia1( "dia1", "generic PDF for diaginal region", "fabs(m1 - m2) < 5.*(0.026 + 0.013*(m1 + m2)/2.)", RooArgSet(m1,m2) );

  //Observed data in signal region
  Double_t massC;
  Double_t massF;
  TTree* tree_dimudimu_signal_2D = new TTree("tree_dimudimu_signal_2D","tree_dimudimu_signal_2D");
  tree_dimudimu_signal_2D->Branch("massC",&massC,"massC/D");
  tree_dimudimu_signal_2D->Branch("massF",&massF,"massF/D");
  massC = 100.; //BLINDED
  massF = 100.;
  tree_dimudimu_signal_2D->Fill();
  tree_dimudimu_signal_2D->Print();
  tree_dimudimu_signal_2D->GetBranch("massC")->SetName("m1");
  tree_dimudimu_signal_2D->GetBranch("massF")->SetName("m2");
  RooDataSet* ds_dimudimu_signal_2D = new RooDataSet( "ds_dimudimu_signal_2D","ds_dimudimu_signal_2D", tree_dimudimu_signal_2D, RooArgSet(m1,m2) );
  ds_dimudimu_signal_2D->Print("v");
  w_H2A4Mu->import(*ds_dimudimu_signal_2D, Rename("data_obs"));

  //Signal
  RooRealVar signal_mA("signal_mA", "signal_mA", mA_GeV);
  RooRealVar signal_sigma("signal_sigma", "signal_sigma", (0.13 + 0.065*mA_GeV)/5.0 );
  RooRealVar signal_alpha("signal_alpha", "signal_alpha", 1.75);
  RooRealVar signal_n("signal_n", "signal_n", 2.0);
  // Diagonal signal
  RooCBShape signal_m1("signal_m1", "signal_m1", m1,signal_mA,signal_sigma,signal_alpha,signal_n);
  w_H2A4Mu->import(signal_m1);
  RooCBShape signal_m2("signal_m2", "signal_m2", m2,signal_mA,signal_sigma,signal_alpha,signal_n);
  w_H2A4Mu->import(signal_m2);
  w_H2A4Mu->factory("PROD::signal(signal_m1,signal_m2)");
  //w_H2A4Mu->factory("EXPR::signal( 'signalAll*( fabs(m1-m2)<5.*(0.026+0.013*(m1+m2)/2.))',signalAll,m1,m2)");


  TFile* file = new TFile("../ws_FINAL.root");
  RooWorkspace *w = (RooWorkspace*) file->Get("w");
  //BB
  w_H2A4Mu->import( *w->pdf("template1D_m1") );
  w_H2A4Mu->import( *w->pdf("template1D_m2") );
  
  w_H2A4Mu->factory("PROD::template_2DAll( template1D_m1, template1D_m2 )");
  w_H2A4Mu->factory("EXPR::template_2D( 'template_2DAll*( fabs(m1-m2)<5.*(0.026+0.013*(m1+m2)/2.))+0.00000001',template_2DAll,m1,m2)");
  w_H2A4Mu->factory("PROD::BBbar_2DAll( template1D_m1, template1D_m2 )");
  w_H2A4Mu->factory("EXPR::BBbar_2D( 'BBbar_2DAll*( fabs(m1-m2)<5.*(0.026+0.013*(m1+m2)/2.))+0.00000001',BBbar_2DAll,m1,m2)");

  //2J/Psi
  w_H2A4Mu->import( *w->pdf("Jpsi_m1") );
  w_H2A4Mu->import( *w->pdf("Jpsi_m2") );
  w_H2A4Mu->factory("PROD::DJpsi_2D(Jpsi_m1,Jpsi_m2)");
  //w_H2A4Mu->factory("EXPR::DJpsi_2D( 'DJpsi_2DAll*( fabs(m1-m2)<5.*(0.026+0.013*(m1+m2)/2.))+0.00000001',DJpsi_2DAll,m1,m2)");

  // Set all fit variables to constants
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
  w_H2A4Mu->var("Jpsi_m1_alpha")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m1_mean")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m1_n")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m1_sigma")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m2_alpha")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m2_mean")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m2_n")->setConstant(true);
  w_H2A4Mu->var("Jpsi_m2_sigma")->setConstant(true);

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

  w_H2A4Mu->var("signal_mA")->setConstant(true);
  w_H2A4Mu->var("signal_n")->setConstant(true);
  w_H2A4Mu->var("signal_sigma")->setConstant(true);

  w_H2A4Mu->Print("v");
  TString ws_fileName = Form("../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root", mA_GeV);
  cout << "save work space to file: " << ws_fileName << endl;
  w_H2A4Mu->writeToFile(ws_fileName);
}

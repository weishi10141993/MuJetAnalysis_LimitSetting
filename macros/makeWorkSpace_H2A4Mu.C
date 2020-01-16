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

  if ( fabs(x1-x2) < 3*(0.003044 + 0.007025*(x1+x2)/2.0 + 0.000053*(x1+x2)*(x1+x2)/4.0) ) {
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

  const double       m_Jpsi_dn = 2.72;
  const double       m_Jpsi_up = 3.24;
  const unsigned int m_bins_below_Jpsi = 63;//bin size is ~0.04GeV, as above
  const unsigned int m_bins_above_Jpsi = 144;
  //RooRealVar m1("m1", "m_{#mu#mu_{1}}", m_min, m_max, "GeV");
  //RooRealVar m2("m2", "m_{#mu#mu_{2}}", m_min, m_max, "GeV");
  //m1.setBins(m_bins);
  //m2.setBins(m_bins);

  RooRealVar m1_below_Jpsi("m1_below_Jpsi", "m_{#mu#mu_{1}}", m_min, m_Jpsi_dn, "GeV");
  RooRealVar m2_below_Jpsi("m2_below_Jpsi", "m_{#mu#mu_{2}}", m_min, m_Jpsi_dn, "GeV");
  //RooRealVar m1_above_Jpsi("m1_above_Jpsi", "m_{#mu#mu_{1}}", m_Jpsi_up, m_max, "GeV");
  //RooRealVar m2_above_Jpsi("m2_above_Jpsi", "m_{#mu#mu_{2}}", m_Jpsi_up, m_max, "GeV");
  m1_below_Jpsi.setBins(m_bins_below_Jpsi);
  m2_below_Jpsi.setBins(m_bins_below_Jpsi);
  //m1_above_Jpsi.setBins(m_bins_above_Jpsi);
  //m2_above_Jpsi.setBins(m_bins_above_Jpsi);

  //w_H2A4Mu->import(m1);
  //w_H2A4Mu->import(m2);
  w_H2A4Mu->import(m1_below_Jpsi);
  w_H2A4Mu->import(m2_below_Jpsi);
  //w_H2A4Mu->import(m1_above_Jpsi);
  //w_H2A4Mu->import(m2_above_Jpsi);

  //Signal Diagonal Area in 2017 and 2018
  RooGenericPdf dia( "dia", "generic PDF for diaginal region", "fabs(m1_below_Jpsi-m2_below_Jpsi) < 3*(0.003044 + 0.007025*(m1_below_Jpsi+m2_below_Jpsi)/2.0 + 0.000053*(m1_below_Jpsi+m2_below_Jpsi)*(m1_below_Jpsi+m2_below_Jpsi)/4.0)", RooArgSet(m1_below_Jpsi, m2_below_Jpsi) );
  w_H2A4Mu->import(dia);

  //Observed data in signal region
  Double_t massC, massF;
  TTree* tree_dimudimu_signal_2D = new TTree("tree_dimudimu_signal_2D", "tree_dimudimu_signal_2D");
  tree_dimudimu_signal_2D->Branch("massC", &massC, "massC/D");
  tree_dimudimu_signal_2D->Branch("massF", &massF, "massF/D");
  //BLINDED DATA
  massC = 100.;
  massF = 100.;

  /*
  //===================
  //2016 Data Unblinded
  //===================
  // massC =0.8079733;   massF = 0.7267103; tree_dimudimu_signal_2D->Fill();
  massC =2.8599584;   massF = 3.0017674; tree_dimudimu_signal_2D->Fill();
  // massC =0.4258973;   massF = 0.5848349; tree_dimudimu_signal_2D->Fill();
  // massC =3.0722196;   massF = 3.2662851; tree_dimudimu_signal_2D->Fill();
  massC =3.0728187;   massF = 3.0538983; tree_dimudimu_signal_2D->Fill();
  // massC =3.0950253;   massF = 3.3617882; tree_dimudimu_signal_2D->Fill();
  massC =3.1521356;   massF = 2.8546791; tree_dimudimu_signal_2D->Fill();
  massC =2.8254406;   massF = 2.6496100; tree_dimudimu_signal_2D->Fill();
  massC =1.2541753;   massF = 1.1524148; tree_dimudimu_signal_2D->Fill();
  massC =2.3863873;   massF = 2.3582603; tree_dimudimu_signal_2D->Fill();
  massC =3.0641751;   massF = 3.0972354; tree_dimudimu_signal_2D->Fill();
  massC =1.9403913;   massF = 1.8196427; tree_dimudimu_signal_2D->Fill();
  massC =1.3540757;   massF = 1.4834892; tree_dimudimu_signal_2D->Fill();
  */

  //===================
  //2017 Data Unblinded
  //===================
  //TBD

  //===================
  //2018 Data Unblinded
  //===================
  //TBD

  cout<<"--- PRINT tree_dimudimu_signal_2D ---"<<endl;
  tree_dimudimu_signal_2D->Print();
  cout<<"-------------------------------------"<<endl;
  tree_dimudimu_signal_2D->GetBranch("massC")->SetName("m1_below_Jpsi");
  tree_dimudimu_signal_2D->GetBranch("massF")->SetName("m2_below_Jpsi");
  RooDataSet* ds_dimudimu_signal_2D = new RooDataSet( "ds_dimudimu_signal_2D","ds_dimudimu_signal_2D", tree_dimudimu_signal_2D, RooArgSet(m1_below_Jpsi, m2_below_Jpsi) );
  cout<<"--- PRINT ds_dimudimu_signal_2D ---"<<endl;
  ds_dimudimu_signal_2D->Print("v");
  cout<<"-------------------------------------"<<endl;
  w_H2A4Mu->import(*ds_dimudimu_signal_2D, Rename("data_obs"));

  //Signal parameteres
  RooRealVar signal_mA("signal_mA", "signal_mA", mA_GeV);
  RooRealVar signal_sigma("signal_sigma", "signal_sigma", 0.003044 + 0.007025*mA_GeV + 0.000053*mA_GeV*mA_GeV );
  RooRealVar signal_alpha("signal_alpha", "signal_alpha", 1.75);
  RooRealVar signal_n("signal_n", "signal_n", 2.0);
  //Signal Shape
  RooCBShape signal_m1("signal_m1", "signal_m1", m1_below_Jpsi, signal_mA, signal_sigma, signal_alpha, signal_n);
  w_H2A4Mu->import(signal_m1);
  RooCBShape signal_m2("signal_m2", "signal_m2", m2_below_Jpsi, signal_mA, signal_sigma, signal_alpha, signal_n);
  w_H2A4Mu->import(signal_m2);
  w_H2A4Mu->factory("PROD::signal(signal_m1, signal_m2)");

  TFile* file = new TFile("../ws_FINAL.root");
  RooWorkspace *w = (RooWorkspace*) file->Get("w");
  w_H2A4Mu->import( *w->pdf("template1D_m1_below_Jpsi") );
  w_H2A4Mu->import( *w->pdf("template1D_m2_below_Jpsi") );
  w_H2A4Mu->factory("PROD::BBbar_below_Jpsi_2D(template1D_m1_below_Jpsi, template1D_m2_below_Jpsi )*dia");
  //w_H2A4Mu->import( *w->pdf("template1D_m1_above_Jpsi") );
  //w_H2A4Mu->import( *w->pdf("template1D_m2_above_Jpsi") );
  //w_H2A4Mu->factory("PROD::BBbar_above_Jpsi_2D(template1D_m1_above_Jpsi, template1D_m2_above_Jpsi )*dia");

  // Set all fit variables to constants
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
/*
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
  w_H2A4Mu->var("norm_psiF_above_Jpsi")->setConstant(true);*/

  w_H2A4Mu->var("signal_mA")->setConstant(true);
  w_H2A4Mu->var("signal_n")->setConstant(true);
  w_H2A4Mu->var("signal_sigma")->setConstant(true);

  cout<<"---------------WORKING-SPACE----------------"<<endl;
  w_H2A4Mu->Print("v");
  TString ws_fileName = Form("../workSpaces/ws_H2A4Mu_mA_%.4f_GeV.root", mA_GeV);
  cout << "save work space to file: " << ws_fileName << endl;
  w_H2A4Mu->writeToFile(ws_fileName);
}

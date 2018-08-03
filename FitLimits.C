#include <stdio.h>
#include <TH1F.h>
#include <TFile.h>
#include <TMath.h>
#include <TCanvas.h>
#include <TH2F.h>
#include <TH1D.h>
#include <TF1.h>
#include <TGraph.h>
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
#include "RooGaussian.h"
#include "RooChebychev.h"
#include "RooPolynomial.h"
#include "RooDataHist.h"
#include "RooAbsPdf.h"
#include "RooAddPdf.h"
#include "RooArgSet.h"
#include "RooArgList.h"
#include "RooPlot.h"
#include "RooFitResult.h"
#include "RooNLLVar.h"
#include "RooChi2Var.h"
#include "RooMinuit.h"
#include "RooRealVar.h"
#include "RooGenericPdf.h"
using namespace RooFit;

void FitLimits(){
  TCanvas *c1 = new TCanvas("c1","");
  gStyle->SetOptStat(111111);
  // Get limit Tgraph
  TString LimitFile = "plots/C/limit_Events_vs_mGammaD_2016.root";
  float NoevIs = 3.205;//2.8;
  //float NoevIs = 2.4; //90% cl
  //TString LimitFile = "Real_Limits.root";
  TFile *f = new TFile(LimitFile.Data());
  TGraph *graph = (TGraph*) f->Get("Graph");
  auto nPoints = graph->GetN();
  // Convert in Th1F
  double xMin, ytmp, bin=100;
  graph->GetPoint(0, xMin, ytmp);
  double xMax;
  graph->GetPoint(nPoints-1, xMax, ytmp);
  TH1F *h = new TH1F("h", "", bin, xMin, xMax);
  float step = (xMax-xMin)/bin;
  for(int i=0; i < nPoints; ++i) {
     double x, y;
     graph->GetPoint(i, x, y);
     int BinToFill = int((x-xMin)/step);
     h->SetBinContent(BinToFill+1, x, y);
  }
  for(int i=0; i < h->GetNbinsX(); ++i) {
    if( h->GetBinContent(i+1) < 2. ){
	h->SetBinContent(i+1,NoevIs);
    }
    h->SetBinError(i+1,0.3);
  }
  h->Draw();
  c1->SaveAs("plots/h.pdf");
  // Create RooDataHist
  RooRealVar x("x", "m(a)", 0.2113, 9., "GeV/c^2");
  RooDataHist dh("dh", "", RooArgList(x), h);
  // Parameters
  RooRealVar co("co", "co", NoevIs, NoevIs-0.03, NoevIs+0.03,"");
  RooGenericPdf p0("p0","","x*0.0000001 + co",RooArgSet(x,co));
  RooRealVar mean1("mean1", "mean",    0.55,  0.5,  0.6,"GeV/c^{2}");
  RooRealVar sigma1("sigma1", "sigma", 0.07, 0.04, 0.1,"GeV/c^{2}");
  RooGaussian gaus1("gaus1","Gaussian",x, mean1,sigma1);
  RooRealVar mean2("mean2", "mean",    0.95,  0.7,   1.,"GeV/c^{2}");
  RooRealVar sigma2("sigma2", "sigma", 0.04, 0.035, 0.1,"GeV/c^{2}");
  RooGaussian gaus2("gaus2","Gaussian",x, mean2,sigma2);
  RooRealVar mean3("mean3", "mean",    1.18,  1.15,   1.2,"GeV/c^{2}");
  RooRealVar sigma3("sigma3", "sigma", 0.035, 0.033, 0.1,"GeV/c^{2}");
  RooGaussian gaus3("gaus3","Gaussian",x, mean3,sigma3);
  RooRealVar mean4("mean4", "mean",    1.5,  1.4,   1.6,"GeV/c^{2}");
  RooRealVar sigma4("sigma4", "sigma", 0.04, 0.03, 0.1,"GeV/c^{2}");
  RooGaussian gaus4("gaus4","Gaussian",x, mean4,sigma4);
  RooRealVar mean5("mean5", "mean",    1.8,  1.75,   2.1,"GeV/c^{2}");
  RooRealVar sigma5("sigma5", "sigma", 0.08, 0.05, 0.1,"GeV/c^{2}");
  RooGaussian gaus5("gaus5","Gaussian",x, mean5,sigma5);
  RooRealVar mean6("mean6", "mean",    2.4,  2.3,   2.5,"GeV/c^{2}");
  RooRealVar sigma6("sigma6", "sigma", 0.07, 0.038, 0.1,"GeV/c^{2}");
  RooGaussian gaus6("gaus6","Gaussian",x, mean6,sigma6);
  RooRealVar mean7("mean7", "mean",    2.9,  2.8,   2.999,"GeV/c^{2}");
  RooRealVar sigma7("sigma7", "sigma", 0.05, 0.004, 0.2,"GeV/c^{2}");
  RooGaussian gaus7("gaus7","Gaussian",x, mean7,sigma7);
  RooRealVar mean8("mean8", "mean",    3.1,  3.,   3.2,"GeV/c^{2}");
  RooRealVar sigma8("sigma8", "sigma", 0.12, 0.07, 0.2,"GeV/c^{2}");
  RooGaussian gaus8("gaus8","Gaussian",x, mean8,sigma8);
  RooRealVar N0("N0","yield",291,100.,400.);
  RooRealVar N1("N1","yield",0.1,0.01,6.0);
  RooRealVar N2("N2","yield",2.0,0.5,6.0);
  RooRealVar N3("N3","yield",1.0,0.1,3.);
  RooRealVar N4("N4","yield",1.0,0.1,1.8);
  RooRealVar N5("N5","yield",6.0,0.1,9.0);
  RooRealVar N6("N6","yield",1.9,1.5,2.5);
  RooRealVar N7("N7","yield",0.4,0.2,10.0);
  RooRealVar N8("N8","yield",10.,7.0,18.);
  RooAddPdf model("model","model",RooArgList(p0,gaus1,gaus2,gaus3,gaus4,gaus5,gaus6,gaus7,gaus8),RooArgList(N0,N1,N2,N3,N4,N5,N6,N7,N8));
  RooAbsPdf* MyModel = &model;
  RooNLLVar nll("nll","log likelihood var",*MyModel,dh, RooFit::Extended(true));
  RooMinuit m(nll);
  m.setVerbose(kFALSE);
  m.migrad();

  //x.setRange("sobRange1",mean1.getVal()-3.*sigma1.getVal(), mean1.getVal()+3.*sigma1.getVal());
  //RooAbsReal* integral1 = gaus1.createIntegral(x,NormSet(x),Range("sobRange"));
  //float norm1 = integral1->getVal();
  //cout<<integral1->getVal()<<"  ->  "<<N1.getVal()*norm1<<"*exp(-0.5*((m-"<<mean1.getVal()<<")/"<<sigma1.getVal()<<")**2) + "<<endl;
  cout<<"RESULTS:"<<endl;
  cout<<N1.getVal()<<"*exp(-0.5*((m-"<<mean1.getVal()<<")/"<<sigma1.getVal()<<")**2) + \\"<<endl;
  cout<<N2.getVal()<<"*exp(-0.5*((m-"<<mean2.getVal()<<")/"<<sigma2.getVal()<<")**2) + \\"<<endl;
  cout<<N3.getVal()<<"*exp(-0.5*((m-"<<mean3.getVal()<<")/"<<sigma3.getVal()<<")**2) + \\"<<endl;
  cout<<N4.getVal()<<"*exp(-0.5*((m-"<<mean4.getVal()<<")/"<<sigma4.getVal()<<")**2) + \\"<<endl;
  cout<<N5.getVal()<<"*exp(-0.5*((m-"<<mean5.getVal()<<")/"<<sigma5.getVal()<<")**2) + \\"<<endl;
  cout<<N6.getVal()<<"*exp(-0.5*((m-"<<mean6.getVal()<<")/"<<sigma6.getVal()<<")**2) + \\"<<endl;
  cout<<N7.getVal()<<"*exp(-0.5*((m-"<<mean7.getVal()<<")/"<<sigma7.getVal()<<")**2) + \\"<<endl;
  cout<<N8.getVal()<<"*exp(-0.5*((m-"<<mean8.getVal()<<")/"<<sigma8.getVal()<<")**2)"<<endl;
  RooPlot* xframe = x.frame(h->GetNbinsX());
  xframe->SetTitle(h->GetTitle());
  dh.plotOn(xframe);
  MyModel->plotOn(xframe,Components(p0),LineStyle(kDashed), LineColor(kRed));
  MyModel->plotOn(xframe);
  xframe->Draw();
  c1->SaveAs("plots/h_fit.pdf");
}

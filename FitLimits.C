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

void FitLimits(){

  TCanvas *c1 = new TCanvas("c1","");
  //Parameters
  TString LimitFile = "plots/C/limit_Events_vs_mGammaD_2015.root";
  TFile *f = new TFile(LimitFile.Data());
  TGraph *graph = (TGraph*) f->Get("Graph");
  //Gauss + constant
  //TF1 *func = new TF1("func","[0]*exp(-0.5*((x-[1])/[2])**2)+[3]",0.223,8.5);
  //func->SetParName(0,"gaus_norm");
  //func->SetParName(1,"gaus_mu");
  //func->SetParName(2,"gaus_sigma");
  //func->SetParName(3,"y");
  //func->SetParLimits(0, 1, 1);
  //func->SetParLimits(1, 0.55, 0.55);
  //func->SetParLimits(2, 0.1, 0.1);
  //func->SetParLimits(3, 3, 3.1);
  //TF1 *func = new TF1("func","0.23*exp(-0.5*((x-0.45)/0.15)**2) + 0.2*exp(-0.5*((x-0.85)/0.15)**2) + 0.1*exp(-0.5*((x-1.1)/0.5)**2) + 3.05 + 1.5*exp(-0.5*((x-3.1)/0.05)**2)",0.223,8.5);
  TF1 *func = new TF1("func","0.13*exp(-0.5*((x-0.4)/0.13)**2)+ 3.03",0.223,8.5);
  //graph->Fit("func");
  graph->SetMinimum(2);
  graph->SetMaximum(4);
  graph->Draw();
  func->Draw("same");
  c1->SaveAs("plots/fit.pdf");
}

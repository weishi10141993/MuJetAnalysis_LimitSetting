import ROOT, array, os, re, math, random
from math import *

execfile("scripts/tdrStyle.py")
execfile("scripts/fSetPalette.py")
execfile("scripts/fRange.py")
execfile("scripts/CmsLimitVsM.py")
execfile("scripts/SMHiggsCrossSections.py")
execfile("scripts/DarkPhotonWidths_and_Branchings.py")
execfile("scripts/R_Hadrons.py")
execfile("scripts/CmsDarkSusyAcceptance.py")
execfile("scripts/CmsNmssmAcceptance.py")
#NMSSM specific functions
execfile("scripts/NMSSM_Br_a_Function.py")

cnv = ROOT.TCanvas("cnv", "cnv")
cnv.SetCanvasSize(900,900)

txtHeader = ROOT.TLegend(.15,.935,0.97,1.)
txtHeader.SetFillColor(ROOT.kWhite)
txtHeader.SetFillStyle(0)
txtHeader.SetBorderSize(0)
txtHeader.SetTextFont(42)
txtHeader.SetTextSize(0.045)
txtHeader.SetTextAlign(22)
txtHeader.SetHeader("#bf{CMS Prelim. 2015}          2.83 fb^{-1} (13 TeV)")
#txtHeader.Draw()

l_CMS = ROOT.TLegend(0.6,0.8,0.9,0.95)
l_CMS.SetFillColor(ROOT.kWhite)
l_CMS.SetFillStyle(4050)
l_CMS.SetBorderSize(0)
l_CMS.SetTextFont(61)
l_CMS.SetTextSize(0.055)
l_CMS.SetTextAlign(22)
l_CMS.SetTextColor(ROOT.kBlack)
l_CMS.SetHeader("CMS Preliminary")

l_CMSLumi = ROOT.TLegend(0.6,0.68,0.9,0.95)
l_CMSLumi.SetFillColor(ROOT.kWhite)
l_CMSLumi.SetFillStyle(4050)
l_CMSLumi.SetBorderSize(0)
l_CMSLumi.SetTextFont(42)
l_CMSLumi.SetTextSize(0.042)
l_CMSLumi.SetTextAlign(22)
l_CMSLumi.SetTextColor(ROOT.kBlack)
l_CMSLumi.SetHeader("2.83 fb^{-1} (13 TeV)")

lumi_fbinv = 2.83 # fb-1
lumi_pbinv = 1000.*lumi_fbinv # pb-1
SF = 0.92 # eFullData / eFullMc
eFullMc_over_aGen = 0.68

mGammaD_GeV = [0.25, 0.40, 0.55, 0.70, 0.85, 1.00]
mGammaD_GeV_bot = 0.00 # low boundary where histograms start in m
mGammaD_GeV_min = 0.25
mGammaD_GeV_max = 2.00
mGammaD_GeV_top = 10.0 # high boundary where histograms stops in m

ctau_mm = [0.0, 0.2, 0.5, 2.0, 5.0]
ctau_mm_bot = -0.5
ctau_mm_min =  0.0
ctau_mm_max =  5.0
ctau_mm_top =  5.5
c_hbar_mm_GeV = 1.974*pow(10.0, -13) # c = 3*10^11 mm/s; hbar = 6.58*10^-25 GeV*sec

epsilon2_min  = 0.000000000001
epsilon2_max  = 0.0001
epsilon2_bins = 1000
logEpsilon2_min = -12.1
logEpsilon2_max =  -7.9

################################################################################
#       Plot Upper 95% CL Limit on number of events: 0.25 < mGammaD < 1.0       
################################################################################

def limit_vs_mGammaD_2015():
  print "------------limit_vs_mGammaD_2015------------"
  cnv.SetLogy(0)
  padTop = ROOT.TPad( "padTop", "padTop", 0.0, 0.3, 1.0, 1.0 )
  padTop.Draw()
  padTop.cd()
  array_mGammaD_limit = []
  array_mGammaD_limit_T5000 = []
  array_mGammaD_limit_T5000_error = []
  rnd = ROOT.TRandom()
  rnd.SetSeed(2015)
  
  for m in MGammaD_array: # MGammaD_array = Array with all masses consdered
    # FIT
    array_mGammaD_limit.append(( m, fCmsLimitVsM(m) )) # fCmsLimitVsM(m) retrieve the limit as a function of m. In the simplest case is a constant and retireve 3.08 always.
    # Point
    array_mGammaD_limit_T5000.append(( m, fCmsLimitVsM_HybridNew(m) )) # fCmsLimitVsM_HybridNew(m) retireve the limit from toys experiments.
    array_mGammaD_limit_T5000_error.append(( m, (fCmsLimitVsM_HybridNew(m) - fCmsLimitVsM(m) ) / fCmsLimitVsM(m) )) # Error is the difference between fit and toy limit

  h_limit_vs_mGammaD_dummy = ROOT.TH2F("h_limit_vs_mGammaD_dummy", "h_limit_vs_mGammaD_dummy", 1000, 0.0, 9.0, 1000, 0.0, 6.0)
  h_limit_vs_mGammaD_dummy.SetXTitle("m_{a} [GeV/#it{c}^{2}]")
  h_limit_vs_mGammaD_dummy.SetYTitle("95% CL upper limit on N_{evt}")
  h_limit_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_limit_vs_mGammaD_dummy.GetXaxis().SetNdivisions(505)
  h_limit_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_limit_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  h_limit_vs_mGammaD_dummy.Draw()
  
  gr_limit_vs_mGammaD_T5000 = ROOT.TGraph( len(array_mGammaD_limit_T5000), array.array("d", zip(*array_mGammaD_limit_T5000)[0]), array.array("d", zip(*array_mGammaD_limit_T5000)[1]) )
  gr_limit_vs_mGammaD_T5000.SetLineWidth(1)
  gr_limit_vs_mGammaD_T5000.SetLineColor(ROOT.kGreen)
  gr_limit_vs_mGammaD_T5000.SetLineStyle(1)
  gr_limit_vs_mGammaD_T5000.Draw("P")
 
  gr_limit_vs_mGammaD = ROOT.TGraph( len(array_mGammaD_limit), array.array("d", zip(*array_mGammaD_limit)[0]), array.array("d", zip(*array_mGammaD_limit)[1]) )
  gr_limit_vs_mGammaD.SetLineWidth(1)
  gr_limit_vs_mGammaD.SetLineColor(ROOT.kRed)
  gr_limit_vs_mGammaD.SetLineStyle(1)
  gr_limit_vs_mGammaD.SetMarkerColor(ROOT.kRed)
  gr_limit_vs_mGammaD.Draw("L")

  l_limit_vs_mGammaD = ROOT.TLegend(0.63,0.65,0.9,0.75)
  l_limit_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_limit_vs_mGammaD.SetMargin(0.13)
  l_limit_vs_mGammaD.SetBorderSize(0)
  l_limit_vs_mGammaD.SetTextFont(42)
  l_limit_vs_mGammaD.SetTextSize(0.035)
  l_limit_vs_mGammaD.AddEntry(gr_limit_vs_mGammaD_T5000,"Toys","L")
  l_limit_vs_mGammaD.AddEntry(gr_limit_vs_mGammaD,"Fit","L")
  l_limit_vs_mGammaD.Draw()
  l_CMS.Draw()
  l_CMSLumi.Draw()
  cnv.cd()
  # Now Draw Errors
  padBot = ROOT.TPad( "padBot", "padBot", 0.0, 0.0, 1.0, 0.3 )
  padBot.Draw()
  padBot.cd()
  padBot.SetGrid()
  h_limit_vs_mGammaD_error_dummy = ROOT.TH2F("h_limit_vs_mGammaD_error_dummy", "h_limit_vs_mGammaD_error_dummy", 1000, 0.0, 9.0, 1000, -1.0, 1.0)
  h_limit_vs_mGammaD_error_dummy.SetXTitle("m_{a} [GeV/#it{c}^{2}]")
  h_limit_vs_mGammaD_error_dummy.SetYTitle("Fit Uncertainty [%]")
  h_limit_vs_mGammaD_error_dummy.SetTitleOffset(1.1, "Y")
  h_limit_vs_mGammaD_error_dummy.GetXaxis().SetNdivisions(505)
  h_limit_vs_mGammaD_error_dummy.GetYaxis().CenterTitle(1)
  h_limit_vs_mGammaD_error_dummy.GetYaxis().SetTitleSize(0.06)
  h_limit_vs_mGammaD_error_dummy.Draw()
  
  gr_limit_vs_mGammaD_T5000_error = ROOT.TGraph( len(array_mGammaD_limit_T5000_error), array.array("d", zip(*array_mGammaD_limit_T5000_error)[0]), array.array("d", zip(*array_mGammaD_limit_T5000_error)[1]) )
  gr_limit_vs_mGammaD_T5000_error.SetLineWidth(1)
  gr_limit_vs_mGammaD_T5000_error.SetLineColor(ROOT.kGreen)
  gr_limit_vs_mGammaD_T5000_error.SetLineStyle(1)
  gr_limit_vs_mGammaD_T5000_error.Draw("L") 

  cnv.cd()
  cnv.Update()
  cnv.SaveAs("plots/PDF/limit_Events_vs_mGammaD_2015_FitUncert.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_Events_vs_mGammaD_2015_FitUncert.pdf -resize 900x900 plots/PNG/limit_Events_vs_mGammaD_2015_FitUncert.png")

  # Now same plots with no errors
  cnv.cd()
  h_limit_vs_mGammaD_dummy.Draw()
  gr_limit_vs_mGammaD_T5000.Draw("P")
  gr_limit_vs_mGammaD.Draw("L")
  l_CMS.Draw()
  l_CMSLumi.Draw()
  
  cnv.Update()
  cnv.SaveAs("plots/PDF/limit_Events_vs_mGammaD_2015.pdf")
  gr_limit_vs_mGammaD_T5000.SaveAs("plots/C/limit_Events_vs_mGammaD_2015.root")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_Events_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/limit_Events_vs_mGammaD_2015.png")
  
################################################################################
#       Plot Upper 95% CL Limit on CSxBR2xAlpha = "Limit on number of events"/Luminosity/"Scale factor"
################################################################################
def limit_CSxBR2xAlpha_fb_vs_mGammaD_2015():
  cnv.SetLogy(0)
  array_mGammaD_limit_CSxBR2xAlpha_fb = []
  for m in fRange(0.25, 8.5, 201):
    array_mGammaD_limit_CSxBR2xAlpha_fb.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/eFullMc_over_aGen )) # Transforming the Limit on N_event to Xsec limit

  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy = ROOT.TH2F("h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy", "h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy", 1000, 0.0, 9.0, 1000, 0.0, 6.0/lumi_fbinv/SF/eFullMc_over_aGen)
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.SetXTitle("m_{a} [GeV/#it{c}^{2}]")
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.SetYTitle("#sigma(pp #rightarrow 2a + X) B^{2}(a #rightarrow 2 #mu) #alpha_{gen} [fb]")
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.SetTitleOffset(1.35, "Y")
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.GetXaxis().SetNdivisions(505);
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  h_limit_CSxBR2xAlpha_fb_vs_mGammaD_dummy.Draw()

  gr_limit_CSxBR2xAlpha_fb_vs_mGammaD = ROOT.TGraph( len(array_mGammaD_limit_CSxBR2xAlpha_fb), array.array("d", zip(*array_mGammaD_limit_CSxBR2xAlpha_fb)[0]), array.array("d", zip(*array_mGammaD_limit_CSxBR2xAlpha_fb)[1]) )
  gr_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetLineWidth(2)
  gr_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetLineColor(ROOT.kRed)
  gr_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetLineStyle(1)
  gr_limit_CSxBR2xAlpha_fb_vs_mGammaD.Draw("C")

  l_limit_CSxBR2xAlpha_fb_vs_mGammaD = ROOT.TLegend(0.6,0.65,0.9,0.75)
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetMargin(0.13)
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetBorderSize(0)
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetTextFont(42)
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.SetTextSize(0.035)
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2xAlpha_fb_vs_mGammaD,"95% CL upper limit","L")
  l_limit_CSxBR2xAlpha_fb_vs_mGammaD.Draw()
  l_CMS.Draw()
  l_CMSLumi.Draw()

  cnv.SaveAs("plots/PDF/limit_CSxBR2xAlpha_fb_vs_mGammaD_2015.pdf")
  cnv.SaveAs("plots/C/limit_CSxBR2xAlpha_fb_vs_mGammaD_2015.C")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CSxBR2xAlpha_fb_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/limit_CSxBR2xAlpha_fb_vs_mGammaD_2015.png")

################################################################################
#           Plot acceptance Alpha vs mGammaD: 0.25 < mGammaD < 1.0              
################################################################################

def Alpha_vs_mGammaD_2015():
  print "------------Alpha_vs_mGammaD_2015------------"
  cnv.SetLogy(0)
  array_Alpha_vs_mGammaD_ctau0mm_LinearFit  = []
  array_Alpha_vs_mGammaD_ctau02mm_LinearFit = []
  array_Alpha_vs_mGammaD_ctau05mm_LinearFit = []
  array_Alpha_vs_mGammaD_ctau2mm_LinearFit  = []
  array_Alpha_vs_mGammaD_ctau5mm_LinearFit  = []
  for m_GeV in fRange(0.25, 8.5, 100):
    array_Alpha_vs_mGammaD_ctau0mm_LinearFit.append((  m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.0, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau02mm_LinearFit.append(( m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.2, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau05mm_LinearFit.append(( m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.5, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau2mm_LinearFit.append((  m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 2.0, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau5mm_LinearFit.append((  m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 5.0, m_GeV ) ))
  array_Alpha_vs_mGammaD_ctau0mm_Marker  = []
  array_Alpha_vs_mGammaD_ctau02mm_Marker = []
  array_Alpha_vs_mGammaD_ctau05mm_Marker = []
  array_Alpha_vs_mGammaD_ctau2mm_Marker  = []
  array_Alpha_vs_mGammaD_ctau5mm_Marker  = []
  array_Alpha_vs_mGammaD_ctau0mm_Marker.append((    0.25,  100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.0, 0.25  ) ))
  array_Alpha_vs_mGammaD_ctau0mm_Marker.append((    0.4,   100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.0, 0.4   ) ))
  for m_GeV in mGammaD_GeV:
    array_Alpha_vs_mGammaD_ctau02mm_Marker.append(( m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.2, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau05mm_Marker.append(( m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.5, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau2mm_Marker.append((  m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 2.0, m_GeV ) ))
    array_Alpha_vs_mGammaD_ctau5mm_Marker.append((  m_GeV, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 5.0, m_GeV ) ))
  
  h_Alpha_vs_mGammaD_dummy = ROOT.TH2F("h_Alpha_vs_mGammaD_dummy", "h_Alpha_vs_mGammaD_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 0.0, 25.0)
  h_Alpha_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_Alpha_vs_mGammaD_dummy.SetYTitle("#alpha (c#tau_{#gamma_{D}}, m_{#gamma_{D}}) [%]")
  h_Alpha_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_Alpha_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_Alpha_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  h_Alpha_vs_mGammaD_dummy.Draw()
  
  gr_Alpha_vs_mGammaD_ctau0mm = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau0mm_LinearFit), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau0mm_LinearFit)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau0mm_LinearFit)[1]) )
  gr_Alpha_vs_mGammaD_ctau0mm.SetLineWidth(2)
  gr_Alpha_vs_mGammaD_ctau0mm.SetLineColor(ROOT.kBlue)
  gr_Alpha_vs_mGammaD_ctau0mm.SetLineStyle(2)
  gr_Alpha_vs_mGammaD_ctau0mm.Draw("C")
  
  gr_Alpha_vs_mGammaD_ctau0mm_Marker = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau0mm_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau0mm_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau0mm_Marker)[1]) )
  gr_Alpha_vs_mGammaD_ctau0mm_Marker.SetMarkerColor(ROOT.kBlue)
  gr_Alpha_vs_mGammaD_ctau0mm_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_mGammaD_ctau0mm_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_mGammaD_ctau0mm_Marker.Draw("P")
  
  gr_Alpha_vs_mGammaD_ctau02mm = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau02mm_LinearFit), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau02mm_LinearFit)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau02mm_LinearFit)[1]) )
  gr_Alpha_vs_mGammaD_ctau02mm.SetLineWidth(2)
  gr_Alpha_vs_mGammaD_ctau02mm.SetLineColor(ROOT.kGreen+2)
  gr_Alpha_vs_mGammaD_ctau02mm.SetLineStyle(9)
  gr_Alpha_vs_mGammaD_ctau02mm.Draw("C")
  
  gr_Alpha_vs_mGammaD_ctau02mm_Marker = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau02mm_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau02mm_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau02mm_Marker)[1]) )
  gr_Alpha_vs_mGammaD_ctau02mm_Marker.SetMarkerColor(ROOT.kGreen+2)
  gr_Alpha_vs_mGammaD_ctau02mm_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_mGammaD_ctau02mm_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_mGammaD_ctau02mm_Marker.Draw("P")

  gr_Alpha_vs_mGammaD_ctau05mm = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau05mm_LinearFit), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau05mm_LinearFit)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau05mm_LinearFit)[1]) )
  gr_Alpha_vs_mGammaD_ctau05mm.SetLineWidth(2)
  gr_Alpha_vs_mGammaD_ctau05mm.SetLineColor(ROOT.kRed)
  gr_Alpha_vs_mGammaD_ctau05mm.SetLineStyle(1)
  gr_Alpha_vs_mGammaD_ctau05mm.Draw("C")
  
  gr_Alpha_vs_mGammaD_ctau05mm_Marker = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau05mm_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau05mm_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau05mm_Marker)[1]) )
  gr_Alpha_vs_mGammaD_ctau05mm_Marker.SetMarkerColor(ROOT.kRed)
  gr_Alpha_vs_mGammaD_ctau05mm_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_mGammaD_ctau05mm_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_mGammaD_ctau05mm_Marker.Draw("P")
  
  gr_Alpha_vs_mGammaD_ctau2mm = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau2mm_LinearFit), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau2mm_LinearFit)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau2mm_LinearFit)[1]) )
  gr_Alpha_vs_mGammaD_ctau2mm.SetLineWidth(2)
  gr_Alpha_vs_mGammaD_ctau2mm.SetLineColor(ROOT.kMagenta)
  gr_Alpha_vs_mGammaD_ctau2mm.SetLineStyle(10)
  gr_Alpha_vs_mGammaD_ctau2mm.Draw("C")
  
  gr_Alpha_vs_mGammaD_ctau2mm_Marker = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau2mm_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau2mm_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau2mm_Marker)[1]) )
  gr_Alpha_vs_mGammaD_ctau2mm_Marker.SetMarkerColor(ROOT.kMagenta)
  gr_Alpha_vs_mGammaD_ctau2mm_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_mGammaD_ctau2mm_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_mGammaD_ctau2mm_Marker.Draw("P")
  
  gr_Alpha_vs_mGammaD_ctau5mm = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau5mm_LinearFit), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau5mm_LinearFit)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau5mm_LinearFit)[1]) )
  gr_Alpha_vs_mGammaD_ctau5mm.SetLineWidth(2)
  gr_Alpha_vs_mGammaD_ctau5mm.SetLineColor(ROOT.kCyan)
  gr_Alpha_vs_mGammaD_ctau5mm.SetLineStyle(8)
  gr_Alpha_vs_mGammaD_ctau5mm.Draw("C")
  
  gr_Alpha_vs_mGammaD_ctau5mm_Marker = ROOT.TGraph( len(array_Alpha_vs_mGammaD_ctau5mm_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau5mm_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau5mm_Marker)[1]) )
  gr_Alpha_vs_mGammaD_ctau5mm_Marker.SetMarkerColor(ROOT.kCyan)
  gr_Alpha_vs_mGammaD_ctau5mm_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_mGammaD_ctau5mm_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_mGammaD_ctau5mm_Marker.Draw("P")
  
  l_Alpha_vs_mGammaD = ROOT.TLegend(0.25,0.6,0.6,0.9)
  l_Alpha_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_Alpha_vs_mGammaD.SetMargin(0.4)
  l_Alpha_vs_mGammaD.SetBorderSize(0)
  l_Alpha_vs_mGammaD.SetTextFont(42)
  l_Alpha_vs_mGammaD.SetTextSize(0.035)
  l_Alpha_vs_mGammaD.SetHeader("Acceptance for samples with #gamma_{D} life-time:")
  l_Alpha_vs_mGammaD.AddEntry(gr_Alpha_vs_mGammaD_ctau0mm, "c#tau_{#gamma_{D}} =   0 mm (prompt)","L")
  l_Alpha_vs_mGammaD.AddEntry(gr_Alpha_vs_mGammaD_ctau02mm,"c#tau_{#gamma_{D}} = 0.2 mm","L")
  l_Alpha_vs_mGammaD.AddEntry(gr_Alpha_vs_mGammaD_ctau05mm,"c#tau_{#gamma_{D}} = 0.5 mm","L")
  l_Alpha_vs_mGammaD.AddEntry(gr_Alpha_vs_mGammaD_ctau2mm, "c#tau_{#gamma_{D}} =   2 mm","L")
  l_Alpha_vs_mGammaD.AddEntry(gr_Alpha_vs_mGammaD_ctau5mm, "c#tau_{#gamma_{D}} =   5 mm","L")
  l_Alpha_vs_mGammaD.Draw()
  txtHeader.Draw()

  cnv.SaveAs("plots/PDF/Alpha_vs_mGammaD_2015.pdf")
  cnv.SaveAs("plots/C/Alpha_vs_mGammaD_2015.C")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/Alpha_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/Alpha_vs_mGammaD_2015.png")

################################################################################
#           Plot acceptance Alpha vs ctau: 0.2 < ctau < 5.0                     
################################################################################

def Alpha_vs_ctau_2015():
  print "------------Alpha_vs_ctau_2015------------"
  cnv.SetLogy(0)
  array_Alpha_vs_ctau_m025GeV = []
  array_Alpha_vs_ctau_m04GeV  = []
  array_Alpha_vs_ctau_m1GeV   = []
  for ctau in fRange(ctau_mm_min, ctau_mm_max, 101):
    array_Alpha_vs_ctau_m025GeV.append(( ctau, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 0.25 ) ))
    array_Alpha_vs_ctau_m04GeV.append((  ctau, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 0.4 )  ))
    array_Alpha_vs_ctau_m1GeV.append((   ctau, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 1.0 )  ))
  array_Alpha_vs_ctau_m025GeV_Marker = []
  array_Alpha_vs_ctau_m04GeV_Marker  = []
  array_Alpha_vs_ctau_m1GeV_Marker   = []
  for ctau in ctau_mm:
    array_Alpha_vs_ctau_m025GeV_Marker.append(( ctau, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 0.25 ), 0.0, 100.0*fCmsDarkSusyAcceptanceUnct_LinearFit_2015_13TeV( ctau, 0.25 ) ))
    array_Alpha_vs_ctau_m04GeV_Marker.append((  ctau, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 0.4  ), 0.0, 100.0*fCmsDarkSusyAcceptanceUnct_LinearFit_2015_13TeV( ctau, 0.4  ) ))
  # not in loop above becuase sample with mGammaD = 1 GeV and ctau = 0 mm is not yet generated as of April 8th, 2014
  array_Alpha_vs_ctau_m1GeV_Marker.append((    0.2,  100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.2,  1.0 ) ))
  array_Alpha_vs_ctau_m1GeV_Marker.append((    0.5,  100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.5,  1.0 ) ))
  array_Alpha_vs_ctau_m1GeV_Marker.append((    2.0,  100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 2.0,  1.0 ) ))
  array_Alpha_vs_ctau_m1GeV_Marker.append((    5.0,  100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 5.0,  1.0 ) ))
  
  h_Alpha_vs_ctau_dummy = ROOT.TH2F("h_Alpha_vs_ctau_dummy", "h_Alpha_vs_ctau_dummy", 1000, ctau_mm_bot, ctau_mm_top, 1000, 0.0, 25.0)
  h_Alpha_vs_ctau_dummy.SetXTitle("c#tau_{#gamma_{D}} [mm]")
  h_Alpha_vs_ctau_dummy.SetYTitle("#alpha (c#tau_{#gamma_{D}}, m_{#gamma_{D}}) [%]")
  h_Alpha_vs_ctau_dummy.SetTitleOffset(1.1, "Y")
  h_Alpha_vs_ctau_dummy.GetYaxis().CenterTitle(1)
  h_Alpha_vs_ctau_dummy.GetYaxis().SetTitleSize(0.06)
  h_Alpha_vs_ctau_dummy.Draw()

  gr_Alpha_vs_ctau_m025GeV = ROOT.TGraph( len(array_Alpha_vs_ctau_m025GeV), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV)[1]) )
  gr_Alpha_vs_ctau_m025GeV.SetLineWidth(2)
  gr_Alpha_vs_ctau_m025GeV.SetLineColor(ROOT.kGreen+2)
  gr_Alpha_vs_ctau_m025GeV.SetLineStyle(9)
#  gr_Alpha_vs_ctau_m025GeV.Draw("C")
  
  gr_Alpha_vs_ctau_m025GeV_Marker = ROOT.TGraph( len(array_Alpha_vs_ctau_m025GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[1]) )
  gr_Alpha_vs_ctau_m025GeV_Marker.SetMarkerColor(ROOT.kGreen+2)
  gr_Alpha_vs_ctau_m025GeV_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_ctau_m025GeV_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_ctau_m025GeV_Marker.Draw("P")
  
  grErr_Alpha_vs_ctau_m025GeV_Marker = ROOT.TGraphErrors( len(array_Alpha_vs_ctau_m025GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[1]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[2]),
array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[3]) )
  grErr_Alpha_vs_ctau_m025GeV_Marker.SetMarkerColor(ROOT.kGreen+2)
  grErr_Alpha_vs_ctau_m025GeV_Marker.SetMarkerStyle(20)
  grErr_Alpha_vs_ctau_m025GeV_Marker.SetMarkerSize(1.5)
#  grErr_Alpha_vs_ctau_m025GeV_Marker.Draw("P")

#  fit_Alpha_vs_ctau_m025GeV = get_Alpha_vs_ctau_FCN()
#  fit_Alpha_vs_ctau_m025GeV.SetLineColor( grErr_Alpha_vs_ctau_m025GeV_Marker.getMarkerColor() )
#  grErr_Alpha_vs_ctau_m025GeV_Marker.Fit(fit_Alpha_vs_ctau_m025GeV,"LVMR","",0.0,5.0);

  gr_Alpha_vs_ctau_m04GeV = ROOT.TGraph( len(array_Alpha_vs_ctau_m04GeV), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV)[1]) )
  gr_Alpha_vs_ctau_m04GeV.SetLineWidth(2)
  gr_Alpha_vs_ctau_m04GeV.SetLineColor(ROOT.kRed)
  gr_Alpha_vs_ctau_m04GeV.SetLineStyle(1)
#  gr_Alpha_vs_ctau_m04GeV.Draw("C")
  
  gr_Alpha_vs_ctau_m04GeV_Marker = ROOT.TGraph( len(array_Alpha_vs_ctau_m04GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[1]) )
  gr_Alpha_vs_ctau_m04GeV_Marker.SetMarkerColor(ROOT.kRed)
  gr_Alpha_vs_ctau_m04GeV_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_ctau_m04GeV_Marker.SetMarkerSize(1.5)
#  gr_Alpha_vs_ctau_m04GeV_Marker.Draw("P")
  
  grErr_Alpha_vs_ctau_m04GeV_Marker = ROOT.TGraphErrors( len(array_Alpha_vs_ctau_m04GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[1]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[2]),
array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[3]) )
  grErr_Alpha_vs_ctau_m04GeV_Marker.SetMarkerColor(ROOT.kRed)
  grErr_Alpha_vs_ctau_m04GeV_Marker.SetMarkerStyle(20)
  grErr_Alpha_vs_ctau_m04GeV_Marker.SetMarkerSize(1.5)
#  grErr_Alpha_vs_ctau_m04GeV_Marker.Draw("PE")
  
#  fit_Alpha_vs_ctau_m04GeV = get_Alpha_vs_ctau_FCN()
#  fFit_Alpha_vs_ctau.Draw("same")
#  grErr_Alpha_vs_ctau_m04GeV_Marker.Fit(fit_Alpha_vs_ctau_m04GeV,"LVMR","",0.0,5.0);
  
  array_Alpha_vs_ctau_m04GeV_Fit  = []
  array_Alpha_vs_ctau_m025GeV_Fit  = []
  for ctau in [0.001,0.2,0.5,2.0,5.0]:
    array_Alpha_vs_ctau_m04GeV_Fit.append((  ctau, 100.0*f_Alpha_vs_ctau(0.4,45,ctau,0.068)  ))
    array_Alpha_vs_ctau_m025GeV_Fit.append((  ctau, 100.0*f_Alpha_vs_ctau(0.25,45,ctau,0.10077)  ))
  
  gr_Alpha_vs_ctau_m04GeV_Fit = ROOT.TGraph( len(array_Alpha_vs_ctau_m04GeV_Fit), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Fit)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Fit)[1]) )
  gr_Alpha_vs_ctau_m04GeV_Fit.SetMarkerColor(ROOT.kBlue)
  gr_Alpha_vs_ctau_m04GeV_Fit.SetMarkerStyle(20)
  gr_Alpha_vs_ctau_m04GeV_Fit.SetMarkerSize(1.5)
#  gr_Alpha_vs_ctau_m04GeV_Fit.Draw("PC")
  
  gr_Alpha_vs_ctau_m025GeV_Fit = ROOT.TGraph( len(array_Alpha_vs_ctau_m025GeV_Fit), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Fit)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Fit)[1]) )
  gr_Alpha_vs_ctau_m025GeV_Fit.SetMarkerColor(ROOT.kBlue)
  gr_Alpha_vs_ctau_m025GeV_Fit.SetMarkerStyle(21)
  gr_Alpha_vs_ctau_m025GeV_Fit.SetMarkerSize(1.5)
  gr_Alpha_vs_ctau_m025GeV_Fit.Draw("PC")
  
  gr_Alpha_vs_ctau_m1GeV = ROOT.TGraph( len(array_Alpha_vs_ctau_m1GeV), array.array("d", zip(*array_Alpha_vs_ctau_m1GeV)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m1GeV)[1]) )
  gr_Alpha_vs_ctau_m1GeV.SetLineWidth(2)
  gr_Alpha_vs_ctau_m1GeV.SetLineColor(ROOT.kBlue)
  gr_Alpha_vs_ctau_m1GeV.SetLineStyle(2)
#  gr_Alpha_vs_ctau_m1GeV.Draw("C")
  
  gr_Alpha_vs_ctau_m1GeV_Marker = ROOT.TGraph( len(array_Alpha_vs_ctau_m1GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m1GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m1GeV_Marker)[1]) )
  gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerColor(ROOT.kBlue)
  gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerSize(1.5)
#  gr_Alpha_vs_ctau_m1GeV_Marker.Draw("P")
  
  l_Alpha_vs_ctau = ROOT.TLegend(0.25,0.7,0.6,0.9)
  l_Alpha_vs_ctau.SetFillColor(ROOT.kWhite)
  l_Alpha_vs_ctau.SetMargin(0.4)
  l_Alpha_vs_ctau.SetBorderSize(0)
  l_Alpha_vs_ctau.SetTextFont(42)
  l_Alpha_vs_ctau.SetTextSize(0.035)
  l_Alpha_vs_ctau.SetHeader("Acceptance for samples with #gamma_{D} mass:")
#  l_Alpha_vs_ctau.AddEntry(gr_Alpha_vs_ctau_m025GeV,"m_{#gamma_{D}} = 0.25 GeV/#it{c}^{2}","L")
  l_Alpha_vs_ctau.AddEntry(gr_Alpha_vs_ctau_m04GeV, "m_{#gamma_{D}} =  0.4 GeV/#it{c}^{2}","LP")
#  l_Alpha_vs_ctau.AddEntry(gr_Alpha_vs_ctau_m1GeV,  "m_{#gamma_{D}} =  1.0 GeV/#it{c}^{2}","L")
  l_Alpha_vs_ctau.Draw()

  txtHeader.Draw()
  cnv.SaveAs("plots/PDF/Alpha_vs_ctau_2015.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/Alpha_vs_ctau_2015.pdf -resize 900x900 plots/PNG/Alpha_vs_ctau_2015.png")

def get_Alpha_vs_ctau_FCN():
  func = ROOT.TF1("Alpha_vs_ctau_FCN",Alpha_vs_ctau_FCN,0.0,5.0,2)
  func.SetParameters(100.0, 0.068)
  func.SetParNames("gamma","eff")
  func.SetParLimits(0, 1.0, 500.0)
  func.SetParLimits(1, 0.0, 1.0)
#  func.FixParameter(1, 0.068)
  return func

def Alpha_vs_ctau_FCN(v, par):
  ctau_mm   = v[0]
  
  gamma = par[0]
  Rmin  = 0.0
  R0    = 44.0
  Rmax  = 600.0
  zmin  = 0.0
  zmax  = 5.0*Rmax
  eff   = par[1]
  
  if ( ctau_mm == 0.0 ):
    N = 1.0
  else:
    N = 0.0
    nSteps = 100
    R_previous = 0.0
    for i in range(nSteps):
      R = (Rmax - Rmin)*float(i*i)/float(nSteps*nSteps)
      dR = R - R_previous
      R_previous = R
      z_previous = 0.0
      for j in range(nSteps):
        z = (zmax - zmin)*float(j*j)/float(nSteps*nSteps)
        dz = z - z_previous
        z_previous = z
        
        if ( gamma != 0.0 and ( R!= 0.0 or z!=0.0 ) ):
          N = N+Eff_vs_R(R0, R)/(gamma*ctau_mm)*R/(R*R+z*z)*exp(-sqrt(R*R+z*z)/(gamma*ctau_mm))*dR*dz
  
  return 100.0*eff*N

def f1(m,E,ctau_mm,R_mm,z_mm):
  gamma = E/m
  if ( gamma == 0.0 or ctau_mm == 0.0 ):
    f1_out = 1.0
  else:
    if ( R_mm >0 or z_mm >0 ):
      f1_out = 1.0/2.0*1.0/(gamma*ctau_mm)*R_mm/(R_mm*R_mm+z_mm*z_mm)*exp(-sqrt(R_mm*R_mm+z_mm*z_mm)/(gamma*ctau_mm))
    else:
      f1_out = 1.0
  
  return f1_out

def f2(m,E,ctau_mm,R_mm):
  gamma = E/m
  f2_out = 0.0
  
  nSteps = 300
  z_mm_min = 0.0
  if 10.0*gamma*ctau_mm < 10.0*R_mm:
    z_mm_max = 10.0*gamma*ctau_mm
  else:
    z_mm_max = 10.0*R_mm
  z_mm_previous = 0.0
  for i in range(nSteps):
    fraction = float(i*i)/float(nSteps*nSteps)
#    fraction = float(i)/float(nSteps)
    z_mm = (z_mm_max - z_mm_min)*fraction
    dz_mm = z_mm - z_mm_previous
    z_mm_previous = z_mm
    f2_out = f2_out + f1(m,E,ctau_mm,R_mm,z_mm) * dz_mm
  
  return 2.0*f2_out

def Eff_vs_R(R0_mm, R_mm):
  
  R_mm_TIB_outer_layer = 600.0
  
  R_mm_min =   0.0 # minimum radius from beamline
  R_mm_max = R_mm_TIB_outer_layer # radius to last layer in TIB. eficiency is 0 after this layer
  
  if ( R_mm >= R_mm_min and R_mm < R0_mm) :
    eff = 1.0
  elif ( R_mm >= R0_mm and R_mm < R_mm_max ) :
#    eff = R0_mm*R0_mm/(R_mm*R_mm) # efficiency per event with 2 dimuons
    eff = R0_mm/R_mm # efficiency per dimuon
  else:
    eff = 0.0
  
  return eff

def Plot_Eff_vs_R():
  print "------------Plot_Eff_vs_R------------"
  cnv.SetLogy(0)  
  R0_mm    = 44.0
  R_mm_bot =   0.0
  R_mm_top = 650.0
  array_Eff_vs_R = []
  for R_mm in fRange(R_mm_bot, R_mm_top, 651):
    # array_Eff_vs_R.append(( R_mm, Eff_vs_R(R0_mm, R_mm) )) # Below is modified version of the efficiency. We decided to use 0 efficiency after first layer of pixel
    if R_mm < R0_mm: array_Eff_vs_R.append(( R_mm, 1.0 ))
    else:            array_Eff_vs_R.append(( R_mm, 0.0 ))
  h_Eff_vs_R_dummy = ROOT.TH2F("h_Eff_vs_R_dummy", "h_Eff_vs_R_dummy", 650, R_mm_bot, R_mm_top, 1000, 0.0, 1.1)
  h_Eff_vs_R_dummy.SetXTitle("Radius from beamline [mm]")
  h_Eff_vs_R_dummy.SetYTitle("#epsilon")
  h_Eff_vs_R_dummy.GetYaxis().CenterTitle(1)
  h_Eff_vs_R_dummy.Draw()
  gr_Eff_vs_R = ROOT.TGraph( len(array_Eff_vs_R), array.array("d", zip(*array_Eff_vs_R)[0]), array.array("d", zip(*array_Eff_vs_R)[1]) )
  gr_Eff_vs_R.SetLineWidth(2)
  gr_Eff_vs_R.SetLineColor(ROOT.kRed)
  gr_Eff_vs_R.SetLineStyle(1)
  gr_Eff_vs_R.Draw("L")
  txtHeader.Draw()
  cnv.SaveAs("plots/PDF/Eff_vs_R.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/Eff_vs_R.pdf -resize 900x900 plots/PNG/Eff_vs_R.png")

def f3(m,E,ctau_mm):
  gamma = E/m
  f3_out = 0.0
  
  nSteps = 500
  R_mm_min = 0.0
  R_mm_TIB_outer_layer   = 600.0
  R_mm_Pixel_inner_layer = 44.0
  if 10.0*gamma*ctau_mm < R_mm_TIB_outer_layer:
    R_mm_max = 10.0*gamma*ctau_mm
  else:
    R_mm_max = R_mm_TIB_outer_layer
  R_mm_previous = 0.0
  for i in range(nSteps):
    fraction = float(i*i)/float(nSteps*nSteps)
#    fraction = float(i)/float(nSteps)
    R_mm = (R_mm_max - R_mm_min)*fraction
    dR_mm = R_mm - R_mm_previous
    R_mm_previous = R_mm
    f3_out = f3_out + Eff_vs_R(R_mm_Pixel_inner_layer, R_mm)*f2(m,E,ctau_mm,R_mm) * dR_mm
  
  return f3_out

def f_Alpha_vs_ctau(m,E,ctau_mm,alpha0):
  f3_ctau = f3(m,E,ctau_mm)
  f3_0    = f3(m,E,0.001)
  return alpha0*f3_ctau*f3_ctau/f3_0/f3_0
  

################################################################################
#           Plot 3D acceptance Alpha vs mGammaD and ctau                        
################################################################################

def Alpha_vs_mGammaD_ctau_3D():
  print "------------Alpha_vs_mGammaD_ctau_3D------------"
  cnv.SetTheta(20.0);
  cnv.SetPhi(-130.0);
  nBins = 100
  h_Alpha_vs_mGammaD_ctau_3D = ROOT.TH2F("h_Alpha_vs_mGammaD_ctau_3D", "h_Alpha_vs_mGammaD_ctau_3D", nBins, mGammaD_GeV_min, mGammaD_GeV_max, nBins, ctau_mm_min, ctau_mm_max)
  h_Alpha_vs_mGammaD_ctau_3D.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_Alpha_vs_mGammaD_ctau_3D.GetXaxis().CenterTitle(1)
  h_Alpha_vs_mGammaD_ctau_3D.GetXaxis().SetNdivisions(506)
  h_Alpha_vs_mGammaD_ctau_3D.GetXaxis().SetTitleOffset(1.44)
  h_Alpha_vs_mGammaD_ctau_3D.SetYTitle("c#tau_{#gamma_{D}} [mm]")
  h_Alpha_vs_mGammaD_ctau_3D.GetYaxis().CenterTitle(1)
  h_Alpha_vs_mGammaD_ctau_3D.GetYaxis().SetNdivisions(506)
  h_Alpha_vs_mGammaD_ctau_3D.GetYaxis().SetTitleOffset(1.35)
  h_Alpha_vs_mGammaD_ctau_3D.SetZTitle("#alpha (c#tau_{#gamma_{D}}, m_{#gamma_{D}}) [%]")
  
  for i_ctau in range(nBins):
    for i_m in range(nBins):
      m    = h_Alpha_vs_mGammaD_ctau_3D.GetXaxis().GetBinCenter( i_m    + 1 )
      ctau = h_Alpha_vs_mGammaD_ctau_3D.GetYaxis().GetBinCenter( i_ctau + 1 )
      rightPart = 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, m )
      h_Alpha_vs_mGammaD_ctau_3D.SetBinContent(i_m+1, i_ctau+1, rightPart)
  
  fSetPalette("RainBow")
  h_Alpha_vs_mGammaD_ctau_3D.Draw("surf1z")
  
  array_Alpha_vs_mGammaD_ctau_3D_Marker = []
  for ctau in ctau_mm:
    for m in mGammaD_GeV:
      if ( ctau == 0 and m >= 0.55 ):
        print "Samples not simulated yet:", ctau, m
      else:
        array_Alpha_vs_mGammaD_ctau_3D_Marker.append(( m, ctau, 100.0*fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, m ) ))
  
  gr_Alpha_vs_ctau_m1GeV_Marker = ROOT.TGraph2D( len(array_Alpha_vs_mGammaD_ctau_3D_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau_3D_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau_3D_Marker)[1]), array.array("d",
zip(*array_Alpha_vs_mGammaD_ctau_3D_Marker)[2]) )
  gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerColor(ROOT.kRed)
  gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerStyle(20)
  gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerSize(1.5)
  gr_Alpha_vs_ctau_m1GeV_Marker.Draw("sameP")
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/Alpha_vs_mGammaD_ctau_3D.pdf")
  cnv.SaveAs("plots/PNG/Alpha_vs_mGammaD_ctau_3D.png")

################################################################################
#       Plot Upper 95% CL Limit on CSxBR2 vs mGammaD: 0.25 < mGammaD < 1.0       
################################################################################

def limit_CSxBR2_fb_vs_mGammaD_2015():

  cnv.SetLogy(1)
  
  array_mGammaD_prediction_CSxBR2_fb = []
  BR_h_to_2n1 = 0.0025
  BR_n1_to_gammaD_nD = 0.5
  print BR_h_to_2n1*BR_n1_to_gammaD_nD*BR_n1_to_gammaD_nD*BR_GammaD_to_2mu( 0.4 )*BR_GammaD_to_2mu( 0.4 )
  
  array_mGammaD_limit_CSxBR2_fb_ctau0mm  = []
  array_mGammaD_limit_CSxBR2_fb_ctau02mm = []
  array_mGammaD_limit_CSxBR2_fb_ctau05mm = []
  array_mGammaD_limit_CSxBR2_fb_ctau2mm  = []
  array_mGammaD_limit_CSxBR2_fb_ctau5mm  = []
  for m in fRange(mGammaD_GeV_min, mGammaD_GeV_max, 101):
    prediction_CSxBR2_fb = 1000.0*fCS_SM_ggH_13TeV_pb(126.0)[0]*BR_h_to_2n1*BR_n1_to_gammaD_nD*BR_n1_to_gammaD_nD*BR_GammaD_to_2mu( m )*BR_GammaD_to_2mu( m )
    array_mGammaD_prediction_CSxBR2_fb.append((  m, prediction_CSxBR2_fb  ))
    array_mGammaD_limit_CSxBR2_fb_ctau0mm.append((  m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.0, m ) ))
    array_mGammaD_limit_CSxBR2_fb_ctau02mm.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.2, m ) ))
    array_mGammaD_limit_CSxBR2_fb_ctau05mm.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.5, m ) ))
    array_mGammaD_limit_CSxBR2_fb_ctau2mm.append((  m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 2.0, m ) ))
    array_mGammaD_limit_CSxBR2_fb_ctau5mm.append((  m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 5.0, m ) ))

  h_limit_CSxBR2_fb_vs_mGammaD_dummy = ROOT.TH2F("h_limit_CSxBR2_fb_vs_mGammaD_dummy", "h_limit_CSxBR2_fb_vs_mGammaD_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 0.01, 1000000.0)
  h_limit_CSxBR2_fb_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_limit_CSxBR2_fb_vs_mGammaD_dummy.SetYTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) B^{2}(#gamma_{D} #rightarrow 2 #mu) [fb]")
  h_limit_CSxBR2_fb_vs_mGammaD_dummy.SetTitleOffset(1.35, "Y")
  h_limit_CSxBR2_fb_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_limit_CSxBR2_fb_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  h_limit_CSxBR2_fb_vs_mGammaD_dummy.Draw()
  
  gr_prediction_CSxBR2_fb_vs_mGammaD = ROOT.TGraph( len(array_mGammaD_prediction_CSxBR2_fb), array.array("d", zip(*array_mGammaD_prediction_CSxBR2_fb)[0]), array.array("d", zip(*array_mGammaD_prediction_CSxBR2_fb)[1]) )
  gr_prediction_CSxBR2_fb_vs_mGammaD.SetLineWidth(2)
  gr_prediction_CSxBR2_fb_vs_mGammaD.SetLineColor(ROOT.kBlack)
  gr_prediction_CSxBR2_fb_vs_mGammaD.SetLineStyle(1)
  gr_prediction_CSxBR2_fb_vs_mGammaD.Draw("C")
  
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm = ROOT.TGraph( len(array_mGammaD_limit_CSxBR2_fb_ctau0mm), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau0mm)[0]), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau0mm)[1]) )
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm.SetLineColor(ROOT.kBlue)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm.SetLineStyle(2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm.Draw("C")
  
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm = ROOT.TGraph( len(array_mGammaD_limit_CSxBR2_fb_ctau02mm), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau02mm)[0]), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau02mm)[1]) )
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm.SetLineColor(ROOT.kGreen+2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm.SetLineStyle(9)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm.Draw("C")

  gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm = ROOT.TGraph( len(array_mGammaD_limit_CSxBR2_fb_ctau05mm), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau05mm)[0]), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau05mm)[1]) )
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm.SetLineColor(ROOT.kRed)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm.SetLineStyle(1)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm.Draw("C")
  
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm = ROOT.TGraph( len(array_mGammaD_limit_CSxBR2_fb_ctau2mm), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau2mm)[0]), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau2mm)[1]) )
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm.SetLineColor(ROOT.kMagenta)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm.SetLineStyle(10)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm.Draw("C")
  
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm = ROOT.TGraph( len(array_mGammaD_limit_CSxBR2_fb_ctau5mm), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau5mm)[0]), array.array("d", zip(*array_mGammaD_limit_CSxBR2_fb_ctau5mm)[1]) )
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm.SetLineColor(ROOT.kCyan)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm.SetLineStyle(8)
  gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm.Draw("C")

  l_limit_CSxBR2_fb_vs_mGammaD = ROOT.TLegend(0.2,0.55,0.8,0.9)
  l_limit_CSxBR2_fb_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_limit_CSxBR2_fb_vs_mGammaD.SetMargin(0.4)
  l_limit_CSxBR2_fb_vs_mGammaD.SetBorderSize(0)
  l_limit_CSxBR2_fb_vs_mGammaD.SetTextFont(42)
  l_limit_CSxBR2_fb_vs_mGammaD.SetTextSize(0.035)
  l_limit_CSxBR2_fb_vs_mGammaD.SetHeader("95% CL limits for samples with #gamma_{D} life-time:")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm, "c#tau_{#gamma_{D}} =   0 mm (prompt)","L")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm,"c#tau_{#gamma_{D}} = 0.2 mm","L")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm,"c#tau_{#gamma_{D}} = 0.5 mm","L")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm, "c#tau_{#gamma_{D}} =   2 mm","L")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm, "c#tau_{#gamma_{D}} =   5 mm","L")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_prediction_CSxBR2_fb_vs_mGammaD, "prediction with Br(h #rightarrow 2n_{1}) = 0.25%","L")
  l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_prediction_CSxBR2_fb_vs_mGammaD, "and Br(n_{1} #rightarrow #gamma_{D} n_{D}) = 50%","")
  l_limit_CSxBR2_fb_vs_mGammaD.Draw()

  txtHeader.Draw()

  cnv.SaveAs("plots/PDF/limit_CSxBR2_fb_vs_mGammaD_2015.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CSxBR2_fb_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/limit_CSxBR2_fb_vs_mGammaD_2015.png")

################################################################################
#       Plot Upper 95% CL Limit on CS vs mGammaD: 0.25 < mGammaD < 1.0       
################################################################################

def limit_CS_fb_vs_mGammaD_2015():

  cnv.SetLogy(0)
  
  array_mGammaD_prediction_CS_fb     = []
  BR_h_to_2n1 = 0.0025
  BR_n1_to_gammaD_nD = 0.5
  
  array_mGammaD_limit_CS_fb_ctau0mm  = []
  array_mGammaD_limit_CS_fb_ctau02mm = []
  array_mGammaD_limit_CS_fb_ctau05mm = []
  array_mGammaD_limit_CS_fb_ctau2mm  = []
  for m in fRange(0.25, 1.0, 101):
    array_mGammaD_prediction_CS_fb.append((  m, 1000.0*fCS_SM_ggH_13TeV_pb(126.0)[0]*BR_h_to_2n1*BR_n1_to_gammaD_nD*BR_n1_to_gammaD_nD ))
    array_mGammaD_limit_CS_fb_ctau0mm.append((  m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.0, m )/BR_GammaD_to_2mu( m )/BR_GammaD_to_2mu( m ) ))
    array_mGammaD_limit_CS_fb_ctau02mm.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.2, m )/BR_GammaD_to_2mu( m )/BR_GammaD_to_2mu( m ) ))
    array_mGammaD_limit_CS_fb_ctau05mm.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 0.5, m )/BR_GammaD_to_2mu( m )/BR_GammaD_to_2mu( m ) ))
    array_mGammaD_limit_CS_fb_ctau2mm.append((  m, fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( 2.0, m )/BR_GammaD_to_2mu( m )/BR_GammaD_to_2mu( m ) ))

  h_limit_CS_fb_vs_mGammaD_dummy = ROOT.TH2F("h_limit_CS_fb_vs_mGammaD_dummy", "h_limit_CS_fb_vs_mGammaD_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 0.0, 120.0)
  h_limit_CS_fb_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_limit_CS_fb_vs_mGammaD_dummy.SetYTitle("#sigma(pp #rightarrow h) #times Br(h #rightarrow 2#gamma_{D} + X) [fb]")
  h_limit_CS_fb_vs_mGammaD_dummy.SetTitleOffset(1.35, "Y")
  h_limit_CS_fb_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_limit_CS_fb_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  h_limit_CS_fb_vs_mGammaD_dummy.Draw()
  
  gr_prediction_CS_fb_vs_mGammaD = ROOT.TGraph( len(array_mGammaD_prediction_CS_fb), array.array("d", zip(*array_mGammaD_prediction_CS_fb)[0]), array.array("d", zip(*array_mGammaD_prediction_CS_fb)[1]) )
  gr_prediction_CS_fb_vs_mGammaD.SetLineWidth(2)
  gr_prediction_CS_fb_vs_mGammaD.SetLineColor(ROOT.kBlack)
  gr_prediction_CS_fb_vs_mGammaD.SetLineStyle(1)
  gr_prediction_CS_fb_vs_mGammaD.Draw("C")
  
  gr_limit_CS_fb_vs_mGammaD_ctau0mm = ROOT.TGraph( len(array_mGammaD_limit_CS_fb_ctau0mm), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau0mm)[0]), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau0mm)[1]) )
  gr_limit_CS_fb_vs_mGammaD_ctau0mm.SetLineWidth(2)
  gr_limit_CS_fb_vs_mGammaD_ctau0mm.SetLineColor(ROOT.kBlue)
  gr_limit_CS_fb_vs_mGammaD_ctau0mm.SetLineStyle(2)
  gr_limit_CS_fb_vs_mGammaD_ctau0mm.Draw("C")
  
  gr_limit_CS_fb_vs_mGammaD_ctau02mm = ROOT.TGraph( len(array_mGammaD_limit_CS_fb_ctau02mm), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau02mm)[0]), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau02mm)[1]) )
  gr_limit_CS_fb_vs_mGammaD_ctau02mm.SetLineWidth(2)
  gr_limit_CS_fb_vs_mGammaD_ctau02mm.SetLineColor(ROOT.kGreen+2)
  gr_limit_CS_fb_vs_mGammaD_ctau02mm.SetLineStyle(9)
  gr_limit_CS_fb_vs_mGammaD_ctau02mm.Draw("C")

  gr_limit_CS_fb_vs_mGammaD_ctau05mm = ROOT.TGraph( len(array_mGammaD_limit_CS_fb_ctau05mm), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau05mm)[0]), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau05mm)[1]) )
  gr_limit_CS_fb_vs_mGammaD_ctau05mm.SetLineWidth(2)
  gr_limit_CS_fb_vs_mGammaD_ctau05mm.SetLineColor(ROOT.kRed)
  gr_limit_CS_fb_vs_mGammaD_ctau05mm.SetLineStyle(1)
  gr_limit_CS_fb_vs_mGammaD_ctau05mm.Draw("C")
  
  gr_limit_CS_fb_vs_mGammaD_ctau2mm = ROOT.TGraph( len(array_mGammaD_limit_CS_fb_ctau2mm), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau2mm)[0]), array.array("d", zip(*array_mGammaD_limit_CS_fb_ctau2mm)[1]) )
  gr_limit_CS_fb_vs_mGammaD_ctau2mm.SetLineWidth(2)
  gr_limit_CS_fb_vs_mGammaD_ctau2mm.SetLineColor(ROOT.kMagenta)
  gr_limit_CS_fb_vs_mGammaD_ctau2mm.SetLineStyle(10)
  gr_limit_CS_fb_vs_mGammaD_ctau2mm.Draw("C")

  l_limit_CS_fb_vs_mGammaD = ROOT.TLegend(0.4,0.6,0.8,0.9)
  l_limit_CS_fb_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_limit_CS_fb_vs_mGammaD.SetMargin(0.4)
  l_limit_CS_fb_vs_mGammaD.SetBorderSize(0)
  l_limit_CS_fb_vs_mGammaD.SetTextFont(42)
  l_limit_CS_fb_vs_mGammaD.SetTextSize(0.035)
  l_limit_CS_fb_vs_mGammaD.SetHeader("95% CL limits for samples")
  l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau0mm, "with #gamma_{D} life-time:","")
  l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau0mm, "c#tau_{#gamma_{D}} =   0 mm (prompt)","L")
  l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau02mm,"c#tau_{#gamma_{D}} = 0.2 mm","L")
  l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau05mm,"c#tau_{#gamma_{D}} = 0.5 mm","L")
  l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau2mm, "c#tau_{#gamma_{D}} =   2 mm","L")
  l_limit_CS_fb_vs_mGammaD.Draw()

  txtHeader.Draw()

  cnv.SaveAs("plots/PDF/limit_CS_fb_vs_mGammaD_2015.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CS_fb_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/limit_CS_fb_vs_mGammaD_2015.png")

################################################################################
#         Plot Upper 95% CL Limit on CSxBR2 vs ctau: 0.2 < ctau < 2.0            
################################################################################

def limit_CSxBR2_fb_vs_ctau_2015():

  cnv.SetLogy(0)
  
  array_ctau_limit_CSxBR2_fb_m025GeV = []
  array_ctau_limit_CSxBR2_fb_m04GeV  = []
  array_ctau_limit_CSxBR2_fb_m1GeV   = []
  for ctau in fRange(0.0, 2.0, 101):
    array_ctau_limit_CSxBR2_fb_m025GeV.append(( ctau, fCmsLimitVsM(0.25)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 0.25 ) ))
    array_ctau_limit_CSxBR2_fb_m04GeV.append((  ctau, fCmsLimitVsM( 0.4)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 0.4  ) ))
    array_ctau_limit_CSxBR2_fb_m1GeV.append((   ctau, fCmsLimitVsM( 1.0)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, 1.0  ) ))

  h_limit_CSxBR2_fb_vs_ctau_dummy = ROOT.TH2F("h_limit_CSxBR2_fb_vs_ctau_dummy", "h_limit_CSxBR2_fb_vs_ctau_dummy", 1000, -0.2, 2.2, 1000, 0.0, 120.0)
  h_limit_CSxBR2_fb_vs_ctau_dummy.SetXTitle("c#tau_{#gamma_{D}} [mm]")
  h_limit_CSxBR2_fb_vs_ctau_dummy.SetYTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) B^{2}(#gamma_{D} #rightarrow 2 #mu) [fb]")
  h_limit_CSxBR2_fb_vs_ctau_dummy.SetTitleOffset(1.35, "Y")
  h_limit_CSxBR2_fb_vs_ctau_dummy.GetYaxis().CenterTitle(1)
  h_limit_CSxBR2_fb_vs_ctau_dummy.GetYaxis().SetTitleSize(0.06)
  h_limit_CSxBR2_fb_vs_ctau_dummy.Draw()

  gr_limit_CSxBR2_fb_vs_ctau_m025GeV = ROOT.TGraph( len(array_ctau_limit_CSxBR2_fb_m025GeV), array.array("d", zip(*array_ctau_limit_CSxBR2_fb_m025GeV)[0]), array.array("d", zip(*array_ctau_limit_CSxBR2_fb_m025GeV)[1]) )
  gr_limit_CSxBR2_fb_vs_ctau_m025GeV.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_ctau_m025GeV.SetLineColor(ROOT.kGreen+2)
  gr_limit_CSxBR2_fb_vs_ctau_m025GeV.SetLineStyle(9)
  gr_limit_CSxBR2_fb_vs_ctau_m025GeV.Draw("C")

  gr_limit_CSxBR2_fb_vs_ctau_m04GeV = ROOT.TGraph( len(array_ctau_limit_CSxBR2_fb_m04GeV), array.array("d", zip(*array_ctau_limit_CSxBR2_fb_m04GeV)[0]), array.array("d", zip(*array_ctau_limit_CSxBR2_fb_m04GeV)[1]) )
  gr_limit_CSxBR2_fb_vs_ctau_m04GeV.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_ctau_m04GeV.SetLineColor(ROOT.kRed)
  gr_limit_CSxBR2_fb_vs_ctau_m04GeV.SetLineStyle(1)
  gr_limit_CSxBR2_fb_vs_ctau_m04GeV.Draw("C")
  
  gr_limit_CSxBR2_fb_vs_ctau_m1GeV = ROOT.TGraph( len(array_ctau_limit_CSxBR2_fb_m1GeV), array.array("d", zip(*array_ctau_limit_CSxBR2_fb_m1GeV)[0]), array.array("d", zip(*array_ctau_limit_CSxBR2_fb_m1GeV)[1]) )
  gr_limit_CSxBR2_fb_vs_ctau_m1GeV.SetLineWidth(2)
  gr_limit_CSxBR2_fb_vs_ctau_m1GeV.SetLineColor(ROOT.kBlue)
  gr_limit_CSxBR2_fb_vs_ctau_m1GeV.SetLineStyle(2)
  gr_limit_CSxBR2_fb_vs_ctau_m1GeV.Draw("C")

  l_limit_CSxBR2_fb_vs_ctau = ROOT.TLegend(0.25,0.65,0.6,0.9)
  l_limit_CSxBR2_fb_vs_ctau.SetFillColor(ROOT.kWhite)
  l_limit_CSxBR2_fb_vs_ctau.SetMargin(0.4)
  l_limit_CSxBR2_fb_vs_ctau.SetBorderSize(0)
  l_limit_CSxBR2_fb_vs_ctau.SetTextFont(42)
  l_limit_CSxBR2_fb_vs_ctau.SetTextSize(0.035)
  l_limit_CSxBR2_fb_vs_ctau.SetHeader("95% CL limits for samples")
  l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m025GeV,"with #gamma_{D} mass:","")
  l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m025GeV,"m_{#gamma_{D}} = 0.25 GeV/#it{c}^{2}","L")
  l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m04GeV, "m_{#gamma_{D}} =  0.4 GeV/#it{c}^{2}","L")
  l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m1GeV,  "m_{#gamma_{D}} =  1.0 GeV/#it{c}^{2}","L")
  l_limit_CSxBR2_fb_vs_ctau.Draw()

  txtHeader.Draw()

  cnv.SaveAs("plots/PDF/limit_CSxBR2_fb_vs_ctau_2015.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CSxBR2_fb_vs_ctau_2015.pdf -resize 900x900 plots/PNG/limit_CSxBR2_fb_vs_ctau_2015.png")

################################################################################
#            Plot 95% CL Limit on CSxBR2 and on CS vs mGammaD and ctau          
################################################################################

def limit_CSxBR2_fb_and_CS_fb_and_CS_over_CSsm_vs_mGammaD_ctau_3D_and_2D():
  
  CSsm_fb = 1000.0 * fCS_SM_ggH_13TeV_pb(126.0)[0]
  
  line_m_ctau_2 = ROOT.TLine(0.25, 2.0, 1.0, 2.0)
  line_m_ctau_2.SetLineStyle(2)
  line_m_ctau_2.SetLineWidth(1)
  line_m_ctau_2.SetLineColor(ROOT.kBlack)
  
  line_m_ctau_5 = ROOT.TLine(0.25, 5.0, 1.0, 5.0)
  line_m_ctau_5.SetLineStyle(2)
  line_m_ctau_5.SetLineWidth(1)
  line_m_ctau_5.SetLineColor(ROOT.kBlack)
  
  line_ctau_m_025 = ROOT.TLine(0.25, 0, 0.25, 2.0)
  line_ctau_m_025.SetLineStyle(2)
  line_ctau_m_025.SetLineWidth(1)
  line_ctau_m_025.SetLineColor(ROOT.kBlack)
  
  line_ctau_m_1 = ROOT.TLine(1.0, 0, 1.0, 2.0)
  line_ctau_m_1.SetLineStyle(2)
  line_ctau_m_1.SetLineWidth(1)
  line_ctau_m_1.SetLineColor(ROOT.kBlack)
  
  line_logEpsilon2_m_025 = ROOT.TLine(0.25, logEpsilon2_min, 0.25, logEpsilon2_max)
  line_logEpsilon2_m_025.SetLineStyle(2)
  line_logEpsilon2_m_025.SetLineWidth(1)
  line_logEpsilon2_m_025.SetLineColor(ROOT.kBlack)
  
  line_logEpsilon2_m_1 = ROOT.TLine(1.0, logEpsilon2_min, 1.0, logEpsilon2_max)
  line_logEpsilon2_m_1.SetLineStyle(2)
  line_logEpsilon2_m_1.SetLineWidth(1)
  line_logEpsilon2_m_1.SetLineColor(ROOT.kBlack)
  
  h_ctau_vs_mGammaD_dummy = ROOT.TH2F("h_ctau_vs_mGammaD_dummy", "h_ctau_vs_mGammaD_dummy", 100, mGammaD_GeV_bot, mGammaD_GeV_top, 100, ctau_mm_bot, ctau_mm_top)
  h_ctau_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_ctau_vs_mGammaD_dummy.SetYTitle("c#tau_{#gamma_{D}} [mm]")
  h_ctau_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_ctau_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_ctau_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  
  nBins = 100
  
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D = ROOT.TH2F("h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D", "h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D", nBins, mGammaD_GeV_min, mGammaD_GeV_max, nBins, ctau_mm_min, ctau_mm_max)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetXaxis().CenterTitle(1)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetXaxis().SetNdivisions(506)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetXaxis().SetTitleOffset(1.4)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.SetYTitle("c#tau [mm]")
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetYaxis().CenterTitle(1)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetYaxis().SetNdivisions(506)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetYaxis().SetTitleOffset(1.45)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.SetZTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) B^{2}(#gamma_{D} #rightarrow 2 #mu) [fb]")
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetZaxis().CenterTitle(1)
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetZaxis().SetTitleOffset(1.3)
  
  h_limit_CS_fb_vs_mGammaD_ctau_3D = ROOT.TH2F("h_limit_CS_fb_vs_mGammaD_ctau_3D", "h_limit_CS_fb_vs_mGammaD_ctau_3D", nBins, mGammaD_GeV_min, mGammaD_GeV_max, nBins, ctau_mm_min, ctau_mm_max)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetXaxis().CenterTitle(1)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetXaxis().SetNdivisions(506)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetXaxis().SetTitleOffset(1.4)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.SetYTitle("c#tau [mm]")
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetYaxis().CenterTitle(1)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetYaxis().SetNdivisions(506)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetYaxis().SetTitleOffset(1.45)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.SetZTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) [fb]")
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetZaxis().CenterTitle(1)
  h_limit_CS_fb_vs_mGammaD_ctau_3D.GetZaxis().SetTitleOffset(1.3)

  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D = ROOT.TH2F("h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D", "h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D", nBins, mGammaD_GeV_min, mGammaD_GeV_max, nBins, ctau_mm_min, ctau_mm_max)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetXaxis().CenterTitle(1)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetXaxis().SetNdivisions(506)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetXaxis().SetTitleOffset(1.4)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.SetYTitle("c#tau [mm]")
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetYaxis().CenterTitle(1)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetYaxis().SetNdivisions(506)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetYaxis().SetTitleOffset(1.45)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.SetZTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) / #sigma_{SM}(pp #rightarrow h)")
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetZaxis().CenterTitle(1)
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetZaxis().SetTitleOffset(1.3)

  h_logEpsilon2_vs_mGammaD_dummy = ROOT.TH2F("h_logEpsilon2_vs_mGammaD_dummy", "h_logEpsilon2_vs_mGammaD_dummy", 100, mGammaD_GeV_bot, mGammaD_GeV_top, 100, logEpsilon2_min, logEpsilon2_max)
  h_logEpsilon2_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_logEpsilon2_vs_mGammaD_dummy.SetYTitle("log_{10}(#epsilon^{2})")
  h_logEpsilon2_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D = ROOT.TH2F("h_limit_CS_over_CSsm_vs_mGammaD_epsilon2_3D", "h_limit_CS_over_CSsm_vs_mGammaD_epsilon2_3D", nBins, mGammaD_GeV_min, mGammaD_GeV_max, nBins, logEpsilon2_min, logEpsilon2_max)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetXaxis().CenterTitle(1)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetXaxis().SetNdivisions(506)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetXaxis().SetTitleOffset(1.4)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.SetYTitle("log_{10}(#epsilon^{2})")
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetYaxis().CenterTitle(1)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetYaxis().SetNdivisions(506)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetYaxis().SetTitleOffset(1.45)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.SetZTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) / #sigma_{SM}(pp #rightarrow h)")
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetZaxis().CenterTitle(1)
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetZaxis().SetTitleOffset(1.3)
  
  # set contour levels
  
#  array_CS_over_CSsm_contourLevels = [0.0001, 0.000625, 0.00075, 0.0010, 0.0025, 0.0050, 0.0100, 0.025, 0.0500, 0.1000]
#  array_CS_over_CSsm_contourLevels = [0.0001, 0.000625, 0.0010, 0.0100, 0.1000]
  array_CS_over_CSsm_contourLevels = [0.05]
  
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.SetContour( len(array_CS_over_CSsm_contourLevels) )
  
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.GetZaxis().SetRangeUser( array_CS_over_CSsm_contourLevels[0], array_CS_over_CSsm_contourLevels[len(array_CS_over_CSsm_contourLevels) - 1]*2.0 )
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.SetContour( len(array_CS_over_CSsm_contourLevels) )
  i = 0
  for contourLevel in array_CS_over_CSsm_contourLevels:
    h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.SetContourLevel( i , contourLevel)
    i = i + 1

  h_limit_CS_fb_vs_mGammaD_ctau_3D.SetContour( len(array_CS_over_CSsm_contourLevels) )
  i = 0
  for contourLevel in array_CS_over_CSsm_contourLevels:
    h_limit_CS_fb_vs_mGammaD_ctau_3D.SetContourLevel( i , contourLevel*CSsm_fb)
    i = i + 1
  
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetZaxis().SetRangeUser( array_CS_over_CSsm_contourLevels[0], array_CS_over_CSsm_contourLevels[len(array_CS_over_CSsm_contourLevels) - 1]*2.0 )
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.SetContour( len(array_CS_over_CSsm_contourLevels) )
  i = 0
  for contourLevel in array_CS_over_CSsm_contourLevels:
    h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.SetContourLevel( i , contourLevel)
    i = i + 1
  
  for i_ctau in range(nBins):
    for i_m in range(nBins):
      m    = h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetXaxis().GetBinCenter( i_m    + 1 )
      ctau = h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.GetYaxis().GetBinCenter( i_ctau + 1 )
      rightPart                    = fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, m )
      rightPart_over_BR2           = rightPart / BR_GammaD_to_2mu( m ) / BR_GammaD_to_2mu( m )
      rightPart_over_BR2_over_CSsm = rightPart_over_BR2 / CSsm_fb
      h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.SetBinContent(    i_m+1, i_ctau+1, rightPart)
      h_limit_CS_fb_vs_mGammaD_ctau_3D.SetBinContent(        i_m+1, i_ctau+1, rightPart_over_BR2)
      h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.SetBinContent( i_m+1, i_ctau+1, rightPart_over_BR2_over_CSsm)
      
      if ctau > 0.0:
        logEpsilon2 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / ctau )
      else:
        logEpsilon2 = logEpsilon2_max
      
      if logEpsilon2 > logEpsilon2_min and logEpsilon2 < logEpsilon2_max:
        i_logEpsilon2 = int( (logEpsilon2 - logEpsilon2_min) * nBins / (logEpsilon2_max - logEpsilon2_min) )
      
  for i_logEpsilon2 in range(nBins):
    for i_m in range(nBins):
      m           = h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetXaxis().GetBinCenter( i_m           + 1 )
      logEpsilon2 = h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.GetYaxis().GetBinCenter( i_logEpsilon2 + 1 )
      ctau = c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / pow(10, logEpsilon2)
      if ctau > 0.0 and ctau < 2.0:
        rightPart_over_BR2_over_CSsm = fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, m ) / BR_GammaD_to_2mu( m ) / BR_GammaD_to_2mu( m ) / CSsm_fb
        h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.SetBinContent( i_m+1, i_logEpsilon2+1, rightPart_over_BR2_over_CSsm)
  
  fSetPalette("RainBow")
  ##############################################################################
  cnv.SetTheta(10);
  cnv.SetPhi(-15);
  
  cnv.SetCanvasSize(1100,900)
  cnv.SetRightMargin(0.2064)
  
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.Draw("surf1z")
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CSxBR2_fb_vs_mGammaD_ctau_3D.pdf")
  cnv.SaveAs("plots/PNG/limit_CSxBR2_fb_vs_mGammaD_ctau_3D.png")
  
  h_ctau_vs_mGammaD_dummy.Draw()
  h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.Draw("sameCONT3COLZ")
  
  line_m_ctau_5.Draw()
  line_ctau_m_025.Draw()
  line_ctau_m_1.Draw()
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CSxBR2_fb_vs_mGammaD_ctau_2D.pdf")
  cnv.SaveAs("plots/PNG/limit_CSxBR2_fb_vs_mGammaD_ctau_2D.png")
  
  ##############################################################################
  
  cnv.SetLogz(1)
  
  h_limit_CS_fb_vs_mGammaD_ctau_3D.Draw("surf1z")
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CS_fb_vs_mGammaD_ctau_3D.pdf")
  cnv.SaveAs("plots/PNG/limit_CS_fb_vs_mGammaD_ctau_3D.png")
  
  h_ctau_vs_mGammaD_dummy.Draw()
  h_limit_CS_fb_vs_mGammaD_ctau_3D.Draw("sameCONT3COLZ")
  
  line_m_ctau_5.Draw()
  line_ctau_m_025.Draw()
  line_ctau_m_1.Draw()
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CS_fb_vs_mGammaD_ctau_2D.pdf")
  cnv.SaveAs("plots/PNG/limit_CS_fb_vs_mGammaD_ctau_2D.png")

  ##############################################################################
  
  cnv.SetLogz(1)
  
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.Draw("surf1z")
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CS_over_CSsm_vs_mGammaD_ctau_3D.pdf")
  cnv.SaveAs("plots/PNG/limit_CS_over_CSsm_vs_mGammaD_ctau_3D.png")
  
  h_ctau_vs_mGammaD_dummy.Draw()
  h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.Draw("sameCONT3COLZ")
  
  line_m_ctau_5.Draw()
  line_ctau_m_025.Draw()
  line_ctau_m_1.Draw()
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CS_over_CSsm_vs_mGammaD_ctau_2D.pdf")
  cnv.SaveAs("plots/PNG/limit_CS_over_CSsm_vs_mGammaD_ctau_2D.png")

  ##############################################################################
  
  cnv.SetLogz(1)
  
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.Draw("surf1z")
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CS_over_CSsm_vs_mGammaD_epsilon2_3D.pdf")
  cnv.SaveAs("plots/PNG/limit_CS_over_CSsm_vs_mGammaD_epsilon2_3D.png")
  
  h_logEpsilon2_vs_mGammaD_dummy.Draw()
#  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.Draw("sameCONT3COLZ")
  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.Draw("sameCONT3")
  
  
#  axis = ROOT.TGaxis(0.0,0.2,0.0,2.2,0.001,10000,510,"")
#  axis.Draw()
  
  line_m_ctau_5.Draw()
  line_logEpsilon2_m_025.Draw()
  line_logEpsilon2_m_1.Draw()
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_CS_over_CSsm_vs_mGammaD_epsilon2_2D.pdf")
  cnv.SaveAs("plots/PNG/limit_CS_over_CSsm_vs_mGammaD_epsilon2_2D.png")

################################################################################
#  Plot 95% CL Limit lines on CSxBR2 vs (mGammaD, ctau) and (mGammaD, epsilon^2) 
################################################################################

def limit_Lines_CSxBR2_fb_vs_mGammaD_ctau():

  line_m_ctau_2 = ROOT.TLine(0.25, 2.0, 1.0, 2.0)
  line_m_ctau_2.SetLineStyle(2)
  line_m_ctau_2.SetLineWidth(1)
  line_m_ctau_2.SetLineColor(ROOT.kBlack)
  
  line_ctau_m_025 = ROOT.TLine(0.25, 0, 0.25, 2.0)
  line_ctau_m_025.SetLineStyle(2)
  line_ctau_m_025.SetLineWidth(1)
  line_ctau_m_025.SetLineColor(ROOT.kBlack)
  
  line_ctau_m_1 = ROOT.TLine(1.0, 0, 1.0, 2.0)
  line_ctau_m_1.SetLineStyle(2)
  line_ctau_m_1.SetLineWidth(1)
  line_ctau_m_1.SetLineColor(ROOT.kBlack)
  
  line_epsilon2_m_025 = ROOT.TLine(0.25, epsilon2_min, 0.25, epsilon2_max)
  line_epsilon2_m_025.SetLineStyle(2)
  line_epsilon2_m_025.SetLineWidth(1)
  line_epsilon2_m_025.SetLineColor(ROOT.kBlack)
  
  line_epsilon2_m_1 = ROOT.TLine(1.0, epsilon2_min, 1.0, epsilon2_max)
  line_epsilon2_m_1.SetLineStyle(2)
  line_epsilon2_m_1.SetLineWidth(1)
  line_epsilon2_m_1.SetLineColor(ROOT.kBlack)
  
  h_ctau_vs_mGammaD_dummy = ROOT.TH2F("h_ctau_vs_mGammaD_dummy", "h_ctau_vs_mGammaD_dummy", 100, mGammaD_GeV_bot, mGammaD_GeV_top, 100, 0.0, 3.0)
  h_ctau_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_ctau_vs_mGammaD_dummy.SetYTitle("c#tau_{#gamma_{D}} [mm]")
  h_ctau_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_ctau_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_ctau_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)

  h_ctau_vs_mGammaD_excl = ROOT.TH2F("h_ctau_vs_mGammaD_excl", "h_ctau_vs_mGammaD_excl", 2000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 0.0, 3.0)
  h_ctau_vs_mGammaD_excl.SetLineColor(ROOT.kRed);
  h_ctau_vs_mGammaD_excl.SetFillColor(ROOT.kRed);
  h_ctau_vs_mGammaD_excl.SetMarkerStyle(1)
  h_ctau_vs_mGammaD_excl.SetMarkerColor(ROOT.kRed)

  h_ctau_vs_mGammaD_incl = ROOT.TH2F("h_ctau_vs_mGammaD_incl", "h_ctau_vs_mGammaD_incl", 2000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 0.0, 3.0)
  h_ctau_vs_mGammaD_incl.SetLineColor(ROOT.kGreen);
  h_ctau_vs_mGammaD_incl.SetFillColor(ROOT.kGreen);
  h_ctau_vs_mGammaD_incl.SetMarkerStyle(1)
  h_ctau_vs_mGammaD_incl.SetMarkerColor(ROOT.kGreen)
  
  h_epsilon2_vs_mGammaD_dummy = ROOT.TH2F("h_epsilon2_vs_mGammaD_dummy", "h_epsilon2_vs_mGammaD_dummy", 100, mGammaD_GeV_bot, mGammaD_GeV_top, epsilon2_bins, epsilon2_min, epsilon2_max)
  h_epsilon2_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_epsilon2_vs_mGammaD_dummy.SetYTitle("#epsilon^{2}")
  h_epsilon2_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_epsilon2_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_epsilon2_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  
  array_ctau_vs_mGammaD     = []
  array_epsilon2_vs_mGammaD = []
  c_hbar_mm_GeV = 1.974*pow(10.0, -13) # c = 3*10^11 mm/s; hbar = 6.58*10^-25 GeV*sec
  
  K_array = [0.00012, 0.00015, 0.00020, 0.00030, 0.00040, 0.00050]
  for K in K_array:
    h_ctau_vs_mGammaD_incl.Reset()
    h_ctau_vs_mGammaD_excl.Reset()
    array_ctau_vs_mGammaD_K = []

    array_epsilon2_vs_mGammaD_K = []
    array_epsilon2_vs_mGammaD_excl_K = []
    array_epsilon2_vs_mGammaD_incl_K = []
    
    leftPart_fb = K * 1000.0*fCS_SM_ggH_13TeV_pb(126.0)[0]
    for m in fRange(mGammaD_GeV_min, mGammaD_GeV_max, 301):
      once = False
      for ctau in fRangeDecending(ctau_mm_max, ctau_mm_min, 301):
        rightPart_fb = fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsDarkSusyAcceptance_LinearFit_2015_13TeV( ctau, m )
        if ctau > 0.0:
          epsilon2 = c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / ctau
        else:
          epsilon2 = 1.0
        if leftPart_fb < rightPart_fb:
          h_ctau_vs_mGammaD_incl.Fill(m, ctau)
          array_epsilon2_vs_mGammaD_incl_K.append(( m, epsilon2 ))
        else:
          h_ctau_vs_mGammaD_excl.Fill(m, ctau)
          array_epsilon2_vs_mGammaD_excl_K.append(( m, epsilon2 ))
          if once == False:
            array_ctau_vs_mGammaD_K.append(( m, ctau ))
            array_epsilon2_vs_mGammaD_K.append(( m, epsilon2 ))
            once = True
    
    array_ctau_vs_mGammaD.append( array_ctau_vs_mGammaD_K )
    array_epsilon2_vs_mGammaD.append( array_epsilon2_vs_mGammaD_K )
    
    cnv.SetLogy(0)
    
    h_ctau_vs_mGammaD_dummy.Draw()
    h_ctau_vs_mGammaD_excl.Draw("same")
    h_ctau_vs_mGammaD_incl.Draw("same")
    
    line_m_ctau_2.Draw("same")
    line_ctau_m_025.Draw("same")
    line_ctau_m_1.Draw("same")
    
    gr_ctau_vs_mGammaD_K = ROOT.TGraph( len(array_ctau_vs_mGammaD_K), array.array("d", zip(*array_ctau_vs_mGammaD_K)[0]), array.array("d", zip(*array_ctau_vs_mGammaD_K)[1]) )
    gr_ctau_vs_mGammaD_K.SetLineWidth(2)
    gr_ctau_vs_mGammaD_K.SetLineColor(ROOT.kRed)
    gr_ctau_vs_mGammaD_K.SetLineStyle(1)
    gr_ctau_vs_mGammaD_K.Draw("L")
    
    l_ctau_vs_mGammaD_K = ROOT.TLegend(0.25,0.75,0.6,0.9)
    l_ctau_vs_mGammaD_K.SetFillColor(ROOT.kWhite)
    l_ctau_vs_mGammaD_K.SetMargin(0.4)
    l_ctau_vs_mGammaD_K.SetBorderSize(0)
    l_ctau_vs_mGammaD_K.SetTextFont(42)
    l_ctau_vs_mGammaD_K.SetTextSize(0.035)
    l_ctau_vs_mGammaD_K.SetHeader("95% CL "+"limits for K = %s"%K)
    l_ctau_vs_mGammaD_K.AddEntry(h_ctau_vs_mGammaD_excl, "excluded region","F")
    l_ctau_vs_mGammaD_K.AddEntry(h_ctau_vs_mGammaD_incl, "not excluded region","F")
    l_ctau_vs_mGammaD_K.Draw()
    
    txtHeader.Draw()

    cnv.SaveAs("plots/PDF/limit_Lines_CSxBR2_fb_vs_mGammaD_ctau_K%s.pdf"%K)
    cnv.SaveAs("plots/PNG/limit_Lines_CSxBR2_fb_vs_mGammaD_ctau_K%s.png"%K)
    
    cnv.SetLogy(1)
    
    h_epsilon2_vs_mGammaD_dummy.Draw()
    
    gr_epsilon2_vs_mGammaD_excl_K = ROOT.TGraph( len(array_epsilon2_vs_mGammaD_excl_K), array.array("d", zip(*array_epsilon2_vs_mGammaD_excl_K)[0]), array.array("d", zip(*array_epsilon2_vs_mGammaD_excl_K)[1]) )
    gr_epsilon2_vs_mGammaD_excl_K.SetFillColor(ROOT.kRed)
    gr_epsilon2_vs_mGammaD_excl_K.SetLineColor(ROOT.kRed)
    gr_epsilon2_vs_mGammaD_excl_K.SetMarkerColor(ROOT.kRed)
    gr_epsilon2_vs_mGammaD_excl_K.SetMarkerStyle(1)
    gr_epsilon2_vs_mGammaD_excl_K.Draw("P")
    
    gr_epsilon2_vs_mGammaD_incl_K = ROOT.TGraph( len(array_epsilon2_vs_mGammaD_incl_K), array.array("d", zip(*array_epsilon2_vs_mGammaD_incl_K)[0]), array.array("d", zip(*array_epsilon2_vs_mGammaD_incl_K)[1]) )
    gr_epsilon2_vs_mGammaD_incl_K.SetFillColor(ROOT.kGreen)
    gr_epsilon2_vs_mGammaD_incl_K.SetLineColor(ROOT.kGreen)
    gr_epsilon2_vs_mGammaD_incl_K.SetMarkerColor(ROOT.kGreen)
    gr_epsilon2_vs_mGammaD_incl_K.SetMarkerStyle(1)
    gr_epsilon2_vs_mGammaD_incl_K.Draw("P")
    
    gr_epsilon2_vs_mGammaD_K = ROOT.TGraph( len(array_epsilon2_vs_mGammaD_K), array.array("d", zip(*array_epsilon2_vs_mGammaD_K)[0]), array.array("d", zip(*array_epsilon2_vs_mGammaD_K)[1]) )
    gr_epsilon2_vs_mGammaD_K.SetLineWidth(2)
    gr_epsilon2_vs_mGammaD_K.SetLineColor(ROOT.kRed)
    gr_epsilon2_vs_mGammaD_K.SetLineStyle(1)
    gr_epsilon2_vs_mGammaD_K.Draw("L")
    
    line_epsilon2_m_025.Draw("same")
    line_epsilon2_m_1.Draw("same")
    
    l_epsilon2_vs_mGammaD_K = ROOT.TLegend(0.25,0.75,0.6,0.9)
    l_epsilon2_vs_mGammaD_K.SetFillColor(ROOT.kWhite)
    l_epsilon2_vs_mGammaD_K.SetMargin(0.4)
    l_epsilon2_vs_mGammaD_K.SetBorderSize(0)
    l_epsilon2_vs_mGammaD_K.SetTextFont(42)
    l_epsilon2_vs_mGammaD_K.SetTextSize(0.035)
    l_epsilon2_vs_mGammaD_K.SetHeader("95% CL "+"limits for K = %s"%K)
    l_epsilon2_vs_mGammaD_K.AddEntry(gr_epsilon2_vs_mGammaD_excl_K, "excluded region","F")
    l_epsilon2_vs_mGammaD_K.AddEntry(gr_epsilon2_vs_mGammaD_incl_K, "not excluded region","F")
    l_epsilon2_vs_mGammaD_K.Draw()
    
    txtHeader.Draw()

    cnv.SaveAs("plots/PDF/limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2_K%s.pdf"%K)
    cnv.SaveAs("plots/PNG/limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2_K%s.png"%K)
  
  cnv.SetLogy(0)
  
  h_ctau_vs_mGammaD_dummy.Draw()
  i = 0
  gr_ctau_vs_mGammaD_K = []
  for K in K_array:
    array_ctau_vs_mGammaD_K = array_ctau_vs_mGammaD[i]
    
    gr_ctau_vs_mGammaD_K.append( ROOT.TGraph( len(array_ctau_vs_mGammaD_K), array.array("d", zip(*array_ctau_vs_mGammaD_K)[0]), array.array("d", zip(*array_ctau_vs_mGammaD_K)[1]) ) )
    gr_ctau_vs_mGammaD_K[i].SetLineWidth(2)
    gr_ctau_vs_mGammaD_K[i].SetLineColor(ROOT.kRed)
    gr_ctau_vs_mGammaD_K[i].SetLineStyle(1)
    gr_ctau_vs_mGammaD_K[i].Draw("L")
    i = i+1
  
  line_m_ctau_2.Draw("same")
  line_ctau_m_025.Draw("same")
  line_ctau_m_1.Draw("same")
  
  l_ctau_vs_mGammaD = ROOT.TLegend(0.25,0.85,0.6,0.9)
  l_ctau_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_ctau_vs_mGammaD.SetMargin(0.4)
  l_ctau_vs_mGammaD.SetBorderSize(0)
  l_ctau_vs_mGammaD.SetTextFont(42)
  l_ctau_vs_mGammaD.SetTextSize(0.035)
  l_ctau_vs_mGammaD.SetHeader("95% CL limits for different K")
#  l_ctau_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m025GeV,"m_{#gamma_{D}} = 0.25 GeV/#it{c}^{2}","L")
  l_ctau_vs_mGammaD.Draw()
  

  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_Lines_CSxBR2_fb_vs_mGammaD_ctau.pdf")
  cnv.SaveAs("plots/PNG/limit_Lines_CSxBR2_fb_vs_mGammaD_ctau.png")
  
  cnv.SetLogy(1)
  
  h_epsilon2_vs_mGammaD_dummy.Draw()
  i = 0
  gr_epsilon2_vs_mGammaD_K = []
  for K in K_array:
    array_epsilon2_vs_mGammaD_K = array_epsilon2_vs_mGammaD[i]
    
    gr_epsilon2_vs_mGammaD_K.append( ROOT.TGraph( len(array_epsilon2_vs_mGammaD_K), array.array("d", zip(*array_epsilon2_vs_mGammaD_K)[0]), array.array("d", zip(*array_epsilon2_vs_mGammaD_K)[1]) ) )
    gr_epsilon2_vs_mGammaD_K[i].SetLineWidth(2)
    gr_epsilon2_vs_mGammaD_K[i].SetLineColor(ROOT.kRed)
    gr_epsilon2_vs_mGammaD_K[i].SetLineStyle(1)
    gr_epsilon2_vs_mGammaD_K[i].Draw("L")
    i = i+1
  
  line_epsilon2_m_025.Draw("same")
  line_epsilon2_m_1.Draw("same")
  
  l_epsilon2_vs_mGammaD = ROOT.TLegend(0.25,0.85,0.6,0.9)
  l_epsilon2_vs_mGammaD.SetFillColor(ROOT.kWhite)
  l_epsilon2_vs_mGammaD.SetMargin(0.4)
  l_epsilon2_vs_mGammaD.SetBorderSize(0)
  l_epsilon2_vs_mGammaD.SetTextFont(42)
  l_epsilon2_vs_mGammaD.SetTextSize(0.035)
  l_epsilon2_vs_mGammaD.SetHeader("95% CL limits for different K")
#  l_epsilon2_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_epsilon2_m025GeV,"m_{#gamma_{D}} = 0.25 GeV/#it{c}^{2}","L")
  l_epsilon2_vs_mGammaD.Draw()
  
  txtHeader.Draw()
  
  cnv.SaveAs("plots/PDF/limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2.pdf")
  cnv.SaveAs("plots/PNG/limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2.png")

################################################################################
#                Plot Decay Width / epsilon^2 in GeV                            
################################################################################

def plot_width_over_e2_GeV():

  cnv.SetLogy(1)
#  ROOT.TGaxis.SetMaxDigits( 2 )
  
  array_mGammaD_width_to_2el_over_e2_GeV = []
  array_mGammaD_width_to_2mu_over_e2_GeV = []
  for m in fRange(0.25, 2.0, 101):
    array_mGammaD_width_to_2el_over_e2_GeV.append(( m, Width_GammaD_to_2el_over_e2_GeV( m ) ))
    array_mGammaD_width_to_2mu_over_e2_GeV.append(( m, Width_GammaD_to_2mu_over_e2_GeV( m ) ))
  
  array_mGammaD_width_to_hadrons_over_e2_GeV = []
  for m in fRange(0.36, 2.0, 101):
    array_mGammaD_width_to_hadrons_over_e2_GeV.append(( m, Width_GammaD_to_hadrons_over_e2_GeV( m ) ))
  
  array_mGammaD_width_to_2pions_over_e2_GeV = []
  for m in fRange(0.28, 0.36, 101):
    array_mGammaD_width_to_2pions_over_e2_GeV.append(( m, Width_GammaD_to_2pi_over_e2_GeV( m ) ))
  
  array_mGammaD_width_total_over_e2_GeV = []
  array_mGammaD_width_total_over_e2_GeV_inverted = []
  for m in fRange(0.25, 2.0, 101):
    array_mGammaD_width_total_over_e2_GeV.append(( m, Width_GammaD_over_e2_GeV( m ) ))
    if Width_GammaD_over_e2_GeV( m ) != 0:
      array_mGammaD_width_total_over_e2_GeV_inverted.append(( m, 1.0/Width_GammaD_over_e2_GeV( m ) ))
    else:
      print "Error! Width_GammaD_over_e2_GeV (m = ", m, ") = ", Width_GammaD_over_e2_GeV( m )
  
  # printout of some values for table
  for m in mGammaD_GeV:
    print "m = ", m, "Width_GammaD_over_e2_GeV = ", Width_GammaD_over_e2_GeV( m ), "Width_GammaD_over_e2_GeV_inverted = ", 1.0/Width_GammaD_over_e2_GeV( m )
  
  h_width_over_e2_GeV_dummy = ROOT.TH2F("h_width_over_e2_GeV_dummy", "h_width_over_e2_GeV_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 0.000005, 5.0)
  h_width_over_e2_GeV_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_width_over_e2_GeV_dummy.SetYTitle("#Gamma_{#gamma_{D}} / #epsilon^{2} [GeV]")
  h_width_over_e2_GeV_dummy.SetTitleOffset(1.35, "Y")
  h_width_over_e2_GeV_dummy.GetXaxis().SetNdivisions(505)
  h_width_over_e2_GeV_dummy.GetYaxis().CenterTitle(1)
  h_width_over_e2_GeV_dummy.GetYaxis().SetTitleSize(0.06)
  h_width_over_e2_GeV_dummy.SetMinimum(0.00001)
  h_width_over_e2_GeV_dummy.Draw()

  gr_width_to_2mu_over_e2_GeV = ROOT.TGraph( len(array_mGammaD_width_to_2mu_over_e2_GeV), array.array("d", zip(*array_mGammaD_width_to_2mu_over_e2_GeV)[0]), array.array("d", zip(*array_mGammaD_width_to_2mu_over_e2_GeV)[1]) )
  gr_width_to_2mu_over_e2_GeV.SetLineWidth(2)
  gr_width_to_2mu_over_e2_GeV.SetLineColor(ROOT.kBlack)
  gr_width_to_2mu_over_e2_GeV.SetLineStyle(9)
  #  Draw below

  gr_width_to_2el_over_e2_GeV = ROOT.TGraph( len(array_mGammaD_width_to_2el_over_e2_GeV), array.array("d", zip(*array_mGammaD_width_to_2el_over_e2_GeV)[0]), array.array("d", zip(*array_mGammaD_width_to_2el_over_e2_GeV)[1]) )
  gr_width_to_2el_over_e2_GeV.SetLineWidth(2)
  gr_width_to_2el_over_e2_GeV.SetLineColor(ROOT.kGreen+2)
  gr_width_to_2el_over_e2_GeV.SetLineStyle(2)
  
  
  gr_width_to_hadrons_over_e2_GeV = ROOT.TGraph( len(array_mGammaD_width_to_hadrons_over_e2_GeV), array.array("d", zip(*array_mGammaD_width_to_hadrons_over_e2_GeV)[0]), array.array("d", zip(*array_mGammaD_width_to_hadrons_over_e2_GeV)[1]) )
  gr_width_to_hadrons_over_e2_GeV.SetLineWidth(2)
  gr_width_to_hadrons_over_e2_GeV.SetLineColor(ROOT.kBlue)
  gr_width_to_hadrons_over_e2_GeV.SetLineStyle(3)
  #  Draw below
  
  gr_width_to_2pi_over_e2_GeV = ROOT.TGraph( len(array_mGammaD_width_to_2pions_over_e2_GeV), array.array("d", zip(*array_mGammaD_width_to_2pions_over_e2_GeV)[0]), array.array("d", zip(*array_mGammaD_width_to_2pions_over_e2_GeV)[1]) )
  gr_width_to_2pi_over_e2_GeV.SetLineWidth(2)
  gr_width_to_2pi_over_e2_GeV.SetLineColor(ROOT.kMagenta)
  gr_width_to_2pi_over_e2_GeV.SetLineStyle(10)
  #  Draw below
  
  gr_width_total_over_e2_GeV = ROOT.TGraph( len(array_mGammaD_width_total_over_e2_GeV), array.array("d", zip(*array_mGammaD_width_total_over_e2_GeV)[0]), array.array("d", zip(*array_mGammaD_width_total_over_e2_GeV)[1]) )
  gr_width_total_over_e2_GeV.SetLineWidth(2)
  gr_width_total_over_e2_GeV.SetLineColor(ROOT.kRed)
  gr_width_total_over_e2_GeV.SetLineStyle(1)
  #  Draw below

  l_width_over_e2_GeV = ROOT.TLegend(0.25,0.7,0.6,0.9)
  l_width_over_e2_GeV.SetFillColor(ROOT.kWhite)
  l_width_over_e2_GeV.SetMargin(0.4)
  l_width_over_e2_GeV.SetBorderSize(0)
  l_width_over_e2_GeV.SetTextFont(42)
  l_width_over_e2_GeV.SetTextSize(0.035)
  l_width_over_e2_GeV.SetHeader("Decay widths normalized to #epsilon^{2} for processes:")
  l_width_over_e2_GeV.AddEntry(gr_width_total_over_e2_GeV,     "#gamma_{D} #rightarrow all",            "L")
  l_width_over_e2_GeV.AddEntry(gr_width_to_2mu_over_e2_GeV,    "#gamma_{D} #rightarrow #mu#mu",         "L")
  l_width_over_e2_GeV.AddEntry(gr_width_to_2el_over_e2_GeV,    "#gamma_{D} #rightarrow ee",             "L")
#  l_width_over_e2_GeV.AddEntry(gr_width_to_hadrons_over_e2_GeV,"#gamma_{D} #rightarrow hadrons",        "L")
#  l_width_over_e2_GeV.AddEntry(gr_width_to_2pi_over_e2_GeV,    "#gamma_{D} #rightarrow #pi^{+}#pi^{-}", "L")
  l_width_over_e2_GeV.Draw()
  
  l_width_over_e2_GeV_2 = ROOT.TLegend(0.6,0.75,0.9,0.85)
  l_width_over_e2_GeV_2.SetFillColor(ROOT.kWhite)
  l_width_over_e2_GeV_2.SetMargin(0.4)
  l_width_over_e2_GeV_2.SetBorderSize(0)
  l_width_over_e2_GeV_2.SetTextFont(42)
  l_width_over_e2_GeV_2.SetTextSize(0.035)
#  l_width_over_e2_GeV_2.SetHeader("Decay widths normalized to #epsilon^{2}:")
#  l_width_over_e2_GeV_2.AddEntry(gr_width_total_over_e2_GeV,     "#gamma_{D} #rightarrow all",            "L")
#  l_width_over_e2_GeV_2.AddEntry(gr_width_to_2mu_over_e2_GeV,    "#gamma_{D} #rightarrow #mu#mu",         "L")
#  l_width_over_e2_GeV_2.AddEntry(gr_width_to_2el_over_e2_GeV,    "#gamma_{D} #rightarrow ee",             "L")
  l_width_over_e2_GeV_2.AddEntry(gr_width_to_hadrons_over_e2_GeV,"#gamma_{D} #rightarrow hadrons",        "L")
  l_width_over_e2_GeV_2.AddEntry(gr_width_to_2pi_over_e2_GeV,    "#gamma_{D} #rightarrow #pi^{+}#pi^{-}", "L")
  l_width_over_e2_GeV_2.Draw()
  
  gr_width_to_2mu_over_e2_GeV.Draw("C")
  gr_width_to_2el_over_e2_GeV.Draw("C")
  gr_width_to_hadrons_over_e2_GeV.Draw("C")
  gr_width_to_2pi_over_e2_GeV.Draw("C")
  gr_width_total_over_e2_GeV.Draw("C")
  
  cnv.SaveAs("plots/PDF/GammaD_Width_over_e2_GeV.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/GammaD_Width_over_e2_GeV.pdf -resize 900x900 plots/PNG/GammaD_Width_over_e2_GeV.png")
  
  h_width_over_e2_GeV_inverted_dummy = ROOT.TH2F("h_width_over_e2_GeV_inverted_dummy", "h_width_over_e2_GeV_inverted_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 1.0/5.0, 1.0/0.000005)
  h_width_over_e2_GeV_inverted_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_width_over_e2_GeV_inverted_dummy.SetYTitle("f(m_{#gamma_{D}}) = (#Gamma_{#gamma_{D}} / #epsilon^{2})^{-1} [GeV^{-1}]")
  h_width_over_e2_GeV_inverted_dummy.SetTitleOffset(1.33, "Y")
  h_width_over_e2_GeV_inverted_dummy.GetYaxis().CenterTitle(1)
  h_width_over_e2_GeV_inverted_dummy.GetYaxis().SetTitleSize(0.06)
  h_width_over_e2_GeV_inverted_dummy.SetMinimum(0.00001)
  h_width_over_e2_GeV_inverted_dummy.Draw()
  
  gr_width_total_over_e2_GeV_inverted = ROOT.TGraph( len(array_mGammaD_width_total_over_e2_GeV_inverted), array.array("d", zip(*array_mGammaD_width_total_over_e2_GeV_inverted)[0]), array.array("d", zip(*array_mGammaD_width_total_over_e2_GeV_inverted)[1]) )
  gr_width_total_over_e2_GeV_inverted.SetLineWidth(2)
  gr_width_total_over_e2_GeV_inverted.SetLineColor(ROOT.kRed)
  gr_width_total_over_e2_GeV_inverted.SetLineStyle(1)
  gr_width_total_over_e2_GeV_inverted.Draw("C")

  cnv.SaveAs("plots/PDF/GammaD_Width_over_e2_GeV_inverted.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/GammaD_Width_over_e2_GeV_inverted.pdf -resize 900x900 plots/PNG/GammaD_Width_over_e2_GeV_inverted.png")
  
################################################################################
#                Plot Branching Fraction BR(gammaD -> 2mu)                      
################################################################################

def plot_BR_GammaD_to_2mu():
  print "------------Executing plot_BR_GammaD_to_2mu------------"
  #print "printing m + BR_GammaD_to_2mu( m ):"
  cnv.SetLogy(0)
  array_mGammaD_BR_to_2mu = []
  for m in fRange(0.25, 10.0, 976):
    #print m, BR_GammaD_to_2mu( m )
    array_mGammaD_BR_to_2mu.append(( m, 100.0*BR_GammaD_to_2mu( m ) ))
  
  h_width_over_e2_GeV_dummy = ROOT.TH2F("h_width_over_e2_GeV_dummy", "h_width_over_e2_GeV_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 100, 0.0, 100.0)
  h_width_over_e2_GeV_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_width_over_e2_GeV_dummy.SetYTitle("Br_{#gamma_{D}} [%]")
  h_width_over_e2_GeV_dummy.SetTitleOffset(1.35, "Y")
  h_width_over_e2_GeV_dummy.GetXaxis().SetNdivisions(505)
  h_width_over_e2_GeV_dummy.GetYaxis().CenterTitle(1)
  h_width_over_e2_GeV_dummy.GetYaxis().SetTitleSize(0.06)
  h_width_over_e2_GeV_dummy.SetMinimum(0.00001)
  h_width_over_e2_GeV_dummy.Draw()

  gr_BR_GammaD_to_2mu = ROOT.TGraph( len(array_mGammaD_BR_to_2mu), array.array("d", zip(*array_mGammaD_BR_to_2mu)[0]), array.array("d", zip(*array_mGammaD_BR_to_2mu)[1]) )
  gr_BR_GammaD_to_2mu.SetLineWidth(1)
  gr_BR_GammaD_to_2mu.SetLineColor(ROOT.kRed)
  gr_BR_GammaD_to_2mu.SetLineStyle(1)
  gr_BR_GammaD_to_2mu.Draw("L")

  l_BR_GammaD_to_2mu = ROOT.TLegend(0.25,0.8,0.6,0.9)
  l_BR_GammaD_to_2mu.SetFillColor(ROOT.kWhite)
  l_BR_GammaD_to_2mu.SetMargin(0.4)
  l_BR_GammaD_to_2mu.SetBorderSize(0)
  l_BR_GammaD_to_2mu.SetTextFont(42)
  l_BR_GammaD_to_2mu.SetTextSize(0.035)
  l_BR_GammaD_to_2mu.SetHeader("Branching fraction:")
  l_BR_GammaD_to_2mu.AddEntry(gr_BR_GammaD_to_2mu, "#gamma_{D} #rightarrow #mu #mu",            "L")
  l_BR_GammaD_to_2mu.Draw()

  cnv.SaveAs("plots/PDF/GammaD_BR_to_2mu.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/GammaD_BR_to_2mu.pdf -resize 900x900 plots/PNG/GammaD_BR_to_2mu.png")

################################################################################
#             Plot lines with constant ctau in (epsilon2, m) plane              
################################################################################

def plot_ctauConst_vs_logEpsilon2_mGammaD():
  
  h_logEpsilon2_vs_mGammaD_dummy = ROOT.TH2F("h_logEpsilon2_vs_mGammaD_dummy", "h_logEpsilon2_vs_mGammaD_dummy", 100, mGammaD_GeV_bot, mGammaD_GeV_top, 100, logEpsilon2_min, logEpsilon2_max)
  h_logEpsilon2_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
  h_logEpsilon2_vs_mGammaD_dummy.SetYTitle("log_{10}(#epsilon^{2})")
  h_logEpsilon2_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
  h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
  h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.06)
  h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().SetNdivisions(506)
  
  
  array_mGammaD_logEpsilon2_ctau_01 = []
  array_mGammaD_logEpsilon2_ctau_02 = []
  array_mGammaD_logEpsilon2_ctau_05 = []
  array_mGammaD_logEpsilon2_ctau_1  = []
  array_mGammaD_logEpsilon2_ctau_2  = []
  array_mGammaD_logEpsilon2_ctau_5  = []
  
  for m in fRange(0.25, 1.0, 101):
    logEpsilon2_ctau_01 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / 0.1 )
    array_mGammaD_logEpsilon2_ctau_01.append(( m, logEpsilon2_ctau_01 ))
    
    logEpsilon2_ctau_02 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / 0.2 )
    array_mGammaD_logEpsilon2_ctau_02.append(( m, logEpsilon2_ctau_02 ))
    
    logEpsilon2_ctau_05 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / 0.5 )
    array_mGammaD_logEpsilon2_ctau_05.append(( m, logEpsilon2_ctau_05 ))
    
    logEpsilon2_ctau_1 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / 1.0 )
    array_mGammaD_logEpsilon2_ctau_1.append(( m, logEpsilon2_ctau_1 ))
    
    logEpsilon2_ctau_2 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / 2.0 )
    array_mGammaD_logEpsilon2_ctau_2.append(( m, logEpsilon2_ctau_2 ))
    
    logEpsilon2_ctau_5 = log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( m ) / 5.0 )
    array_mGammaD_logEpsilon2_ctau_5.append(( m, logEpsilon2_ctau_5 ))
  
  h_logEpsilon2_vs_mGammaD_dummy.Draw()
  
  gr_ctau_01_vs_logEpsilon2_mGammaD = ROOT.TGraph( len(array_mGammaD_logEpsilon2_ctau_01), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_01)[0]), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_01)[1]) )
  gr_ctau_01_vs_logEpsilon2_mGammaD.SetLineWidth(1)
  gr_ctau_01_vs_logEpsilon2_mGammaD.SetLineColor(ROOT.kBlue)
  gr_ctau_01_vs_logEpsilon2_mGammaD.SetLineStyle(2)
  gr_ctau_01_vs_logEpsilon2_mGammaD.Draw("C")
  
  gr_ctau_02_vs_logEpsilon2_mGammaD = ROOT.TGraph( len(array_mGammaD_logEpsilon2_ctau_02), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_02)[0]), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_02)[1]) )
  gr_ctau_02_vs_logEpsilon2_mGammaD.SetLineWidth(1)
  gr_ctau_02_vs_logEpsilon2_mGammaD.SetLineColor(ROOT.kBlack)
  gr_ctau_02_vs_logEpsilon2_mGammaD.SetLineStyle(1)
  gr_ctau_02_vs_logEpsilon2_mGammaD.Draw("C")
  
  gr_ctau_05_vs_logEpsilon2_mGammaD = ROOT.TGraph( len(array_mGammaD_logEpsilon2_ctau_05), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_05)[0]), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_05)[1]) )
  gr_ctau_05_vs_logEpsilon2_mGammaD.SetLineWidth(1)
  gr_ctau_05_vs_logEpsilon2_mGammaD.SetLineColor(ROOT.kBlack)
  gr_ctau_05_vs_logEpsilon2_mGammaD.SetLineStyle(1)
  gr_ctau_05_vs_logEpsilon2_mGammaD.Draw("C")
  
  gr_ctau_1_vs_logEpsilon2_mGammaD = ROOT.TGraph( len(array_mGammaD_logEpsilon2_ctau_1), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_1)[0]), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_1)[1]) )
  gr_ctau_1_vs_logEpsilon2_mGammaD.SetLineWidth(1)
  gr_ctau_1_vs_logEpsilon2_mGammaD.SetLineColor(ROOT.kBlue)
  gr_ctau_1_vs_logEpsilon2_mGammaD.SetLineStyle(2)
  gr_ctau_1_vs_logEpsilon2_mGammaD.Draw("C")
  
  gr_ctau_2_vs_logEpsilon2_mGammaD = ROOT.TGraph( len(array_mGammaD_logEpsilon2_ctau_2), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_2)[0]), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_2)[1]) )
  gr_ctau_2_vs_logEpsilon2_mGammaD.SetLineWidth(1)
  gr_ctau_2_vs_logEpsilon2_mGammaD.SetLineColor(ROOT.kBlack)
  gr_ctau_2_vs_logEpsilon2_mGammaD.SetLineStyle(1)
  gr_ctau_2_vs_logEpsilon2_mGammaD.Draw("C")
  
  gr_ctau_5_vs_logEpsilon2_mGammaD = ROOT.TGraph( len(array_mGammaD_logEpsilon2_ctau_5), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_5)[0]), array.array("d", zip(*array_mGammaD_logEpsilon2_ctau_5)[1]) )
  gr_ctau_5_vs_logEpsilon2_mGammaD.SetLineWidth(1)
  gr_ctau_5_vs_logEpsilon2_mGammaD.SetLineColor(ROOT.kBlack)
  gr_ctau_5_vs_logEpsilon2_mGammaD.SetLineStyle(1)
  gr_ctau_5_vs_logEpsilon2_mGammaD.Draw("C")
  
  line_logEpsilon2_m_025 = ROOT.TLine(0.25, array_mGammaD_logEpsilon2_ctau_5[0][1], 0.25, logEpsilon2_max)
  line_logEpsilon2_m_025.SetLineStyle(2)
  line_logEpsilon2_m_025.SetLineWidth(1)
  line_logEpsilon2_m_025.SetLineColor(ROOT.kBlack)
  line_logEpsilon2_m_025.Draw()
  
  line_logEpsilon2_m_1 = ROOT.TLine(1.0, array_mGammaD_logEpsilon2_ctau_5[ len(array_mGammaD_logEpsilon2_ctau_2)-1 ][1], 1.0, logEpsilon2_max)
  line_logEpsilon2_m_1.SetLineStyle(2)
  line_logEpsilon2_m_1.SetLineWidth(1)
  line_logEpsilon2_m_1.SetLineColor(ROOT.kBlack)
  line_logEpsilon2_m_1.Draw()
  
  text_ctau = ROOT.TLatex(1.01, logEpsilon2_ctau_01+0.5, "c#tau_{#gamma_{D}}")
  text_ctau.SetTextColor(ROOT.kBlack)
  text_ctau.SetTextSize(0.044)
  text_ctau.SetTextFont(42)
  text_ctau.Draw()
  
  text_ctau_01 = ROOT.TText(1.01, logEpsilon2_ctau_01, "0.1")
  text_ctau_01.SetTextColor(ROOT.kBlue)
  text_ctau_01.SetTextSize(0.044)
  text_ctau_01.SetTextFont(42)
  text_ctau_01.Draw()
  
  text_ctau_02 = ROOT.TText(1.01, logEpsilon2_ctau_02, "0.2")
  text_ctau_02.SetTextColor(ROOT.kBlack)
  text_ctau_02.SetTextSize(0.044)
  text_ctau_02.SetTextFont(42)
  text_ctau_02.Draw()
  
  text_ctau_05 = ROOT.TText(1.01, logEpsilon2_ctau_05, "0.5")
  text_ctau_05.SetTextColor(ROOT.kBlack)
  text_ctau_05.SetTextSize(0.044)
  text_ctau_05.SetTextFont(42)
  text_ctau_05.Draw()
  
  text_ctau_1 = ROOT.TText(1.01, logEpsilon2_ctau_1, "1.0")
  text_ctau_1.SetTextColor(ROOT.kBlue)
  text_ctau_1.SetTextSize(0.044)
  text_ctau_1.SetTextFont(42)
  text_ctau_1.Draw()
  
  text_ctau_2 = ROOT.TText(1.01, logEpsilon2_ctau_2, "2.0")
  text_ctau_2.SetTextColor(ROOT.kBlack)
  text_ctau_2.SetTextSize(0.044)
  text_ctau_2.SetTextFont(42)
  text_ctau_2.Draw()
  
  text_ctau_5 = ROOT.TText(1.01, logEpsilon2_ctau_5, "5.0")
  text_ctau_5.SetTextColor(ROOT.kBlack)
  text_ctau_5.SetTextSize(0.044)
  text_ctau_5.SetTextFont(42)
  text_ctau_5.Draw()
  
  cnv.SaveAs("plots/PDF/ctauConst_vs_logEpsilon2_mGammaD.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/ctauConst_vs_logEpsilon2_mGammaD.pdf -resize 900x900 plots/PNG/ctauConst_vs_logEpsilon2_mGammaD.png")

################################################################################
#                                 NMSSM Plots                                   
################################################################################

################################################################################
#                 Plot limit on CSxBr2 vs ma for 2015 data                      
################################################################################

def limit_CSxBR2_fb_vs_ma_2015():
  BR_h_aa = 0.03

  cnv.SetLogy(1)

  h_CSxBR_vs_ma_dummy = ROOT.TH2F("h_CSxBR_vs_ma_dummy", "h_CSxBR_vs_ma_dummy", 1000, 0., 4., 1000, 0.8, 1000.)
  h_CSxBR_vs_ma_dummy.SetXTitle("mass of a_{1} [GeV]")
  h_CSxBR_vs_ma_dummy.SetYTitle("#sigma(pp #rightarrow h_{i} #rightarrow 2a_{1}) B^{2}(a_{1} #rightarrow 2 #mu) [fb]")
  h_CSxBR_vs_ma_dummy.SetTitleOffset(1.1, "Y")
  h_CSxBR_vs_ma_dummy.GetYaxis().CenterTitle(1)
  h_CSxBR_vs_ma_dummy.GetYaxis().SetTitleSize(0.06)
  h_CSxBR_vs_ma_dummy.SetNdivisions(20210, "Y")
  h_CSxBR_vs_ma_dummy.Draw()

  array_ma_mh_86  = []
  array_ma_mh_125 = []
  array_ma_mh_150 = []
  array_ma = [0.25, 0.5, 0.75, 1.0, 2.0, 3.55]
  for ma_i in array_ma:
    array_ma_mh_86.append((  ma_i, fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(ma_i, 86. ) )) # Transform Limits on N_ev to xsection
    array_ma_mh_125.append(( ma_i, fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(ma_i, 125.) ))
    array_ma_mh_150.append(( ma_i, fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(ma_i, 150.) ))
  
  gr_CSxBR_vs_ma_mh_86 = ROOT.TGraph(len(array_ma_mh_86), array.array("d", zip(*array_ma_mh_86)[0]), array.array("d", zip(*array_ma_mh_86)[1]))
  gr_CSxBR_vs_ma_mh_86.SetLineWidth(2)
  gr_CSxBR_vs_ma_mh_86.SetLineColor(ROOT.kMagenta+2)
  gr_CSxBR_vs_ma_mh_86.SetLineStyle(9)
  gr_CSxBR_vs_ma_mh_86.SetMarkerColor(ROOT.kMagenta+2)
  gr_CSxBR_vs_ma_mh_86.SetMarkerStyle(22)
  gr_CSxBR_vs_ma_mh_86.SetMarkerSize(1.5)
  gr_CSxBR_vs_ma_mh_86.Draw("CP")

  gr_CSxBR_vs_ma_mh_125 = ROOT.TGraph(len(array_ma_mh_125), array.array("d", zip(*array_ma_mh_125)[0]), array.array("d", zip(*array_ma_mh_125)[1]))
  gr_CSxBR_vs_ma_mh_125.SetLineWidth(2)
  gr_CSxBR_vs_ma_mh_125.SetLineColor(2)
  gr_CSxBR_vs_ma_mh_125.SetLineStyle(10)
  gr_CSxBR_vs_ma_mh_125.SetMarkerColor(2)
  gr_CSxBR_vs_ma_mh_125.SetMarkerStyle(20)
  gr_CSxBR_vs_ma_mh_125.SetMarkerSize(1.5)
  gr_CSxBR_vs_ma_mh_125.Draw("CP")

  gr_CSxBR_vs_ma_mh_150 = ROOT.TGraph(len(array_ma_mh_150), array.array("d", zip(*array_ma_mh_150)[0]), array.array("d", zip(*array_ma_mh_150)[1]))
  gr_CSxBR_vs_ma_mh_150.SetLineWidth(2)
  gr_CSxBR_vs_ma_mh_150.SetLineColor(ROOT.kBlue)
  gr_CSxBR_vs_ma_mh_150.SetLineStyle(3)
  gr_CSxBR_vs_ma_mh_150.SetMarkerColor(ROOT.kBlue)
  gr_CSxBR_vs_ma_mh_150.SetMarkerStyle(23)
  gr_CSxBR_vs_ma_mh_150.SetMarkerSize(1.5)
  gr_CSxBR_vs_ma_mh_150.Draw("CP")
  
  array_ma_mh_125_SM = []
  for ma_i in fRange(0.3, 3.55, 100):
    CS_h125_fb = 1000.0*fCS_SM_ggH_13TeV_pb(125.)[0]
    Br_a_mumu = fNMSSM_Br_a(ma_i, 20., 'mumu')
    CSxBR = CS_h125_fb*BR_h_aa*Br_a_mumu*Br_a_mumu
    array_ma_mh_125_SM.append(( ma_i, CSxBR ))
  gr_CSxBR_vs_ma_mh_125_SM = ROOT.TGraph(len(array_ma_mh_125_SM), array.array("d", zip(*array_ma_mh_125_SM)[0]), array.array("d", zip(*array_ma_mh_125_SM)[1]))
  gr_CSxBR_vs_ma_mh_125_SM.SetLineWidth(3)
  gr_CSxBR_vs_ma_mh_125_SM.SetLineColor(ROOT.kGreen+3)
  gr_CSxBR_vs_ma_mh_125_SM.SetLineStyle(1)
  gr_CSxBR_vs_ma_mh_125_SM.Draw("C")
  
  print "Branching fraction h->aa for which limit and prediction  are the same at ma=2GeV and mh=125GeV :", fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(ma_i,125.)/(1000.0*fCS_SM_ggH_13TeV_pb(125.)[0]*fNMSSM_Br_a(2.0, 20., 'mumu')*fNMSSM_Br_a(2.0, 20., 'mumu'))
  
  l_CSxBR_vs_ma = ROOT.TLegend(0.35,0.72,0.9,0.92)
  l_CSxBR_vs_ma.SetFillColor(ROOT.kWhite)
  l_CSxBR_vs_ma.SetMargin(0.13)
  l_CSxBR_vs_ma.SetBorderSize(0)
  l_CSxBR_vs_ma.SetTextFont(42)
  l_CSxBR_vs_ma.SetTextSize(0.035)
  l_CSxBR_vs_ma.SetHeader("NMSSM 95% CL upper limits:")
  l_CSxBR_vs_ma.AddEntry(gr_CSxBR_vs_ma_mh_86,"m_{h_{1}} =   86 GeV/#it{c}^{2}","LP")
  l_CSxBR_vs_ma.AddEntry(gr_CSxBR_vs_ma_mh_125,"m_{h_{1}} = 125 GeV/#it{c}^{2}","LP")
  l_CSxBR_vs_ma.AddEntry(gr_CSxBR_vs_ma_mh_150,"m_{h_{1}} = 150 GeV/#it{c}^{2}","LP")
  l_CSxBR_vs_ma.Draw()
  
  l_CSxBR_vs_ma_2 = ROOT.TLegend(0.35,0.57,0.9,0.72)
  l_CSxBR_vs_ma_2.SetFillColor(ROOT.kWhite)
  l_CSxBR_vs_ma_2.SetMargin(0.13)
  l_CSxBR_vs_ma_2.SetBorderSize(0)
  l_CSxBR_vs_ma_2.SetTextFont(42)
  l_CSxBR_vs_ma_2.SetTextSize(0.035)
  l_CSxBR_vs_ma_2.SetHeader("Reference model:")
  l_CSxBR_vs_ma_2.AddEntry(gr_CSxBR_vs_ma_mh_125_SM,"#sigma(pp #rightarrow h_{i} #rightarrow 2a_{1} ) = 0.03 #times #sigma_{SM}","L")
  l_CSxBR_vs_ma_2.AddEntry(gr_CSxBR_vs_ma_mh_125_SM,"#sigma(pp #rightarrow h_{j}) #times B(h_{j} #rightarrow 2a_{1}) = 0 for j #neq i","")
  l_CSxBR_vs_ma_2.Draw()

  gr_CSxBR_vs_ma_mh_125_SM.Draw("C")
  txtHeader.Draw()

  cnv.SaveAs("plots/PDF/CSxBR_vs_ma_2015.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/CSxBR_vs_ma_2015.pdf -resize 900x900 plots/PNG/CSxBR_vs_ma_2015.png")


################################################################################
#                 Plot limit on CSxBr2 vs mh for 2015 data                      
################################################################################

def limit_CSxBR2_fb_vs_mh_2015():  
  BR_h_aa = 0.03
 
  cnv.SetLogy(0)
  h_CSxBR_NMSSM_vs_mh_dummy = ROOT.TH2F("h_CSxBR_NMSSM_vs_mh_dummy", "h_CSxBR_NMSSM_vs_mh_dummy", 1000, 83., 153., 1000, 0., 30.)
  h_CSxBR_NMSSM_vs_mh_dummy.SetXTitle("mass of h_{i} [GeV]")
  h_CSxBR_NMSSM_vs_mh_dummy.SetYTitle("#sigma(pp #rightarrow h_{i}#rightarrow 2a_{1}) B^{2}(a_{1}#rightarrow 2 #mu) [fb]")
  h_CSxBR_NMSSM_vs_mh_dummy.SetTitleOffset(1.2, "Y")
  h_CSxBR_NMSSM_vs_mh_dummy.GetYaxis().CenterTitle(1)
  h_CSxBR_NMSSM_vs_mh_dummy.GetYaxis().SetTitleSize(0.05)
  h_CSxBR_NMSSM_vs_mh_dummy.SetTitleOffset(1.1, "X")
  h_CSxBR_NMSSM_vs_mh_dummy.GetXaxis().CenterTitle(1)
  h_CSxBR_NMSSM_vs_mh_dummy.GetXaxis().SetTitleSize(0.05)
  h_CSxBR_NMSSM_vs_mh_dummy.Draw()

  array_mh_CSxBR_NMSSM_ma_025 = []
  array_mh_CSxBR_NMSSM_ma_2   = []
  array_mh_CSxBR_NMSSM_ma_355 = []
  array_mh = [86., 90., 100., 110., 125., 150.]
  for mh_i in array_mh:
    array_mh_CSxBR_NMSSM_ma_025.append(( mh_i, fCmsLimitVsM(0.25)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(0.25, mh_i ) )) # Model Independent limits transformed to Xsec
    array_mh_CSxBR_NMSSM_ma_2.append((   mh_i, fCmsLimitVsM(2.00)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(2.00, mh_i ) ))
    array_mh_CSxBR_NMSSM_ma_355.append(( mh_i, fCmsLimitVsM(3.55)/lumi_fbinv/SF/fCmsNmssmAcceptance_2015_13TeV(3.55, mh_i ) ))

  gr_CSxBR_NMSSM_vs_mh_ma_025 = ROOT.TGraph(len(array_mh_CSxBR_NMSSM_ma_025), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_025)[0]), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_025)[1]))
  gr_CSxBR_NMSSM_vs_mh_ma_025.SetLineWidth(2)
  gr_CSxBR_NMSSM_vs_mh_ma_025.SetLineColor(ROOT.kMagenta+2)
  gr_CSxBR_NMSSM_vs_mh_ma_025.SetLineStyle(9)
  gr_CSxBR_NMSSM_vs_mh_ma_025.SetMarkerColor(ROOT.kMagenta+2)
  gr_CSxBR_NMSSM_vs_mh_ma_025.SetMarkerStyle(22)
  gr_CSxBR_NMSSM_vs_mh_ma_025.SetMarkerSize(1.5)
  #gr_CSxBR_NMSSM_vs_mh_ma_025.Draw("CP")

  gr_CSxBR_NMSSM_vs_mh_ma_2 = ROOT.TGraph(len(array_mh_CSxBR_NMSSM_ma_2), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_2)[0]), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_2)[1]))
  gr_CSxBR_NMSSM_vs_mh_ma_2.SetLineWidth(2)
  gr_CSxBR_NMSSM_vs_mh_ma_2.SetLineColor(2)
  gr_CSxBR_NMSSM_vs_mh_ma_2.SetLineStyle(10)
  gr_CSxBR_NMSSM_vs_mh_ma_2.SetMarkerColor(2)
  gr_CSxBR_NMSSM_vs_mh_ma_2.SetMarkerStyle(20)
  gr_CSxBR_NMSSM_vs_mh_ma_2.SetMarkerSize(1.5)
  #gr_CSxBR_NMSSM_vs_mh_ma_2.Draw("CP")

  gr_CSxBR_NMSSM_vs_mh_ma_355 = ROOT.TGraph(len(array_mh_CSxBR_NMSSM_ma_355), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_355)[0]), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_355)[1]))
  gr_CSxBR_NMSSM_vs_mh_ma_355.SetLineWidth(2)
  gr_CSxBR_NMSSM_vs_mh_ma_355.SetLineColor(ROOT.kBlue)
  gr_CSxBR_NMSSM_vs_mh_ma_355.SetLineStyle(3)
  gr_CSxBR_NMSSM_vs_mh_ma_355.SetMarkerColor(ROOT.kBlue)
  gr_CSxBR_NMSSM_vs_mh_ma_355.SetMarkerStyle(23)
  gr_CSxBR_NMSSM_vs_mh_ma_355.SetMarkerSize(1.5)
  #gr_CSxBR_NMSSM_vs_mh_ma_355.Draw("CP")

  execfile("scripts/NMSSM_Br_a_Function.py")
  array_mh_ma_2_SM = []
  for mh_i in fRange(86., 149., 100):
      CS_fb = 1000.0*fCS_SM_ggH_13TeV_pb(mh_i)[0]
      Br_a_mumu = fNMSSM_Br_a(2.0, 20., 'mumu')
      CSxBR = CS_fb*BR_h_aa*Br_a_mumu*Br_a_mumu
  #    print mh_i, CS_fb, CSxBR
      array_mh_ma_2_SM.append(( mh_i, CSxBR ))
  gr_CSxBR_SM = ROOT.TGraph(len(array_mh_ma_2_SM), array.array("d", zip(*array_mh_ma_2_SM)[0]), array.array("d", zip(*array_mh_ma_2_SM)[1]))
  gr_CSxBR_SM.SetLineWidth(3)
  gr_CSxBR_SM.SetLineColor(ROOT.kGreen+3)
  gr_CSxBR_SM.SetLineStyle(1)
  #gr_CSxBR_SM.Draw("C")

  box1 = ROOT.TBox(125.0, 0.0, 153.0, 30.0)
  box1.SetFillStyle(3001)
  box1.SetFillColor(ROOT.kRed - 10)
  box1.Draw()
  
  a_mh_125 = ROOT.TArrow(125.0, 0.0, 125.0, 30.0, 0.02, "--")
  a_mh_125.SetLineColor(ROOT.kBlack)
  a_mh_125.SetLineWidth(1)
  a_mh_125.SetLineStyle(7)
  a_mh_125.Draw()
  
  ROOT.gPad.RedrawAxis()

  l_CSxBR_NMSSM_vs_mh = ROOT.TLegend(0.20,0.71,0.93,0.91)
  l_CSxBR_NMSSM_vs_mh.SetFillColor(ROOT.kWhite)
  l_CSxBR_NMSSM_vs_mh.SetFillStyle(4050)
  l_CSxBR_NMSSM_vs_mh.SetBorderSize(0)
  l_CSxBR_NMSSM_vs_mh.SetTextFont(42)
  l_CSxBR_NMSSM_vs_mh.SetTextSize(0.035)
  l_CSxBR_NMSSM_vs_mh.SetMargin(0.13)
  l_CSxBR_NMSSM_vs_mh.SetHeader("NMSSM 95% CL upper limits:")
  l_CSxBR_NMSSM_vs_mh.AddEntry(gr_CSxBR_NMSSM_vs_mh_ma_355,"m_{a_{1}} = 3.55 GeV/#it{c}^{2}","LP")
  l_CSxBR_NMSSM_vs_mh.AddEntry(gr_CSxBR_NMSSM_vs_mh_ma_2,  "m_{a_{1}} = 2 GeV/#it{c}^{2}",   "LP")
  l_CSxBR_NMSSM_vs_mh.AddEntry(gr_CSxBR_NMSSM_vs_mh_ma_025,"m_{a_{1}} = 0.25 GeV/#it{c}^{2}","LP")
  l_CSxBR_NMSSM_vs_mh.Draw()
  
  l_CSxBR_NMSSM_vs_mh_2 = ROOT.TLegend(0.20,0.56,0.93,0.71)
  l_CSxBR_NMSSM_vs_mh_2.SetFillColor(ROOT.kWhite)
  l_CSxBR_NMSSM_vs_mh_2.SetFillStyle(4050)
  l_CSxBR_NMSSM_vs_mh_2.SetBorderSize(0)
  l_CSxBR_NMSSM_vs_mh_2.SetTextFont(42)
  l_CSxBR_NMSSM_vs_mh_2.SetTextSize(0.035)
  l_CSxBR_NMSSM_vs_mh_2.SetMargin(0.13)
  l_CSxBR_NMSSM_vs_mh_2.SetHeader("Reference model:")
  l_CSxBR_NMSSM_vs_mh_2.AddEntry(gr_CSxBR_SM,"#sigma(pp #rightarrow h_{i} #rightarrow 2a_{1} ) = 0.03 #times #sigma_{SM}","L")
  l_CSxBR_NMSSM_vs_mh_2.AddEntry(gr_CSxBR_SM,"B(a_{1}#rightarrow 2#mu)=7.7%","")
  l_CSxBR_NMSSM_vs_mh_2.Draw()
  
  l_mh1 = ROOT.TLegend(0.22,0.15,0.6,0.3)
  l_mh1.SetFillColor(ROOT.kWhite)
  l_mh1.SetFillStyle(4050)
  l_mh1.SetBorderSize(0)
  l_mh1.SetTextFont(42)
  l_mh1.SetTextSize(0.035)
  l_mh1.SetTextColor(ROOT.kBlack)
  l_mh1.SetMargin(0.13)
  l_mh1.SetHeader("")
  l_mh1.AddEntry(gr_CSxBR_SM,"h_{i} = h_{1}:","")
  l_mh1.AddEntry(gr_CSxBR_SM,"m_{h_{1}} < m_{h_{2}}=125 GeV","")
  l_mh1.Draw()

  l_mh2 = ROOT.TLegend(0.63,0.15,0.9,0.3)
  l_mh2.SetFillColor(ROOT.kWhite)
  l_mh2.SetFillStyle(4050)
  l_mh2.SetBorderSize(0)
  l_mh2.SetTextFont(42)
  l_mh2.SetTextSize(0.035)
  l_mh2.SetTextColor(ROOT.kBlack)
  l_mh2.SetMargin(0.13)
  l_mh2.SetHeader("")
  l_mh2.AddEntry(gr_CSxBR_SM,"h_{i} = h_{2}:","")
  l_mh2.AddEntry(gr_CSxBR_SM,"125 GeV = m_{h_{1}} #leq m_{h_{2}}","")
  l_mh2.Draw()

#  l_CMS = ROOT.TLegend(0.7,0.9,0.9,0.95)
#  l_CMS.SetFillColor(ROOT.kWhite)
#  l_CMS.SetFillStyle(4050)
#  l_CMS.SetBorderSize(0)
#  l_CMS.SetTextFont(61)
#  l_CMS.SetTextSize(30./600.)
#  l_CMS.SetTextColor(ROOT.kBlack)
#  #l_CMS.SetMargin(0.13)
#  l_CMS.SetHeader("CMS")
#  l_CMS.Draw()

  gr_CSxBR_NMSSM_vs_mh_ma_355.Draw("CP")
  gr_CSxBR_NMSSM_vs_mh_ma_2.Draw("CP")
  gr_CSxBR_NMSSM_vs_mh_ma_025.Draw("CP")
  gr_CSxBR_SM.Draw("C")

  txtHeader.Draw()

  cnv.SaveAs("plots/PDF/CSxBR_NMSSM_vs_mh_2015.pdf")
  os.system("convert -define pdf:use-cropbox=true -density 300 plots/CSxBR_NMSSM_vs_mh_2015.pdf -resize 900x900 plots/PNG/CSxBR_NMSSM_vs_mh_2015.png")


import ROOT, array, os, re, math, random
from math import *
import numpy as np
import sys

execfile("tdrStyle.py")
execfile("fSetPalette.py")
execfile("fRange.py")

execfile("UserInput.py") # miscellaneous inputs
execfile("UserConfig.py") # user config year
execfile("CmsAlpAcceptance.py") #ALP acceptance and width from GEN LHE
execfile("CmsNmssmAcceptance.py")
execfile("CmsLimitVsM.py") # functions and limits
execfile("SMHiggsCrossSections.py")
execfile("DarkPhotonWidths_and_Branchings.py")
execfile("R_Hadrons.py")
execfile("CmsDarkSusyAcceptance.py")
execfile("NMSSM_Br_a_Function.py")

txtHeader = ROOT.TLegend(.05, .933, .99, 1.)
txtHeader.SetFillColor(ROOT.kWhite)
txtHeader.SetFillStyle(0)
txtHeader.SetBorderSize(0)
txtHeader.SetTextFont(42)
txtHeader.SetTextSize(0.045)
txtHeader.SetTextAlign(22)
txtHeader.SetHeader(header); # header defined in UserConfig.py

## output directory
topDirectory = "plots%d"%CL # CL defined in UserInput.py
PNGDir = os.path.join(topDirectory, "PNG")
PDFDir = os.path.join(topDirectory, "PDF")
CDir   = os.path.join(topDirectory, "C")
if not os.path.exists(PNGDir):
    os.makedirs(PNGDir)
if not os.path.exists(PDFDir):
    os.makedirs(PDFDir)
if not os.path.exists(CDir):
    os.makedirs(CDir)

cnv = ROOT.TCanvas("cnv", "cnv")
cnv.SetCanvasSize(900, 900)

################################################################################
#       Plot Upper %CL% CL Limit on number of events: 0.25 < mGammaD < 1.0
################################################################################

def save_canvas(cnv, title):
    cnv.SaveAs(topDirectory + "/PNG/" + title + ".png")
    cnv.SaveAs(topDirectory + "/PDF/" + title + ".pdf")
    cnv.SaveAs(topDirectory + "/C/" + title + ".C")


def limit_vs_mGammaD():
    print "------------limit_vs_mGammaD------------"
    cnv.SetLogy(0)

    padTop = ROOT.TPad( "padTop", "padTop", 0.0, 0.3, 1.0, 1.0 )
    padTop.Draw()
    padTop.cd()
    padTop.SetLogx()
    array_mGammaD_limit_toy_SR1 = [] #Expected median @specified XX% CL
    array_mGammaD_limit_toy_SR2 = []
    array_mGammaD_limit_toy_SR3 = []
    array_mGammaD_limit_toy_p_one_sigma_SR1 = [] #Expected +1 sigma @specified XX% CL
    array_mGammaD_limit_toy_p_one_sigma_SR2 = []
    array_mGammaD_limit_toy_p_one_sigma_SR3 = []
    array_mGammaD_limit_toy_n_one_sigma_SR1 = [] #Expected -1 sigma @specified XX% CL
    array_mGammaD_limit_toy_n_one_sigma_SR2 = []
    array_mGammaD_limit_toy_n_one_sigma_SR3 = []
    array_mGammaD_limit_toy_p_two_sigma_SR1 = [] #Expected +2 sigma @specified XX% CL
    array_mGammaD_limit_toy_p_two_sigma_SR2 = []
    array_mGammaD_limit_toy_p_two_sigma_SR3 = []
    array_mGammaD_limit_toy_n_two_sigma_SR1 = [] #Expected -2 sigma @specified XX% CL
    array_mGammaD_limit_toy_n_two_sigma_SR2 = []
    array_mGammaD_limit_toy_n_two_sigma_SR3 = []
    array_mGammaD_limit_fit_SR1 = [] #Fit to toy limit
    array_mGammaD_limit_fit_SR2 = []
    array_mGammaD_limit_fit_SR3 = []
    array_mGammaD_limit_fit_uncertainty = [] # don't need specify SR1 as we only draw discrete points, no lines
    rnd = ROOT.TRandom()
    rnd.SetSeed(2016)

    # Fitted function to limits at SR1/2/3, Avoid J/psi and Upsilon regions
    for m in np.arange(m_SR1_min, m_SR1_max, 0.005):
        array_mGammaD_limit_fit_SR1.append( (m, fCmsLimitVsM(m)) )
    for m in np.arange(m_SR2_min, m_SR2_max, 0.005):
        array_mGammaD_limit_fit_SR2.append( (m, fCmsLimitVsM(m)) )
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        for m in np.arange(m_SR3_min, m_SR3_max, 0.005):
            array_mGammaD_limit_fit_SR3.append( (m, fCmsLimitVsM(m)) )

    # Start: Limits from toy experiment
    for m in masses:
        if (m >= m_SR1_min and m <= m_SR1_max):
            array_mGammaD_limit_toy_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew) )) # expected median limit from toys experiments
            array_mGammaD_limit_toy_p_two_sigma_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p975_HybridNew) )) # expected 95 CI upper bound "
            array_mGammaD_limit_toy_n_two_sigma_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p025_HybridNew) )) # expected 95 CI lower bound "
            array_mGammaD_limit_toy_p_one_sigma_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p84_HybridNew) )) # expected 68 CI upper bound "
            array_mGammaD_limit_toy_n_one_sigma_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p16_HybridNew) )) # expected 68 CI lower bound "
            array_mGammaD_limit_fit_uncertainty.append(( m, (ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew) - fCmsLimitVsM(m) ) / fCmsLimitVsM(m) )) # Fit uncertainties for expected median @XX% CL
        elif (m >= m_SR2_min and m <= m_SR2_max):
            array_mGammaD_limit_toy_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew) ))
            array_mGammaD_limit_toy_p_two_sigma_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p975_HybridNew) ))
            array_mGammaD_limit_toy_n_two_sigma_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p025_HybridNew) ))
            array_mGammaD_limit_toy_p_one_sigma_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p84_HybridNew) ))
            array_mGammaD_limit_toy_n_one_sigma_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p16_HybridNew) ))
            array_mGammaD_limit_fit_uncertainty.append(( m, (ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew) - fCmsLimitVsM(m) ) / fCmsLimitVsM(m) ))
        elif (m >= m_SR3_min and m <= m_SR3_max):
            array_mGammaD_limit_toy_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew) ))
            array_mGammaD_limit_toy_p_two_sigma_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p975_HybridNew) ))
            array_mGammaD_limit_toy_n_two_sigma_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p025_HybridNew) ))
            array_mGammaD_limit_toy_p_one_sigma_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p84_HybridNew) ))
            array_mGammaD_limit_toy_n_one_sigma_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p16_HybridNew) ))
            array_mGammaD_limit_fit_uncertainty.append(( m, (ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew) - fCmsLimitVsM(m) ) / fCmsLimitVsM(m) ))
    # End: Limits from toy experiment

    # histogram range: x: mass; y: N_evt @%XX%CL
    h_limit_vs_mGammaD_dummy = ROOT.TH2F("h_limit_vs_mGammaD_dummy", "h_limit_vs_mGammaD_dummy", 1000, m_SR1_min-0.04, MaxGraphMass, 1000, 0.0, NMax)
    h_limit_vs_mGammaD_dummy.SetXTitle("m_{a} [GeV]")
    h_limit_vs_mGammaD_dummy.SetYTitle("%d%% CL upper limit on N_{evt}"%CL)
    h_limit_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
    h_limit_vs_mGammaD_dummy.GetXaxis().SetNdivisions(505)
    h_limit_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)
    h_limit_vs_mGammaD_dummy.Draw()

    # Start: Limit from toy experiments median SR1/2/3
    gr_limit_vs_mGammaD_toy_SR1 = ROOT.TGraph( len(array_mGammaD_limit_toy_SR1), array.array("d", zip(*array_mGammaD_limit_toy_SR1)[0]), array.array("d", zip(*array_mGammaD_limit_toy_SR1)[1]) )
    gr_limit_vs_mGammaD_toy_SR1.SetLineColor(1)
    gr_limit_vs_mGammaD_toy_SR1.SetLineWidth(2)
    gr_limit_vs_mGammaD_toy_SR1.SetLineStyle(2) #dashed line, for showing expected median @%XX%CL
    gr_limit_vs_mGammaD_toy_SR1.SetMarkerColor(ROOT.kBlack)
    gr_limit_vs_mGammaD_toy_SR1.Draw("P")
    ## SR2
    gr_limit_vs_mGammaD_toy_SR2 = ROOT.TGraph( len(array_mGammaD_limit_toy_SR2), array.array("d", zip(*array_mGammaD_limit_toy_SR2)[0]), array.array("d", zip(*array_mGammaD_limit_toy_SR2)[1]) )
    gr_limit_vs_mGammaD_toy_SR2.SetLineColor(1)
    gr_limit_vs_mGammaD_toy_SR2.SetLineWidth(2)
    gr_limit_vs_mGammaD_toy_SR2.SetLineStyle(2)
    gr_limit_vs_mGammaD_toy_SR2.SetMarkerColor(ROOT.kBlack)
    gr_limit_vs_mGammaD_toy_SR2.Draw("P")
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_limit_vs_mGammaD_toy_SR3 = ROOT.TGraph( len(array_mGammaD_limit_toy_SR3), array.array("d", zip(*array_mGammaD_limit_toy_SR3)[0]), array.array("d", zip(*array_mGammaD_limit_toy_SR3)[1]) )
        gr_limit_vs_mGammaD_toy_SR3.SetLineColor(1)
        gr_limit_vs_mGammaD_toy_SR3.SetLineWidth(2)
        gr_limit_vs_mGammaD_toy_SR3.SetLineStyle(2)
        gr_limit_vs_mGammaD_toy_SR3.SetMarkerColor(ROOT.kBlack)
        gr_limit_vs_mGammaD_toy_SR3.Draw("P")
    # End: Limit from toy experiments median SR1/2/3

    # Similar as above, but expected +/- 1, 2 sigma @ %XX%CL from toy experiments for Brazilian Plot below
    # An example: https://wiki.physik.uzh.ch/cms/limits:brazilianplotexample
    gr_limit_vs_mGammaD_toy_one_sigma_SR1 = ROOT.TGraph(2*len(array_mGammaD_limit_toy_p_one_sigma_SR1))
    gr_limit_vs_mGammaD_toy_two_sigma_SR1 = ROOT.TGraph(2*len(array_mGammaD_limit_toy_p_two_sigma_SR1)) # length should both equal array_mGammaD_limit_toy
    for i in range(len(array_mGammaD_limit_toy_p_one_sigma_SR1)):
        gr_limit_vs_mGammaD_toy_two_sigma_SR1.SetPoint(i, array_mGammaD_limit_toy_p_two_sigma_SR1[i][0], array_mGammaD_limit_toy_p_two_sigma_SR1[i][1]) # + 2 sigma
        gr_limit_vs_mGammaD_toy_one_sigma_SR1.SetPoint(i, array_mGammaD_limit_toy_p_one_sigma_SR1[i][0], array_mGammaD_limit_toy_p_one_sigma_SR1[i][1]) # + 1 sigma
        gr_limit_vs_mGammaD_toy_one_sigma_SR1.SetPoint(2*len(array_mGammaD_limit_toy_p_one_sigma_SR1)-1-i, array_mGammaD_limit_toy_n_one_sigma_SR1[i][0], array_mGammaD_limit_toy_n_one_sigma_SR1[i][1]) # - 1 sigma
        gr_limit_vs_mGammaD_toy_two_sigma_SR1.SetPoint(2*len(array_mGammaD_limit_toy_p_two_sigma_SR1)-1-i, array_mGammaD_limit_toy_n_two_sigma_SR1[i][0], array_mGammaD_limit_toy_n_two_sigma_SR1[i][1]) # - 2 sigma

    gr_limit_vs_mGammaD_toy_one_sigma_SR2 = ROOT.TGraph(2*len(array_mGammaD_limit_toy_p_one_sigma_SR2))
    gr_limit_vs_mGammaD_toy_two_sigma_SR2 = ROOT.TGraph(2*len(array_mGammaD_limit_toy_p_two_sigma_SR2)) # length should both equal array_mGammaD_limit_toy
    for i in range(len(array_mGammaD_limit_toy_p_one_sigma_SR2)):
        gr_limit_vs_mGammaD_toy_two_sigma_SR2.SetPoint(i, array_mGammaD_limit_toy_p_two_sigma_SR2[i][0], array_mGammaD_limit_toy_p_two_sigma_SR2[i][1]) # + 2 sigma
        gr_limit_vs_mGammaD_toy_one_sigma_SR2.SetPoint(i, array_mGammaD_limit_toy_p_one_sigma_SR2[i][0], array_mGammaD_limit_toy_p_one_sigma_SR2[i][1]) # + 1 sigma
        gr_limit_vs_mGammaD_toy_one_sigma_SR2.SetPoint(2*len(array_mGammaD_limit_toy_p_one_sigma_SR2)-1-i, array_mGammaD_limit_toy_n_one_sigma_SR2[i][0], array_mGammaD_limit_toy_n_one_sigma_SR2[i][1]) # - 1 sigma
        gr_limit_vs_mGammaD_toy_two_sigma_SR2.SetPoint(2*len(array_mGammaD_limit_toy_p_two_sigma_SR2)-1-i, array_mGammaD_limit_toy_n_two_sigma_SR2[i][0], array_mGammaD_limit_toy_n_two_sigma_SR2[i][1]) # - 2 sigma

    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_limit_vs_mGammaD_toy_one_sigma_SR3 = ROOT.TGraph(2*len(array_mGammaD_limit_toy_p_one_sigma_SR3))
        gr_limit_vs_mGammaD_toy_two_sigma_SR3 = ROOT.TGraph(2*len(array_mGammaD_limit_toy_p_two_sigma_SR3)) # length should both equal array_mGammaD_limit_toy
        for i in range(len(array_mGammaD_limit_toy_p_one_sigma_SR3)):
            gr_limit_vs_mGammaD_toy_two_sigma_SR3.SetPoint(i, array_mGammaD_limit_toy_p_two_sigma_SR3[i][0], array_mGammaD_limit_toy_p_two_sigma_SR3[i][1]) # + 2 sigma
            gr_limit_vs_mGammaD_toy_one_sigma_SR3.SetPoint(i, array_mGammaD_limit_toy_p_one_sigma_SR3[i][0], array_mGammaD_limit_toy_p_one_sigma_SR3[i][1]) # + 1 sigma
            gr_limit_vs_mGammaD_toy_one_sigma_SR3.SetPoint(2*len(array_mGammaD_limit_toy_p_one_sigma_SR3)-1-i, array_mGammaD_limit_toy_n_one_sigma_SR3[i][0], array_mGammaD_limit_toy_n_one_sigma_SR3[i][1]) # - 1 sigma
            gr_limit_vs_mGammaD_toy_two_sigma_SR3.SetPoint(2*len(array_mGammaD_limit_toy_p_two_sigma_SR3)-1-i, array_mGammaD_limit_toy_n_two_sigma_SR3[i][0], array_mGammaD_limit_toy_n_two_sigma_SR3[i][1]) # - 2 sigma

    # Start: Fitted function to toy limit: SR1/2/3
    gr_limit_vs_mGammaD_fit_SR1 = ROOT.TGraph( len(array_mGammaD_limit_fit_SR1), array.array("d", zip(*array_mGammaD_limit_fit_SR1)[0]), array.array("d", zip(*array_mGammaD_limit_fit_SR1)[1]) )
    gr_limit_vs_mGammaD_fit_SR1.SetLineWidth(2)
    gr_limit_vs_mGammaD_fit_SR1.SetLineColor(ROOT.kRed)
    gr_limit_vs_mGammaD_fit_SR1.SetLineStyle(1)
    gr_limit_vs_mGammaD_fit_SR1.SetMarkerColor(ROOT.kRed)
    gr_limit_vs_mGammaD_fit_SR1.Draw("L")
    ## SR2
    gr_limit_vs_mGammaD_fit_SR2 = ROOT.TGraph( len(array_mGammaD_limit_fit_SR2), array.array("d", zip(*array_mGammaD_limit_fit_SR2)[0]), array.array("d", zip(*array_mGammaD_limit_fit_SR2)[1]) )
    gr_limit_vs_mGammaD_fit_SR2.SetLineWidth(2)
    gr_limit_vs_mGammaD_fit_SR2.SetLineColor(ROOT.kRed)
    gr_limit_vs_mGammaD_fit_SR2.SetLineStyle(1)
    gr_limit_vs_mGammaD_fit_SR2.SetMarkerColor(ROOT.kRed)
    gr_limit_vs_mGammaD_fit_SR2.Draw("L")
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_limit_vs_mGammaD_fit_SR3 = ROOT.TGraph( len(array_mGammaD_limit_fit_SR3), array.array("d", zip(*array_mGammaD_limit_fit_SR3)[0]), array.array("d", zip(*array_mGammaD_limit_fit_SR3)[1]) )
        gr_limit_vs_mGammaD_fit_SR3.SetLineWidth(2)
        gr_limit_vs_mGammaD_fit_SR3.SetLineColor(ROOT.kRed)
        gr_limit_vs_mGammaD_fit_SR3.SetLineStyle(1)
        gr_limit_vs_mGammaD_fit_SR3.SetMarkerColor(ROOT.kRed)
        gr_limit_vs_mGammaD_fit_SR3.Draw("L")
    # End: Fitted function to toy limit: SR1/2/3

    l_limit_vs_mGammaD = ROOT.TLegend(0.63, 0.65, 0.9, 0.75)
    l_limit_vs_mGammaD.SetFillColor(ROOT.kWhite)
    l_limit_vs_mGammaD.SetMargin(0.13)
    l_limit_vs_mGammaD.SetBorderSize(0)
    l_limit_vs_mGammaD.SetTextFont(42)
    l_limit_vs_mGammaD.SetTextSize(0.035)
    l_limit_vs_mGammaD.AddEntry(gr_limit_vs_mGammaD_toy_SR1, "Toys", "P")
    l_limit_vs_mGammaD.AddEntry(gr_limit_vs_mGammaD_fit_SR1, "Fit",  "L")
    l_limit_vs_mGammaD.Draw()

    txtHeader.Draw()
    cnv.cd()

    # Draw fit errors (as to the toy result) in lower panel
    padBot = ROOT.TPad( "padBot", "padBot", 0.0, 0.0, 1.0, 0.3 )
    padBot.Draw()
    padBot.cd()
    padBot.SetGrid()
    padBot.SetLogx()

    # Specify ranges for mass and fit uncertainty
    h_limit_vs_mGammaD_error_dummy = ROOT.TH2F("h_limit_vs_mGammaD_error_dummy", "h_limit_vs_mGammaD_error_dummy", 1000, m_SR1_min-0.04, MaxGraphMass, 1000, -0.2, 0.2)
    h_limit_vs_mGammaD_error_dummy.SetXTitle("m_{a} [GeV]")
    h_limit_vs_mGammaD_error_dummy.SetYTitle("Fit Uncertainty [%]")
    h_limit_vs_mGammaD_error_dummy.SetTitleOffset(1.1, "Y")
    h_limit_vs_mGammaD_error_dummy.GetXaxis().SetNdivisions(505)
    h_limit_vs_mGammaD_error_dummy.GetYaxis().SetTitleSize(0.05)
    h_limit_vs_mGammaD_error_dummy.Draw()

    gr_limit_vs_mGammaD_fit_uncertainty = ROOT.TGraph( len(array_mGammaD_limit_fit_uncertainty), array.array("d", zip(*array_mGammaD_limit_fit_uncertainty)[0]), array.array("d", zip(*array_mGammaD_limit_fit_uncertainty)[1]) )
    gr_limit_vs_mGammaD_fit_uncertainty.SetLineWidth(1)
    gr_limit_vs_mGammaD_fit_uncertainty.SetLineColor(ROOT.kBlue)
    gr_limit_vs_mGammaD_fit_uncertainty.SetLineStyle(1)
    gr_limit_vs_mGammaD_fit_uncertainty.SetMarkerColor(ROOT.kBlue)
    gr_limit_vs_mGammaD_fit_uncertainty.Draw("P") #Don't draw line, it will connect Jpsi and Upsilon regions
    cnv.cd()
    cnv.Update()
    save_canvas(cnv, "limit_Events_vs_mGammaD_FitUncert")

    # Now simply draw toy (no fit)
    cnv.cd()
    cnv.SetLogx()
    h_limit_vs_mGammaD_dummy.Draw()
    gr_limit_vs_mGammaD_toy_SR1.Draw("P") #toy
    gr_limit_vs_mGammaD_toy_SR2.Draw("P")
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_limit_vs_mGammaD_toy_SR3.Draw("P")
    txtHeader.Draw()
    cnv.Update()
    save_canvas(cnv, "limit_Events_vs_mGammaD")

    ##################
    # Brazilian plot #
    ##################
    # CMS requirment: https://ghm.web.cern.ch/ghm/plots
    cnv.cd()
    cnv.SetLogx()
    h_limit_vs_mGammaD_dummy.Draw()
    gr_limit_vs_mGammaD_toy_two_sigma_SR1.SetFillColor(ROOT.kOrange) #CMS requirement for showing expected 95% CI
    gr_limit_vs_mGammaD_toy_two_sigma_SR1.SetLineColor(ROOT.kOrange)
    gr_limit_vs_mGammaD_toy_two_sigma_SR1.SetFillStyle(1001)
    gr_limit_vs_mGammaD_toy_two_sigma_SR1.Draw("F") #expected +/- 2 sigma
    gr_limit_vs_mGammaD_toy_one_sigma_SR1.SetFillColor(ROOT.kGreen+1) #CMS requirement for showing expected 68% CI
    gr_limit_vs_mGammaD_toy_one_sigma_SR1.SetLineColor(ROOT.kGreen+1)
    gr_limit_vs_mGammaD_toy_one_sigma_SR1.SetFillStyle(1001)
    gr_limit_vs_mGammaD_toy_one_sigma_SR1.Draw("F") #expected +/- 1 sigma
    gr_limit_vs_mGammaD_toy_SR1.Draw("L") #expected median @ %XX% CL
    ## SR2
    gr_limit_vs_mGammaD_toy_two_sigma_SR2.SetFillColor(ROOT.kOrange)
    gr_limit_vs_mGammaD_toy_two_sigma_SR2.SetLineColor(ROOT.kOrange)
    gr_limit_vs_mGammaD_toy_two_sigma_SR2.SetFillStyle(1001)
    gr_limit_vs_mGammaD_toy_two_sigma_SR2.Draw("F")
    gr_limit_vs_mGammaD_toy_one_sigma_SR2.SetFillColor(ROOT.kGreen+1)
    gr_limit_vs_mGammaD_toy_one_sigma_SR2.SetLineColor(ROOT.kGreen+1)
    gr_limit_vs_mGammaD_toy_one_sigma_SR2.SetFillStyle(1001)
    gr_limit_vs_mGammaD_toy_one_sigma_SR2.Draw("F")
    gr_limit_vs_mGammaD_toy_SR2.Draw("L")

    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_limit_vs_mGammaD_toy_two_sigma_SR3.SetFillColor(ROOT.kOrange)
        gr_limit_vs_mGammaD_toy_two_sigma_SR3.SetLineColor(ROOT.kOrange)
        gr_limit_vs_mGammaD_toy_two_sigma_SR3.SetFillStyle(1001)
        gr_limit_vs_mGammaD_toy_two_sigma_SR3.Draw("F")
        gr_limit_vs_mGammaD_toy_one_sigma_SR3.SetFillColor(ROOT.kGreen+1)
        gr_limit_vs_mGammaD_toy_one_sigma_SR3.SetLineColor(ROOT.kGreen+1)
        gr_limit_vs_mGammaD_toy_one_sigma_SR3.SetFillStyle(1001)
        gr_limit_vs_mGammaD_toy_one_sigma_SR3.Draw("F")
        gr_limit_vs_mGammaD_toy_SR3.Draw("L")

    l_limit_Events_vs_mGammaD_Brazil_Bands = ROOT.TLegend(0.6,0.65,0.9,0.75)
    l_limit_Events_vs_mGammaD_Brazil_Bands.SetFillColor(ROOT.kWhite)
    l_limit_Events_vs_mGammaD_Brazil_Bands.SetMargin(0.13)
    l_limit_Events_vs_mGammaD_Brazil_Bands.SetBorderSize(0)
    l_limit_Events_vs_mGammaD_Brazil_Bands.SetTextFont(42)
    l_limit_Events_vs_mGammaD_Brazil_Bands.SetTextSize(0.035)
    l_limit_Events_vs_mGammaD_Brazil_Bands.AddEntry(gr_limit_vs_mGammaD_toy_SR1, "Expected", "L")
    l_limit_Events_vs_mGammaD_Brazil_Bands.AddEntry(gr_limit_vs_mGammaD_toy_one_sigma_SR1, "#pm 1 std. deviation", "f")
    l_limit_Events_vs_mGammaD_Brazil_Bands.AddEntry(gr_limit_vs_mGammaD_toy_two_sigma_SR1, "#pm 2 std. deviation", "f")
    l_limit_Events_vs_mGammaD_Brazil_Bands.Draw()
    txtHeader.Draw()
    cnv.Update()
    save_canvas(cnv, "limit_Events_vs_mGammaD_Brazil_Bands")

    gr_limit_vs_mGammaD_toy_SR1.SaveAs(topDirectory + "/C/limit_Events_vs_mGammaD_SR1.root")
    gr_limit_vs_mGammaD_toy_SR2.SaveAs(topDirectory + "/C/limit_Events_vs_mGammaD_SR2.root")
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_limit_vs_mGammaD_toy_SR3.SaveAs(topDirectory + "/C/limit_Events_vs_mGammaD_SR3.root")


#####################################################################################################
#   Plot Upper Limit on XSec*BR^2*Alpha = "Limit on number of events"/Luminosity/"Scale factor"
#   SF, lumi_fbinv, eFullMc_over_aGen of each year defined in UserConfig.py
#####################################################################################################
def limit_CSxBR2xAlpha_fb_vs_mGammaD():
    print "------------limit_CSxBR2xAlpha_fb_vs_mGammaD------------"
    cnv.SetLogy(0)
    cnv.SetLogx()

    #***************************************************************************
    # Transforming the Limit on N_event to Xsec limit using the fitted function
    #***************************************************************************
    CSxBR2xAlpha_fb_fit_SR1 = []
    CSxBR2xAlpha_fb_fit_SR2 = []
    CSxBR2xAlpha_fb_fit_SR3 = []
    # Specify correct mass ranges, use fitted function
    for m in np.arange(m_SR1_min, m_SR1_max, 0.005):
        CSxBR2xAlpha_fb_fit_SR1.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/eFullMc_over_aGen ))
    for m in np.arange(m_SR2_min, m_SR2_max, 0.005):
        CSxBR2xAlpha_fb_fit_SR2.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/eFullMc_over_aGen ))
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        for m in np.arange(m_SR3_min, m_SR3_max, 0.005):
            CSxBR2xAlpha_fb_fit_SR3.append(( m, fCmsLimitVsM(m)/lumi_fbinv/SF/eFullMc_over_aGen ))

    # specify mass range: MaxGraphMass is specifief in UserConfig for each year
    h_CSxBR2xAlpha_fb_dummy = ROOT.TH2F("h_CSxBR2xAlpha_fb_dummy", "h_CSxBR2xAlpha_fb_dummy", 1000, m_SR1_min-0.04, MaxGraphMass, 1000, 0.0, NMax/lumi_fbinv/SF/eFullMc_over_aGen)
    h_CSxBR2xAlpha_fb_dummy.SetXTitle("m_{a} [GeV]")
    h_CSxBR2xAlpha_fb_dummy.SetYTitle("#sigma(pp #rightarrow 2a + X) B^{2}(a #rightarrow 2 #mu) #alpha_{gen} [fb]")
    h_CSxBR2xAlpha_fb_dummy.SetTitleOffset(1.47, "Y")
    h_CSxBR2xAlpha_fb_dummy.GetXaxis().SetNdivisions(505)
    h_CSxBR2xAlpha_fb_dummy.GetYaxis().SetTitleSize(0.05)
    h_CSxBR2xAlpha_fb_dummy.Draw()

    # Fitted function to toy limit: SR1
    gr_CSxBR2xAlpha_fb_fit_SR1 = ROOT.TGraph( len(CSxBR2xAlpha_fb_fit_SR1), array.array("d", zip(*CSxBR2xAlpha_fb_fit_SR1)[0]), array.array("d", zip(*CSxBR2xAlpha_fb_fit_SR1)[1]) )
    gr_CSxBR2xAlpha_fb_fit_SR1.SetLineWidth(2)
    gr_CSxBR2xAlpha_fb_fit_SR1.SetLineColor(ROOT.kRed)
    gr_CSxBR2xAlpha_fb_fit_SR1.SetLineStyle(1)
    gr_CSxBR2xAlpha_fb_fit_SR1.Draw("C") # Draw smooth curve
    # Fitted function to toy limit: SR2
    gr_CSxBR2xAlpha_fb_fit_SR2 = ROOT.TGraph( len(CSxBR2xAlpha_fb_fit_SR2), array.array("d", zip(*CSxBR2xAlpha_fb_fit_SR2)[0]), array.array("d", zip(*CSxBR2xAlpha_fb_fit_SR2)[1]) )
    gr_CSxBR2xAlpha_fb_fit_SR2.SetLineWidth(2)
    gr_CSxBR2xAlpha_fb_fit_SR2.SetLineColor(ROOT.kRed)
    gr_CSxBR2xAlpha_fb_fit_SR2.SetLineStyle(1)
    gr_CSxBR2xAlpha_fb_fit_SR2.Draw("C")
    # Fitted function to toy limit: SR3
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_CSxBR2xAlpha_fb_fit_SR3 = ROOT.TGraph( len(CSxBR2xAlpha_fb_fit_SR3), array.array("d", zip(*CSxBR2xAlpha_fb_fit_SR3)[0]), array.array("d", zip(*CSxBR2xAlpha_fb_fit_SR3)[1]) )
        gr_CSxBR2xAlpha_fb_fit_SR3.SetLineWidth(2)
        gr_CSxBR2xAlpha_fb_fit_SR3.SetLineColor(ROOT.kRed)
        gr_CSxBR2xAlpha_fb_fit_SR3.SetLineStyle(1)
        gr_CSxBR2xAlpha_fb_fit_SR3.Draw("C")

    l_CSxBR2xAlpha_fb_fit = ROOT.TLegend(0.6,0.65,0.9,0.75)
    l_CSxBR2xAlpha_fb_fit.SetFillColor(ROOT.kWhite)
    l_CSxBR2xAlpha_fb_fit.SetMargin(0.13)
    l_CSxBR2xAlpha_fb_fit.SetBorderSize(0)
    l_CSxBR2xAlpha_fb_fit.SetTextFont(42)
    l_CSxBR2xAlpha_fb_fit.SetTextSize(0.035)
    l_CSxBR2xAlpha_fb_fit.AddEntry(gr_CSxBR2xAlpha_fb_fit_SR1, "%d%% CL upper limits"%CL,"L")
    l_CSxBR2xAlpha_fb_fit.Draw()

    txtHeader.Draw()
    save_canvas(cnv, "CSxBR2xAlpha_fb_fit")

    ##############################################################################
    # Transforming the Limit on N_event to Xsec limit using toy experiment values
    # at discrete mass points, not the fitted function
    ##############################################################################
    CSxBR2xAlpha_fb_toy_median_limit_SR1 = [] #Expected median @specified XX% CL
    CSxBR2xAlpha_fb_toy_median_limit_SR2 = []
    CSxBR2xAlpha_fb_toy_median_limit_SR3 = []
    CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1 = [] #Expected +1 sigma @specified XX% CL
    CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2 = []
    CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3 = []
    CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR1 = [] #Expected -1 sigma @specified XX% CL
    CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR2 = []
    CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR3 = []
    CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR1 = [] #Expected +2 sigma @specified XX% CL
    CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR2 = []
    CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR3 = []
    CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR1 = [] #Expected -2 sigma @specified XX% CL
    CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR2 = []
    CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR3 = []
    # Start: CSxBR2xAlpha
    for m in masses:
        if (m >= m_SR1_min and m <= m_SR1_max):
            CSxBR2xAlpha_fb_toy_median_limit_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p84_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p16_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p975_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR1.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p025_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
        elif (m >= m_SR2_min and m <= m_SR2_max):
            CSxBR2xAlpha_fb_toy_median_limit_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p84_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p16_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p975_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR2.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p025_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
        elif (m >= m_SR3_min and m <= m_SR3_max):
            CSxBR2xAlpha_fb_toy_median_limit_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p5_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p84_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p16_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p975_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
            CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR3.append(( m, ExpectedLimitVsM_HybridNew(m, Expected_Limits_Quantile_0p025_HybridNew)/lumi_fbinv/SF/eFullMc_over_aGen ))
    # End: CSxBR2xAlpha

    # Start: Brazilian Plot CSxBR2xAlpha
    ## SR1
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR1 = ROOT.TGraph( len(CSxBR2xAlpha_fb_toy_median_limit_SR1), array.array("d", zip(*CSxBR2xAlpha_fb_toy_median_limit_SR1)[0]), array.array("d", zip(*CSxBR2xAlpha_fb_toy_median_limit_SR1)[1]) )
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR1.SetLineColor(1)
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR1.SetLineWidth(2)
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR1.SetLineStyle(2) #dashed line, for showing expected median @%XX%CL
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR1.SetMarkerColor(ROOT.kBlack)
    ## SR2
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR2 = ROOT.TGraph( len(CSxBR2xAlpha_fb_toy_median_limit_SR2), array.array("d", zip(*CSxBR2xAlpha_fb_toy_median_limit_SR2)[0]), array.array("d", zip(*CSxBR2xAlpha_fb_toy_median_limit_SR2)[1]) )
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR2.SetLineColor(1)
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR2.SetLineWidth(2)
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR2.SetLineStyle(2)
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR2.SetMarkerColor(ROOT.kBlack)
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_CSxBR2xAlpha_fb_toy_median_limit_SR3 = ROOT.TGraph( len(CSxBR2xAlpha_fb_toy_median_limit_SR3), array.array("d", zip(*CSxBR2xAlpha_fb_toy_median_limit_SR3)[0]), array.array("d", zip(*CSxBR2xAlpha_fb_toy_median_limit_SR3)[1]) )
        gr_CSxBR2xAlpha_fb_toy_median_limit_SR3.SetLineColor(1)
        gr_CSxBR2xAlpha_fb_toy_median_limit_SR3.SetLineWidth(2)
        gr_CSxBR2xAlpha_fb_toy_median_limit_SR3.SetLineStyle(2)
        gr_CSxBR2xAlpha_fb_toy_median_limit_SR3.SetMarkerColor(ROOT.kBlack)

    # Similar as above, but expected +/- 1, 2 sigma @ %XX%CL from toy experiments
    ## SR1
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1 = ROOT.TGraph(2*len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1))
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1 = ROOT.TGraph(2*len(CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR1)) # length should equal to above
    for i in range(len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1)):
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1.SetPoint(i, CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR1[i][0], CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR1[i][1]) # + 2 sigma
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1.SetPoint(i, CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1[i][0], CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1[i][1]) # + 1 sigma
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1.SetPoint(2*len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR1)-1-i, CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR1[i][0], CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR1[i][1]) # - 1 sigma
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1.SetPoint(2*len(CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR1)-1-i, CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR1[i][0], CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR1[i][1]) # - 2 sigma

    ## SR2
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2 = ROOT.TGraph(2*len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2))
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2 = ROOT.TGraph(2*len(CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR2)) # length should equal to above
    for i in range(len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2)):
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2.SetPoint(i, CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR2[i][0], CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR2[i][1]) # + 2 sigma
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2.SetPoint(i, CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2[i][0], CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2[i][1]) # + 1 sigma
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2.SetPoint(2*len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR2)-1-i, CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR2[i][0], CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR2[i][1]) # - 1 sigma
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2.SetPoint(2*len(CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR2)-1-i, CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR2[i][0], CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR2[i][1]) # - 2 sigma
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3 = ROOT.TGraph(2*len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3))
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3 = ROOT.TGraph(2*len(CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR3)) # length should equal to above
        for i in range(len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3)):
            gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3.SetPoint(i, CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR3[i][0], CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR3[i][1]) # + 2 sigma
            gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3.SetPoint(i, CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3[i][0], CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3[i][1]) # + 1 sigma
            gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3.SetPoint(2*len(CSxBR2xAlpha_fb_toy_p_one_sigma_limit_SR3)-1-i, CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR3[i][0], CSxBR2xAlpha_fb_toy_n_one_sigma_limit_SR3[i][1]) # - 1 sigma
            gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3.SetPoint(2*len(CSxBR2xAlpha_fb_toy_p_two_sigma_limit_SR3)-1-i, CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR3[i][0], CSxBR2xAlpha_fb_toy_n_two_sigma_limit_SR3[i][1]) # - 2 sigma

    cnv.cd()
    cnv.SetLogx()
    h_CSxBR2xAlpha_fb_dummy.Draw()
    ## SR1
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1.SetFillColor(ROOT.kOrange) #CMS requirement for showing expected 95% CI
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1.SetLineColor(ROOT.kOrange)
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1.SetFillStyle(1001)
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1.Draw("F") #expected +/- 2 sigma
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1.SetFillColor(ROOT.kGreen+1) #CMS requirement for showing expected 68% CI
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1.SetLineColor(ROOT.kGreen+1)
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1.SetFillStyle(1001)
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1.Draw("F") #expected +/- 1 sigma
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR1.Draw("L") #expected median @ %XX% CL
    ## SR2
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2.SetFillColor(ROOT.kOrange)
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2.SetLineColor(ROOT.kOrange)
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2.SetFillStyle(1001)
    gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR2.Draw("F")
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2.SetFillColor(ROOT.kGreen+1)
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2.SetLineColor(ROOT.kGreen+1)
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2.SetFillStyle(1001)
    gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR2.Draw("F")
    gr_CSxBR2xAlpha_fb_toy_median_limit_SR2.Draw("L")
    ###########################################################
    ## SR3: don't plot this region if do combine for 2016+2018
    ###########################################################
    if year != 2020:
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3.SetFillColor(ROOT.kOrange)
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3.SetLineColor(ROOT.kOrange)
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3.SetFillStyle(1001)
        gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR3.Draw("F")
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3.SetFillColor(ROOT.kGreen+1)
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3.SetLineColor(ROOT.kGreen+1)
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3.SetFillStyle(1001)
        gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR3.Draw("F")
        gr_CSxBR2xAlpha_fb_toy_median_limit_SR3.Draw("L")

    l_CSxBR2xAlpha_fb_toy_Brazil_Bands = ROOT.TLegend(0.6,0.65,0.9,0.75)
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.SetFillColor(ROOT.kWhite)
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.SetMargin(0.13)
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.SetBorderSize(0)
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.SetTextFont(42)
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.SetTextSize(0.035)
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.AddEntry(gr_CSxBR2xAlpha_fb_toy_median_limit_SR1, "Expected", "L")
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.AddEntry(gr_CSxBR2xAlpha_fb_toy_one_sigma_limit_SR1, "#pm 1 std. deviation", "f")
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.AddEntry(gr_CSxBR2xAlpha_fb_toy_two_sigma_limit_SR1, "#pm 2 std. deviation", "f")
    l_CSxBR2xAlpha_fb_toy_Brazil_Bands.Draw()
    txtHeader.Draw()
    cnv.Update()
    save_canvas(cnv, "CSxBR2xAlpha_fb_toy_Brazil_Bands")

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
    ## Specify correct mass ranges
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
    h_Alpha_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV]")
    h_Alpha_vs_mGammaD_dummy.SetYTitle("#alpha (c#tau_{#gamma_{D}}, m_{#gamma_{D}}) [%]")
    h_Alpha_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
    #h_Alpha_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
    h_Alpha_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)
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

    cnv.SaveAs(topDirectory + "/PDF/Alpha_vs_mGammaD_2015.pdf")
    cnv.SaveAs(topDirectory + "/C/Alpha_vs_mGammaD_2015.C")
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
    #h_Alpha_vs_ctau_dummy.GetYaxis().CenterTitle(1)
    h_Alpha_vs_ctau_dummy.GetYaxis().SetTitleSize(0.05)
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

    grErr_Alpha_vs_ctau_m025GeV_Marker = ROOT.TGraphErrors( len(array_Alpha_vs_ctau_m025GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[1]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[2]), array.array("d", zip(*array_Alpha_vs_ctau_m025GeV_Marker)[3]) )
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

    grErr_Alpha_vs_ctau_m04GeV_Marker = ROOT.TGraphErrors( len(array_Alpha_vs_ctau_m04GeV_Marker), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[0]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[1]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[2]), array.array("d", zip(*array_Alpha_vs_ctau_m04GeV_Marker)[3]) )
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
    l_Alpha_vs_ctau.AddEntry(gr_Alpha_vs_ctau_m04GeV, "m_{#gamma_{D}} =  0.4 GeV","LP")
    #  l_Alpha_vs_ctau.AddEntry(gr_Alpha_vs_ctau_m1GeV,  "m_{#gamma_{D}} =  1.0 GeV/#it{c}^{2}","L")
    l_Alpha_vs_ctau.Draw()

    txtHeader.Draw()
    cnv.SaveAs(topDirectory + "/PDF/Alpha_vs_ctau_2015.pdf")
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
    R_mm_bot = 0.0
    R_mm_top = 650.0
    array_Eff_vs_R = []
    for R_mm in fRange(R_mm_bot, R_mm_top, 651):
        # array_Eff_vs_R.append(( R_mm, Eff_vs_R(R0_mm, R_mm) )) # Below is modified version of the efficiency. We decided to use 0 efficiency after first layer of pixel
        if R_mm < R0_mm: array_Eff_vs_R.append(( R_mm, 1.0 ))
        else:            array_Eff_vs_R.append(( R_mm, 0.0 ))

    h_Eff_vs_R_dummy = ROOT.TH2F("h_Eff_vs_R_dummy", "h_Eff_vs_R_dummy", 650, R_mm_bot, R_mm_top, 1000, 0.0, 1.1)
    h_Eff_vs_R_dummy.SetXTitle("Radius from beamline [mm]")
    h_Eff_vs_R_dummy.SetYTitle("#epsilon")
    #h_Eff_vs_R_dummy.GetYaxis().CenterTitle(1)
    h_Eff_vs_R_dummy.Draw()
    gr_Eff_vs_R = ROOT.TGraph( len(array_Eff_vs_R), array.array("d", zip(*array_Eff_vs_R)[0]), array.array("d", zip(*array_Eff_vs_R)[1]) )
    gr_Eff_vs_R.SetLineWidth(2)
    gr_Eff_vs_R.SetLineColor(ROOT.kRed)
    gr_Eff_vs_R.SetLineStyle(1)
    gr_Eff_vs_R.Draw("L")
    txtHeader.Draw()
    cnv.SaveAs(topDirectory + "/PDF/Eff_vs_R.pdf")
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
    h_Alpha_vs_mGammaD_ctau_3D.SetXTitle("m_{#gamma_{D}} [GeV]")
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
            m = h_Alpha_vs_mGammaD_ctau_3D.GetXaxis().GetBinCenter( i_m    + 1 )
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

    gr_Alpha_vs_ctau_m1GeV_Marker = ROOT.TGraph2D( len(array_Alpha_vs_mGammaD_ctau_3D_Marker), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau_3D_Marker)[0]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau_3D_Marker)[1]), array.array("d", zip(*array_Alpha_vs_mGammaD_ctau_3D_Marker)[2]) )
    gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerColor(ROOT.kRed)
    gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerStyle(20)
    gr_Alpha_vs_ctau_m1GeV_Marker.SetMarkerSize(1.5)
    gr_Alpha_vs_ctau_m1GeV_Marker.Draw("sameP")

    txtHeader.Draw()

    save_canvas(cnv,"Alpha_vs_mGammaD_ctau_3D")

################################################################################
#       Plot Upper %XX% CL Limit on CSxBR2 vs mGammaD: 0.25 < mGammaD < 1.0
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
    h_limit_CSxBR2_fb_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV]")
    h_limit_CSxBR2_fb_vs_mGammaD_dummy.SetYTitle("#sigma(pp #rightarrow 2#gamma_{D} + X) B^{2}(#gamma_{D} #rightarrow 2 #mu) [fb]")
    h_limit_CSxBR2_fb_vs_mGammaD_dummy.SetTitleOffset(1.35, "Y")
    h_limit_CSxBR2_fb_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
    h_limit_CSxBR2_fb_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)
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
    l_limit_CSxBR2_fb_vs_mGammaD.SetHeader("%d%% CL limits for samples with #gamma_{D} life-time:"%CL)
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau0mm, "c#tau_{#gamma_{D}} =   0 mm (prompt)","L")
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau02mm,"c#tau_{#gamma_{D}} = 0.2 mm","L")
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau05mm,"c#tau_{#gamma_{D}} = 0.5 mm","L")
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau2mm, "c#tau_{#gamma_{D}} =   2 mm","L")
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_mGammaD_ctau5mm, "c#tau_{#gamma_{D}} =   5 mm","L")
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_prediction_CSxBR2_fb_vs_mGammaD, "prediction with Br(h #rightarrow 2n_{1}) = 0.25%","L")
    l_limit_CSxBR2_fb_vs_mGammaD.AddEntry(gr_prediction_CSxBR2_fb_vs_mGammaD, "and Br(n_{1} #rightarrow #gamma_{D} n_{D}) = 50%","")
    l_limit_CSxBR2_fb_vs_mGammaD.Draw()

    txtHeader.Draw()
    cnv.SaveAs(topDirectory + "/PDF/limit_CSxBR2_fb_vs_mGammaD_2015.pdf")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CSxBR2_fb_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/limit_CSxBR2_fb_vs_mGammaD_2015.png")

################################################################################
#       Plot Upper %XX% CL Limit on CS vs mGammaD: 0.25 < mGammaD < 1.0
################################################################################
def limit_CS_fb_vs_mGammaD_2015():
    cnv.SetLogy(0)
    array_mGammaD_prediction_CS_fb   = []
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
    h_limit_CS_fb_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV]")
    h_limit_CS_fb_vs_mGammaD_dummy.SetYTitle("#sigma(pp #rightarrow h) #times Br(h #rightarrow 2#gamma_{D} + X) [fb]")
    h_limit_CS_fb_vs_mGammaD_dummy.SetTitleOffset(1.35, "Y")
    h_limit_CS_fb_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
    h_limit_CS_fb_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)
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
    l_limit_CS_fb_vs_mGammaD.SetHeader("%d%% CL limits for samples"%CL)
    l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau0mm, "with #gamma_{D} life-time:","")
    l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau0mm, "c#tau_{#gamma_{D}} =   0 mm (prompt)","L")
    l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau02mm,"c#tau_{#gamma_{D}} = 0.2 mm","L")
    l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau05mm,"c#tau_{#gamma_{D}} = 0.5 mm","L")
    l_limit_CS_fb_vs_mGammaD.AddEntry(gr_limit_CS_fb_vs_mGammaD_ctau2mm, "c#tau_{#gamma_{D}} =   2 mm","L")
    l_limit_CS_fb_vs_mGammaD.Draw()

    txtHeader.Draw()
    cnv.SaveAs(topDirectory + "/PDF/limit_CS_fb_vs_mGammaD_2015.pdf")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CS_fb_vs_mGammaD_2015.pdf -resize 900x900 plots/PNG/limit_CS_fb_vs_mGammaD_2015.png")

################################################################################
#         Plot Upper %XX% CL Limit on CSxBR2 vs ctau: 0.2 < ctau < 2.0
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
    h_limit_CSxBR2_fb_vs_ctau_dummy.GetYaxis().SetTitleSize(0.05)
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
    l_limit_CSxBR2_fb_vs_ctau.SetHeader("%d%% CL limits for samples"%CL)
    l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m025GeV,"with #gamma_{D} mass:","")
    l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m025GeV,"m_{#gamma_{D}} = 0.25 GeV","L")
    l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m04GeV, "m_{#gamma_{D}} =  0.4 GeV","L")
    l_limit_CSxBR2_fb_vs_ctau.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m1GeV,  "m_{#gamma_{D}} =  1.0 GeV","L")
    l_limit_CSxBR2_fb_vs_ctau.Draw()

    txtHeader.Draw()
    cnv.SaveAs(topDirectory + "/PDF/limit_CSxBR2_fb_vs_ctau_2015.pdf")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/limit_CSxBR2_fb_vs_ctau_2015.pdf -resize 900x900 plots/PNG/limit_CSxBR2_fb_vs_ctau_2015.png")

################################################################################
#            Plot %XX% CL Limit on CSxBR2 and on CS vs mGammaD and ctau
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
    h_ctau_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV]")
    h_ctau_vs_mGammaD_dummy.SetYTitle("c#tau_{#gamma_{D}} [mm]")
    h_ctau_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
    h_ctau_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
    h_ctau_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)

    nBins = 100

    h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D = ROOT.TH2F("h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D", "h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D", nBins, mGammaD_GeV_min, mGammaD_GeV_max, nBins, ctau_mm_min, ctau_mm_max)
    h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.SetXTitle("m_{#gamma_{D}} [GeV]")
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
    h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)

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
    save_canvas(cnv, "limit_CSxBR2_fb_vs_mGammaD_ctau_3D")

    h_ctau_vs_mGammaD_dummy.Draw()
    h_limit_CSxBR2_fb_vs_mGammaD_ctau_3D.Draw("sameCONT3COLZ")

    line_m_ctau_5.Draw()
    line_ctau_m_025.Draw()
    line_ctau_m_1.Draw()

    txtHeader.Draw()
    save_canvas(cnv, "limit_CSxBR2_fb_vs_mGammaD_ctau_2D")

    ##############################################################################
    cnv.SetLogz(1)
    h_limit_CS_fb_vs_mGammaD_ctau_3D.Draw("surf1z")
    txtHeader.Draw()
    save_canvas(cnv, "limit_CS_fb_vs_mGammaD_ctau_3D")

    h_ctau_vs_mGammaD_dummy.Draw()
    h_limit_CS_fb_vs_mGammaD_ctau_3D.Draw("sameCONT3COLZ")

    line_m_ctau_5.Draw()
    line_ctau_m_025.Draw()
    line_ctau_m_1.Draw()

    txtHeader.Draw()
    save_canvas(cnv, "limit_CS_fb_vs_mGammaD_ctau_2D")

    ##############################################################################
    cnv.SetLogz(1)

    h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.Draw("surf1z")

    txtHeader.Draw()
    save_canvas(cnv, "limit_CS_over_CSsm_vs_mGammaD_ctau_3D")

    h_ctau_vs_mGammaD_dummy.Draw()
    h_limit_CS_over_CSsm_vs_mGammaD_ctau_3D.Draw("sameCONT3COLZ")

    line_m_ctau_5.Draw()
    line_ctau_m_025.Draw()
    line_ctau_m_1.Draw()

    txtHeader.Draw()
    save_canvas(cnv,"limit_CS_over_CSsm_vs_mGammaD_ctau_2D")

    ##############################################################################
    cnv.SetLogz(1)
    h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.Draw("surf1z")
    txtHeader.Draw()
    save_canvas(cnv,"limit_CS_over_CSsm_vs_mGammaD_epsilon2_3D")
    h_logEpsilon2_vs_mGammaD_dummy.Draw()
    #  h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.Draw("sameCONT3COLZ")
    h_limit_CS_over_CSsm_vs_mGammaD_logEpsilon2_3D.Draw("sameCONT3")


    #  axis = ROOT.TGaxis(0.0,0.2,0.0,2.2,0.001,10000,510,"")
    #  axis.Draw()

    line_m_ctau_5.Draw()
    line_logEpsilon2_m_025.Draw()
    line_logEpsilon2_m_1.Draw()

    txtHeader.Draw()
    save_canvas(cnv,"limit_CS_over_CSsm_vs_mGammaD_epsilon2_2D")

################################################################################
#  Plot %XX% CL Limit lines on CSxBR2 vs (mGammaD, ctau) and (mGammaD, epsilon^2)
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
    h_ctau_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)

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
    h_epsilon2_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)

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
        l_ctau_vs_mGammaD_K.SetHeader("%d%% CL "%CL+"limits for K = %s"%K)
        l_ctau_vs_mGammaD_K.AddEntry(h_ctau_vs_mGammaD_excl, "excluded region","F")
        l_ctau_vs_mGammaD_K.AddEntry(h_ctau_vs_mGammaD_incl, "not excluded region","F")
        l_ctau_vs_mGammaD_K.Draw()

        txtHeader.Draw()

        cnv.SaveAs(topDirectory + "/PDF/limit_Lines_CSxBR2_fb_vs_mGammaD_ctau_K%s.pdf"%K)
        cnv.SaveAs(topDirectory + "/PNG/limit_Lines_CSxBR2_fb_vs_mGammaD_ctau_K%s.png"%K)

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
        l_epsilon2_vs_mGammaD_K.SetHeader("%d%% CL "%CL+"limits for K = %s"%K)
        l_epsilon2_vs_mGammaD_K.AddEntry(gr_epsilon2_vs_mGammaD_excl_K, "excluded region","F")
        l_epsilon2_vs_mGammaD_K.AddEntry(gr_epsilon2_vs_mGammaD_incl_K, "not excluded region","F")
        l_epsilon2_vs_mGammaD_K.Draw()

        txtHeader.Draw()

        cnv.SaveAs(topDirectory + "/PDF/limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2_K%s.pdf"%K)
        cnv.SaveAs(topDirectory + "/PNG/limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2_K%s.png"%K)

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
    l_ctau_vs_mGammaD.SetHeader("%d%% CL limits for different K"%d)
    #  l_ctau_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_ctau_m025GeV,"m_{#gamma_{D}} = 0.25 GeV/#it{c}^{2}","L")
    l_ctau_vs_mGammaD.Draw()

    txtHeader.Draw()

    save_canvas(cnv,"limit_Lines_CSxBR2_fb_vs_mGammaD_ctau")

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
    l_epsilon2_vs_mGammaD.SetHeader("%d%% CL limits for different K"%CL)
    #  l_epsilon2_vs_mGammaD.AddEntry(gr_limit_CSxBR2_fb_vs_epsilon2_m025GeV,"m_{#gamma_{D}} = 0.25 GeV/#it{c}^{2}","L")
    l_epsilon2_vs_mGammaD.Draw()

    txtHeader.Draw()

    save_canvas(cnv,"limit_Lines_CSxBR2_fb_vs_mGammaD_epsilon2")

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
    h_width_over_e2_GeV_dummy.GetYaxis().SetTitleSize(0.05)
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

    cnv.SaveAs(topDirectory + "/PDF/GammaD_Width_over_e2_GeV.pdf")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/GammaD_Width_over_e2_GeV.pdf -resize 900x900 plots/PNG/GammaD_Width_over_e2_GeV.png")

    h_width_over_e2_GeV_inverted_dummy = ROOT.TH2F("h_width_over_e2_GeV_inverted_dummy", "h_width_over_e2_GeV_inverted_dummy", 1000, mGammaD_GeV_bot, mGammaD_GeV_top, 1000, 1.0/5.0, 1.0/0.000005)
    h_width_over_e2_GeV_inverted_dummy.SetXTitle("m_{#gamma_{D}} [GeV/#it{c}^{2}]")
    h_width_over_e2_GeV_inverted_dummy.SetYTitle("f(m_{#gamma_{D}}) = (#Gamma_{#gamma_{D}} / #epsilon^{2})^{-1} [GeV^{-1}]")
    h_width_over_e2_GeV_inverted_dummy.SetTitleOffset(1.33, "Y")
    h_width_over_e2_GeV_inverted_dummy.GetYaxis().CenterTitle(1)
    h_width_over_e2_GeV_inverted_dummy.GetYaxis().SetTitleSize(0.05)
    h_width_over_e2_GeV_inverted_dummy.SetMinimum(0.00001)
    h_width_over_e2_GeV_inverted_dummy.Draw()

    gr_width_total_over_e2_GeV_inverted = ROOT.TGraph( len(array_mGammaD_width_total_over_e2_GeV_inverted), array.array("d", zip(*array_mGammaD_width_total_over_e2_GeV_inverted)[0]), array.array("d", zip(*array_mGammaD_width_total_over_e2_GeV_inverted)[1]) )
    gr_width_total_over_e2_GeV_inverted.SetLineWidth(2)
    gr_width_total_over_e2_GeV_inverted.SetLineColor(ROOT.kRed)
    gr_width_total_over_e2_GeV_inverted.SetLineStyle(1)
    gr_width_total_over_e2_GeV_inverted.Draw("C")

    save_canvas(cnv,"GammaD_Width_over_e2_GeV_inverted")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/GammaD_Width_over_e2_GeV_inverted.pdf -resize 900x900 plots/PNG/GammaD_Width_over_e2_GeV_inverted.png")

################################################################################
#                Plot Branching Fraction BR(gammaD -> 2mu)
################################################################################
def plot_BR_GammaD_to_2mu():
    print "------------plot_BR_GammaD_to_2mu------------"
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
    h_width_over_e2_GeV_dummy.GetYaxis().SetTitleSize(0.05)
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

    save_canvas(cnv,"GammaD_BR_to_2mu")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/GammaD_BR_to_2mu.pdf -resize 900x900 plots/PNG/GammaD_BR_to_2mu.png")

################################################################################
#             Plot lines with constant ctau in (epsilon2, m) plane
################################################################################

def plot_ctauConst_vs_logEpsilon2_mGammaD():
    h_logEpsilon2_vs_mGammaD_dummy = ROOT.TH2F("h_logEpsilon2_vs_mGammaD_dummy", "h_logEpsilon2_vs_mGammaD_dummy", 100, mGammaD_GeV_bot, mGammaD_GeV_top, 100, logEpsilon2_min, logEpsilon2_max)
    h_logEpsilon2_vs_mGammaD_dummy.SetXTitle("m_{#gamma_{D}} [GeV]")
    h_logEpsilon2_vs_mGammaD_dummy.SetYTitle("log_{10}(#epsilon^{2})")
    h_logEpsilon2_vs_mGammaD_dummy.SetTitleOffset(1.1, "Y")
    h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().CenterTitle(1)
    h_logEpsilon2_vs_mGammaD_dummy.GetYaxis().SetTitleSize(0.05)
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

    cnv.SaveAs(topDirectory + "/PDF/ctauConst_vs_logEpsilon2_mGammaD.pdf")
    os.system("convert -define pdf:use-cropbox=true -density 300 plots/PDF/ctauConst_vs_logEpsilon2_mGammaD.pdf -resize 900x900 plots/PNG/ctauConst_vs_logEpsilon2_mGammaD.png")

################################################################################
#
#                                 NMSSM Plots
#
################################################################################

################################################################################
#                 Plot limit on CSxBr2 vs ma
################################################################################
def limit_CSxBR2_fb_vs_ma():
    print "----------- NMSSM limit_CSxBR2_fb_vs_ma -----------"
    BR_h_aa = 0.003 #reference
    cnv.SetLogy(1)
    cnv.SetLogx(0)
    h_CSxBR_vs_ma_dummy = ROOT.TH2F("h_CSxBR_vs_ma_dummy", "h_CSxBR_vs_ma_dummy", 1000, 0.21, 3.3, 1000, 0.08, 150.)
    h_CSxBR_vs_ma_dummy.SetXTitle("m_{a_{1}} [GeV]")
    h_CSxBR_vs_ma_dummy.SetYTitle("#sigma(pp #rightarrow h_{i} #rightarrow 2a_{1}) B^{2}(a_{1} #rightarrow 2 #mu) [fb]")
    h_CSxBR_vs_ma_dummy.SetTitleOffset(1.1, "Y")
    #h_CSxBR_vs_ma_dummy.GetYaxis().CenterTitle(1)
    h_CSxBR_vs_ma_dummy.GetYaxis().SetTitleSize(0.05)
    h_CSxBR_vs_ma_dummy.SetNdivisions(20210, "Y")
    h_CSxBR_vs_ma_dummy.Draw()

    #Draw actual upper limits
    array_ma_mh_90  = []
    array_ma_mh_125 = []
    array_ma_mh_150 = []
    for ma_i in array_ma: #defined in UserInput.py
        array_ma_mh_90.append((  ma_i, fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmExtrapolate(ma_i, 90.,  CmsNmssmAcceptance) ))
        array_ma_mh_125.append(( ma_i, fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmExtrapolate(ma_i, 125., CmsNmssmAcceptance) ))
        array_ma_mh_150.append(( ma_i, fCmsLimitVsM(ma_i)/lumi_fbinv/SF/fCmsNmssmExtrapolate(ma_i, 150., CmsNmssmAcceptance) ))

    gr_CSxBR_vs_ma_mh_90 = ROOT.TGraph(len(array_ma_mh_90), array.array("d", zip(*array_ma_mh_90)[0]), array.array("d", zip(*array_ma_mh_90)[1]))
    gr_CSxBR_vs_ma_mh_90.SetLineWidth(2)
    gr_CSxBR_vs_ma_mh_90.SetLineColor(ROOT.kMagenta+2)
    gr_CSxBR_vs_ma_mh_90.SetLineStyle(9)
    gr_CSxBR_vs_ma_mh_90.SetMarkerColor(ROOT.kMagenta+2)
    gr_CSxBR_vs_ma_mh_90.SetMarkerStyle(22)
    gr_CSxBR_vs_ma_mh_90.SetMarkerSize(1.5)
    gr_CSxBR_vs_ma_mh_90.Draw("CP")

    gr_CSxBR_vs_ma_mh_125 = ROOT.TGraph(len(array_ma_mh_125), array.array("d", zip(*array_ma_mh_125)[0]), array.array("d", zip(*array_ma_mh_125)[1]))
    gr_CSxBR_vs_ma_mh_125.SetLineWidth(2)
    gr_CSxBR_vs_ma_mh_125.SetLineColor(2)
    gr_CSxBR_vs_ma_mh_125.SetLineStyle(6)
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

    #Draw reference model
    array_ma_mh_125_SM = []
    for ma_i in fRange(0.5, 3.0, 100):
        CS_h125_fb = 1000.0*fCS_SM_ggH_13TeV_pb(125.)[0]
        CS_h125_fb = CS_h125_fb + CS_h125_fb * (1000.0*fCS_SM_VBFH_13TeV_pb(125.)[0])/(1000.0*fCS_SM_ggH_13TeV_pb(125.)[0])                      # Adding VBF contribution, assuming it have the same acceptance in analsyis. Verifyied in 2016 analysis.
        CS_h125_fb = CS_h125_fb + CS_h125_fb * (1000.0*fCS_SM_HW_13TeV_pb(125.)[0])/(1000.0*fCS_SM_ggH_13TeV_pb(125.)[0]) + CS_h125_fb * (0.02)  # Adding WH Contribution, assuming acceptance is 10% instead of 12% (measured with cutflow tables in gg and VH NMSSM samples)
        CS_h125_fb = CS_h125_fb + CS_h125_fb * (1000.0*fCS_SM_HZ_13TeV_pb(125.)[0])/(1000.0*fCS_SM_ggH_13TeV_pb(125.)[0]) + CS_h125_fb * (0.02)  # Adding ZH Contribution, assuming acceptance is 10% instead of 12% (measured with cutflow tables in gg and VH NMSSM samples)
        Br_a_mumu = fNMSSM_Br_a(ma_i, 20., 'mumu')
        CSxBR = CS_h125_fb*BR_h_aa*Br_a_mumu*Br_a_mumu
        array_ma_mh_125_SM.append(( ma_i, CSxBR ))

    gr_CSxBR_vs_ma_mh_125_SM = ROOT.TGraph(len(array_ma_mh_125_SM), array.array("d", zip(*array_ma_mh_125_SM)[0]), array.array("d", zip(*array_ma_mh_125_SM)[1]))
    gr_CSxBR_vs_ma_mh_125_SM.SetLineWidth(3)
    gr_CSxBR_vs_ma_mh_125_SM.SetLineColor(ROOT.kGreen+3)
    gr_CSxBR_vs_ma_mh_125_SM.SetLineStyle(1)
    gr_CSxBR_vs_ma_mh_125_SM.Draw("C")

    l_CSxBR_vs_ma = ROOT.TLegend(0.35,0.72,0.9,0.92)
    l_CSxBR_vs_ma.SetFillColor(ROOT.kWhite)
    l_CSxBR_vs_ma.SetMargin(0.13)
    l_CSxBR_vs_ma.SetBorderSize(0)
    l_CSxBR_vs_ma.SetTextFont(42)
    l_CSxBR_vs_ma.SetTextSize(0.035)
    l_CSxBR_vs_ma.SetHeader("NMSSM: Expected %d%% CL upper limits:"%CL)
    l_CSxBR_vs_ma.AddEntry(gr_CSxBR_vs_ma_mh_90, "m_{h_{1}} =  90 GeV", "LP")
    l_CSxBR_vs_ma.AddEntry(gr_CSxBR_vs_ma_mh_125,"m_{h_{1}} = 125 GeV", "LP")
    l_CSxBR_vs_ma.AddEntry(gr_CSxBR_vs_ma_mh_150,"m_{h_{2}} = 150 GeV", "LP")
    l_CSxBR_vs_ma.Draw()

    l_CSxBR_vs_ma_2 = ROOT.TLegend(0.35,0.56,0.9,0.71)
    l_CSxBR_vs_ma_2.SetFillColor(ROOT.kWhite)
    l_CSxBR_vs_ma_2.SetMargin(0.13)
    l_CSxBR_vs_ma_2.SetBorderSize(0)
    l_CSxBR_vs_ma_2.SetTextFont(42)
    l_CSxBR_vs_ma_2.SetTextSize(0.035)
    l_CSxBR_vs_ma_2.SetHeader("Reference model:")
    l_CSxBR_vs_ma_2.AddEntry(gr_CSxBR_vs_ma_mh_125_SM,"#sigma(pp #rightarrow h_{i} #rightarrow 2a_{1}) = 0.003 #times #sigma_{SM}","L")
    l_CSxBR_vs_ma_2.AddEntry(gr_CSxBR_vs_ma_mh_125_SM,"#sigma(pp #rightarrow h_{j}) #times B(h_{j} #rightarrow 2a_{1}) = 0 for j #neq i","")
    l_CSxBR_vs_ma_2.Draw()

    gr_CSxBR_vs_ma_mh_125_SM.Draw("C")
    txtHeader.Draw()

    save_canvas(cnv,"CSxBR_NMSSM_vs_ma")

################################################################################
#                 Plot limit on CSxBr2 vs mh
################################################################################
def limit_CSxBR2_fb_vs_mh():
    print "----------- NMSSM limit_CSxBR2_fb_vs_mh -----------"
    BR_h_aa = 0.003 #reference
    cnv.SetLogy(0)
    cnv.SetLogx(0)
    h_CSxBR_NMSSM_vs_mh_dummy = ROOT.TH2F("h_CSxBR_NMSSM_vs_mh_dummy", "h_CSxBR_NMSSM_vs_mh_dummy", 1000, 85., 155., 1000, 0., 3.2)
    h_CSxBR_NMSSM_vs_mh_dummy.SetXTitle("m_{h_{i}} [GeV]")
    h_CSxBR_NMSSM_vs_mh_dummy.SetYTitle("#sigma(pp #rightarrow h_{i}#rightarrow 2a_{1}) B^{2}(a_{1}#rightarrow 2 #mu) [fb]")
    h_CSxBR_NMSSM_vs_mh_dummy.SetTitleOffset(1.2, "Y")
    #h_CSxBR_NMSSM_vs_mh_dummy.GetYaxis().CenterTitle(1)
    h_CSxBR_NMSSM_vs_mh_dummy.GetYaxis().SetTitleSize(0.05)
    #h_CSxBR_NMSSM_vs_mh_dummy.SetTitleOffset(1.1, "X")
    #h_CSxBR_NMSSM_vs_mh_dummy.GetXaxis().CenterTitle(1)
    #h_CSxBR_NMSSM_vs_mh_dummy.GetXaxis().SetTitleSize(0.05)
    h_CSxBR_NMSSM_vs_mh_dummy.Draw()

    array_mh_CSxBR_NMSSM_ma_0p5 = []
    array_mh_CSxBR_NMSSM_ma_3 = []
    for mh_i in array_mh:
        array_mh_CSxBR_NMSSM_ma_0p5.append(( mh_i, fCmsLimitVsM(0.5)/lumi_fbinv/SF/fCmsNmssmExtrapolate(0.5, mh_i, CmsNmssmAcceptance) )) # Model Independent limits transformed to Xsec
        array_mh_CSxBR_NMSSM_ma_3.append(( mh_i,   fCmsLimitVsM(3)/lumi_fbinv/SF/fCmsNmssmExtrapolate(3, mh_i, CmsNmssmAcceptance) ))

    gr_CSxBR_NMSSM_vs_mh_ma_0p5 = ROOT.TGraph(len(array_mh_CSxBR_NMSSM_ma_0p5), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_0p5)[0]), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_0p5)[1]))
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.SetLineWidth(2)
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.SetLineColor(ROOT.kMagenta+2)
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.SetLineStyle(9)
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.SetMarkerColor(ROOT.kMagenta+2)
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.SetMarkerStyle(22)
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.SetMarkerSize(1.5)

    gr_CSxBR_NMSSM_vs_mh_ma_3 = ROOT.TGraph(len(array_mh_CSxBR_NMSSM_ma_3), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_3)[0]), array.array("d", zip(*array_mh_CSxBR_NMSSM_ma_3)[1]))
    gr_CSxBR_NMSSM_vs_mh_ma_3.SetLineWidth(2)
    gr_CSxBR_NMSSM_vs_mh_ma_3.SetLineColor(ROOT.kBlue)
    gr_CSxBR_NMSSM_vs_mh_ma_3.SetLineStyle(3)
    gr_CSxBR_NMSSM_vs_mh_ma_3.SetMarkerColor(ROOT.kBlue)
    gr_CSxBR_NMSSM_vs_mh_ma_3.SetMarkerStyle(23)
    gr_CSxBR_NMSSM_vs_mh_ma_3.SetMarkerSize(1.5)

    execfile("NMSSM_Br_a_Function.py") # contains fNMSSM_Br_a def (the BR given m(a), tan(beta), final state)
    array_mh_ma_2_SM = []
    for mh_i in fRange(90., 149., 100):
        CS_fb = 1000.0*fCS_SM_ggH_13TeV_pb(mh_i)[0] # Xsec of ggH production
        CS_fb = CS_fb + CS_fb * (1000.0*fCS_SM_VBFH_13TeV_pb(mh_i)[0])/(1000.0*fCS_SM_ggH_13TeV_pb(mh_i)[0])                # Adding VBF contribution, assuming it have the same acceptance in analsyis. Verifyied in 2016 analysis.
        CS_fb = CS_fb + CS_fb * (1000.0*fCS_SM_HW_13TeV_pb(mh_i)[0])/(1000.0*fCS_SM_ggH_13TeV_pb(mh_i)[0]) + CS_fb * (0.02) # Adding WH Contribution, assuming acceptance is 10% instead of 12% (measured with cutflow tables in gg and VH NMSSM samples)
        CS_fb = CS_fb + CS_fb * (1000.0*fCS_SM_HZ_13TeV_pb(mh_i)[0])/(1000.0*fCS_SM_ggH_13TeV_pb(mh_i)[0]) + CS_fb * (0.02) # Adding ZH Contribution, assuming acceptance is 10% instead of 12% (measured with cutflow tables in gg and VH NMSSM samples)
        Br_a_mumu = fNMSSM_Br_a(2.0, 20., 'mumu')   # the BR(H->aa) given m(a), tan(beta), final state
        CSxBR = CS_fb*BR_h_aa*Br_a_mumu*Br_a_mumu
        #    print mh_i, CS_fb, CSxBR
        array_mh_ma_2_SM.append(( mh_i, CSxBR ))
    gr_CSxBR_SM = ROOT.TGraph(len(array_mh_ma_2_SM), array.array("d", zip(*array_mh_ma_2_SM)[0]), array.array("d", zip(*array_mh_ma_2_SM)[1]))
    gr_CSxBR_SM.SetLineWidth(3)
    gr_CSxBR_SM.SetLineColor(ROOT.kGreen+3)
    gr_CSxBR_SM.SetLineStyle(1)
    #gr_CSxBR_SM.Draw("C")

    box1 = ROOT.TBox(125.0, 0.0, 153.0, 3.2)
    box1.SetFillStyle(3001)
    box1.SetFillColor(ROOT.kRed - 10)
    #box1.Draw()

    a_mh_125 = ROOT.TArrow(125.0, 0, 125.0, 3.2, 0.02, "--")
    a_mh_125.SetLineColor(ROOT.kBlack)
    a_mh_125.SetLineWidth(1)
    a_mh_125.SetLineStyle(7)
    #a_mh_125.Draw()

    ROOT.gPad.RedrawAxis()

    l_CSxBR_NMSSM_vs_mh = ROOT.TLegend(0.20,0.71,0.93,0.91)
    l_CSxBR_NMSSM_vs_mh.SetFillColor(ROOT.kWhite)
    l_CSxBR_NMSSM_vs_mh.SetFillStyle(4050)
    l_CSxBR_NMSSM_vs_mh.SetBorderSize(0)
    l_CSxBR_NMSSM_vs_mh.SetTextFont(42)
    l_CSxBR_NMSSM_vs_mh.SetTextSize(0.035)
    l_CSxBR_NMSSM_vs_mh.SetMargin(0.13)
    l_CSxBR_NMSSM_vs_mh.SetHeader("NMSSM: Expected %d%% CL upper limits:"%CL)
    l_CSxBR_NMSSM_vs_mh.AddEntry(gr_CSxBR_NMSSM_vs_mh_ma_3,  "m_{a_{1}} = 3.00 GeV", "LP")
    l_CSxBR_NMSSM_vs_mh.AddEntry(gr_CSxBR_NMSSM_vs_mh_ma_0p5,"m_{a_{1}} = 0.50 GeV", "LP")
    l_CSxBR_NMSSM_vs_mh.Draw()

    l_CSxBR_NMSSM_vs_mh_2 = ROOT.TLegend(0.20,0.56,0.93,0.71)
    l_CSxBR_NMSSM_vs_mh_2.SetFillColor(ROOT.kWhite)
    l_CSxBR_NMSSM_vs_mh_2.SetFillStyle(4050)
    l_CSxBR_NMSSM_vs_mh_2.SetBorderSize(0)
    l_CSxBR_NMSSM_vs_mh_2.SetTextFont(42)
    l_CSxBR_NMSSM_vs_mh_2.SetTextSize(0.035)
    l_CSxBR_NMSSM_vs_mh_2.SetMargin(0.13)
    l_CSxBR_NMSSM_vs_mh_2.SetHeader("Reference model:")
    l_CSxBR_NMSSM_vs_mh_2.AddEntry(gr_CSxBR_SM,"#sigma(pp #rightarrow h_{i} #rightarrow 2a_{1}) = 0.003 #times #sigma_{SM}","L")
    l_CSxBR_NMSSM_vs_mh_2.AddEntry(gr_CSxBR_SM,"B(a_{1}#rightarrow 2#mu) = 7.7%","")
    l_CSxBR_NMSSM_vs_mh_2.Draw()

    l_mh1 = ROOT.TLegend(0.22,0.15,0.6,0.23)
    l_mh1.SetFillColor(ROOT.kWhite)
    l_mh1.SetFillStyle(4050)
    l_mh1.SetBorderSize(0)
    l_mh1.SetTextFont(42)
    l_mh1.SetTextSize(0.025)
    l_mh1.SetTextColor(ROOT.kBlack)
    l_mh1.SetMargin(0.13)
    l_mh1.SetHeader("")
    l_mh1.AddEntry(gr_CSxBR_SM,"h_{i} = h_{1}:","")
    l_mh1.AddEntry(gr_CSxBR_SM,"m_{h_{1}} < m_{h_{2}}=125 GeV","")
    #l_mh1.Draw()

    l_mh2 = ROOT.TLegend(0.63,0.15,0.9,0.23)
    l_mh2.SetFillColor(ROOT.kWhite)
    l_mh2.SetFillStyle(4050)
    l_mh2.SetBorderSize(0)
    l_mh2.SetTextFont(42)
    l_mh2.SetTextSize(0.025)
    l_mh2.SetTextColor(ROOT.kBlack)
    l_mh2.SetMargin(0.13)
    l_mh2.SetHeader("")
    l_mh2.AddEntry(gr_CSxBR_SM,"h_{i} = h_{2}:","")
    l_mh2.AddEntry(gr_CSxBR_SM,"125 GeV = m_{h_{1}} #leq m_{h_{2}}","")
    #l_mh2.Draw()

    gr_CSxBR_NMSSM_vs_mh_ma_3.Draw("CP")
    gr_CSxBR_NMSSM_vs_mh_ma_0p5.Draw("CP")
    gr_CSxBR_SM.Draw("C")

    txtHeader.Draw()
    save_canvas(cnv,"CSxBR_NMSSM_vs_mh")

################################################################################
#
#                                 ALP Limits
#
################################################################################

################################################################################
#          Produce limits and store in txt file: 3 txt files for 3 SRs
################################################################################
def limit_ALP_Higgs_vs_ma():
    print "----------- limit_ALP_Higgs_vs_ma -----------"
    cnv.SetLogy()
    cnv.SetLogx()
    # Xsec(ggH) * Br(H->2ALP) * Br(ALP->mumu)^2 = N_evt/Lumi/SF/FullSelEffALPMC.
    # Assume Br(ALP->mumu) = Br_ALP_Lepton = 1 and 0.1: following theory paper Fig. 13 for same flavor
    # Assume ggF->H Xsec @ LHC 13TeV, ggHXsecpb 48.52 [pb]
    # From above get Br(H->2ALP).
    # Define: Br(H->2ALP) = Width(H->2ALP) / [Width(H->2ALP) + Width(H->SM)]
    # Assume Width(H->SM) = HiggsSMWidthMeV = 4.1 MeV arxiv:1901.00174
    # Then Width(H->2ALP) = Width(H->SM) / (1./Br(H->2ALP)-1) / 1000, [GeV]
    # Use Eq. (5.12) in theory paper to get |Cah|/Lambda^2
    # |Cah|/Lambda^2 = sqrt[ Width(H->2ALP)*32*Pi/v^2/m_h^3/(1-2m_a^2/m_h^2)^2/sqrt( 1 - 4m_a^2/m_h^2) ]

    h_CahEff_over_LambdaSquare_TeV = ROOT.TH2F("h_CahEff_over_LambdaSquare_TeV", "h_CahEff_over_LambdaSquare_TeV", 1000, 0.2, 70, 1000, 1E-3, 1.)
    h_CahEff_over_LambdaSquare_TeV.SetXTitle("m_{a} [GeV]")
    h_CahEff_over_LambdaSquare_TeV.SetYTitle("|C_{ah}^{eff}|/#Lambda^{2} [TeV^{-2}]")
    h_CahEff_over_LambdaSquare_TeV.SetTitleOffset(1.47, "Y")
    h_CahEff_over_LambdaSquare_TeV.GetXaxis().SetNdivisions(505)
    h_CahEff_over_LambdaSquare_TeV.GetYaxis().SetTitleSize(0.05)
    h_CahEff_over_LambdaSquare_TeV.Draw()

    CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1 = []
    CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2 = []
    CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3 = []
    CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1 = []
    CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2 = []
    CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3 = []

    # Specify correct mass ranges, use fitted function [m] = GeV
    for m in np.arange(0.5, m_SR1_max, 0.005):
        CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1.append(( m, math.sqrt( (HiggsSMWidthMeV/1000.)/(1./(fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000)/Br_ALP_Lepton_1**2) - 1)*32*3.1415/(HiggsVEV**2)/(HiggsMass**3)/( (1 - 2*(m/HiggsMass)**2)**2 )/math.sqrt(1 - 4*(m/HiggsMass)**2) )*10**6 ))
        CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1.append(( m, math.sqrt( (HiggsSMWidthMeV/1000.)/(1./(fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000)/Br_ALP_Lepton_0p1**2) - 1)*32*3.1415/(HiggsVEV**2)/(HiggsMass**3)/( (1 - 2*(m/HiggsMass)**2)**2 )/math.sqrt(1 - 4*(m/HiggsMass)**2) )*10**6 ))
    for m in np.arange(m_SR2_min, m_SR2_max, 0.005):
        CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2.append(( m, math.sqrt( (HiggsSMWidthMeV/1000.)/(1./(fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000)/Br_ALP_Lepton_1**2) - 1)*32*3.1415/(HiggsVEV**2)/(HiggsMass**3)/( (1 - 2*(m/HiggsMass)**2)**2 )/math.sqrt(1 - 4*(m/HiggsMass)**2) )*10**6 ))
        CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2.append(( m, math.sqrt( (HiggsSMWidthMeV/1000.)/(1./(fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000)/Br_ALP_Lepton_0p1**2) - 1)*32*3.1415/(HiggsVEV**2)/(HiggsMass**3)/( (1 - 2*(m/HiggsMass)**2)**2 )/math.sqrt(1 - 4*(m/HiggsMass)**2) )*10**6 ))
    for m in np.arange(m_SR3_min, 30, 0.005):
        CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3.append(( m, math.sqrt( (HiggsSMWidthMeV/1000.)/(1./(fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000)/Br_ALP_Lepton_1**2) - 1)*32*3.1415/(HiggsVEV**2)/(HiggsMass**3)/( (1 - 2*(m/HiggsMass)**2)**2 )/math.sqrt(1 - 4*(m/HiggsMass)**2) )*10**6 ))
        CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3.append(( m, math.sqrt( (HiggsSMWidthMeV/1000.)/(1./(fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000)/Br_ALP_Lepton_0p1**2) - 1)*32*3.1415/(HiggsVEV**2)/(HiggsMass**3)/( (1 - 2*(m/HiggsMass)**2)**2 )/math.sqrt(1 - 4*(m/HiggsMass)**2) )*10**6 ))

    # For Br_ALP_Lepton_1
    # SR1
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1 = ROOT.TGraph( len(CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1)[0]), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1)[1]) )
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1.SetLineWidth(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1.SetLineColor(ROOT.kRed)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1.SetLineStyle(1)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1.Draw("L")
    # SR2
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2 = ROOT.TGraph( len(CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2)[0]), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2)[1]) )
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2.SetLineWidth(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2.SetLineColor(ROOT.kRed)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2.SetLineStyle(1)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR2.Draw("L")
    # SR3
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3 = ROOT.TGraph( len(CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3)[0]), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3)[1]) )
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3.SetLineWidth(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3.SetLineColor(ROOT.kRed)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3.SetLineStyle(1)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR3.Draw("L")

    # For Br_ALP_Lepton_0p1
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1 = ROOT.TGraph( len(CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1)[0]), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1)[1]) )
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1.SetLineWidth(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1.SetLineColor(ROOT.kRed)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1.SetLineStyle(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1.Draw("L")

    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2 = ROOT.TGraph( len(CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2)[0]), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2)[1]) )
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2.SetLineWidth(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2.SetLineColor(ROOT.kRed)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2.SetLineStyle(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR2.Draw("L")

    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3 = ROOT.TGraph( len(CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3)[0]), array.array("d", zip(*CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3)[1]) )
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3.SetLineWidth(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3.SetLineColor(ROOT.kRed)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3.SetLineStyle(2)
    gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR3.Draw("L")

    l_CahEff_over_LambdaSquare_TeV_fit = ROOT.TLegend(0.20,0.71,0.93,0.91)
    l_CahEff_over_LambdaSquare_TeV_fit.SetFillColor(ROOT.kWhite)
    l_CahEff_over_LambdaSquare_TeV_fit.SetMargin(0.13)
    l_CahEff_over_LambdaSquare_TeV_fit.SetBorderSize(0)
    l_CahEff_over_LambdaSquare_TeV_fit.SetTextFont(42)
    l_CahEff_over_LambdaSquare_TeV_fit.SetTextSize(0.035)
    l_CahEff_over_LambdaSquare_TeV_fit.SetHeader("ALP Expected %d%% CL upper limits:"%CL)
    l_CahEff_over_LambdaSquare_TeV_fit.AddEntry(gr_CahEff_over_LambdaSquare_TeV_LeptBr_1_fit_SR1, "Br(a #rightarrow #mu^{+}#mu^{-}) = %.1f"%Br_ALP_Lepton_1, "L")
    l_CahEff_over_LambdaSquare_TeV_fit.AddEntry(gr_CahEff_over_LambdaSquare_TeV_LeptBr_0p1_fit_SR1, "Br(a #rightarrow #mu^{+}#mu^{-}) = %.1f"%Br_ALP_Lepton_0p1, "L")
    l_CahEff_over_LambdaSquare_TeV_fit.Draw()

    txtHeader.Draw()
    save_canvas(cnv, "CahEff_over_LambdaSquare_TeV_fit")

def limit_ALP_Lepton_vs_ma():
    print "----------- limit_ALP_Lepton_vs_ma -----------"
    cnv.SetLogy()
    cnv.SetLogx()
    # Xsec(ggH) * Br(H->2ALP) * Br(ALP->mumu)^2 = N_evt/Lumi/SF/FullSelEffALPMC.
    # Use ggF->H Xsec @ LHC 13TeV, ggHXsecpb 48.52 [pb]
    # Use h->SM=4.1MeV, define: Br(H->2ALP) = Width(H->2ALP) / [Width(H->2ALP) + Width(H->SM)]
    # Assume Cah/Lambda^2 = 1, 0.1, 0.01 TeV^-2 can get Width(H->2ALP) and Br(H->2ALP)
    # From above get Br(ALP->mumu)
    # Assume ALP total Width 10^-5GeV, Use Eq. (3.12) in theory paper to get |Cll|/Lambda
    # Width(ALP->mumu) = ALPWidthGeV * sqrt( N_evt/Lumi/SF/FullSelEffALPMC/Xec/Br(H->2ALP) )

    h_clleff_over_Lambda_TeV = ROOT.TH2F("h_clleff_over_Lambda_TeV", "h_clleff_over_Lambda_TeV", 1000, 0.2, 70, 1000, 1E-3, 1E3)
    h_clleff_over_Lambda_TeV.SetXTitle("m_{a} [GeV]")
    h_clleff_over_Lambda_TeV.SetYTitle("|c_{ll}^{eff}|/#Lambda [TeV^{-1}]")
    h_clleff_over_Lambda_TeV.SetTitleOffset(1.47, "Y")
    h_clleff_over_Lambda_TeV.GetXaxis().SetNdivisions(505)
    h_clleff_over_Lambda_TeV.GetYaxis().SetTitleSize(0.05)
    h_clleff_over_Lambda_TeV.Draw()

    clleff_over_Lambda_TeV_Cah_1_fit_SR1 = []
    clleff_over_Lambda_TeV_Cah_1_fit_SR2 = []
    clleff_over_Lambda_TeV_Cah_1_fit_SR3 = []
    clleff_over_Lambda_TeV_Cah_0p1_fit_SR1 = []
    clleff_over_Lambda_TeV_Cah_0p1_fit_SR2 = []
    clleff_over_Lambda_TeV_Cah_0p1_fit_SR3 = []
    clleff_over_Lambda_TeV_Cah_0p01_fit_SR1 = []
    clleff_over_Lambda_TeV_Cah_0p01_fit_SR2 = []
    clleff_over_Lambda_TeV_Cah_0p01_fit_SR3 = []

    # Specify correct mass ranges, use fitted function [m] = GeV
    # 1./Br(H->2ALP) = ( 1+ HiggsSMWidthMeV/1000./( (CahEff_over_LambdaSquare_TeV_1/1000/1000)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2)/32/3.1415 ) )
    for m in np.arange(0.5, m_SR1_max, 0.005):
        clleff_over_Lambda_TeV_Cah_1_fit_SR1.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_1/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
        clleff_over_Lambda_TeV_Cah_0p1_fit_SR1.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_0p1/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
        clleff_over_Lambda_TeV_Cah_0p01_fit_SR1.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_0p01/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
    for m in np.arange(m_SR2_min, m_SR2_max, 0.005):
        clleff_over_Lambda_TeV_Cah_1_fit_SR2.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_1/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
        clleff_over_Lambda_TeV_Cah_0p1_fit_SR2.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_0p1/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
        clleff_over_Lambda_TeV_Cah_0p01_fit_SR2.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_0p01/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
    for m in np.arange(m_SR3_min, 30, 0.005):
        clleff_over_Lambda_TeV_Cah_1_fit_SR3.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_1/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
        clleff_over_Lambda_TeV_Cah_0p1_fit_SR3.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_0p1/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))
        clleff_over_Lambda_TeV_Cah_0p01_fit_SR3.append(( m, math.sqrt( ( 8*3.1415/MuMassGeV**2/m/math.sqrt( 1-4*(MuMassGeV/m)**2 ) )*fCmsAlpExtrapolate(m, ALPTotWidthGeV)*math.sqrt( 1+ HiggsSMWidthMeV*32*3.1415/1000./( (CahEff_over_LambdaSquare_TeV_0p01/10**6)**2*HiggsVEV**2*HiggsMass**3*(1 - 2*(m/HiggsMass)**2)**2*math.sqrt(1 - 4*(m/HiggsMass)**2) ) )*fCmsLimitVsM(m)/lumi_fbinv/SF/fCmsAlpExtrapolate(m, CmsAlpAcceptance)/(ggHXsecpb*1000) )*10**3 ))

    # For CahEff_over_LambdaSquare_TeV_1
    # SR1
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR1 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_1_fit_SR1), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_1_fit_SR1)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_1_fit_SR1)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR1.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR1.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR1.SetLineStyle(1)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR1.Draw("L")
    # SR2
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR2 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_1_fit_SR2), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_1_fit_SR2)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_1_fit_SR2)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR2.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR2.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR2.SetLineStyle(1)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR2.Draw("L")
    # SR3
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR3 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_1_fit_SR3), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_1_fit_SR3)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_1_fit_SR3)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR3.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR3.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR3.SetLineStyle(1)
    gr_clleff_over_Lambda_TeV_Cah_1_fit_SR3.Draw("L")

    print "     ------ write: ../ALPLimits/CMSRun2ALP_cll_TeV_Cah_1_SR*.txt"
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_1_SR1.txt", "w") as A1:
        for a, b in clleff_over_Lambda_TeV_Cah_1_fit_SR1:
            print >> A1, "%.3f"%a, b
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_1_SR2.txt", "w") as A2:
        for a, b in clleff_over_Lambda_TeV_Cah_1_fit_SR2:
            print >> A2, "%.3f"%a, b
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_1_SR3.txt", "w") as A3:
        for a, b in clleff_over_Lambda_TeV_Cah_1_fit_SR3:
            print >> A3, "%.3f"%a, b

    # For CahEff_over_LambdaSquare_TeV_0p1
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR1 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_0p1_fit_SR1), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p1_fit_SR1)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p1_fit_SR1)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR1.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR1.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR1.SetLineStyle(2)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR1.Draw("L")

    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR2 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_0p1_fit_SR2), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p1_fit_SR2)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p1_fit_SR2)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR2.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR2.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR2.SetLineStyle(2)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR2.Draw("L")


    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR3 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_0p1_fit_SR3), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p1_fit_SR3)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p1_fit_SR3)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR3.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR3.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR3.SetLineStyle(2)
    gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR3.Draw("L")

    print "     ------ write: ../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p1_SR*.txt"
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p1_SR1.txt", "w") as B1:
        for a, b in clleff_over_Lambda_TeV_Cah_0p1_fit_SR1:
            print >> B1, "%.3f"%a, b
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p1_SR2.txt", "w") as B2:
        for a, b in clleff_over_Lambda_TeV_Cah_0p1_fit_SR2:
            print >> B2, "%.3f"%a, b
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p1_SR3.txt", "w") as B3:
        for a, b in clleff_over_Lambda_TeV_Cah_0p1_fit_SR3:
            print >> B3, "%.3f"%a, b

    # For CahEff_over_LambdaSquare_TeV_0p01
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR1 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_0p01_fit_SR1), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p01_fit_SR1)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p01_fit_SR1)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR1.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR1.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR1.SetLineStyle(3)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR1.Draw("L")

    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR2 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_0p01_fit_SR2), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p01_fit_SR2)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p01_fit_SR2)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR2.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR2.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR2.SetLineStyle(3)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR2.Draw("L")

    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR3 = ROOT.TGraph( len(clleff_over_Lambda_TeV_Cah_0p01_fit_SR3), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p01_fit_SR3)[0]), array.array("d", zip(*clleff_over_Lambda_TeV_Cah_0p01_fit_SR3)[1]) )
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR3.SetLineWidth(2)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR3.SetLineColor(ROOT.kRed)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR3.SetLineStyle(3)
    gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR3.Draw("L")

    print "     ------ write: ../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p01_SR*.txt"
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p01_SR1.txt", "w") as C1:
        for a, b in clleff_over_Lambda_TeV_Cah_0p01_fit_SR1:
            print >> C1, "%.3f"%a, b
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p01_SR2.txt", "w") as C2:
        for a, b in clleff_over_Lambda_TeV_Cah_0p01_fit_SR2:
            print >> C2, "%.3f"%a, b
    with open("../ALPLimits/CMSRun2ALP_cll_TeV_Cah_0p01_SR3.txt", "w") as C3:
        for a, b in clleff_over_Lambda_TeV_Cah_0p01_fit_SR3:
            print >> C3, "%.3f"%a, b

    l_clleff_over_Lambda_TeV_Cah_fit = ROOT.TLegend(0.20,0.71,0.93,0.91)
    l_clleff_over_Lambda_TeV_Cah_fit.SetFillColor(ROOT.kWhite)
    l_clleff_over_Lambda_TeV_Cah_fit.SetMargin(0.13)
    l_clleff_over_Lambda_TeV_Cah_fit.SetBorderSize(0)
    l_clleff_over_Lambda_TeV_Cah_fit.SetTextFont(42)
    l_clleff_over_Lambda_TeV_Cah_fit.SetTextSize(0.035)
    l_clleff_over_Lambda_TeV_Cah_fit.SetHeader("ALP Expected %d%% CL upper limits:"%CL)
    l_clleff_over_Lambda_TeV_Cah_fit.AddEntry(gr_clleff_over_Lambda_TeV_Cah_1_fit_SR1,    "|C_{ah}^{eff}|/#Lambda^{2} = %.2f TeV^{-2}"%CahEff_over_LambdaSquare_TeV_1,    "L")
    l_clleff_over_Lambda_TeV_Cah_fit.AddEntry(gr_clleff_over_Lambda_TeV_Cah_0p1_fit_SR1,  "|C_{ah}^{eff}|/#Lambda^{2} = %.2f TeV^{-2}"%CahEff_over_LambdaSquare_TeV_0p1,  "L")
    l_clleff_over_Lambda_TeV_Cah_fit.AddEntry(gr_clleff_over_Lambda_TeV_Cah_0p01_fit_SR1, "|C_{ah}^{eff}|/#Lambda^{2} = %.2f TeV^{-2}"%CahEff_over_LambdaSquare_TeV_0p01, "L")
    l_clleff_over_Lambda_TeV_Cah_fit.Draw()

    txtHeader.Draw()
    save_canvas(cnv, "clleff_over_Lambda_TeV_fit")

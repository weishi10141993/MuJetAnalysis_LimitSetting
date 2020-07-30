import ROOT
ROOT.gROOT.SetBatch(True)

#from Plots import *
execfile("Plots.py")

###------ Model Independent Limits ------###
#--Limits on N_ext vs m
limit_vs_mGammaD()
#--Limits on xsec*Br^2*alpha vs m
limit_CSxBR2xAlpha_fb_vs_mGammaD()

###------ Limits Interpreted in NMSSM ------###
limit_CSxBR2_fb_vs_ma()
limit_CSxBR2_fb_vs_mh()

#print f1(0.4,40.0,5.0,1.0,1.0)
#print f2(0.4,40,5,1.0)
#print f3(0.4,40.0,5.0)
#print f_Alpha_vs_ctau(0.4,40.0,5.0,0.068)
#print f_Alpha_vs_ctau(0.4,40.0,0.05,0.068)
#print f_Alpha_vs_ctau(0.4,40.0,0.1,0.068)
#print f_Alpha_vs_ctau(0.4,40.0,5.0,0.068)

###------ Limits Interpreted in ALP -------###
###############################################################################
## Don't plot ALP limits if do combine for 2016+2018, ALP not searched in 2016
###############################################################################
if year != 2020:
    limit_ALP_Higgs_vs_ma()
    limit_ALP_Lepton_vs_ma()

###-------       MSSMD       -------###
#--BR(a->mumu) vs m(a)
#plot_BR_GammaD_to_2mu()
#--Acceptance vs things-------
#Alpha_vs_ctau_2015()     # Use alpha for Dark SUSY in scripts/CmsDarkSusyAcceptance.py
#Alpha_vs_mGammaD_2015()  # Use alpha for Dark SUSY in scripts/CmsDarkSusyAcceptance.py
#Alpha_vs_mGammaD_ctau_3D()
#Plot_Eff_vs_R()          # Step function

###-------       MSSMD       -------###
#limit_CSxBR2_fb_vs_mGammaD_2015()
#!limit_CS_fb_vs_mGammaD_2015()
#!limit_CSxBR2_fb_vs_ctau_2015()
#!limit_CSxBR2_fb_and_CS_fb_and_CS_over_CSsm_vs_mGammaD_ctau_3D_and_2D()
#
#plot_width_over_e2_GeV()
#plot_ctauConst_vs_logEpsilon2_mGammaD()

#limit_Lines_CSxBR2_fb_vs_mGammaD_ctau() #TBA
#!limit_Lines_CS_vs_mGammaD_ctau()

#print log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( 0.4 ) / 0.1 )
#print log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( 0.4 ) / 0.2 )
#print log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( 0.4 ) / 0.5 )
#print log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( 0.4 ) / 1.0 )
#print log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( 0.4 ) / 2.0 )
#print log10( c_hbar_mm_GeV / Width_GammaD_over_e2_GeV( 0.4 ) / 5.0 )

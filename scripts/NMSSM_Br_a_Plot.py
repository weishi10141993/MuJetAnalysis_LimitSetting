import ROOT, array, os, re, math, random
from math import *

execfile("NMSSM_Br_a_Function.py")

def MyFloatRange(start,stop,step):
    if (step > 0. and stop < start) or (step < 0. and start < stop): raise Exception
    array = []
    i = 0.
    while(1):
        cur = start + i*step
        if cur <= stop and stop > start: array.append(cur)
        elif cur >= stop and stop < start: array.append(cur)
        else: break
        i = i + 1.
    return array

tanBeta = [[1., 'tan(#beta) = 1'],
           [1.5, 'tan(#beta) = 1.5'],
           [2., 'tan(#beta) = 2'],
           [3., 'tan(#beta) = 3'],
           [20., 'tan(#beta) = 20'],
           [50., 'tan(#beta) = 50'],
          ]

channel = [['mumu', 'a -> #mu^{+} #mu^{-}'],
           ['tautau', 'tautau label'],
           ['ss', 'ss label'],
           ['cc', 'cc label'],
           ['bb', 'bb label'],
           ['gluglu', 'gluglu label'],
           ['gamgam', 'gamgam label'],
          ]

execfile("tdrStyle.py")
c1 = ROOT.TCanvas("c1", "c1")
h_dummy = ROOT.TH2F("h_dummy", "h_dummy", 40, 0., 4., 100, 0., 1.)
h_dummy.SetXTitle("m_{a_{1}} [GeV]")
h_dummy.SetYTitle("B(a_{1} #rightarrow  X)")
h_dummy.Draw()

gr_Br_a_vs_ma = []
i = 0
for tanBeta_i in tanBeta:
    for channel_i in channel:
        array_ma_Br_a = []
        for ma_i in MyFloatRange(0.2, 3.61, 0.1):
            Br_a = fNMSSM_Br_a(ma_i, tanBeta_i[0], channel_i[0])
            print ma_i, Br_a
            array_ma_Br_a.append(( ma_i, Br_a ))
        gr_Br_a_vs_ma.append( ROOT.TGraph(len(array_ma_Br_a), array.array("d", zip(*array_ma_Br_a)[0]), array.array("d", zip(*array_ma_Br_a)[1])) )
        gr_Br_a_vs_ma[i].SetLineWidth(2)
        gr_Br_a_vs_ma[i].SetLineColor(1)
        gr_Br_a_vs_ma[i].SetLineStyle(9)
        i = i + 1

gr_Br_a_vs_ma[0].Draw("Csame")
gr_Br_a_vs_ma[1].Draw("Csame")

c1.SaveAs("NMSSM_Br_a.png")

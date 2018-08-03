import ROOT, array, os, re, math, random
from math import *

execfile("scripts/CmsNmssmAcceptance.py")

#print type(CmsNmssmAcceptance_2016_13TeV) #<type 'dict'>
#print CmsNmssmAcceptance_2016_13TeV

Hmasses = [90,100,110,125,150]
#Amassed = [0.25,0.5,0.75,1.,2.,3.]
Amassed = [2.,3.]
for Hm in Hmasses:
    dxdy_tot = 0
    for iAm in (range(len(Amassed)-1)):
        dxdy = (CmsNmssmAcceptance_2016_13TeV[Amassed[iAm],Hm]-CmsNmssmAcceptance_2016_13TeV[Amassed[iAm+1],Hm])/(Amassed[iAm+1]-Amassed[iAm])
        dxdy_tot = dxdy_tot + dxdy
        print "(",CmsNmssmAcceptance_2016_13TeV[Amassed[iAm],Hm], " - ", CmsNmssmAcceptance_2016_13TeV[Amassed[iAm+1],Hm], ") / ",(Amassed[iAm+1]-Amassed[iAm]), " = ",dxdy
    print "dxdy for ", Hm, " is in average: ", dxdy_tot,"/",(len(Amassed)-1)," = ", dxdy_tot/(len(Amassed)-1)
    print "(3.55,",Hm,"): (", CmsNmssmAcceptance_2016_13TeV[Amassed[len(Amassed)-1],Hm] - dxdy_tot/(len(Amassed)-1) * (3.55-3.00),"),"


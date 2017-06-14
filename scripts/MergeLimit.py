import ROOT, array, os, sys, re, math, random
from math import *

TxtToMerge=["file1.txt","file1.txt","file1.txt"]

SUM_nJobs = []; SUM_Mass = []; SUM_Limit = [];
First=True
for txt_tmp in TxtToMerge:
  print "Reading: ", txt_tmp
  with open(txt_tmp) as f:
    content = f.readlines()
  nMass=0
  for line in content:
    line = line.replace(")","")
    line = line.replace(","," ")
    line = line.replace("["," ")
    line = line.replace("]"," ")
    line = line.replace("\n"," ")
    list_line = line.split()
    if len(list_line) == 3 and First:
      SUM_nJobs.append(float(list_line[0]))
      SUM_Mass.append(float(list_line[1]))
      SUM_Limit.append(float(list_line[2]))
    if len(list_line) == 3 and not First:
      if SUM_Mass[nMass] != float(list_line[1]): print "WARNING, the masses in the files are not matching!!!"; sys.exit(0)
      SUM_Limit[nMass] = (float(list_line[2])*float(list_line[0]) + SUM_Limit[nMass]*SUM_nJobs[nMass])/(float(list_line[0])+SUM_nJobs[nMass])
      SUM_nJobs[nMass] = float(list_line[0]) + SUM_nJobs[nMass]
      nMass+=1
  First = False

for iM in range(len(SUM_Mass)):
  print SUM_nJobs[iM],") [",SUM_Mass[iM],",",SUM_Limit[iM],"],"

import ROOT, array, os, sys, re, random, subprocess
import math
from math import *
import subprocess
import os.path
import commands

execfile("../scripts/UserInput.py") #define CLsymbol, quantile, pwd, basetxt, masses, pwd etc

print "Your will run on N files:"
if   "T30000" in endtxt: gr = "grep T30000 | grep -v T50000 | grep -v T10000"
elif "T50000" in endtxt: gr = "grep T50000 | grep -v T30000 | grep -v T10000"
elif "T10000" in endtxt: gr = "grep T10000 | grep -v T30000 | grep -v T50000"
else: gr = "grep -v T50000 | grep -v 10000 | grep -v 30000"

bashCommand = "ls " + pwd + "  | grep OutPut | " + gr + " | sort | grep -c '" + endtxt + "'"
print str(bashCommand)
subprocess.call(bashCommand, shell=True)
print "That contain N limits:"
bashCommand = "grep 'Limit: r <' " + pwd + str(year) + basetxt + quantile + "*" + endtxt + "* | grep -c txt"
print str(bashCommand)
subprocess.call(bashCommand, shell=True)

cmd1 = "grep 'Hybrid New' " + pwd + str(year) + basetxt + quantile + "*" + endtxt + "* "
cmd2 = " | awk  '{print $1}' | sed 's/.$//'"
i=0; oldline=""; average=0; average_n=0; average_m=0; average_m_n=0;
Resulter_TOT=[]

lim_file_name = "limits_quant_" + quantile + ".txt"
lim_file = open(lim_file_name, "w")
lim_file.write("STANDARD\n")

#Save all values in a list of lists
listoflists = []
for mass in masses:
  single_list = []
  # Only get file for a given mass
  Resulter=[]
  cmd = cmd1 + " | grep _" + '{:.4f}'.format(mass) + "_" + cmd2
  output = commands.getoutput(cmd)
  for name in output.rstrip().split('\n'):
    if( os.path.exists(str(name)) ):
      with open(name) as f:
        for line in f:
          if 'Limit: r < ' in line and CLsymbol in line and "Hybrid New" in oldline:
            words=line.split()
            if(debug): print "Mass: " + str(masses[i]) + " is " + str(words[3])
            average   = average+float(words[3]);
            average_n = average_n+1
            average_m = average_m+float(words[3]);
            average_m_n = average_m_n+1
            Resulter.append(float(words[3]))
            single_list.append(float(words[3]))
          oldline=line
    else:
      if(debug1): print name, " -> NOT found!"
  if(average_m_n!=0):
    print "[" + str(masses[i]) + "," + str(average_m/average_m_n) + "]," + " #(" + str(average_m_n) + ")"
    lim_file.write("[" + str(masses[i]) + "," + str(average_m/average_m_n) + "],\n")
  else:
    print "Cannot print the mean, average_m_n is zero!"
    lim_file.write("Cannot print the mean, average_m_n is zero!\n")
  average_m=0; average_m_n=0;
  i=i+1
  Resulter_TOT.append(Resulter)
  listoflists.append(single_list)
if(average_n!=0): print "Global limit averaged is: " + str(average/average_n)
else: print "Cannot print the mean, average_n is zero!"

#Now save plots of the limit for each mass
folderCreation  = subprocess.Popen(['mkdir -p Limit_histo/'], stdout=subprocess.PIPE, shell=True);
folderCreation  = subprocess.Popen(['rm -rf Limit_histo/*'], stdout=subprocess.PIPE, shell=True);
folderCreation.communicate()
c1 = ROOT.TCanvas("c1")
it = 0
for Mylist in listoflists:
  h1 = ROOT.TH1F("h_"+str(masses[it]), "Mass " + str(masses[it]), 50, 0., 10. )
  for limit in Mylist:
    h1.Fill(limit)
  h1.Draw()
  c1.SaveAs("Limit_histo/mass_" + str(masses[it]) + ".pdf")
  it = it + 1

#Now remove the worse items
print ""
print "Now remove the worse items"
lim_file.write("\n"); lim_file.write("NOW SKIMMED VERSION\n")
i=0; average=0; average_n=0
for mass in Resulter_TOT:
  mass_Sorted = sorted(mass)
  #print mass_Sorted
  mass_Sorted = mass_Sorted[1:-6]
  #print mass_Sorted
  Value=0; Value_n=0;
  for m in mass_Sorted:
    Value=Value+float(m)
    Value_n=Value_n+1
    average   = average+float(m); average_n = average_n+1
  if(Value_n!=0):
    print "[" + str(masses[i]) + "," + str(Value/Value_n) + "]," + " #(" + str(Value_n) + ")"
    lim_file.write("[" + str(masses[i]) + "," + str(Value/Value_n) + "],\n")
  else:
    print "Cannot print the mean, Value_n is zero!"
    lim_file.write("Cannot print the mean, average_m_n is zero!\n")
  i=i+1
lim_file.close()
if(average_n!=0): print "Global limit averaged is: " + str(average/average_n)
else: print "Cannot print the mean, average_n is zero!"

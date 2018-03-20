import ROOT, array, os, sys, re, random, subprocess
import math
from math import *
import subprocess
import os.path
import commands

debug=False
debug1=False

#masses=[0.2113,0.2200,0.2300,0.2400,0.2500,0.2600,0.2700,0.2800,0.2900,0.3000,0.3100,0.3200,0.3300,0.3400,0.3500,0.3600,0.3700,0.3800,0.3900,0.4000,0.4100,0.4200,0.4300,0.4400,0.4500,0.4600,0.4700,0.4800,0.4900,0.5000,0.6000,0.7000,0.8000,0.9000,1.0000,2.0000,2.6000,2.7000,2.8000,2.9000,3.0000,3.1000,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]
#2018 granularity
masses=[0.2113,0.2400,0.2600,0.3000,0.3300,0.3600,0.4000,0.4300,0.4600,0.5000,0.5300,0.5600,0.6000,0.7000,0.8000,0.8800,0.9000,0.9100,0.9200,0.9300,0.9400,1.0000,1.1000,1.2000,1.3000,1.4000,1.5000,1.6000,1.7000,1.8000,1.9000,2.0000,2.1000,2.2000,2.3000,2.4000,2.5000,2.6000,2.7000,2.8000,2.9000,3.0000,3.0200,3.0500,3.0800,3.0900,3.1000,3.1200,3.1500,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]
basetxt="sh/OutPut_"

endtxt="_T50000_";
#endtxt="_T30000_";
#endtxt="_";

print "Your will run on N files:"
if   "T30000" in endtxt: gr="grep T30000 | grep -v T50000 | grep -v T10000"
elif "T50000" in endtxt: gr="grep T50000 | grep -v T30000 | grep -v T10000"
elif "T10000" in endtxt: gr="grep T10000 | grep -v T30000 | grep -v T50000"
else: gr="grep -v T50000 | grep -v 10000 | grep -v 30000" 
bashCommand="ls sh/  | grep OutPut | " + gr + " | sort | grep -c '" + endtxt + "'"
print str(bashCommand)
subprocess.call(bashCommand,shell=True)
print "That contain N limits:"
bashCommand="grep 'Limit: r <' " + basetxt + "*" + endtxt + "* | grep -c txt"
print str(bashCommand)
subprocess.call(bashCommand,shell=True)
cmd1 = "grep 'Hybrid New' sh/OutPut_*" + endtxt + "* "
cmd2 = " | awk  '{print $1}' | sed 's/.$//'"
i=0; oldline=""; average=0; average_n=0; average_m=0; average_m_n=0;
Resulter_TOT=[]
lim_file = open("limits.txt","w")
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
          if 'Limit: r < ' in line and '95%' in line and "Hybrid New" in oldline:
            words=line.split()
            if(debug): print "Mass: " + str(masses[i]) + " is " + str(words[3])
            average   = average+float(words[3]); average_n = average_n+1
            average_m = average_m+float(words[3]); average_m_n = average_m_n+1
            Resulter.append(float(words[3]))
            single_list.append(float(words[3]))
          oldline=line
    else:
      if(debug1): print name, " -> NOT found!"
  if(average_m_n!=0):
    print str(average_m_n) + ") [" + str(masses[i]) + "," + str(average_m/average_m_n) + "],"
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
  mass_Sorted = mass_Sorted[1:-6]
  Value=0; Value_n=0;
  for m in mass_Sorted:
    Value=Value+float(m)
    Value_n=Value_n+1
    average   = average+float(m); average_n = average_n+1
  if(Value_n!=0):
    print str(Value_n) + ") [" + str(masses[i]) + "," + str(Value/Value_n) + "],"
    lim_file.write("[" + str(masses[i]) + "," + str(Value/Value_n) + "],\n")
  else:
    print "Cannot print the mean, Value_n is zero!"
    lim_file.write("Cannot print the mean, average_m_n is zero!\n")
  i=i+1
lim_file.close() 
if(average_n!=0): print "Global limit averaged is: " + str(average/average_n)
else: print "Cannot print the mean, average_n is zero!"

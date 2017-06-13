import math
from math import *
import subprocess
import os.path

Standard=True
Focus=False
Niters=100
debug=False
debug1=False

if(Standard):
  masses=[0.2113,0.2200,0.2300,0.2400,0.2500,0.2600,0.2700,0.2800,0.2900,0.3000,0.3100,0.3200,0.3300,0.3400,0.3500,0.3600,0.3700,0.3800,0.3900,0.4000,0.4100,0.4200,0.4300,0.4400,0.4500,0.4600,0.4700,0.4800,0.4900,0.5000,0.6000,0.7000,0.8000,0.9000,1.0000,2.0000,2.6000,2.7000,2.8000,2.9000,3.0000,3.1000,3.2000,3.3000,3.4000,3.7000,4.0000,5.0000,6.0000,7.0000,8.0000,8.5000]
  basetxt="sh/OutPut_"
  #endtxt="_"; endtxt2=""
  endtxt="_T30000_"; endtxt2="T30000"
  #endtxt="_T50000_"; endtxt2="T50000"
  #endtxt="_T30000_"; endtxt2="T30000"

  print "Your will run on N files:"
  if   "T30000" in endtxt: gr="grep T30000 | grep -v T50000 | grep -v T10000"
  elif "T50000" in endtxt: gr="grep T50000 | grep -v T30000 | grep -v T10000"
  elif "T10000" in endtxt: gr="grep T10000 | grep -v T30000 | grep -v T50000"
  else: gr="grep -v T50000 | grep -v 10000 | grep -v 30000" 
  bashCommand="ls sh/  | grep OutPut | " + gr + " | sort | grep -c '" + endtxt + "'"
  print str(bashCommand)
  subprocess.call(bashCommand,shell=True)
  print "That contain N limits:"
  bashCommand="grep 'Hybrid New' " + basetxt + "*" + endtxt + "* | grep -c txt"
  if(debug1): print str(bashCommand)
  subprocess.call(bashCommand,shell=True)

  i=0; oldline=""; average=0; average_n=0; average_m=0; average_m_n=0;
  Resulter_TOT=[]
  for mass in masses:
    Resulter=[]
    for iN in range(Niters):
      name=basetxt + str("{0:.4f}".format(masses[i])) + "_" + endtxt2 + '_' + str(iN) + ".txt"
      if(debug): print "Opening: " + str(name)
      if( os.path.exists(str(name)) ):
        if(debug1): print "-> Found!"
        with open(name) as f:
          for line in f:
            if 'Limit: r < ' in line and '95%' in line and "Hybrid New" in oldline:
              words=line.split() 
              if(debug): print "Mass: " + str(masses[i]) + " is " + str(words[3])
              average   = average+float(words[3]); average_n = average_n+1
              average_m = average_m+float(words[3]); average_m_n = average_m_n+1
              Resulter.append(float(words[3]))
            oldline=line
      else:
        if(debug1): print "-> NOT found!"
    if(average_m_n!=0): print str(average_m_n) + ") [" + str(masses[i]) + "," + str(average_m/average_m_n) + "],"
    else: print "Cannot print the mean, average_m_n is zero!"
    average_m=0; average_m_n=0;
    i=i+1
    Resulter_TOT.append(Resulter)
  if(average_n!=0): print "Global limit averaged is: " + str(average/average_n)
  else: print "Cannot print the mean, average_n is zero!"
  #Now remove the worse items
  print "Now remove the worse items"
  i=0
  for mass in Resulter_TOT:
    mass_Sorted = sorted(mass)
    mass_Sorted = mass_Sorted[5:-5]
    Value=0; Value_n=0;
    if(masses[i]==0.27): mass_Sorted = mass_Sorted[5:-7];
    for m in mass_Sorted:
      Value=Value+float(m)
      Value_n=Value_n+1
    if(Value_n!=0): print str(Value_n) + ") [" + str(masses[i]) + "," + str(Value/Value_n) + "],"
    else: print "Cannot print the mean, Value_n is zero!"
    i=i+1

if(Focus):
  #Focus in some masses
  masses=[0.4200,0.8000]
  iterations=[1,2,3,4,5,6,7,8,9,10]
  basetxt="sh/OutPut_"
  i=0; j=0; oldline="";
  for mass in masses:
    j=0; average=0; average_n=0
    for N in iterations:
      name=basetxt + str("{0:.4f}".format(masses[i])) + "_T50000_" + str(iterations[j]) + ".txt"
      with open(name) as f:
        for line in f:
          if 'Limit: r < ' in line and '95%' in line and "Hybrid New" in oldline:
            words=line.split() 
            print "[" + str(masses[i]) + "," + str(words[3]) + "],"
            average = average+float(words[3])
            average_n = average_n+1
          oldline=line
      j=j+1
    if(average_n!=0): print "Average limit is " + str(average/average_n)
    else: print "Cannot print the mean, average_n is zero!"
    i=i+1

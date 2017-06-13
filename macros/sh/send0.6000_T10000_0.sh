#!/bin/bash
cd /afs/cern.ch/work/l/lpernie/H2a4Mu/DisplacedMuonJetAnalysis_2015/LIMITS/CMSSW_7_4_7/src/limits_2a4mu 
eval `scramv1 runtime -sh`
combine -n .H2A4Mu_mA_0.6000_GeV_T10000_0 -m 125 -M HybridNew --rule CLs --testStat LHC -H ProfileLikelihood -s -1 -T 10000 Datacards/datacard_H2A4Mu_mA_0.6000_GeV.txt > macros/sh/OutPut_0.6000_T10000_0.txt 

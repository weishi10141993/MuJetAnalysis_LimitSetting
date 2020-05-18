#!/bin/bash
#SBATCH --job-name=ToyLimit
#SBATCH --time=02:59:00
#SBATCH --nodes=1
#SBATCH --mem-per-cpu=4000
#SBATCH --ntasks-per-node=28
#SBATCH --output=ToyLimit.out.%j

module load cctools
export PARROT_CVMFS_ALIEN_CACHE=/scratch/group/mitchcomp/CVMFS_cache
cmsSite=/scratch/group/mitchcomp/CMS/LOCAL_TAMU_HPRC
cmsMount=--mount=/cvmfs/cms.cern.ch/SITECONF/local=$cmsSite

parrot_run $cmsMount $SHELL << EOF
shopt -s expand_aliases
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /home/ws13/Run2Limit/CMSSW_10_2_13/src/MuJetAnalysis_LimitSetting/
cmsenv
combine -n .H2A4Mu_mA_0.2113_GeV_LHC_T30000_0 -m 125 -M HybridNew --saveHybridResult --expectedFromGrid 0.500 --rule CLs --testStat LHC --cl 0.95 --rAbsAcc 0.01 --rRelAcc 0.001 -s 811544624 -T 600000 --fork 50 Datacards/TEST/datacardCombined_mA_0.2113_GeV.txt > Datacards/TEST/output_combined_0.500_0.2113_T30000_0.txt
EOF

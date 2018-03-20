CS_SM_ggH_14TeV = [
	[	85	,	95.27	], # <- this value linearly extrapolated from next two
	[	90	,	87.55	],
	[	95	,	79.83	],
	[	100	,	73.27	],
	[	105	,	67.34	],
	[	110	,	62.16	],
	[	115	,	57.57	],
	[	120	,	53.49	],
	[	125	,	49.85	],
	[	130	,	46.55	],
	[	135	,	43.61	],
	[	140	,	40.93	],
	[	145	,	38.49	],
	[	150	,	36.27	],
	[	155	,	34.22	],
	]

CS_SM_ggH_7TeV = [
	[	85	,	32.36	], # <- this value linearly extrapolated from next two
	[	90	,	29.47	],
	[	95	,	26.58	],
	[	100	,	24.02	],
	[	105	,	21.78	],
	[	110	,	19.84	],
	[	115	,	18.13	],
	[	120	,	16.63	],
	[	125	,	15.31	],
	[	130	,	14.12	],
	[	135	,	13.08	],
	[	140	,	12.13	],
	[	145	,	11.27	],
	[	150	,	10.5	],
	[	155	,	9.795	],
	]

################################################################################
#                    8 TeV                                                      
################################################################################

# 0 - Higgs mass in GeV
# 1 - Cross Section in pb
# 2,3 - uncertainty in %
CS_SM_ggH_8TeV_pb = [
  [	80	,	46.12, 16.7, -15.9 ],
  [	85	,	41.07, 16.5, -15.6 ],
	[	90	,	36.80, 16.1, -15.4 ],
	[	95	,	33.19, 15.9, -15.1 ],
	[	100	,	30.12, 15.7, -14.9 ],
	[	105	,	27.39, 15.5, -14.8 ],
	[	110	,	25.04, 15.3, -14.9 ],
	[	115	,	22.96, 15.0, -14.9 ],
	[	120	,	21.13, 14.8, -14.8 ],
	[	125	,	19.52, 14.7, -14.7 ],
	[	130	,	18.07, 14.6, -14.6 ],
	[	135	,	16.79, 14.4, -14.7 ],
	[	140	,	15.63, 14.3, -14.5 ],
	[	145	,	14.59, 14.1, -14.4 ],
	[	150	,	13.65, 14.1, -14.4 ],
	[	155	,	12.79, 14.1, -14.4 ],
  ]

def fCS_SM_ggH_8TeV_pb(mh):
    mh_min = CS_SM_ggH_8TeV_pb[0][0]
    mh_max = CS_SM_ggH_8TeV_pb[len(CS_SM_ggH_8TeV_pb)-1][0]
    if mh < mh_min or mh > mh_max: raise Exception
    # get the bin number
    i = int(floor( (mh - mh_min)/(mh_max - mh_min) * ( len(CS_SM_ggH_8TeV_pb)-1 ) ))
    low, high = CS_SM_ggH_8TeV_pb[i], CS_SM_ggH_8TeV_pb[i+1]
    kh = (mh - low[0])/(high[0] - low[0])
    CS = kh * (high[1] - low[1]) + low[1]
    CS_errP = kh * (high[2] - low[2]) + low[2]
    CS_errM = kh * (high[3] - low[3]) + low[3]
    return CS, CS_errP, CS_errM

################################################################################
#                    13 TeV                                                      
# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageBSMAt13TeV
################################################################################

# 0 - Higgs mass in GeV
# 1 - Cross Section in pb
# 2,3 - uncertainty in %
CS_SM_ggH_13TeV_pb = [
  [	85	,	93.4	,	2.4	,	-4.5	],
  [	90	,	84.2	,	2.3	,	-4.3	],
  [	95	,	76.3	,	2.2	,	-4.1	],
  [	100	,	69.3	,	2	,	-4	],
  [	105	,	63.2	,	2	,	-3.9	],
  [	110	,	57.9	,	1.9	,	-3.9	],
  [	115	,	53.1	,	1.8	,	-3.8	],
  [	120	,	48.9	,	1.8	,	-3.7	],
  [	125	,	45.2	,	1.7	,	-3.7	],
  [	130	,	41.8	,	1.7	,	-3.6	],
  [	135	,	38.8	,	1.6	,	-3.5	],
  [	140	,	36	,	1.6	,	-3.5	],
  [	145	,	33.5	,	1.5	,	-3.5	],
  [	150	,	31.29	,	1.5	,	-3.4	],
]

def fCS_SM_ggH_13TeV_pb(mh):
    mh_min = CS_SM_ggH_13TeV_pb[0][0]
    mh_max = CS_SM_ggH_13TeV_pb[len(CS_SM_ggH_13TeV_pb)-1][0]
    if mh < mh_min or mh > mh_max: raise Exception
    # get the bin number
    i = int(floor( (mh - mh_min)/(mh_max - mh_min) * ( len(CS_SM_ggH_13TeV_pb)-1 ) ))
    low, high = CS_SM_ggH_13TeV_pb[i], CS_SM_ggH_13TeV_pb[i+1]
    kh = (mh - low[0])/(high[0] - low[0])
    CS = kh * (high[1] - low[1]) + low[1]
    CS_errP = kh * (high[2] - low[2]) + low[2]
    CS_errM = kh * (high[3] - low[3]) + low[3]
    return CS, CS_errP, CS_errM

#VBF xSec from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt14TeV2010#VBF_Process
CS_SM_VBGH_13TeV_pb = [
  [	85	,	5.769	,	2.9	,	3.0	],
  [	90	,	5.569	,	2.9	,	3.0	],
  [	95	,	5.338	,	3.0	,	3.1	],
  [	100	,	5.114	,	2.8	,	3.1	],
  [	105	,	4.900	,	3.2	,	2.9	],
  [	110	,	4.750	,	2.2	,	3.9	],
  [	115	,	4.520	,	2.9	,	3.0	],
  [	120	,	4.361	,	2.5	,	3.5	],
  [	125	,	4.180	,	2.8	,	3.0	],
  [	130	,	4.029	,	2.5	,	3.1	],
  [	135	,	3.862	,	3.1	,	2.8	],
  [	140	,	3.732	,	2.6	,	3.3	],
  [	145	,	3.590	,	3.0	,	3.0	],
  [	150	,	3.460	,	2.8	,	3.0	],
]

def fCS_SM_VBFH_13TeV_pb(mh):
    mh_min = CS_SM_VBGH_13TeV_pb[0][0]
    mh_max = CS_SM_VBGH_13TeV_pb[len(CS_SM_VBGH_13TeV_pb)-1][0]
    if mh < mh_min or mh > mh_max: raise Exception
    # get the bin number
    i = int(floor( (mh - mh_min)/(mh_max - mh_min) * ( len(CS_SM_VBGH_13TeV_pb)-1 ) ))
    low, high = CS_SM_VBGH_13TeV_pb[i], CS_SM_VBGH_13TeV_pb[i+1]
    kh = (mh - low[0])/(high[0] - low[0])
    CS = kh * (high[1] - low[1]) + low[1]
    CS_errP = kh * (high[2] - low[2]) + low[2]
    CS_errM = kh * (high[3] - low[3]) + low[3]
    return CS, CS_errP, CS_errM

#HW XSec from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt14TeV2010#HW_Process
CS_SM_HW_13TeV_pb = [
  [	85	,	4.681	,	4.3	,	4.6	],
  [	90	,	4.090	,	4.3	,	4.6	],
  [	95	,	3.499	,	4.4	,	4.5	],
  [	100	,	3.002	,	4.5	,	4.3	],
  [	105	,	2.596	,	4.1	,	4.0	],
  [	110	,	2.246	,	4.1	,	4.6	],
  [	115	,	1.952	,	4.5	,	4.0	],
  [	120	,	1.710	,	4.4	,	4.1	],
  [	125	,	1.504	,	4.1	,	4.4	],
  [	130	,	1.324	,	3.7	,	3.7	],
  [	135	,	1.167	,	3.4	,	3.4	],
  [	140	,	1.034	,	3.8	,	3.8	],
  [	145	,	0.920	,	3.7	,	3.7	],
  [	150	,	0.8156,	3.3	,	3.3	],
]

def fCS_SM_HW_13TeV_pb(mh):
    mh_min = CS_SM_HW_13TeV_pb[0][0]
    mh_max = CS_SM_HW_13TeV_pb[len(CS_SM_HW_13TeV_pb)-1][0]
    if mh < mh_min or mh > mh_max: raise Exception
    # get the bin number
    i = int(floor( (mh - mh_min)/(mh_max - mh_min) * ( len(CS_SM_HW_13TeV_pb)-1 ) ))
    low, high = CS_SM_HW_13TeV_pb[i], CS_SM_HW_13TeV_pb[i+1]
    kh = (mh - low[0])/(high[0] - low[0])
    CS = kh * (high[1] - low[1]) + low[1]
    CS_errP = kh * (high[2] - low[2]) + low[2]
    CS_errM = kh * (high[3] - low[3]) + low[3]
    return CS, CS_errP, CS_errM

#HZ XSec from https://twiki.cern.ch/twiki/bin/view/LHCPhysics/CERNYellowReportPageAt14TeV2010#HZ_Process
CS_SM_HZ_13TeV_pb = [
  [	85	,	2.549	,	5.3	,	5.7	],
  [	90	,	2.245	,	5.2	,	5.7	],
  [	95	,	1.941	,	5.7	,	5.2	],
  [	100	,	1.683	,	5.4	,	5.3	],
  [	105	,	1.468	,	6.1	,	5.4	],
  [	110	,	1.283	,	6.0	,	5.6	],
  [	115	,	1.130	,	6.4	,	5.2	],
  [	120	,	0.9967,	6.3	,	5.5	],
  [	125	,	0.8830,	5.9	,	5.7	],
  [	130	,	0.7846,	5.8	,	5.2	],
  [	135	,	0.6981,	6.7	,	5.2	],
  [	140	,	0.6256,	6.0	,	5.5	],
  [	145	,	0.5601,	6.5	,	4.7	],
  [	150	,	0.5016,	6.0	,	5.5	],
]

def fCS_SM_HZ_13TeV_pb(mh):
    mh_min = CS_SM_HZ_13TeV_pb[0][0]
    mh_max = CS_SM_HZ_13TeV_pb[len(CS_SM_HZ_13TeV_pb)-1][0]
    if mh < mh_min or mh > mh_max: raise Exception
    # get the bin number
    i = int(floor( (mh - mh_min)/(mh_max - mh_min) * ( len(CS_SM_HZ_13TeV_pb)-1 ) ))
    low, high = CS_SM_HZ_13TeV_pb[i], CS_SM_HZ_13TeV_pb[i+1]
    kh = (mh - low[0])/(high[0] - low[0])
    CS = kh * (high[1] - low[1]) + low[1]
    CS_errP = kh * (high[2] - low[2]) + low[2]
    CS_errM = kh * (high[3] - low[3]) + low[3]
    return CS, CS_errP, CS_errM

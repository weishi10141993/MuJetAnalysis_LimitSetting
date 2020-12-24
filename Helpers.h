//CB fitted mean mass [GeV] for prompt signals
double mean[11] = {0.2560, 0.4012, 0.7003, 1.0000, 1.9990, 4.9980, 8.4920, 14.990, 24.980, 34.970, 57.930};

//80% signal eff needed mass window size for prompt signals
//double window[11] = {0.030922364, 0.0201698988, 0.02337757474, 0.0275968, 0.04615657165, 0.124742502, 0.2110350916, 0.3849085576, 0.67586519, 0.914118934, 1.860449598};

//85% signal eff needed mass window size for prompt signals
//double window[11] = {0.0359823872, 0.0252123735, 0.02787326219, 0.0326656, 0.056518251, 0.1538490858, 0.2586881768, 0.46940068, 0.849659096, 1.102319891, 2.524895883};

//90% signal eff needed mass window size from above prompt signals
double window[11] = {0.0438535344, 0.0336164980, 0.0359654996, 0.0428032000, 0.0753576680, 0.2037460866, 0.3539943472, 0.7041010200, 1.1972469080, 1.6131510600, 3.9866777100};

//95% signal eff needed mass window size for prompt signals
//double window[11] = {0.0629691776, 0.05176940692, 0.05574652438, 0.0664576, 0.1224562105, 0.3617532558, 0.748834196, 1.40820204, 2.70346076, 2.6885851, 9.523730085};

Double_t MCBinCenterMass[14] = {12.75, 16.25, 19.75, 23.25, 26.75, 30.25, 33.75, 37.25, 40.75, 44.25, 47.75, 51.25, 54.75, 58.25};

Double_t MCBinContentm1[14] = {0.0260007, 0.070103, 0.457687, 0.161783, 0.157428, 0.62272, 0.599198, 0.887516, 1.56432, 2.07059, 0.707749, 1.12067, 2.29358, 0.954618};
Double_t MCBinErrm1[14] = {0.00764504, 0.0148186, 0.357686, 0.0232653, 0.0228677, 0.160303, 0.117906, 0.195744, 0.530653, 0.765715, 0.117726, 0.224549, 0.773769, 0.375918};

Double_t MCBinContentm2[14] = {0.0263188, 0.0750433, 0.462819, 0.149645, 0.17395, 0.482848, 0.851617, 0.792001, 1.40641, 2.22213, 0.8121, 1.09374, 1.93753, 1.20782};
Double_t MCBinErrm2[14] = {0.00767975, 0.0153949, 0.357711, 0.0224435, 0.0240383, 0.116155, 0.195536, 0.162129, 0.518903, 0.773695, 0.16106, 0.224314, 0.563703, 0.640463};

namespace Helpers_cfg {

  double My_MassWindow(double x, double y) {
    //return this mass window size given m1 and m2
    double mysize = 0.0;

    //Interpolation
    //Start and end with 0.2113 and 60GeV to match bkg analysis
    if ( (x+y)/2 >= 0.2113   && (x+y)/2 < mean[1] ) mysize = window[0] + ( (x+y)/2 - mean[0] )*( window[1]  - window[0] )/( mean[1]  - mean[0] );
    if ( (x+y)/2 >= mean[1]  && (x+y)/2 < mean[2] ) mysize = window[1] + ( (x+y)/2 - mean[1] )*( window[2]  - window[1] )/( mean[2]  - mean[1] );
    if ( (x+y)/2 >= mean[2]  && (x+y)/2 < mean[3] ) mysize = window[2] + ( (x+y)/2 - mean[2] )*( window[3]  - window[2] )/( mean[3]  - mean[2] );
    if ( (x+y)/2 >= mean[3]  && (x+y)/2 < mean[4] ) mysize = window[3] + ( (x+y)/2 - mean[3] )*( window[4]  - window[3] )/( mean[4]  - mean[3] );
    if ( (x+y)/2 >= mean[4]  && (x+y)/2 < mean[5] ) mysize = window[4] + ( (x+y)/2 - mean[4] )*( window[5]  - window[4] )/( mean[5]  - mean[4] );
    if ( (x+y)/2 >= mean[5]  && (x+y)/2 < mean[6] ) mysize = window[5] + ( (x+y)/2 - mean[5] )*( window[6]  - window[5] )/( mean[6]  - mean[5] );
    if ( (x+y)/2 >= mean[6]  && (x+y)/2 < mean[7] ) mysize = window[6] + ( (x+y)/2 - mean[6] )*( window[7]  - window[6] )/( mean[7]  - mean[6] );
    if ( (x+y)/2 >= mean[7]  && (x+y)/2 < mean[8] ) mysize = window[7] + ( (x+y)/2 - mean[7] )*( window[8]  - window[7] )/( mean[8]  - mean[7] );
    if ( (x+y)/2 >= mean[8]  && (x+y)/2 < mean[9] ) mysize = window[8] + ( (x+y)/2 - mean[8] )*( window[9]  - window[8] )/( mean[9]  - mean[8] );
    if ( (x+y)/2 >= mean[9]  && (x+y)/2 < 60.000  ) mysize = window[9] + ( (x+y)/2 - mean[9] )*( window[10] - window[9] )/( mean[10] - mean[9] );

    return mysize;
  }

  Double_t My_BKGShapem1(double x)
  {
     Double_t mybkg = 0.0;

     if ( x >= 11.                 && x < MCBinCenterMass[0] )   mybkg = MCBinContentm1[0];
     if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm1[0]  + ( x - MCBinCenterMass[0] )*( MCBinContentm1[1] - MCBinContentm1[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
     if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm1[1]  + ( x - MCBinCenterMass[1] )*( MCBinContentm1[2] - MCBinContentm1[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
     if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm1[2]  + ( x - MCBinCenterMass[2] )*( MCBinContentm1[3] - MCBinContentm1[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
     if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm1[3]  + ( x - MCBinCenterMass[3] )*( MCBinContentm1[4] - MCBinContentm1[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
     if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm1[4]  + ( x - MCBinCenterMass[4] )*( MCBinContentm1[5] - MCBinContentm1[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
     if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm1[5]  + ( x - MCBinCenterMass[5] )*( MCBinContentm1[6] - MCBinContentm1[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
     if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm1[6]  + ( x - MCBinCenterMass[6] )*( MCBinContentm1[7] - MCBinContentm1[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
     if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm1[7]  + ( x - MCBinCenterMass[7] )*( MCBinContentm1[8] - MCBinContentm1[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
     if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm1[8]  + ( x - MCBinCenterMass[8] )*( MCBinContentm1[9] - MCBinContentm1[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
     if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm1[9]  + ( x - MCBinCenterMass[9] )*( MCBinContentm1[10] - MCBinContentm1[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
     if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm1[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm1[11] - MCBinContentm1[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
     if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm1[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm1[12] - MCBinContentm1[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
     if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm1[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm1[13] - MCBinContentm1[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
     if ( x >= MCBinCenterMass[13]  && x <= 60.                ) mybkg = MCBinContentm1[13];

     return mybkg;
  }

  Double_t My_BKGShapem2(double x)
  {
    Double_t mybkg = 0.0;

    if ( x >= 11.                 && x < MCBinCenterMass[0] )   mybkg = MCBinContentm2[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm2[0]  + ( x - MCBinCenterMass[0] )*( MCBinContentm2[1] - MCBinContentm2[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm2[1]  + ( x - MCBinCenterMass[1] )*( MCBinContentm2[2] - MCBinContentm2[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm2[2]  + ( x - MCBinCenterMass[2] )*( MCBinContentm2[3] - MCBinContentm2[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm2[3]  + ( x - MCBinCenterMass[3] )*( MCBinContentm2[4] - MCBinContentm2[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm2[4]  + ( x - MCBinCenterMass[4] )*( MCBinContentm2[5] - MCBinContentm2[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm2[5]  + ( x - MCBinCenterMass[5] )*( MCBinContentm2[6] - MCBinContentm2[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm2[6]  + ( x - MCBinCenterMass[6] )*( MCBinContentm2[7] - MCBinContentm2[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm2[7]  + ( x - MCBinCenterMass[7] )*( MCBinContentm2[8] - MCBinContentm2[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm2[8]  + ( x - MCBinCenterMass[8] )*( MCBinContentm2[9] - MCBinContentm2[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm2[9]  + ( x - MCBinCenterMass[9] )*( MCBinContentm2[10] - MCBinContentm2[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm2[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm2[11] - MCBinContentm2[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm2[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm2[12] - MCBinContentm2[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm2[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm2[13] - MCBinContentm2[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.                ) mybkg = MCBinContentm2[13];

    return mybkg;
  }

  double My_BKGShapem1SigmaUp(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm1[0] + MCBinErrm1[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm1[0] + MCBinErrm1[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm1[1] + MCBinErrm1[1] - MCBinContentm1[0] - MCBinErrm1[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm1[1] + MCBinErrm1[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm1[2] + MCBinErrm1[2] - MCBinContentm1[1] - MCBinErrm1[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm1[2] + MCBinErrm1[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm1[3] + MCBinErrm1[3] - MCBinContentm1[2] - MCBinErrm1[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm1[3] + MCBinErrm1[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm1[4] + MCBinErrm1[4] - MCBinContentm1[3] - MCBinErrm1[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm1[4] + MCBinErrm1[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm1[5] + MCBinErrm1[5] - MCBinContentm1[4] - MCBinErrm1[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm1[5] + MCBinErrm1[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm1[6] + MCBinErrm1[6] - MCBinContentm1[5] - MCBinErrm1[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm1[6] + MCBinErrm1[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm1[7] + MCBinErrm1[7] - MCBinContentm1[6] - MCBinErrm1[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm1[7] + MCBinErrm1[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm1[8] + MCBinErrm1[8] - MCBinContentm1[7] - MCBinErrm1[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm1[8] + MCBinErrm1[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm1[9] + MCBinErrm1[9] - MCBinContentm1[8] - MCBinErrm1[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm1[9] + MCBinErrm1[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm1[10] + MCBinErrm1[10] - MCBinContentm1[9] - MCBinErrm1[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm1[10] + MCBinErrm1[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm1[11] + MCBinErrm1[11] - MCBinContentm1[10] - MCBinErrm1[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm1[11] + MCBinErrm1[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm1[12] + MCBinErrm1[12] - MCBinContentm1[11] - MCBinErrm1[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm1[12] + MCBinErrm1[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm1[13] + MCBinErrm1[13] - MCBinContentm1[12] - MCBinErrm1[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm1[13] + MCBinErrm1[13];

    return mybkg;
  }

  double My_BKGShapem1SigmaDn(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm1[0] - MCBinErrm1[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm1[0] - MCBinErrm1[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm1[1] - MCBinErrm1[1] - MCBinContentm1[0] + MCBinErrm1[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm1[1] - MCBinErrm1[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm1[2] - MCBinErrm1[2] - MCBinContentm1[1] + MCBinErrm1[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm1[2] - MCBinErrm1[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm1[3] - MCBinErrm1[3] - MCBinContentm1[2] + MCBinErrm1[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm1[3] - MCBinErrm1[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm1[4] - MCBinErrm1[4] - MCBinContentm1[3] + MCBinErrm1[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm1[4] - MCBinErrm1[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm1[5] - MCBinErrm1[5] - MCBinContentm1[4] + MCBinErrm1[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm1[5] - MCBinErrm1[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm1[6] - MCBinErrm1[6] - MCBinContentm1[5] + MCBinErrm1[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm1[6] - MCBinErrm1[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm1[7] - MCBinErrm1[7] - MCBinContentm1[6] + MCBinErrm1[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm1[7] - MCBinErrm1[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm1[8] - MCBinErrm1[8] - MCBinContentm1[7] + MCBinErrm1[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm1[8] - MCBinErrm1[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm1[9] - MCBinErrm1[9] - MCBinContentm1[8] + MCBinErrm1[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm1[9] - MCBinErrm1[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm1[10] - MCBinErrm1[10] - MCBinContentm1[9] + MCBinErrm1[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm1[10] - MCBinErrm1[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm1[11] - MCBinErrm1[11] - MCBinContentm1[10] + MCBinErrm1[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm1[11] - MCBinErrm1[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm1[12] - MCBinErrm1[12] - MCBinContentm1[11] + MCBinErrm1[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm1[12] - MCBinErrm1[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm1[13] - MCBinErrm1[13] - MCBinContentm1[12] + MCBinErrm1[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm1[13] - MCBinErrm1[13];

    return mybkg;
  }

  //BraidA starts from +1sigma for the first bin then the -1 sigma for the next, etc
  double My_BKGShapem1SigmaBraidA(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm1[0] + MCBinErrm1[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm1[0] + MCBinErrm1[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm1[1] - MCBinErrm1[1] - MCBinContentm1[0] - MCBinErrm1[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm1[1] - MCBinErrm1[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm1[2] + MCBinErrm1[2] - MCBinContentm1[1] + MCBinErrm1[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm1[2] + MCBinErrm1[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm1[3] - MCBinErrm1[3] - MCBinContentm1[2] - MCBinErrm1[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm1[3] - MCBinErrm1[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm1[4] + MCBinErrm1[4] - MCBinContentm1[3] + MCBinErrm1[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm1[4] + MCBinErrm1[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm1[5] - MCBinErrm1[5] - MCBinContentm1[4] - MCBinErrm1[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm1[5] - MCBinErrm1[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm1[6] + MCBinErrm1[6] - MCBinContentm1[5] + MCBinErrm1[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm1[6] + MCBinErrm1[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm1[7] - MCBinErrm1[7] - MCBinContentm1[6] - MCBinErrm1[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm1[7] - MCBinErrm1[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm1[8] + MCBinErrm1[8] - MCBinContentm1[7] + MCBinErrm1[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm1[8] + MCBinErrm1[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm1[9] - MCBinErrm1[9] - MCBinContentm1[8] - MCBinErrm1[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm1[9] - MCBinErrm1[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm1[10] + MCBinErrm1[10] - MCBinContentm1[9] + MCBinErrm1[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm1[10] + MCBinErrm1[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm1[11] - MCBinErrm1[11] - MCBinContentm1[10] - MCBinErrm1[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm1[11] - MCBinErrm1[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm1[12] + MCBinErrm1[12] - MCBinContentm1[11] + MCBinErrm1[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm1[12] + MCBinErrm1[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm1[13] - MCBinErrm1[13] - MCBinContentm1[12] - MCBinErrm1[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm1[13] - MCBinErrm1[13];

    return mybkg;
  }

  //BraidB starts from -1sigma for the first bin then the +1 sigma for the next, etc
  double My_BKGShapem1SigmaBraidB(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm1[0] - MCBinErrm1[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm1[0] - MCBinErrm1[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm1[1] + MCBinErrm1[1] - MCBinContentm1[0] + MCBinErrm1[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm1[1] + MCBinErrm1[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm1[2] - MCBinErrm1[2] - MCBinContentm1[1] - MCBinErrm1[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm1[2] - MCBinErrm1[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm1[3] + MCBinErrm1[3] - MCBinContentm1[2] + MCBinErrm1[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm1[3] + MCBinErrm1[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm1[4] - MCBinErrm1[4] - MCBinContentm1[3] - MCBinErrm1[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm1[4] - MCBinErrm1[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm1[5] + MCBinErrm1[5] - MCBinContentm1[4] + MCBinErrm1[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm1[5] + MCBinErrm1[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm1[6] - MCBinErrm1[6] - MCBinContentm1[5] - MCBinErrm1[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm1[6] - MCBinErrm1[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm1[7] + MCBinErrm1[7] - MCBinContentm1[6] + MCBinErrm1[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm1[7] + MCBinErrm1[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm1[8] - MCBinErrm1[8] - MCBinContentm1[7] - MCBinErrm1[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm1[8] - MCBinErrm1[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm1[9] + MCBinErrm1[9] - MCBinContentm1[8] + MCBinErrm1[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm1[9] + MCBinErrm1[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm1[10] - MCBinErrm1[10] - MCBinContentm1[9] - MCBinErrm1[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm1[10] - MCBinErrm1[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm1[11] + MCBinErrm1[11] - MCBinContentm1[10] + MCBinErrm1[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm1[11] + MCBinErrm1[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm1[12] - MCBinErrm1[12] - MCBinContentm1[11] - MCBinErrm1[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm1[12] - MCBinErrm1[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm1[13] + MCBinErrm1[13] - MCBinContentm1[12] + MCBinErrm1[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm1[13] + MCBinErrm1[13];

    return mybkg;
  }


  double My_BKGShapem2SigmaUp(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm2[0] + MCBinErrm2[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm2[0] + MCBinErrm2[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm2[1] + MCBinErrm2[1] - MCBinContentm2[0] - MCBinErrm2[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm2[1] + MCBinErrm2[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm2[2] + MCBinErrm2[2] - MCBinContentm2[1] - MCBinErrm2[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm2[2] + MCBinErrm2[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm2[3] + MCBinErrm2[3] - MCBinContentm2[2] - MCBinErrm2[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm2[3] + MCBinErrm2[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm2[4] + MCBinErrm2[4] - MCBinContentm2[3] - MCBinErrm2[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm2[4] + MCBinErrm2[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm2[5] + MCBinErrm2[5] - MCBinContentm2[4] - MCBinErrm2[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm2[5] + MCBinErrm2[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm2[6] + MCBinErrm2[6] - MCBinContentm2[5] - MCBinErrm2[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm2[6] + MCBinErrm2[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm2[7] + MCBinErrm2[7] - MCBinContentm2[6] - MCBinErrm2[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm2[7] + MCBinErrm2[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm2[8] + MCBinErrm2[8] - MCBinContentm2[7] - MCBinErrm2[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm2[8] + MCBinErrm2[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm2[9] + MCBinErrm2[9] - MCBinContentm2[8] - MCBinErrm2[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm2[9] + MCBinErrm2[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm2[10] + MCBinErrm2[10] - MCBinContentm2[9] - MCBinErrm2[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm2[10] + MCBinErrm2[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm2[11] + MCBinErrm2[11] - MCBinContentm2[10] - MCBinErrm2[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm2[11] + MCBinErrm2[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm2[12] + MCBinErrm2[12] - MCBinContentm2[11] - MCBinErrm2[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm2[12] + MCBinErrm2[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm2[13] + MCBinErrm2[13] - MCBinContentm2[12] - MCBinErrm2[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm2[13] + MCBinErrm2[13];

    return mybkg;
  }

  double My_BKGShapem2SigmaDn(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm2[0] - MCBinErrm2[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm2[0] - MCBinErrm2[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm2[1] - MCBinErrm2[1] - MCBinContentm2[0] + MCBinErrm2[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm2[1] - MCBinErrm2[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm2[2] - MCBinErrm2[2] - MCBinContentm2[1] + MCBinErrm2[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm2[2] - MCBinErrm2[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm2[3] - MCBinErrm2[3] - MCBinContentm2[2] + MCBinErrm2[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm2[3] - MCBinErrm2[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm2[4] - MCBinErrm2[4] - MCBinContentm2[3] + MCBinErrm2[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm2[4] - MCBinErrm2[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm2[5] - MCBinErrm2[5] - MCBinContentm2[4] + MCBinErrm2[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm2[5] - MCBinErrm2[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm2[6] - MCBinErrm2[6] - MCBinContentm2[5] + MCBinErrm2[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm2[6] - MCBinErrm2[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm2[7] - MCBinErrm2[7] - MCBinContentm2[6] + MCBinErrm2[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm2[7] - MCBinErrm2[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm2[8] - MCBinErrm2[8] - MCBinContentm2[7] + MCBinErrm2[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm2[8] - MCBinErrm2[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm2[9] - MCBinErrm2[9] - MCBinContentm2[8] + MCBinErrm2[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm2[9] - MCBinErrm2[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm2[10] - MCBinErrm2[10] - MCBinContentm2[9] + MCBinErrm2[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm2[10] - MCBinErrm2[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm2[11] - MCBinErrm2[11] - MCBinContentm2[10] + MCBinErrm2[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm2[11] - MCBinErrm2[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm2[12] - MCBinErrm2[12] - MCBinContentm2[11] + MCBinErrm2[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm2[12] - MCBinErrm2[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm2[13] - MCBinErrm2[13] - MCBinContentm2[12] + MCBinErrm2[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm2[13] - MCBinErrm2[13];

    return mybkg;
  }

  //BraidA starts from +1sigma for the first bin then the -1 sigma for the next, etc
  double My_BKGShapem2SigmaBraidA(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm2[0] + MCBinErrm2[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm2[0] + MCBinErrm2[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm2[1] - MCBinErrm2[1] - MCBinContentm2[0] - MCBinErrm2[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm2[1] - MCBinErrm2[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm2[2] + MCBinErrm2[2] - MCBinContentm2[1] + MCBinErrm2[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm2[2] + MCBinErrm2[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm2[3] - MCBinErrm2[3] - MCBinContentm2[2] - MCBinErrm2[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm2[3] - MCBinErrm2[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm2[4] + MCBinErrm2[4] - MCBinContentm2[3] + MCBinErrm2[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm2[4] + MCBinErrm2[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm2[5] - MCBinErrm2[5] - MCBinContentm2[4] - MCBinErrm2[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm2[5] - MCBinErrm2[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm2[6] + MCBinErrm2[6] - MCBinContentm2[5] + MCBinErrm2[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm2[6] + MCBinErrm2[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm2[7] - MCBinErrm2[7] - MCBinContentm2[6] - MCBinErrm2[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm2[7] - MCBinErrm2[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm2[8] + MCBinErrm2[8] - MCBinContentm2[7] + MCBinErrm2[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm2[8] + MCBinErrm2[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm2[9] - MCBinErrm2[9] - MCBinContentm2[8] - MCBinErrm2[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm2[9] - MCBinErrm2[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm2[10] + MCBinErrm2[10] - MCBinContentm2[9] + MCBinErrm2[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm2[10] + MCBinErrm2[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm2[11] - MCBinErrm2[11] - MCBinContentm2[10] - MCBinErrm2[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm2[11] - MCBinErrm2[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm2[12] + MCBinErrm2[12] - MCBinContentm2[11] + MCBinErrm2[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm2[12] + MCBinErrm2[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm2[13] - MCBinErrm2[13] - MCBinContentm2[12] - MCBinErrm2[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm2[13] - MCBinErrm2[13];

    return mybkg;
  }

  //BraidB starts from -1sigma for the first bin then the +1 sigma for the next, etc
  double My_BKGShapem2SigmaBraidB(double x) {
    double mybkg = 0.0;

    if ( x >= 11.000              && x < MCBinCenterMass[0] )   mybkg = MCBinContentm2[0] - MCBinErrm2[0];
    if ( x >= MCBinCenterMass[0]  && x < MCBinCenterMass[1] )   mybkg = MCBinContentm2[0] - MCBinErrm2[0] + ( x - MCBinCenterMass[0] )*( MCBinContentm2[1] + MCBinErrm2[1] - MCBinContentm2[0] + MCBinErrm2[0] )/( MCBinCenterMass[1] - MCBinCenterMass[0] );
    if ( x >= MCBinCenterMass[1]  && x < MCBinCenterMass[2] )   mybkg = MCBinContentm2[1] + MCBinErrm2[1] + ( x - MCBinCenterMass[1] )*( MCBinContentm2[2] - MCBinErrm2[2] - MCBinContentm2[1] - MCBinErrm2[1] )/( MCBinCenterMass[2] - MCBinCenterMass[1] );
    if ( x >= MCBinCenterMass[2]  && x < MCBinCenterMass[3] )   mybkg = MCBinContentm2[2] - MCBinErrm2[2] + ( x - MCBinCenterMass[2] )*( MCBinContentm2[3] + MCBinErrm2[3] - MCBinContentm2[2] + MCBinErrm2[2] )/( MCBinCenterMass[3] - MCBinCenterMass[2] );
    if ( x >= MCBinCenterMass[3]  && x < MCBinCenterMass[4] )   mybkg = MCBinContentm2[3] + MCBinErrm2[3] + ( x - MCBinCenterMass[3] )*( MCBinContentm2[4] - MCBinErrm2[4] - MCBinContentm2[3] - MCBinErrm2[3] )/( MCBinCenterMass[4] - MCBinCenterMass[3] );
    if ( x >= MCBinCenterMass[4]  && x < MCBinCenterMass[5] )   mybkg = MCBinContentm2[4] - MCBinErrm2[4] + ( x - MCBinCenterMass[4] )*( MCBinContentm2[5] + MCBinErrm2[5] - MCBinContentm2[4] + MCBinErrm2[4] )/( MCBinCenterMass[5] - MCBinCenterMass[4] );
    if ( x >= MCBinCenterMass[5]  && x < MCBinCenterMass[6] )   mybkg = MCBinContentm2[5] + MCBinErrm2[5] + ( x - MCBinCenterMass[5] )*( MCBinContentm2[6] - MCBinErrm2[6] - MCBinContentm2[5] - MCBinErrm2[5] )/( MCBinCenterMass[6] - MCBinCenterMass[5] );
    if ( x >= MCBinCenterMass[6]  && x < MCBinCenterMass[7] )   mybkg = MCBinContentm2[6] - MCBinErrm2[6] + ( x - MCBinCenterMass[6] )*( MCBinContentm2[7] + MCBinErrm2[7] - MCBinContentm2[6] + MCBinErrm2[6] )/( MCBinCenterMass[7] - MCBinCenterMass[6] );
    if ( x >= MCBinCenterMass[7]  && x < MCBinCenterMass[8] )   mybkg = MCBinContentm2[7] + MCBinErrm2[7] + ( x - MCBinCenterMass[7] )*( MCBinContentm2[8] - MCBinErrm2[8] - MCBinContentm2[7] - MCBinErrm2[7] )/( MCBinCenterMass[8] - MCBinCenterMass[7] );
    if ( x >= MCBinCenterMass[8]  && x < MCBinCenterMass[9] )   mybkg = MCBinContentm2[8] - MCBinErrm2[8] + ( x - MCBinCenterMass[8] )*( MCBinContentm2[9] + MCBinErrm2[9] - MCBinContentm2[8] + MCBinErrm2[8] )/( MCBinCenterMass[9] - MCBinCenterMass[8] );
    if ( x >= MCBinCenterMass[9]  && x < MCBinCenterMass[10]  ) mybkg = MCBinContentm2[9] + MCBinErrm2[9] + ( x - MCBinCenterMass[9] )*( MCBinContentm2[10] - MCBinErrm2[10] - MCBinContentm2[9] - MCBinErrm2[9] )/( MCBinCenterMass[10] - MCBinCenterMass[9] );
    if ( x >= MCBinCenterMass[10]  && x < MCBinCenterMass[11] ) mybkg = MCBinContentm2[10] - MCBinErrm2[10] + ( x - MCBinCenterMass[10] )*( MCBinContentm2[11] + MCBinErrm2[11] - MCBinContentm2[10] + MCBinErrm2[10] )/( MCBinCenterMass[11] - MCBinCenterMass[10] );
    if ( x >= MCBinCenterMass[11]  && x < MCBinCenterMass[12] ) mybkg = MCBinContentm2[11] + MCBinErrm2[11] + ( x - MCBinCenterMass[11] )*( MCBinContentm2[12] - MCBinErrm2[12] - MCBinContentm2[11] - MCBinErrm2[11] )/( MCBinCenterMass[12] - MCBinCenterMass[11] );
    if ( x >= MCBinCenterMass[12]  && x < MCBinCenterMass[13] ) mybkg = MCBinContentm2[12] - MCBinErrm2[12] + ( x - MCBinCenterMass[12] )*( MCBinContentm2[13] + MCBinErrm2[13] - MCBinContentm2[12] + MCBinErrm2[12] )/( MCBinCenterMass[13] - MCBinCenterMass[12] );
    if ( x >= MCBinCenterMass[13]  && x <= 60.000             ) mybkg = MCBinContentm2[13] + MCBinErrm2[13];

    return mybkg;
  }

}

from Br_2016 import *
from R_2016 import *

##
def efficiencyModel(m, E, ct, R, z):
    return (R/(2*(E/m)*ct*(R^2+z^2))) (exp[-sqrt[R^2+z^2]/((E/m)*ct)])  # Exponencial decay of the GammaD *)

##
def Zmax(m, E, ct, R):
    if 10.0 (E/m) ct < (10 R):
        10*(E/m)*ct
    else:
        10*R

##
def Rmax(m, E, ct):
    if 10*(E/m)*ct<600:
        return 10*(E/m)*ct
    elif 10*(E/m)*ct>=600:
        return 600.0

# efficiency 1 before R0=9.8cm (3rd pixel layer) and zero above this value *)
def effR(R0, R):
    if R>0 && R<R0:
        return 1.0
    elif R>R0:
        return 0.0
        
#Efficiencies for ctau=0, this obtained from cutflow*)
def alpha0(m):
    if m==0.25: 
        return 0.0911856 
    elif (m==0.4): 
        return 0.0645557 
    elif m==0.7:
        return 0.0604557 
    elif m==1.0:
        return 0.0587443 
    elif m==5.0: 
        return 0.0657431 
    elif m==8.5: 
        return 0.127751
    
datapoints = [
    (0.25, alpha0(0.25)),
    (0.4,  alpha0(0.4)),
    (0.7,  alpha0(0.7)),
    (1.0,  alpha0(1.0)),
    (5.0,  alpha0(5.0)),
    (8.5,  alpha0(8.5)),
    ]


feffR=Interpolation[datapoints,InterpolationOrder->1];

f3[m_,E_,ct_]:=NIntegrate[effR[98.0,R]2f1[m,E,ct,R,z], {R,0.0,Rmax[m,E,ct]}, {z,0.0,Zmax[m,E,ct,R]}]

# Final expression of the model with to variables m and ctau, the Energy for the GamamD = 50 GeV which is mean value of distribution *)
def alphavsctau(m, E, ct):
    return feffR[m]*f3[m,E,ct]*f3[m,E,ct]  

##Calling external data for limit setting (Br, limit on N, f(m), etc...)
xsec = ReadList["/Users/Alfredo/Desktop/limite_DarkSUSY_2017/R_2016.dat",{Real,Real}];


R=Interpolation[xsec,InterpolationOrder->1]
InterpolatingFunction[Domain: {{0.36,10.3}}
Output: scalar

]
Plot[R[x],{x,0.25,9.0},PlotRange->{{0.0,9.0},{0.0,30.0}}]
InterpolatingFunction::dmval: Input value {0.250179} lies outside the range of data in the interpolating function. Extrapolation will be used.

# Model Independent Limit *)
#Nlimitf[x_]:=2.+0.196258*Exp[-0.5*((x-0.585342)/0.0400199)^2]+1.32241*Exp[-0.5*((x-0.833146)/0.0350001)^2]+0.893637*Exp[-0.5*((x-1.16449)/0.033)^2]+1.79953*Exp[-0.5*((x-1.41323)/0.03)^2]+0.59907*Exp[-0.5*((x-1.90641)/0.05)^2]+1.1*Exp[-0.5*((x-2.40133)/0.042)^2]+2.20401*Exp[-0.5*((x-2.999)/0.169458)^2]+3.57*Exp[-0.5*((x-3.1005)/0.134076)^2*)
Nlimitf[x_]:=2.33591576728+0.490467147856 *Exp[-0.15* ((x- 1.20105406966)/0.0158823287785)^2]+1.75 *Exp[-0.5*((x-1.37980913362)/0.0363780607304)^2]+0.46814803103 *Exp[-0.5*((x-1.89383556463)/0.0619017859509)^2]+1.2 *Exp[-0.5*((x-2.37120887758)/0.0524109033795)^2]+2.04831493617 *Exp[-0.5*((x-2.84399373813)/0.07)^2]+4.482483411 *Exp[-0.5*((x-3.05938898807)/0.0696193158778)^2]
Nlimitf[0.25]
2.33592

Plot[Nlimitf[m],{m,0.25,9.0},PlotRange->{{0.1,6.0},{0.0,7.0}}]

5
Br = ReadList["/Users/Alfredo/Desktop/limite_DarkSUSY_2017/Br_2016.dat",{Real,Real}]; # Br  GammaD to 2 mu *)
ListLogLogPlot[Br]

Brf = Interpolation[Br,InterpolationOrder->1]
InterpolatingFunction[Domain: {{0.25,10.}}
Output: scalar

]
listBrf = Table[{m,Brf[m]},{m,0.0,9.0,0.01}];
InterpolatingFunction::dmval: Input value {0.} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.01} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.02} lies outside the range of data in the interpolating function. Extrapolation will be used.
General::stop: Further output of InterpolatingFunction::dmval will be suppressed during this calculation.
Brlog=ListLogLogPlot[listBrf,Joined->True,Joined->True,ImageSize->500,AspectRatio->1.0,TicksStyle->Directive[FontSize->16],Frame->True,FrameLabel->{"Subscript[m, γD] [GeV]","Br"},RotateLabel->True,BaseStyle->{FontSize->20},PlotRange->{{0.25,10.0},{0.01,1.0}}]

# Partial witdths*)
alpha=0.0072973525664
mass_electron= 0.000510998928
mass_muon= .1056583715

def ParWidthE(m):
    return 1/3*alpha*m*sqrt[1-(4 mass_electron^2)/m^2](1+(2 mass_electron^2)/m^2)

def ParWidthM(m):
    return 1/3*alpha*m*sqrt[1-(4 mass_muon^2)/m^2](1+(2 mass_muon^2)/m^2)

def ParWidthHad(m):
    return 1/3*alpha*m*sqrt[1-(4 mass_muon^2)/m^2](1+(2 mass_muon^2)/m^2) * R(m) 

def ParWidthTot(m):
    return ParWidthE(m) + ParWidthM(m) + ParWidthHad(m)

def funfm(m):
    return 1/ParWidthTot[m]

print funfm(1.0)


Plot[funfm[m],{m,0.25,9.0},PlotRange->{{0.0,9.0},{0.0,800}}]
InterpolatingFunction::dmval: Input value {0.250179} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.250179} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
General::stop: Further output of InterpolatingFunction::dmval will be suppressed during this calculation.


# Since we have epsilon as a function of the mass and ctau we cannot just plot the distributions as above, the limit is done in an iterative way getting the value in every mass bin and scanning in epsilon until it converges to the value of limit on N(m))*)
Limit on  Br(H->2γ)  as a function of mass and ctau for different values (1%,  5%,10%,20%,40%)

# since our efficiency model is expresed in terms of ctau we need to correlate to which epsilon variable it correspond, at this step using epsilon^2 to avoid the sqrt *)
ctauval[m_] := (1.97*10^-13 funfm[m])/10^Mineps2;  

# This is the expression for the limit this expresion will be evaluated in the mass and ctau space until it converges to a value close to the limit on N(m) *)
Nlimit2[m_,BrHtoGam_]:= 35.9 * 48580 * BrHtoGam *  alphavsctau[m,50,ctauval[m]]* Brf[m] * Brf[m];


Labelepsvsctau={"cτ=100.0","cτ=50.0","cτ=20.0","cτ=10.0","cτ=5.0","cτ=3.0","cτ=1.0","cτ=0.1","cτ=0.001","cτ=0.00001"}

{cτ=100.0,cτ=50.0,cτ=20.0,cτ=10.0,cτ=5.0,cτ=3.0,cτ=1.0,cτ=0.1,cτ=0.001,cτ=0.00001}
Br=0.1%   
listbr01={{Null,Null}} # This list will store the epsilon value in which the limit converges close to 3.07 *)
BrIn=0.001; # value of Br(HGammaD) *)
min= {0.25,0.75}; # Just to split the mass range different precision needed in dificult regions where the Br drops around 0.8 and 1.0 GeV for this Br=0.1% makes not much difference since the distribution doesnt go above mass aprox 0.7 GeV*)
mfin={0.75,8.5};
step={0.01,0.05};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2; # Initial steps to increase the 10^(epsilon^2 )value*)
Mineps2=-16.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision demanded for the limit *)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-16.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m] #&& nval≠pval *)&& Mineps2<-4.0), # once the limit value is above 3.07 break the loop *)
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01; # If the limit was too far from the 3.07 repite the scan with finer steps *)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr01,{m,Mineps2}]; # Here the values will be stored for the whole mass range for specific Br *)
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,2,1}];
Export["/Users/Alfredo/Desktop/limite_DarkSUSY_2018_forPLB/Limit_epsvsmass_BrHtoGamD_01_2018.dat",listbr01];

{{Null,Null}}
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
General::stop: Further output of InterpolatingFunction::dmval will be suppressed during this calculation.
Br=1%   
listbr1={{Null,Null}} # This list will store the epsilon value in which the limit converges close to 3.07 *)
BrIn=0.01; # value of Br(HGammaD) *)
min= {0.25,0.7,0.85,1.1,1.25,1.5,1.8,2.0,2.2,2.5,2.7,3.2}; # Just to split the mass range different precision needed in dificult regions where the Br drops around 0.8 and 1.0 GeV*)
mfin={0.7,0.85,1.0,1.25,1.5,1.8,2.0,2.2,2.5,2.7,3.2,8.5};
step={0.05,0.01,0.01,0.01,0.01,0.05,0.01,0.05,0.01,0.05,0.01,0.1};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2; # Initial steps to increase the 10^(epsilon^2 )value*)
Mineps2=-16.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision demanded for the limit *)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-16.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m] #&& nval≠pval *)&& Mineps2<-4.0), # once the limit value is above 3.07 break the loop *)
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01; # If the limit was too far from the 3.07 repite the scan with finer steps *)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr1,{m,Mineps2}]; # Here the values will be stored for the whole mass range for specific Br *)
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,12,1}];
Export["/Users/Alfredo/Desktop/limite_DarkSUSY_2018_forPLB/Limit_epsvsmass_BrHtoGamD_1_2018.dat",listbr1];

{{Null,Null}}
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
General::stop: Further output of InterpolatingFunction::dmval will be suppressed during this calculation.
Br=5%   
listbr5={{Null,Null}} # To Store the limit value *)
BrIn=0.05; # value of Br(HGammaD) *)
min= {0.25,0.7,0.85,1.0,1.2,2.0,3.5,5.0}; # Just to split the mass range different precision needed in dificult regions where the Br drops around 0.8 and 1.0 GeV*)
mfin={0.7,0.85,1.0,1.2,2.0,3.5,5.0,9.0};
step={0.05,0.01,0.05,0.01,0.1,0.1,0.1,0.1};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2;
Mineps2=-16.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision or closenest to the 3.0*)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-16.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m] #&& nval≠pval *)&& Mineps2<-4.0),
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01;
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr5,{m,Mineps2}];
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,8,1}];
Export["/Users/Alfredo/Desktop/limite_DarkSUSY_2018_forPLB/Limit_epsvsmass_BrHtoGamD_5_2018.dat",listbr5];

Br=10%   
listbr10={{Null,Null}} # To Store the limit value *)
BrIn=0.1; # value of Br(HGammaD) *)
min= {0.25,0.7,0.85,1.1,1.25,1.5,1.8,2.0,2.2,2.5,2.7,3.2}; # Just to split the mass range different precision needed in dificult regions where the Br drops around 0.8 and 1.0 GeV*)
mfin={0.7,0.85,1.0,1.25,1.5,1.8,2.0,2.2,2.5,2.7,3.2,8.5};
step={0.05,0.01,0.01,0.01,0.01,0.05,0.01,0.05,0.01,0.05,0.01,0.1};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2;
Mineps2=-16.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision or closenest to the 3.0*)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-16.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m] #&& nval≠pval *)&& Mineps2<-4.0),
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01;
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr10,{m,Mineps2}];
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,12,1}];
Export["/Users/Alfredo/Desktop/limite_DarkSUSY_2018_forPLB/Limit_epsvsmass_BrHtoGamD_10_2018.dat",listbr10];

{{Null,Null}}
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
General::stop: Further output of InterpolatingFunction::dmval will be suppressed during this calculation.
Br=20%   
listbr20={{Null,Null}} # To Store the limit value *)
BrIn=0.2; # value of Br(HGammaD) *)
min= {0.25,0.7,0.85,1.0,1.2,2.0,3.5,5.0}; # Just to split the mass range different precision needed in dificult regions where the Br drops around 0.8 and 1.0 GeV*)
mfin={0.7,0.85,1.0,1.2,2.0,3.5,5.0,9.0};
step={0.05,0.01,0.05,0.01,0.05,0.05,0.01,0.05};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2;
Mineps2=-16.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision or closenest to the 3.0*)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-16.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m] #&& nval≠pval *)&& Mineps2<-4.0),
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01;
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr20,{m,Mineps2}];
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,8,1}];
Export["/Users/Alfredo/Desktop/limite_DarkSUSY_2018_forPLB/Limit_epsvsmass_BrHtoGamD_20_2018.dat",listbr20];

Br=40%   
listbr40={{Null,Null}} # To Store the limit value *)
BrIn=0.4; # value of Br(HGammaD) *)
min= {0.25,0.7,0.85,1.1,1.25,1.5,1.8,2.0,2.2,2.5,2.7,3.2}; # Just to split the mass range different precision needed in dificult regions where the Br drops around 0.8 and 1.0 GeV*)
mfin={0.7,0.85,1.0,1.25,1.5,1.8,2.0,2.2,2.5,2.7,3.2,8.5};
step={0.05,0.01,0.01,0.01,0.01,0.05,0.01,0.05,0.01,0.05,0.01,0.1};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2;
Mineps2=-16.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision or closenest to the 3.0*)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-16.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m]#&& nval≠pval *)&& Mineps2<-4.0),
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01;
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr40,{m,Mineps2}];
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,12,1}];
Export["/Users/Alfredo/Desktop/limite_DarkSUSY_2018_forPLB/Limit_epsvsmass_BrHtoGamD_40_2018.dat",listbr40];

{{Null,Null}}
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
InterpolatingFunction::dmval: Input value {0.25} lies outside the range of data in the interpolating function. Extrapolation will be used.
General::stop: Further output of InterpolatingFunction::dmval will be suppressed during this calculation.
 
Br=60%   
#listbr60={{Null,Null}} # To Store the limit value *)
BrIn=0.6; # value of Br(HGammaD) *)
min= {0.25,0.7,0.8,1.0,1.1};
mfin={0.7,0.8,1.0,1.1,2.0};
step={0.05,0.001,0.05,0.01,0.1};
Table[
#Print["  i  ",i,"   massmin  ",min[[i]],"   massf  ",mfin[[i]],"  step  ",step[[i]]];*)
Do[
#pval=2.0;
nval=3.0;*)
iterbin=0.2;
Mineps2=-14.0;
#Print[{"initial parameters","mass",m,"limit",Nlimit2[m,BrIn]}];*)
While[ (Abs[Nlimit2[m,BrIn]-Nlimitf[m]]>0.5 #&& nval≠pval *)&& Mineps2<-4.0), #0.5 is the precision or closenest to the 3.0*)
#Print[{m,iterbin,Abs[Nlimit2[m,BrIn]-3.0]}];*)
Mineps2=-14.0;
While[
(Nlimit2[m,BrIn]<Nlimitf[m]#&& nval≠pval *)&& Mineps2<-4.0),
#pval= Nlimit2[m,BrIn];*)
#Print[{"oldval",pval}];*)
#Print[{iterbin,Mineps2,Nlimit2[m,BrIn]}];*)
Mineps2 = Mineps2+iterbin;
#nval= Nlimit2[m,BrIn];*)
#Print[{m,Mineps2,Nlimit2[m,BrIn]}]*)
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
iterbin=iterbin-0.01;
];
#Print[{iterbin,m,Mineps2,Nlimit2[m,BrIn]}];*)
AppendTo[listbr40,{m,Mineps2}];
,{m,min[[i]],mfin[[i]],step[[i]]}]
,{i,1,5,1}];
Export["/Users/Luca2/Downloads/LIMITS/Limit_epsvsmass_BrHtoGamD_60_1ev.dat",listbr60];*)

Plot the limit
#Function to convert mass, Log[10,epsilon^{2}]   to   mass, epsilon*)
DataConvertermine[data_]:=Table[{data[[i,1]],Sqrt[10^data[[i,2]]]},{i,Length[data]}]
Labelslin={"Br(H->2Subscript[γ, D])=0.1%","Br(H->2Subscript[γ, D])=1%","Br(H->2Subscript[γ, D])=5%","Br(H->2Subscript[γ, D])=10%","Br(H->2Subscript[γ, D])=20%","Br(H->2Subscript[γ, D])=40%"}
{Br(H->2Subscript[γ, D])=0.1%,Br(H->2Subscript[γ, D])=1%,Br(H->2Subscript[γ, D])=5%,Br(H->2Subscript[γ, D])=10%,Br(H->2Subscript[γ, D])=20%,Br(H->2Subscript[γ, D])=40%}
legendlin=SwatchLegend[{Darker[Cyan,0.2],Darker[Blue,0.2],Darker[Green,0.2],Darker[Yellow,0.2],Darker[Orange,0.2],Darker[Red,0.2],{Black,Dashed},{Purple,Dashed},{Brown,Dashed},{Cyan,Dashed},{Pink,Dashed}},Labelslin,LegendMarkerSize->{{15,15}},LabelStyle->{Italic,9},LegendMarkers->{"Line"}];
listbr01 = Import["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_epsvsmass_BrHtoGamD_01_2017.dat"];
listbr1   = Import["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_epsvsmass_BrHtoGamD_1_2017.dat"];
listbr5   = Import["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_epsvsmass_BrHtoGamD_5_2017.dat"];
listbr10 = Import["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_epsvsmass_BrHtoGamD_10_2017.dat"];
listbr20 = Import["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_epsvsmass_BrHtoGamD_20_2017.dat"];
listbr40 = Import["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_epsvsmass_BrHtoGamD_40_2017.dat"];

plotLimEpsilonvsmass = Legended[ListLogPlot[{DataConvertermine[DeleteCases[listbr01,{Null,Null}]],DataConvertermine[DeleteCases[listbr1,{Null,Null}]],DataConvertermine[DeleteCases[listbr5,{Null,Null}]],DataConvertermine[DeleteCases[listbr10,{Null,Null}]],DataConvertermine[DeleteCases[listbr20,{Null,Null}]],DataConvertermine[DeleteCases[listbr40,{Null,Null}]]}, Joined->True,PlotRange->{{0.25,9.0},{0.4 10^-9,0.1 10^-1}},ImageSize->500,AspectRatio->1.0,TicksStyle->Directive[FontSize->18],Frame->True,FrameLabel->{"Subscript[m, γD][GeV]","Kinetic Mixing Parameter ϵ"},RotateLabel->True,BaseStyle->{FontSize->18},PlotStyle->{Darker[Cyan,0.2],Darker[Blue,0.2],Darker[Green,0.2],Darker[Yellow,0.2],Darker[Orange,0.2],Darker[Red,0.2],{Black,Dashed},{Purple,Dashed},{Brown,Dashed},{Cyan,Dashed},{Pink,Dashed}}],Placed[legendlin,{0.74,0.70}]]
Part::partw: Part 1 of {} does not exist. >>
Part::partw: Part 2 of {} does not exist. >>
Part::partw: Part 1 of {} does not exist. >>
General::stop: Further output of Part::partw will be suppressed during this calculation. >>

Export["/Users/Usuario/Desktop/limite_DarkSUSY_2017/Limit_DarkPhoton_Epsilon_vs_mass_Run2.pdf",plotLimEpsilonvsmass]
/Users/Alfredo/Documents/Shared_Ubuntu/Limit_DarkPhoton_Epsilon_vs_mass_Run2.pdf

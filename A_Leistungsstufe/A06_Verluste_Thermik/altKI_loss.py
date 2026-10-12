# altKI – Entwurf einer früheren KI-Sitzung, ungeprüft. Nur zur Gegenprobe, nicht als Vorgabe übernehmen.
import numpy as np, itertools
Vout, Iout = 12.0, 3.0
# XAL6060 data (typ DCR, mOhm): L -> DCR
ind = {6.8:18.9, 8.2:24.0, 10:27.0, 15:39.8, 22:55.1}
Isat = {6.8:9.2, 8.2:8.4, 10:7.6, 15:5.8, 22:5.6}
# FET models: R4.5 max [mOhm], Qg@4.5V [nC], Crss [pF] (Crss = ASSUMPTION)
fets = {
 'BSZ063N04LS6': dict(R=8.8e-3, Qg=5.2e-9, Crss=10e-12),
 'BSZ097N04LS' : dict(R=14.2e-3,Qg=9.5e-9, Crss=16e-12),   # Crss=16pF from LTC7800 datasheet example
}
Rsense=5e-3
Tj_factor = 1.0+0.005*(80-25)      # hot RDS(on), delta=0.005/K per datasheet
Tcu = 1+0.0039*(80-25)             # copper at 80C
RDR=2.5; Vintvcc=5.1; Vplat=2.5
def losses(Vin,f,L,fet,P0core=0.05,Schottky=True):
    D=Vout/Vin
    dI=Vout*(1-D)/(f*L*1e-6)
    Irms2=Iout**2+dI**2/12
    F=fets[fet]; R=F['R']*Tj_factor
    Ptop=D*Irms2*R + Vin**2*(Iout/2)*RDR*F['Crss']*(1/(Vintvcc-Vplat)+1/Vplat)*f
    Pbot=(1-D)*Irms2*R
    Pdcr=Irms2*ind[L]*1e-3*Tcu
    Prs=Irms2*Rsense
    # core loss (guess): ~f^1.5 * (sqrt(L)*dI)^2.5
    Bref=np.sqrt(10)*(Vout*(1-12/26)/(500e3*10e-6))
    Pcore=P0core*(f/500e3)**1.5*((np.sqrt(L)*dI)/Bref)**2.5
    # gate drive from EXTVCC=Vout
    Pgate=Vout*f*2*F['Qg']
    Pctl=Vout*2e-3
    tdead=2*20e-9
    Vf=0.5 if Schottky else 0.8
    Qrr=5e-9 if Schottky else 25e-9
    Pdead=Vf*Iout*tdead*f + Qrr*Vin*f
    Pother=0.02
    tot=Ptop+Pbot+Pdcr+Prs+Pcore+Pgate+Pctl+Pdead+Pother
    parts=dict(top=Ptop,bot=Pbot,dcr=Pdcr,rs=Prs,core=Pcore,gate=Pgate,ctl=Pctl,dead=Pdead,oth=Pother)
    return tot,dI,parts
Pout=Vout*Iout
print("Sweep f,L (BSZ063, Vin=24V) -> eta%  [dI@26V]")
for L in ind:
    row=[]
    for f in [320e3,400e3,500e3,650e3,800e3]:
        tot,_,_=losses(24,f,L,'BSZ063N04LS6')
        dI26=losses(26,f,L,'BSZ063N04LS6')[1]
        row.append(f"{f/1e3:.0f}k:{100*Pout/(Pout+tot):.2f}({dI26:.2f}A)")
    print(f"L={L:>4}uH  "+"  ".join(row))
print()
for fet in fets:
    for Vin in (22,24,26):
        tot,dI,p=losses(Vin,500e3,10,fet)
        print(fet,Vin,f"Ploss={tot:.2f}W eta={100*Pout/(Pout+tot):.2f}% dI={dI:.2f}A", {k:round(v,3) for k,v in p.items()})
print()
# sensitivity
for P0 in (0.02,0.05,0.15):
  for Cr in (6e-12,10e-12,20e-12):
    fets['BSZ063N04LS6']['Crss']=Cr
    tot,_,_=losses(24,500e3,10,'BSZ063N04LS6',P0core=P0)
    print(f"core P0={P0} Crss={Cr*1e12:.0f}pF -> eta={100*Pout/(Pout+tot):.2f}%  Ploss={tot:.2f}W")

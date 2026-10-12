# altKI – Entwurf einer früheren KI-Sitzung, ungeprüft. Nur zur Gegenprobe, nicht als Vorgabe übernehmen.
import numpy as np
# --- plant: peak-current-mode buck, 12V/3A, f=500kHz, L=10uH, Rsense=5mOhm
fs=500e3; Rs=5e-3; gm=2e-3; Vref=0.8; Vout=12.0
Gi=1/(10*Rs)          # A/V  (assumption: Vsense=(VITH-0.7)/10 from datasheet curve G13)
beta=Vref/Vout
def T(f,Rc,Cc,Cc2,Cout,Rload,Q=1.0,ESR=3e-3):
    s=2j*np.pi*f
    Z=(Rc+1/(s*Cc))/(1+s*Cc2*(Rc+1/(s*Cc)))      # ITH network (ro neglected)
    wp=1/(Rload*Cout)*1.0
    Gvc=Gi*Rload/(1+s/wp)*(1+s*ESR*Cout)
    wn=np.pi*fs
    Hs=1/(1+s/(wn*Q)+(s/wn)**2)
    return beta*gm*Z*Gvc*Hs
def margins(Rc,Cc,Cc2,Cout,Rload,Q=1.0):
    f=np.logspace(2,6,40000)
    t=T(f,Rc,Cc,Cc2,Cout,Rload,Q)
    mag=np.abs(t); ph=np.unwrap(np.angle(t))*180/np.pi
    i=np.where(mag<1)[0][0]; fc=f[i]; pm=180+ph[i]
    j=np.where(ph<-180)[0]
    gm_db=None
    if len(j): gm_db=-20*np.log10(mag[j[0]])
    return fc,pm,gm_db
print("Candidate: Rc=2.2k, Cc=10nF, Cc2=100pF")
for Cout,lab in [(20e-6,'Cout 20uF (stark derated)'),(33e-6,'Cout 33uF (nominal)'),(45e-6,'Cout 45uF')]:
    for Rload,labl in [(12/3,'3A'),(12/1.5,'1.5A'),(12/0.5,'0.5A')]:
        for Q in (0.7,1.0,2.0):
            fc,pm,g=margins(2.2e3,10e-9,100e-12,Cout,Rload,Q)
            print(f"{lab:28s} {labl:5s} Q={Q}: fc={fc/1e3:5.1f} kHz PM={pm:5.1f} deg GM={g if g is None else round(g,1)} dB")

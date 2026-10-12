# altKI – Entwurf einer früheren KI-Sitzung, ungeprüft. Nur zur Gegenprobe, nicht als Vorgabe übernehmen.
import numpy as np
Vout,Iout=12.0,3.0; f=500e3; L=10.0
Pout=36.0
hot=1+0.005*(80-25); Tcu=1+0.0039*(80-25)
def run(name,R45,Qg,Crss,Qoss,DCRmax,P0core,Rs=5e-3,Schottky=True,Vin=24):
    D=Vout/Vin; dI=Vout*(1-D)/(f*L*1e-6); Irms2=Iout**2+dI**2/12
    R=R45*hot
    top=D*Irms2*R+Vin**2*(Iout/2)*2.5*Crss*(1/(5.1-2.5)+1/2.5)*f
    bot=(1-D)*Irms2*R
    dcr=Irms2*DCRmax*Tcu
    rs=Irms2*Rs
    core=P0core*(dI/1.29)**2.5
    gate=Vout*f*2*Qg
    ctl=Vout*2e-3
    dead=(0.5 if Schottky else 0.8)*Iout*40e-9*f+ (5e-9 if Schottky else 25e-9)*Vin*f
    coss=Qoss*Vin*f
    oth=0.07
    tot=top+bot+dcr+rs+core+gate+ctl+dead+coss+oth
    return name,tot,100*Pout/(Pout+tot),dict(top=top,bot=bot,dcr=dcr,rs=rs,core=core,gate=gate,ctl=ctl,dead=dead,coss=coss,oth=oth)
cases=[
 ("Wuerth 1510 (6.5mOhm) + BSZ097",14.2e-3,9.5e-9,16e-12,12e-9,6.5e-3,0.10),
 ("Wuerth 6060 (26.5mOhm max) + BSZ097",14.2e-3,9.5e-9,16e-12,12e-9,26.5e-3,0.04),
 ("Wuerth 1510 + BSZ063 (if available)",8.8e-3,5.2e-9,10e-12,10.2e-9,6.5e-3,0.10),
]
for c in cases:
    for Vin in (22,26):
        n,t,e,p=run(*c,Vin=Vin)
        print(f"{n:38s} Vin={Vin} Ploss={t:.2f}W eta={e:.2f}%")
    n,t,e,p=run(*c,Vin=24)
    print("   24V breakdown",{k:round(float(v),3) for k,v in p.items()})
# core loss sensitivity for 1510
for P0 in (0.05,0.10,0.20,0.30):
    n,t,e,_=run("x",14.2e-3,9.5e-9,16e-12,12e-9,6.5e-3,P0)
    print("1510 core P0",P0,"eta",round(e,2))
# Cin/Cout with 10uF 50V X7R parts
print("Cin dV (3x10uF ~55% bias@24V = 16.5uF):",3*0.25/(500e3*16.5e-6)*1e3,"mV")
print("Cout ripple (5x10uF ~72% @12V =36uF):",1.29*(2e-3+1/(8*500e3*36e-6))*1e3,"mV")

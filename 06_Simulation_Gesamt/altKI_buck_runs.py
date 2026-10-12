# altKI – Entwurf einer früheren KI-Sitzung, ungeprüft. Nur zur Gegenprobe, nicht als Vorgabe übernehmen.
import numpy as np
from altKI_buck_sim import simulate
res={}
# 2) load step 0.6 -> 2.4 A (slew 1A/us) at 5 ms, back at 6.5 ms ; start already at regulated Vout (seed 12V) with SS done
def Iload(t):
    if t<5e-3: return 0.6
    if t<5e-3+1.8e-6: return 0.6+(t-5e-3)/1.8e-6*1.8
    if t<6.5e-3: return 2.4
    if t<6.5e-3+1.8e-6: return 2.4-(t-6.5e-3)/1.8e-6*1.8
    return 0.6
for Vin in (22.0,26.0):
    r=simulate(Vin=Vin,Iload_fn=Iload,T=8e-3,seed_vout=12.0,Css=1e-12)   # tiny Css => reference already at 0.8
    t,vo=r['t'],r['vo']
    # initialise ITH: let it settle during first ms
    a=(t>4.9e-3)&(t<5.0e-3); b=(t>5.0e-3)&(t<5.4e-3); c=(t>6.5e-3)&(t<6.9e-3)
    base=vo[a].mean()
    ts=t[b][np.argmin(vo[b])]
    # settling within 1% (120mV) after step
    def settle(mask,t0,ref):
        idx=np.where(np.abs(vo[mask]-ref)>0.06)[0]
        return (t[mask][idx[-1]]-t0)*1e6 if len(idx) else 0
    print(f"Laststufe 0.6->2.4A, Vin={Vin:.0f}V: Vor Stufe {base:.4f} V | Einbruch min {vo[b].min():.3f} V ({(vo[b].min()-base)*1e3:.0f} mV) | Rueckschritt Ueberschwingen max {vo[c].max():.3f} V ({(vo[c].max()-base)*1e3:.0f} mV) | Beruhigung <=0.5%: {settle(b,5e-3,base):.0f} us")
# 3) line step 22 -> 26 V at 5 ms (ramp 10 us) with 1.5A load
def Vin_fn(t):
    if t<5e-3: return 22.0
    if t<5e-3+10e-6: return 22.0+(t-5e-3)/10e-6*4
    return 26.0
r=simulate(Vin_fn=Vin_fn,Iload_fn=lambda t:1.5,T=7e-3,seed_vout=12.0,Css=1e-12)
t,vo=r['t'],r['vo']; a=(t>4.9e-3)&(t<5e-3); b=(t>5e-3)&(t<5.5e-3)
print(f"Eingangssprung 22->26V, 1.5A: Abweichung max {(np.abs(vo[b]-vo[a].mean()).max())*1e3:.1f} mV")
# 4) short circuit at 5 ms (10 mOhm), Vin=26
def Rsh(t): return 0.01 if t>5e-3 else 4.0
r=simulate(Vin=26.0,Iload_fn=lambda t:0.0,Rshort_fn=Rsh,T=7e-3,seed_vout=12.0,Css=1e-12)
t,il,vo=r['t'],r['il'],r['vo']; m=t>5.2e-3
print(f"Kurzschluss (10mOhm) bei 26V: iL Spitze direkt nach Kurzschluss {il[(t>5e-3)&(t<5.1e-3)].max():.2f} A, mittlere iL nach 0.2ms {il[m].mean():.2f} A, Spitze {il[m].max():.2f} A, Vout {vo[m].mean():.2f} V")
# 5) steady-state ripple/duty at 22 / 26 V, 3A
for Vin in (22.0,26.0):
    r=simulate(Vin=Vin,Iload_fn=lambda t:3.0,T=4e-3,seed_vout=12.0,Css=1e-12); t,vo,il=r['t'],r['vo'],r['il']; m=t>3.8e-3
    print(f"Dauerbetrieb 3A Vin={Vin:.0f}V: Vout={vo[m].mean():.4f} V, Ripple={ (vo[m].max()-vo[m].min())*1e3:.1f} mVss, iL pp={il[m].max()-il[m].min():.2f} A, iL max={il[m].max():.2f} A")
# 6) light load 0.1A (DCM / pulse-skipping behaviour, no burst model)
r=simulate(Vin=24.0,Iload_fn=lambda t:0.1,T=4e-3,seed_vout=12.0,Css=1e-12); t,vo,il=r['t'],r['vo'],r['il']; m=t>3.5e-3
print(f"Schwachlast 0.1A: Vout={vo[m].mean():.3f} V, Ripple={(vo[m].max()-vo[m].min())*1e3:.1f} mVss")

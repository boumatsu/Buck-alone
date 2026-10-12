# altKI – Entwurf einer früheren KI-Sitzung, ungeprüft. Nur zur Gegenprobe, nicht als Vorgabe übernehmen.
import numpy as np
def simulate(Vin=24.0, Iload_fn=None, Rshort_fn=None, T=8e-3, dt=10e-9, fs=500e3, L=10e-6, DCR=8e-3, Rs=5e-3,
             Rtop=18e-3, Rbot=18e-3, Cout=36e-6, ESR=2e-3, Vin_fn=None, Css=47e-9, ilim_mV=30e-3, seed_vout=0.0,
             RC=2.2e3, CC=10e-9, C2=100e-12, gm=2e-3, beta=0.8/12.0, slope_frac=0.35, record=True):
    Ts=1/fs; n=int(T/dt); nclk=int(round(Ts/dt))
    iL=0.0; vc=seed_vout; vith=0.7; vcc=0.7; top=False; k_in_cycle=0
    ton_steps=0
    Iload_fn = Iload_fn or (lambda t:0.0)
    t_arr=[];vo_arr=[];il_arr=[];ith_arr=[];vsw=[]
    dec=max(1,int(2e-7/dt))   # record every 200 ns
    Vcl=None
    peak_il=0
    for k in range(n):
        t=k*dt
        vin = Vin_fn(t) if Vin_fn else Vin
        if k % nclk == 0:   # clock: turn on top
            top=True; ton_steps=0
        vfb=(vc + ESR*(iL-Iload_fn(t)))*beta if True else 0
        vref=min(0.8, 10e-6*t/Css)
        # foldback (disabled during soft-start while FB follows ramp)
        ss_active = (vref<0.8)
        fold = 1.0 if ss_active else (0.45+0.55*min(1.0, vfb/(0.7*0.8)))
        Ilim = fold*ilim_mV/Rs
        Icmd = max(0.0,(vith-0.7)*20.0)         # A  (Vsense=(VITH-0.7)/10)
        Icmd = min(Icmd, Ilim)
        if top:
            ton_steps+=1
            Itrip = Icmd - slope_frac*(vc/L)*ton_steps*dt   # slope compensation
            if iL>=Itrip or ton_steps*dt>0.98*Ts:
                top=False
        if top:
            vsw = vin - iL*Rtop
        else:
            if iL>0: vsw = -iL*Rbot
            else: vsw = None
        iload=Iload_fn(t)
        vo = vc + ESR*(iL-iload)
        if vsw is None:   # DCM, inductor current zero, no reverse
            diL=0.0; iL=0.0
        else:
            diL=(vsw - iL*(DCR+Rs) - vo)/L
            iL+=diL*dt
            if (not top) and iL<0: iL=0.0
        # output cap
        if Rshort_fn is not None and Rshort_fn(t) is not None:
            iload = max(0.0,vo)/Rshort_fn(t)
        vc += (iL-iload)/Cout*dt
        # compensation
        Igm = gm*(vref - vfb)
        Igm = max(-200e-6,min(200e-6,Igm))
        dvith=(Igm-(vith-vcc)/RC)/C2
        dvcc=(vith-vcc)/(RC*CC)
        vith+=dvith*dt; vcc+=dvcc*dt
        vith=min(1.6,max(0.0,vith))
        peak_il=max(peak_il,iL)
        if record and k%dec==0:
            t_arr.append(t);vo_arr.append(vo);il_arr.append(iL);ith_arr.append(vith)
    return dict(t=np.array(t_arr),vo=np.array(vo_arr),il=np.array(il_arr),ith=np.array(ith_arr),peak=peak_il)
if __name__=="__main__":
    # 1) startup into 3A (resistive 4 ohm)
    I=lambda t: 3.0 if t>0 else 0.0
    # resistive load during startup: use current proportional to Vout/4ohm
    r=simulate(Vin=24.0,Iload_fn=lambda t:0.0,T=8e-3,Rshort_fn=lambda t:4.0)   # 4 ohm resistive load (3A at 12V)
    t,vo,il=r['t'],r['vo'],r['il']
    print("Startup 24V, 4 Ohm: Vout(8ms)=%.3f V; max Vout=%.3f V (overshoot %.0f mV); max iL=%.2f A; t(Vout>=11.4V)=%.2f ms"%(vo[-1],vo.max(),(vo.max()-12)*1e3,il.max(),t[np.argmax(vo>=11.4)]*1e3))
    # steady state ripple (last 100us)
    m=t>7.9e-3
    print("  steady: Vout mean=%.4f V, ripple pp=%.1f mV, iL mean=%.2f A, iL pp=%.2f A"%(vo[m].mean(),(vo[m].max()-vo[m].min())*1e3,il[m].mean(),il[m].max()-il[m].min()))
    np.save("startup.npy",np.vstack([t,vo,il]))

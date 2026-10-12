> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# Bauteil-Dimensionierung – LTC7800-Buck (rechnen + simulieren + dokumentieren)

Methodik je Bauteil: **Funktion → Formel (mit Einheiten) → Wert → Datenblatt-Beleg → Simulation
(LTspice, echte Modelle) → Status.** Simulationsdateien in `ltspice\`, Nachweise in `docs\03–07`.

Statusstufen: **S0** Annahme · **S1** gerechnet · **S2** simuliert · **S3** Datenblatt + Simulation.

---

## 1. Leistungsteil (Buck 22–26 V → 12 V/3 A, LTC7800)

### 1.1 Schaltfrequenz
- **Formel/Quelle:** R_FREQ laut Datenblatt **Fig. 8**, aus der PDF-**Vektorgrafik digitalisiert**
  (siehe `docs\10`): f[kHz] ≈ 23,9·R[kΩ] − 278 (Steigung 24,11 kHz/kΩ).
  Stützpunkte: 25 k→320 kHz, 40 k→657 kHz, 62 k→1,15 MHz, 100 k→2,10 MHz, 105 k→2,23 MHz.
- **Wert:** R_FREQ = **33 kΩ** (E12) → rechnerisch **≈ 511 kHz** (Ziel 500 kHz).
- **Toleranz (neu, `docs\13` N3):** die El.-Char.-Tabelle (S. 4) gibt f25k = 0,27/0,32/0,36 MHz und
  f100k = 1,75/2,1/2,4 MHz ⇒ **±14 %** ⇒ bei 33 kΩ **434…575 kHz** (typ. 504 kHz; zusätzlich +5…7 % über
  Temperatur, Kurve G24). ⇒ ΔI_L-Bandbreite statt eines Punktwerts rechnen.
- **Sim:** stabiler Betrieb bei ~500 kHz (SW-Knoten), `Rfreq FREQ 0 33k` in allen Läufen.
- **Status: S3** (Datenblatt-Fig. 8 digitalisiert **und** simuliert).

### 1.2 Induktivität
- **Formel:** ΔI_L = V_OUT·(1−V_OUT/V_IN)/(f·L);  D = V_OUT/V_IN.
- **Rechnung:** bei 26 V: ΔI_L = 12·(1−12/26)/(500 k·L). Mit L = 10 µH → **1,29 A**; bei 22 V → 1,09 A; I_pk = 3 + ΔI/2 = 3,65 A.
- **Bauteil:** Würth **74439370100** (WE-XHMI 1510): **L = 10,4 µH**, R_DC 6,4 mΩ typ / **7,04 mΩ max**, I_SAT,30% **31,2 A** (≫ I_pk).
- **Datenblatt-Richtwert (S. 16, Applications Information):** ΔI_L ≈ **0,3·I_MAX** (= 0,9 A), Maximum bei V_IN,max.
  Unser ΔI_L (26 V, 10,4 µH) ≈ 1,24 A = **41 %** von I_MAX → etwas hoch (Ripple/Zielkonflikt).
  **Option:** L = **15 µH** (`74439370150`, im WE-XHMI-Modellinventar vorhanden) → ΔI_L ≈ 0,86 A = **29 %** ✔
  (gegen größeren Baukörper, DCR und Regelkreis neu abwägen).
- **Sim:** Buck läuft stabil; Ripple-Messungen (1.5) passen zu L.
- **Status: S2/S3.**

### 1.3 Strommessung R_SENSE
- **Formel:** R_SENSE = V_SENSE(MAX,min)/I_pk = 22 mV/3,65 A = 6,0 mΩ → gewählt **5 mΩ**.
- **Realisierung:** 2× **10 mΩ** (Vishay WSL2512R0100FEA) parallel = 5 mΩ; ILIM = GND.
- **Stromlimit:** 22 mV/5 mΩ = **4,4 A** (min) … 36 mV/5 mΩ = **7,2 A** (max).
- **Sim:** Kurzschluss (0,01 Ω) → Ausgang fällt auf **0,02 V** (Foldback aktiv), I_pk unkritisch.
- **Status: S1/S2.**

### 1.4 Eingangskondensator C_IN
- **Formel:** I_CIN(RMS) = I_OUT·√(D(1−D));  ΔV_IN = I·D(1−D)/(f·C_eff).
- **Rechnung:** I_RMS = 3·√(0,5·0,5) ≈ **1,5 A** (bei D=0,5); ΔV_IN = 3·0,25/(500 k·15,4 µ) = **98 mV** (C_eff worst case 15,4 µF).
- **Bauteil:** 6× **4,7 µF/100 V X7R** (Murata GRM32ER72A475KE14L, 1210) – nur X7R, Derating beachten.
- **Status: S1/S2.**

### 1.5 Ausgangskondensator C_OUT
- **Formel:** ΔV_OUT ≈ ΔI_L·(ESR + 1/(8·f·C_OUT)).
- **Rechnung:** mit C_eff ≈ 27,7 µF, ESR 2 mΩ → ΔV_OUT ≈ **14 mV** (Worst-Case-Annahme).
- **Bauteil:** 9× **4,7 µF/100 V X7R**.
- **Sim (echte Modelle, 33 µF):** Ripple = **9,7 / 10,6 / 11,9 mV** ss (22/24/26 V); Laststufe
  1,0→2,8 A (sprungförmig): −0,91 V / +0,91 V (kompensationsabhängig, s.u.).
- **Status: S2.**

### 1.6 MOSFETs
- **Bauteil:** 2× **BSZ097N04LS G** (Infineon, 40 V, logic-level, PG-TSDSON-8): R_DS(on)max 9,7 mΩ,
  Qg 8,6 nC@4,5 V, V_GS(th) 1,2–2,0 V, C_iss ≈1,4 nF → C_B ≥ 100·C_iss = 140…190 nF → **0,22 µF**.
- **Sim (Verlustaufschlüsselung, 24 V/3 A):** **P_M1 = 0,374 W** (inkl. Schaltverluste),
  **P_M2 = 0,091 W**, gesamt 0,744 W → **η = 97,96 %**.
- **Status: S2/S3.**

### 1.7 Kompensation (ITH)
- **Werte:** R_ITH = **2,2 kΩ**, C_ITH = **10 nF** (C0G), C_ITH2 = **100 pF** (C0G).
- **Sim:** Laststufe zeigt ~0,9 V Auslenkung (sprungförmig) → Kompensation noch **optimierbar**
  (mehr Bandbreite / größeres C_OUT). 
- **Status: S1/S2 (Feintuning offen).**

### 1.8 UVLO (RUN)
- **Formel:** V_UVLO,rise = 1,21·(1+R_B/R_A) − 7 µA·R_B.
- **Werte:** R_A = 22 kΩ, R_B = 330 kΩ → **ein 17,05 V / aus 16,25 V** (kollidiert nicht mit 22–26 V).
- **Status: S1.**

### 1.9 Soft-Start (TRACK/SS)
- **Formel:** t_SS = C_SS·0,8 V/10 µA = 100 nF·0,8/10 µ → **8 ms** (Rampenstart).
- **Status: S1** (Zeit simuliert als Rampe sichtbar; exakter 8-ms-Lauf rechenintensiv).

### 1.10 Rückkopplung
- **Formel:** V_OUT = V_FB·(1+R1/R2), V_FB = 0,8 V.
- **Werte:** R1 = **150 k + 18 k = 168 k** (E12 in Reihe), R2 = **12 k** → **V_OUT = 12,000 V**.
- **Sim:** Vout = **11,996 V** (24 V) ✔.
- **Status: S2/S3.**

### 1.11 Bootstrap
- **Regel:** C_B ≥ 100·C_iss(Q1) = 140…190 nF → **C_B = 0,22 µF** (50 V, X7R, 0805).
- **Diode:** **PMEG4030ER-QX** (40 V, 3 A, Schottky) in `vendor\PMEG4030ER.lib` (BV 44 V).
- **Status: S1.**

### 1.12 EXTVCC
- **Entscheidung:** EXTVCC = V_OUT (12 V).
- **Sim-Beleg:** η(EXTVCC=Vout) = **93,4–93,7 %** vs. η(EXTVCC=GND) = **91,0–92,0 %**
  → **+1,7…2,4 Prozentpunkte** (echtes Modell).
- **Status: S2.**

---

## 2. Eingangsschutz (LTC4364-2 Surge Stopper / Hot-Swap) — jetzt datenblatt-belegt
Quelle: `models\datasheets\ltc4364f.pdf` (Rev. B, 29 S.), digitalisiert nach `docs\14` →
`models\datasheets\_extract\ltc4364f\`. Vollständige Auswertung + Abgleich: **`docs\16`**.

### 2.1 Ausgangsklemme V_REG (OV-Regelung)
- **Formel:** V_REG = V_FB·(1+R7/R8) mit **V_FB = 1,25 V (1,22…1,28 V)** (S. 3).
- **Werte:** R7 = 100 kΩ, R8 = **4,7 kΩ** → **27,85 V**; Toleranzrechnung: **26,67…29,07 V** ⇒ min nur
  **0,67 V** über V_IN,max = 26 V (zu knapp).
- **Änderung (docs\16):** **R8 = 4,32 kΩ (E96)** ⇒ 30,2 V nominal, min 28,9 V (**2,9 V Abstand**).
  Das Datenblatt-Beispiel (102 k/4,99 k → 26,8 V) ist für 26 V Eingang **nicht** brauchbar.
- **Status: S3 (nach R8-Änderung).**

### 2.2 UV/OV
- **Formel/Schwellen:** V_UV = V_OV = **1,25 V (1,22…1,28 V)**, UV-Hysterese **50 mV** typ,
  Pin-Strom **I_IN = ±1 µA** (Fehler über Teiler-Thevenin) (S. 4).
- **Werte:** R1 = 220 kΩ, R2 = 8,2 kΩ, R3 = 10 kΩ → **UV 16,36 V** (15,96…16,75 V), aus bei **~15,7 V**;
  **OV 29,78 V** (28,9…30,5 V). **UV erzeugt kein FLT-Signal** ✔ (OV schon).
- **Neu:** Filter-**C an UV/OV (1…10 nF)** + Serien-R, **τ_UV/τ_OV > 50** (Datenblatt Fig. 2) – sonst startet
  das Board bei Hot-Swap in eine Überspannung sofort.
- **Status: S3** (Filter: S0 → ergänzen).

### 2.3 Strommessung R_SNS
- **Schwellen (S. 3):** ΔV_SNS = **45/50/55 mV** (0…125 °C), **43/50/57 mV** (−40…125 °C),
  **im Kurzschluss (OUT = 0…1,5 V) nur 18/25/32 mV**.
- **Werte:** R_SNS = **10 mΩ** ⇒ **5,0 A typ, 4,3 A min** (Reserve bei 3 A: 1,67× typ / **1,43× min**);
  Kurzschluss ⇒ **2,5 A typ (1,8–3,2 A)** – eingebauter Foldback, bleibt unter F1 (5 A).
- R_SNS = 10 mΩ = **Datenblatt-Wert** (Fig. 1 und Fig. 10) ✔; **Kelvin-Verbindung Pflicht** (I_SNS = 55 µA typ).
- **Status: S3.**

### 2.4 Fehler-Timer C_TMR
- **Formeln (S. 13/14):** I_TMR(UP)OV = 2 µA + 0,644 µA/V·(V_CC−V_OUT−0,5 V);
  I_TMR(UP)OC = 10 µA + 3,36 µA/V·(V_CC−V_OUT−0,5 V); V_TMR = 1,25 V → FLT-Warnung, 1,35 V → M1 aus
  (OV-Warnzeit = **20 ms/µF**).
- **Wert:** **C_TMR = 47 nF** (= Datenblatt-Design-Beispiel S. 19) ⇒ OV-Warnung **0,94 ms**;
  OC-Abschaltung **0,71 ms @22 V / 0,61 ms @26 V**.
- **Kurzschluss-Stress:** P²t ≈ (V_IN·ΔV_SNS/R_SNS)²·t_OC ⇒ **2,6 W²s**, mit Toleranzen **5,2 W²s**
  ⇒ gegen FET-SOA prüfen.
- **Status: S3** (SOA-Prüfung offen).

### 2.5 Pass-FETs
- **Datenblatt-Beleg (Fig. 9, S. 21):** M1 = FDB3632, **M2 = FDMS86101** – unser FDMS86101 ist damit für die
  Ideal-Diode-Position **wörtlich das Datenblatt-Bauteil** ✔; für M1 nennt das Datenblatt FDB3632/FDB33N25
  (SOA-stark).
- **≥ 24 V Versorgung ⇒ 15-V-Zener an JEDEN MOSFET** (S. 16; D6/D7 = DDZ9702T in Fig. 9/10) ⇒ **zweiten Zener
  ergänzen** (HGATE–SOURCE und DGATE–SOURCE).
- **Offen:** SOA von M1 gegen Kurzschluss (5,2 W²s) und Transienten (P²t-Methode S. 16/17); Modellproblem bleibt
  (BSIM3) ⇒ Sim mit Proxy BSC082N10LS + Bauteiltest mit echtem FDMS86101 (`docs\06`).

### 2.6 VCC, Gate, C_HG, Zeners
- R4 = 2,2 kΩ, C1 = 0,1 µF/100 V (der Datenblatt-Wert; R4 kostet **~1 V** Mindestspannung bei 750 µA);
  **15-V-Zener** gate-source (DDZ9702, `vendor\DDZ9702.lib`) – **2× nötig** (s. 2.5);
  D1 = 68-V-Zener am VCC (CMZ5945B in Fig. 10) – bei unserem geklemmten Eingang optional, aber empfohlen.
- **Neu (Datenblatt S. 17): C_HG = 6,8 nF + R6 = 10 Ω + D5** (Kathode an C_HG) am HGATE-Pin.
  Wirkung: Inrush-Begrenzung (eigene Rechnung: I_INRUSH = I_HGATE(UP)·C_L/C_HG = 20 µA·28 µF/6,8 nF ≈ **82 mA**)
  und Schleifenkompensation im OV/OC-Fall. Fig. 8–10 nutzen 47 nF statt 6,8 nF.
- **Status: S0 → ergänzen.**

### 2.7 Ausgangspuffer (neu aus dem Datenblatt, S. 18)
- „In all applications the output must be bypassed with **at least 22 µF low ESR electrolytic**"; Keramik nur
  bis 1/10 davon, sonst werden Spannungs- und Strombegrenzungs-Schleife instabil.
- Unser C_IN (6 × 4,7 µF X7R = 28 µF Keramik) ist **mehr** als 1/10 ⇒ Elko am LTC4364-Ausgang prüfen
  (`865080543009`: Kapazität ≥ 22 µF, Low-ESR) – sonst Elko vergrößern oder 100 mΩ in Reihe (Fig. 16).
- **Status: S1 → prüfen.**

### 2.8 Package und Statusausgänge
- Variante **-2 (Auto-Retry)** ✔ gewollt; Package festlegen: **DE** 14-DFN 4×3 (θ_JA 45 °C/W, EP = Pin 15/GND
  optional, OUT auf Pin 1+2) · **MS** 16-MSOP (120 °C/W) · **S** 16-SO (100 °C/W). Verlust ≈ 26 mW ⇒ thermisch
  unkritisch.
- **FLT** = Fehleranzeige (offen-drain, low bei OV/OC, **nicht** bei UV); **ENOUT** = „Power good"
  (high-Z ab OUT ≈ V_CC − 0,7 V, Reset bei OUT < 2,2 V). Pull-ups an **Logikspannung** legen, ≥ 100 kΩ.
- **Status: S0 → festlegen.**

---

## 3. Eingangsfilter / Transientenschutz

| Bauteil | Dimensionierung | Formel/Beleg | Status |
|---|---|---|---|
| **F1** Sicherung | 5 A träge, R ≈ 14 mΩ | I_IN = 36 W/(η·V_IN) = 1,4–1,7 A; Limit bis 4,1 A | S1 |
| **CMC1** 744841414 | 14 µH, DCR 15 mΩ, 4 A | DM-Dämpfung; CM nach Layout | S0/S1 |
| **L1/L2** 74439370220 | 22 µH, DCR 12,5 mΩ | LC-Filter DM-EMV | S1/S2 |
| **RV1** MOV 820542501 | 39 V, Vc 77 V@10 A, 1 kA, 9,4 J | Grobschutz; Sim: 102 V/440 A | S2 |
| **D_TVS** 824551281 | 28 V bidir., V_BR 32,75 V, Vc 45,4 V@66 A | Feinschutz; Sim: 77 V bei ~230 A | S2/S3 |

---

## 4. Verifikations-Simulationen (echte Modelle)

| Test | Ergebnis | Datei |
|---|---|---|
| Buck-Wirkungsgrad | η = **97,85 / 97,96 / 98,16 %** (22/24/26 V) | `buck_main_bsz.cir` |
| EXTVCC-Vergleich | Vout < GND um 1,7–2,4 Pkt. | `buck_main_ev*.cir` |
| Verlustaufschlüsselung | P_M1 0,374 W, P_M2 0,091 W, Σ 0,744 W | `buck_loss.cir` |
| Laststufe 1,0→2,8 A | −0,91 V / +0,91 V | `buck_dyn.cir` |
| Kurzschluss | Vout → 0,02 V (Foldback) | `buck_sc.cir` |
| Surge 1 kV/2 Ω | Buck-Eingang ≤ **23 V** (geklemmt) | `surge_inprot7.cir` |
| Burst 2 kV (EFT) | von L1 geblockt, ±0,5 V | `burst_eft.cir` |
| FDMS86101 Bauteil | R_DS(on) = 8,2 mΩ | `fdms86101_test.cir` |

---

## 5. Offene Punkte (Dimensionierung)
1. **Kompensation feinjustieren** (Laststufe −0,91 V) – Regelkreis/Bode mit echtem Modell.
2. **C_IN/C_OUT** mit Datenblatt-DC-Bias-Kurve (Murata SimSurfing) statt Annahme 0,75.
3. **Startzeit t_SS** exakt mit realem C_SS = 100 nF messen (rechenintensiv).
4. **Linienregelung** 22→26 V messen (noch offen).
5. **Wirkungsgrad über Last** (0,5/1/2/3 A) und **über Temperatur** (`.temp`).
6. **Monte-Carlo** der Teiler-Toleranz (V_OUT-Streuung).
7. **Thermik** M1/Q1/Q2 (R_th, T_j) mit Verlustleistungen aus 1.6.
8. Gleichtakt-Burst + EMV erst nach **Layout**.
9. **ΔI_L-Ziel prüfen (Datenblatt-Richtwert 30 % von I_MAX):** L = **15 µH** (`74439370150`) gegen das
   aktuelle **10,4 µH** (`74439370100`) vergleichen – Wirkungsgrad, Ripple, Laststufe und Bauteilgröße.
10. **C_FF (Feedforward-Kondensator) über R_B prüfen:** Das Datenblatt erlaubt/empfiehlt C_FF (S. 18), und
   **4 von 6 Referenzschaltungen** nutzen **10 pF** über dem oberen Teilerwiderstand (`docs\11` §11, Fig. 16
   = unser Zwilling 12 V/2,1 MHz). Mit unserem R_B = 168 kΩ läge die Nullstelle bei 10 pF aber erst bei
   ~95 kHz → **Kandidat ≈ 68 pF** (f_zero ≈ 13,9 kHz, f_pol ≈ 209 kHz < f_sw = 504 kHz). In LTspice prüfen:
   Sprungantwort **und** VFB-Ripple – C_FF hebt den HF-Gewinn des Teilers auf 0 dB (Ripple-/Rauscheinkopplung).
   **Ergänzung (`docs\13` N15):** Fig. 16 nutzt 10 pF bei R_B = **487 kΩ** (f_zero = 32,7 kHz); die *gleiche*
   Nullstelle bei unseren 168 kΩ wären **29 pF** – die 68 pF sind also **keine** Referenz-Skalierung, sondern
   eine eigene Wahl. ⇒ **Sim-Reihe 10 / 29 / 68 pF** fahren und erst danach bestücken (C0G).
11. **Sense-Filterwiderstand NUR in der SENSE+ -Leitung** (Fig. 15/16: 10–20 Ω + 1–2 nF): Der **SENSE−-Pin zieht
   ≈ 700 µA**, sobald er über INTVCC + 0,5 V liegt (bei uns 12 V ≫ 5,6 V) – ein 20 Ω in der SENSE−-Leitung
   ergäbe 700 µA·20 Ω = **14 mV Fehler** (≈ 50 % der 28-mV-Schwelle!). Also: R_EL (20 Ω) in **SENSE+**,
   Filter-C (1…2 nF) **direkt am IC**, Kelvin am Shunt (`docs\11` §2/§10).
12. **Stromlimit-Gegenrechnung erledigt (vektorexakt):** Kurve „Max. Current Sense Threshold vs. Duty Cycle"
   (S. 6) exakt ausgelesen (`docs\10` §16) → **28,2 mV @ D = 54,5 %** (22 V). Mit R_SENSE = 5 mΩ ergibt das
   **5,0 A Mittelwert-Limit** → **1,67× Reserve** bei 3 A Last (Worst-Case-Minimum 3,5 A = 1,17×).
   Keine Änderung nötig; falls mehr Reserve gewünscht, R_SENSE auf 4 mΩ oder ILIM = INTVCC prüfen.
13. **R_FREQ gegengeprüft:** Fig.-8-Vektorkurve (`docs\10` §9) + Datenblatt-Design-Beispiel + Referenzkreise
   (< 25,5 kΩ ↔ 320 kHz, 54,9 kΩ ↔ 1 MHz, 100 kΩ ↔ 2,1 MHz) ⇒ **33 kΩ ≈ 504 kHz** ist konsistent ✔
14. **L-Wahl über den f_sw-Worst-Case entscheiden (`docs\13` N3):** mit 434…575 kHz ergibt sich
   ΔI_L = **36…48 %** (L = 10,4 µH) bzw. **25…33 %** (L = 15 µH) von I_MAX ⇒ das stützt die
   15-µH-Option (Punkt 9) und muss in Ripple-/Verlustrechnung als Band, nicht als Punktwert, stehen.
15. **Bestückungs-/Abnahmeprüfung (`docs\13` N9):** R_FREQ = 33 kΩ nach SGND **muss** bestückt und messbar sein
   (der FREQ-Pin hat einen internen 20 µA-Pull-up ⇒ offener Pin ⇒ f_sw = **1,44 MHz**!);
   EXTVCC darf nie offen bleiben (max. 14 V, ab 4,7 V aktiv).
16. **ΔV_IN(t) am C_IN messen (`docs\13` N13/N14):** Datenblatt nennt für 25 W „min. 20–40 µF, ESR 20–50 mΩ"
   (auf 36 W: 29–58 µF) – unsere 28,2 µF nominal / 15,4 µF worst case stützen sich auf die Elko-Kette davor;
   zusätzlich I_RMS = **1,5 A** (Maximum bei **V_IN = 24 V**, also *innerhalb* 22–26 V) ⇒ Rating prüfen.
17. **V_FB-Temperaturgang in die Ausgangstoleranz aufnehmen (`docs\13` N6):** Kurve G21 zeigt
   0,796…0,801 V über −50…150 °C (≈ −0,5 %/+0,1 %) – zusätzlich zu den Min/Max-Grenzen 0,792/0,808 V.


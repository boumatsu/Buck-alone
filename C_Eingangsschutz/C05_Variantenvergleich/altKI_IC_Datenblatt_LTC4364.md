> **altKI – ungeprüfter Entwurf einer früheren KI-Sitzung.** Nur zur Gegenprobe nach eigener Rechnung, nicht als Vorgabe übernehmen. Pfade im Text beziehen sich auf die alte Ordnerstruktur.

# IC-Datenblatt LTC4364-1/LTC4364-2 (Rev. B) – Auswertung + Abgleich mit unserer Dimensionierung

Quelle: `models\datasheets\ltc4364f.pdf` (= `ltc4364-1-4364-2.pdf`, Rev. B, 29 Seiten),
vollständig digitalisiert mit der Pipeline aus `docs\14` → `models\datasheets\_extract\ltc4364f\`
(`INDEX.md`, 29 × `seiten\pNN.md`, 29 × `svg\pNN.svg`, **27 Kurven-CSV**, 25 Figuren-Crops, 39 Panel-Bilder).
Alle Zahlen unten sind aus dieser Extraktion (Seitenzahl in Klammern) – keine Schätzung.

## 1. Absolute Maximum Ratings + Packages (S. 2)

| Pin/Größe | Grenze |
|---|---|
| **V_CC, SOURCE, OV, UV, SHDN** | **−40 V … 100 V** |
| **OUT, SENSE** | **−20 V … 100 V** |
| ENOUT, FLT | −0,3 … 100 V |
| DGATE, HGATE | (SOURCE − 0,3 V) … (SOURCE + 10 V) — Note 3: interne Clamps ≥ 10 V über SOURCE |
| Spannungsdifferenzen | SENSE–OUT: −30 … 30 V · OUT–V_CC: ±100 V · SENSE–SOURCE: ±100 V |
| FB, TMR | −0,3 … 5,5 V |
| T_J,max | 150 °C (alle Packages) |
| **DE** 14-Lead DFN 4×3 mm | θ_JA = **45 °C/W**, EP = Pin 15, GND-Anschluss **optional** |
| **MS** 16-Lead MSOP | θ_JA = 120 °C/W · **S** 16-Lead SO: θ_JA = 100 °C/W |
| Bestellnummern | **-1 = Latch-off**, **-2 = Auto-Retry** (unsere Variante), Grade C/I/H, Marking 43641/43642 |

## 2. Electrical Characteristics (S. 3–5) – die für uns relevanten Zeilen

| Symbol | Bedeutung | MIN | TYP | MAX | Bedingung |
|---|---|---|---|---|---|
| V_CC | Betriebsbereich | 4 V | | 80 V | |
| I_CC | Eigenstrom | | 370 µA | 750 µA | keine Störung |
| I_CC(SHDN) | Shutdown | | 10 µA | 50 µA | SHDN < 0,5 V |
| **ΔV_SNS** | **Überstrom-Schwelle (V_SENSE − V_OUT)** | **45 mV** | **50 mV** | **55 mV** | OUT = 2,5 V…V_CC, 0…125 °C |
| | | 43 mV | 50 mV | 57 mV | −40…125 °C |
| | **bei Kurzschluss (OUT = 0…1,5 V)** | **18 mV** | **25 mV** | **32 mV** | ⇒ eingebauter Foldback |
| ΔV_SD | Ideal-Diode-Regelspannung (V_SOURCE − V_SENSE) | 10 mV | **30 mV** | 45 mV | V_CC = 12 V |
| **V_FB** | FB-Servospannung | 1,22 V | **1,25 V** | 1,28 V | V_CC = 12…80 V |
| I_FB | FB-Eingangsstrom | | 0 | ±1 µA | |
| **V_UV / V_OV** | UV-/OV-Schwelle | 1,22 V | **1,25 V** | 1,28 V | UV fallend / OV steigend |
| V_UV(HYST) | UV-Hysterese | 25 mV | 50 mV | 80 mV | OV-Hysterese: 12 mV typ |
| I_IN | UV-, OV-Pin-Strom @ 1,25 V | | 0 | **±1 µA** | ⇒ Fehler über Teiler-Thevenin |
| **I_HGATE(UP)** | Gate-Ladestrom | −10 µA | **−20 µA** | −30 µA | |
| I_HGATE(DN) | Gate-Entladestrom (OV/OC) | 60 mA | 130 mA | | Shutdown/Fault: 1 mA |
| ΔV_HGATE | Gate-Hub über SOURCE | 10 V | **12 V** | 16 V | V_CC ≥ 8 V (⇒ Standard-FETs) |
| I_DGATE(UP) / ΔV_DGATE | Ideal-Diode-Gate | −5 µA | −10 µA | −15 µA / 12 V typ | |
| **I_TMR(UP)OV** | Timerstrom OV | 1,3 µA | **2,2 µA** | 3 µA | V_CC−OUT = 0,5 V (bis 50 µA bei 75 V) |
| **I_TMR(UP)OC** | Timerstrom OC | 6 µA | **10 µA** | 14 µA | V_CC−OUT = 0,5 V (bis 260 µA bei 75 V) |
| I_TMR(UP)Warning / Retry | Warnung / Retry | 3 / 1,3 µA | 5 / 2 µA | 7 / 3 µA | |
| **V_TMR(F) / V_TMR(G) / V_TMR(R)** | FLT-Schwelle / Gate-off / Retry | 1,22 / 1,32 / 0,125 V | **1,25 / 1,35 / 0,15 V** | 1,28 / 1,38 / 0,175 V | ΔV_TMR (Warnfenster) = 100 mV typ |
| I_SNS | SENSE-Pin-Strom | | 55 µA | 110 µA | SENSE = V_CC = 12 V ⇒ **Kelvin Pflicht** |
| I_SRC / I_OUT | SOURCE-/OUT-Pin-Strom | | 18 / 40 µA | 40 / 80 µA | Shutdown (I_SNS+I_OUT): 12 µA typ |
| D | Retry-Duty-Cycle (OV / Kurzschluss) | | **0,2 % / 0,12 %** | | Mittelwertbelastung im Dauerfehler |
| t_OFF | UV→HGATE low / OV→HGATE low / OC→HGATE low | | 1,3 / 0,25 / 0,5 µs | 4 / 1 / 2 µs | Reaktionszeit für Surge-Betrachtung |
## 3. Formeln (aus S. 13–20) und Referenzapplikationen (S. 21–22)

**UV/OV-Teiler (S. 13, Fig. 1/2):**
- V_UV = 1,25 V · (R1+R2+R3)/(R2+R3) · (1 + I_IN-Fehler) · UV-Hysterese 50 mV typ
- V_OV = 1,25 V · (R1+R2+R3)/R3
- Beim Hot-Swap in eine **Überspannung** startet das Teil nicht, wenn man **getrennte Teiler mit RC-Filter**
  nutzt und **τ_UV/τ_OV > 50** einhält (Fig. 2: τ_UV = (383k∥100k)·10 nF, τ_OV = (475k∥10k)·1 nF).
- Nach dem Hochfahren schaltet eine OV-Bedingung den FET **nicht** ab, sondern **verhindert den Neustart**
  (kein Dauer-Cycling) ✔. **UV erzeugt kein FLT-Signal.**

**Fault-Timer (S. 13–15):**
- Timerstrom steigt mit der Spannung über dem FET: **I_TMR(UP)OV = 2 µA + 0,644 µA/V·(V_CC−V_OUT−0,5 V)**,
  **I_TMR(UP)OC = 10 µA + 3,36 µA/V·(V_CC−V_OUT−0,5 V)** ⇒ höhere V_DS = kürzere Zeit = bessere SOA-Nutzung.
- V_TMR = 1,25 V → **FLT low (Warnung)**; V_TMR = 1,35 V → **M1 aus**. Im OV-Fall schaltet der Timerstrom
  danach auf feste 5 µA ⇒ **Warnzeit = C_TMR·100 mV/5 µA = 20 ms/µF**; im OC-Fall bleibt der Strom ⇒
  t_WARN = C_TMR·100 mV/I_TMR(UP)OC, **t_FLT = C_TMR·1,25 V/I_TMR(UP)OC**.
- Danach **Cool-Down: 32 Zyklen** TMR 0,15 V ↔ 1,35 V mit ±2 µA, am Ende wird **OV geprüft**; dann Retry
  (nur **-2**). **-1** bleibt verriegelt (Reset über UV < 0,6 V > 10 µs oder SHDN < 0,5 V > 200 µs).
- Retry-Duty-Cycle D = 0,2 % (OV) bzw. 0,12 % (Kurzschluss) ⇒ mittlere Verlustleistung im Dauerfehler.

**Inrush + Gate-Kompensation (S. 17):**
- **C_HG = I_HGATE(UP)·C_L / I_INRUSH** (C_L = Lastkapazität am Ausgang) — Datenblattempfehlung:
  **C_HG = 6,8 nF** für die Schleifenkompensation; in den Hot-Swap-Beispielen Fig. 8–10 werden **47 nF**
  (mit **10 Ω** in Reihe) verwendet. **D5** (Kathode an C_HG) über den Serienwiderstand, damit schnelle
  Eingangssprünge C_HG umgehen und HGATE unten halten. C_HG verlangsamt das Abschalten ⇒ höhere Spitzenströme
  im Kurzschluss ⇒ Serien-R + D5 nötig.
- Bei Eingangssprüngen **> 5 V/µs** hilft ein größeres C_HG gegen Selbsteinschalten des N-FET.

**SOA / Stress (S. 16–17, 20):**
- Transientenmodell: Rampe t_r auf V_PK, exponentieller Abfall mit τ; **P²t ist für t < 100 ms maßgeblich**
  (SOA), darüber Thermik. Beispiel: V_PK = 80 V, V_IN = 12 V, V_REG = 16 V, t_r = 10 µs, τ = 1 ms, 3 A
  ⇒ **P²t = 18,4 W²s** (D-Pak-tauglich).
- **Kurzschluss: P²t ≈ (V_IN·ΔV_SNS/R_SNS)² · t_OC**; Beispiel V_IN = 15 V, OUT = 0, ΔV_SNS = 25 mV,
  R_SNS = 12 mΩ, C_TMR = 100 nF ⇒ **2,2 W²s**, mit Toleranzen **verdoppeln**.
- **≥ 24 V Versorgung ⇒ 15-V-Zener Gate-Source an jeden MOSFET** (D6/D7 = DDZ9702T in Fig. 9/10) ✔

**Ausgangspuffer (S. 18):** „In all applications the output must be bypassed with **at least 22 µF low ESR
electrolytic**" – Keramik nur bis 1/10 davon; sonst sind Spannungs- und Strombegrenzungs-Schleife instabil.
Keramik am Ausgang **plus 100 mΩ in Reihe**, wenn der Ausgang unter GND gehen kann (Fig. 16).

**Layout (S. 20):** **Kelvin** an R_SNS; Widerstand SOURCE-Pin → MOSFET-Sources **< 10 Ω**;
**0,02 Zoll Leiterbahnbreite pro Ampere** bei 1 oz Kupfer (≈ 0,5 mm/A ⇒ bei 4 A ≈ 2 mm!);
Teiler **direkt am IC** mit kurzen VCC-/GND-Leitungen; kurze, breite Leistungspfade wegen
Kurzschluss-Transienten (parasitäre Induktivität).

**Referenzapplikationen (S. 21–22) – Werte zum Vergleich:**

| Fig. | Anwendung | M1 / M2 | R_SNS | C_TMR | C_HG | R7/R8 | Teiler |
|---|---|---|---|---|---|---|---|
| 1 (S. 1/S. 12) | **4 A, 12 V OV-Regler mit Reverse-Schutz** (= TA01A) | FDB33N25 / FDB3682 | **10 mΩ** | **47 nF** | – | **102k/4,99k** (V_OUT ≤ 27 V) | R1 383k, R2 90,9k, R3 10k (UV 6 V / OV 60 V) |
| 8 (S. 21) | 2 A Wide-Range-Hot-Swap, 5–28 V, Circuit Breaker | SUD50N03-9 | 20 mΩ | 0,22 µF | 47 nF + 10 Ω | – | 118k/44,2k/5,9k (UV 4,2 V / OV 36 V) |
| **9 (S. 21)** | **28 V Hot-Swap, OV-Regelung auf 36 V, Circuit Breaker + Reverse-Schutz** (18–33 V, 2,5 A) | **FDB3632 / FDMS86101** | 15 mΩ | 0,1 µF | 47 nF + 10 Ω | 110k/4,02k | 100k/6,04k/3,01k (UV 15 V / OV 45 V) |
| 10 (S. 22) | 48 V → 72 V, 4 A | FDB33N25 / FDB3632 | 10 mΩ | 0,1 µF | 47 nF + 10 Ω | 226k/4,02k | 205k/3,92k/3,48k (UV 36 V / OV 76 V) |
| 11 (S. 22) | Redundante Diode-OR, 12 V → 16 V | FDD16AN08A0 ×2 | 10 mΩ | 0,22 µF | **6,8 nF** + 10 Ω | 59k/4,99k | – |

⇒ **Unsere Architektur entspricht Fig. 9** (OV-Regelung + Circuit Breaker + Reverse-Schutz) – inklusive
**FDMS86101 als M2**, genau dem von uns gewählten Bauteil.

## 4. Abgleich mit unserer Dimensionierung (`docs\08` §2) – S1 → S3

| Punkt | Datasheet-Wert (Quelle) | Unsere Werte | Bewertung / Korrektur | Status |
|---|---|---|---|---|
| **Stromlimit R_SNS** | ΔV_SNS = **45/50/55 mV** (0…125 °C), 43/50/57 mV (−40…125 °C) (S. 3) | R_SNS = **10 mΩ** (Δ = 45 mV/4,5 A gerechnet) | **typ 50 mV/10 mΩ = 5,0 A**, min 43 mV → **4,3 A**; Reserve bei 3 A: 1,67× typ / **1,43× min**. R_SNS = 10 mΩ ist **exakt der Wert aus Fig. 1 und Fig. 10** ✔ | **S3** |
| **Kurzschluss-Strom** | ΔV_SNS fällt bei **OUT = 0…1,5 V auf 18/25/32 mV** (S. 3) | war nicht berücksichtigt | ⇒ im Kurzschluss begrenzt das IC auf **2,5 A typ (1,8–3,2 A)** – eingebauter Foldback, liegt **unter F1 (5 A)** und schont M1 | **S3 (neu)** |
| **Timer C_TMR** | Warnzeit 20 ms/µF (OV); I_TMR(UP)OC = 10 µA + 3,36 µA/V·(V_CC−V_OUT−0,5 V) (S. 13/14); Design-Beispiel: 47 nF für 1 ms Warnung (S. 19) | C_TMR = **47 nF** | **wörtlich der Datenblatt-Wert** ✔. Bei uns: OV-Warnung **0,94 ms**; **OC-Abschaltung t_FLT = C·1,25 V/I_TMR(UP)OC → 0,71 ms @22 V, 0,61 ms @26 V** (eigene Rechnung) | **S3** |
| **Kurzschluss-Stress M1** | P²t ≈ (V_IN·ΔV_SNS/R_SNS)²·t_OC, Toleranzen ×2 (S. 17) | war offen | eigene Rechnung: I = 2,5 A, V_IN = 26 V → P = 65 W, t_OC = 0,61 ms ⇒ **P²t ≈ 2,6 W²s**, doppelt **5,2 W²s**. Datenblatt-Beispiel (FDB33N25) verkraftet 5,7 W²s ⇒ **FDMS86101-SOA bei ~26 V / 0,6 ms muss belegt werden** (FDMS86101-Datenblatt fehlt lokal) | **S1 → To-do** |
| **Clamp V_REG** | V_FB = **1,25 V (1,22…1,28)** (S. 3); Fig. 1/11 nutzen **R8 = 4,99 k**, Design-Beispiel **R7 = 102 k** (S. 19) | R7 = **100 k**, R8 = **4,7 k** → 27,85 V | eigene Toleranzrechnung: **26,67 V (min) … 29,07 V (max)** ⇒ min nur **0,67 V über V_IN,max = 26 V** (knapp!). Empfehlung: **R8 = 4,32 k (E96)** → nom 30,2 V, min 28,9 V (2,9 V Abstand). Das Datenblatt-Beispiel 102k/4,99k (26,8 V) ist für 26 V Eingang **nicht** brauchbar | **S1 → ändern** |
| **UV/OV** | V_UV/V_OV = 1,25 V (1,22…1,28), UV-Hysterese **50 mV**, **I_IN ±1 µA** (S. 4) | R1 = 220k / R2 = 8,2k / R3 = 10k → 16,4 V / 29,8 V | eigene Rechnung: **UV = 16,36 V (15,96…16,75 V, ±1,3 % durch I_IN), Hysterese 0,65 V ⇒ aus bei ~15,7 V; OV = 29,78 V (28,9…30,5 V)**. OV(min) 28,9 V überlappt V_REG(max) 29,07 V → nur im Fehlerfall relevant (OV verhindert nur den **Neustart**). **UV erzeugt kein FLT** ✔ | **S3** |
| **Filter an UV/OV** | Fig. 2: getrennte Teiler + RC, **τ_UV/τ_OV > 50** (S. 13) | keine Kondensatoren | ⇒ bei „Hot-Swap in Überspannung" würden wir sofort starten; Empfehlung: **C an UV/OV (1…10 nF) + Serien-R**, τ-Verhältnis > 50 (schützt auch vor Fehlauslösung durch Surge) | **S0 → ergänzen** |
| **C_HG (Gate-Kondensator)** | **6,8 nF empfohlen** (S. 17); Fig. 8–10: **47 nF + 10 Ω + D5** | **fehlt** | ⇒ **nachrüsten**: C_HG = 6,8 nF **+ 10 Ω (R6) + D5** (Kathode an C_HG). Wirkung: Inrush-Begrenzung (eigene Rechnung: I_INRUSH = 20 µA·28 µF/6,8 nF ≈ **82 mA**, ~7,5 ms) und Schleifenkompensation im OV/OC-Fall | **S0 → ergänzen** |
| **Ausgangspuffer** | „mindestens **22 µF Low-ESR-Elko** am Ausgang, Keramik ≤ 1/10 davon" (S. 18) | C_IN = 6 × 4,7 µF X7R (28 µF Keramik) + Elko-Kette | ⇒ **Elko ≥ 22 µF direkt am LTC4364-Ausgang** belegen (`865080543009`: Wert + ESR prüfen); 28 µF Keramik ist mehr als 1/10 ⇒ ggf. Elko größer oder 100 mΩ in Reihe | **S1 → prüfen** |
| **Gate-Zener** | ≥ 24 V Versorgung ⇒ **15-V-Zener an JEDEN MOSFET** (S. 16, D6/D7 = DDZ9702T in Fig. 9/10) | 1× 15-V-Zener geplant (DDZ9702) | ⇒ **zweiten Zener** ergänzen (D6 an HGATE–SOURCE, D7 an DGATE–SOURCE) – Typ passt (15 V) | **S1 → ergänzen** |
| **VCC-RC + Zener** | R4 = 2,2 k addiert **~1 V** Mindestspannung (750 µA max); D1/CMZ5945B (68 V) für 200-V-Transienten (S. 18/19) | R4 = 2,2 k, C1 = 0,1 µF, 68-V-Zener optional | ✔ deckt sich mit Fig. 10; bei unserem 1-kV/2-Ω-Surge (TVS klemmt ~45 V) ist D1 optional, aber empfohlen | **S3 (D1: Option)** |
| **M1/M2-Auswahl** | Fig. 9: **FDB3632 (M1) / FDMS86101 (M2)**; V_BR(DSS) > V_IN,max; SOA für M1 (S. 15/16) | 2× **FDMS86101** (100 V, 8 mΩ) | ✔ **M2 = Datenblatt-Bauteil**; für M1 liefert das Datenblatt FDB3632/FDB33N25 (SOA-stark). FDMS86101 als M1 zulässig, wenn die SOA-Rechnung (5,2 W²s) bestätigt wird. Modellproblem bleibt (BSIM3): Proxy BSC082N10LS + Bauteiltest | **S2 → SOA offen** |
| **Ideal-Diode / Reverse** | ΔV_SD = 30 mV typ (10…45) @ V_CC = 12 V; Pins −40 V (S. 5 / S. 2) | M2 als Ideal-Diode | ⇒ Rückwärtsstrom wird aktiv abgeschaltet (DGATE → SOURCE), Ausgang hält (C_OUT); unsere Verpol-/Brownout-Betrachtung (docs\06/07) ist damit **datenblatt-belegt** | **S3** |
| **Package/Pinout** | DE (14-DFN 4×3, θ_JA 45 °C/W, EP = Pin 15 GND *optional*, OUT = Pin 1+2) · MS (16-MSOP, 120 °C/W) · S (16-SO, 100 °C/W) (S. 2/25–27) | nicht fixiert | Verlust ≈ I_CC·V_IN + Gate ≈ **26 mW** ⇒ thermisch unkritisch; **Package muss für BOM/KiCad fixiert werden** (Empfehlung MS/S wegen Löten, DE wegen Fläche) | **S0 → festlegen** |
| **FLT / ENOUT** | FLT low bei OV/OC (**nicht** bei UV); ENOUT high-Z wenn OUT ≈ V_CC − 0,7 V, Reset bei OUT < 2,2 V, Pull-up ≥ 100 k an OUT (S. 4/13) | LED (150060GS75000) im Projekt, Nutzung offen | ⇒ FLT als **Fehleranzeige** (offen-drain), ENOUT als **„Power good"**; Pull-up an **Logikspannung** (nicht 12 V!) – Beschaltung im Schaltplan festlegen | **S0 → festlegen** |
| **Retry (Variante -2)** | D = 0,2 % (OV) / 0,12 % (Kurzschluss), 32-Zyklen-Cool-Down, am Ende OV-Check (S. 4/14/15) | -2 gewählt | ✔ gewollt (Selbstheilung nach transienter Störung); mittlere Verlustleistung im Dauerfehler = 0,12–0,2 % der Fehlerleistung ⇒ thermisch harmlos | **S3** |
| **Layout** | Kelvin an R_SNS, R(SOURCE→FET-Sources) **< 10 Ω**, **0,5 mm/A** bei 1 oz, Teiler am IC (S. 20) | Layout macht der Student | ⇒ als verbindliche Checkliste aufnehmen (bei 4 A ≈ **2 mm** breite Leistungspfade) | **S0 → Checkliste** |

## 5. Was daraus für Rechnung und Simulation folgt (Arbeitsliste)

**Rechnungen (neu/zu korrigieren):**
1. **R_SNS-Reserve gegen min** angeben: 43 mV/10 mΩ = 4,3 A ⇒ **1,43×** bei 3 A (nicht 1,67×).
2. **V_REG-Teiler** auf mehr Abstand zu 26 V bringen (**R8 → 4,32 k E96**) und die Toleranzkette dokumentieren.
3. **Kurzschluss-P²t = 5,2 W²s** gegen die SOA von M1 prüfen (FDMS86101-Datenblatt beschaffen).
4. **UV/OV als Band** rechnen (I_IN ±1 µA, Hysterese 50 mV/12 mV) – erledigt, s. o.
5. **Inrush** mit/ohne C_HG (82 mA mit 6,8 nF) und Ladezeit der 28 µF–C_IN.
6. **Elko am LTC4364-Ausgang ≥ 22 µF** prüfen (`865080543009`).
7. **Package + FLT/ENOUT-Beschaltung** festlegen (BOM/KiCad).

**Simulationen (auf Datenblattwerte kalibrieren):**
1. `ltc4364-2_ref.asc` / `TA01A`: ΔV_SNS = **50 mV** (und **25 mV** im Kurzschluss), V_FB = 1,25 V,
   V_UV/V_OV = 1,25 V, I_HGATE(UP) = 20 µA, TMR-Ströme (2,2 µA OV / 10 µA OC) einsetzen.
2. **Kurzschluss-Sim** (OUT → 0): Strombegrenzung ≈ 2,5 A, M1-Abschaltung nach ≈ 0,6 ms, ∫P²dt messen.
3. **Inrush-Sim** mit C_HG = 0 / 6,8 nF / 47 nF (+ 10 Ω / D5): Einschaltstrom und Dauer.
4. **Surge/EFT** (`surge_inprot7/8/9/10.cir`, `burst_eft.cir`) mit dem ergänzten Netz (C_HG, 2. Zener,
   RC an UV/OV) wiederholen – Kriterium: Buck-Eingang < 30 V, kein Fehlauslösen.
5. **Retry-Timing**: Dauer-OV → Warnung (0,94 ms) → Abschaltung → 32 Zyklen → Neustart messen.
6. **Verluste/T_J**: M1/M2 im Normalbetrieb (8 mΩ · 3 A ⇒ ≈ 72 mW je FET) und im Retry-Betrieb.

**Wichtig:** Die Punkte 1–3 der Rechnungen ändern Werte im Schaltplan (R8, C_HG+R6+D5, zweiter Zener,
Elko) – sie müssen **vor** dem Einfrieren des Layouts erledigt sein.



